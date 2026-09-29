# TD Set 1 — Correct Answer Review (46 questions)

Source: `TD_SAP_Review_Set1_Full.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/⚠️/🧠 are study notes. Wrong answers: `td_set_1_review.md`.

## Purpose

Confirm each correct answer was **knowledge, not a guess**. Answer again without looking; if you can't justify why every wrong option fails, tick **Guessed** and treat it as a wrong answer.

## ⚠️ Inconsistent concepts (right here, wrong elsewhere in this test)

| Right | Wrong | Concept |
|---|---|---|
| Q58 | Q27 | Cross-account private hosted zone → VPC association authorization |
| Q54 | Q74 | Parameter Store vs Secrets Manager (rotation → Secrets Manager) |
| Q70 | Q36 | Direct Connect VIF types (private VIF vs public VIF for VPN) |
| Q39 | Q61 | NAT Gateway placement / private-subnet egress |
| Q11 | Q65, Q21 | Web identity federation (STS AssumeRoleWithWebIdentity / Cognito) |
| Q2 | Q13, Q53 | Systems Manager patching (patch groups, baselines, maintenance windows) |
| Q48, Q63 | Q40 | SCP inheritance from root → OU placement |
| Q19 | Q12 | AWS Config rules for compliance detection |

These are partial knowledge — review each pair together.

## Tracker

| Group | Q | Guessed? | Pass 1 | Pass 2 |
|---|---|---|---|---|
| A | [Q3](#q3) | ☐ | ☐ | ☐ |
| A | [Q9](#q9) | ☐ | ☐ | ☐ |
| A | [Q35](#q35) | ☐ | ☐ | ☐ |
| A | [Q39](#q39) | ☐ | ☐ | ☐ |
| A | [Q52](#q52) | ☐ | ☐ | ☐ |
| A | [Q58](#q58) | ☐ | ☐ | ☐ |
| A | [Q70](#q70) | ☐ | ☐ | ☐ |
| B | [Q1](#q1) | ☐ | ☐ | ☐ |
| B | [Q7](#q7) | ☐ | ☐ | ☐ |
| B | [Q23](#q23) | ☐ | ☐ | ☐ |
| B | [Q34](#q34) | ☐ | ☐ | ☐ |
| B | [Q46](#q46) | ☐ | ☐ | ☐ |
| B | [Q50](#q50) | ☐ | ☐ | ☐ |
| B | [Q54](#q54) | ☐ | ☐ | ☐ |
| B | [Q56](#q56) | ☐ | ☐ | ☐ |
| B | [Q59](#q59) | ☐ | ☐ | ☐ |
| B | [Q67](#q67) | ☐ | ☐ | ☐ |
| C | [Q2](#q2) | ☐ | ☐ | ☐ |
| C | [Q15](#q15) | ☐ | ☐ | ☐ |
| C | [Q18](#q18) | ☐ | ☐ | ☐ |
| C | [Q20](#q20) | ☐ | ☐ | ☐ |
| C | [Q24](#q24) | ☐ | ☐ | ☐ |
| C | [Q37](#q37) | ☐ | ☐ | ☐ |
| C | [Q45](#q45) | ☐ | ☐ | ☐ |
| C | [Q49](#q49) | ☐ | ☐ | ☐ |
| D | [Q19](#q19) | ☐ | ☐ | ☐ |
| D | [Q33](#q33) | ☐ | ☐ | ☐ |
| D | [Q38](#q38) | ☐ | ☐ | ☐ |
| D | [Q48](#q48) | ☐ | ☐ | ☐ |
| D | [Q63](#q63) | ☐ | ☐ | ☐ |
| D | [Q66](#q66) | ☐ | ☐ | ☐ |
| D | [Q71](#q71) | ☐ | ☐ | ☐ |
| D | [Q75](#q75) | ☐ | ☐ | ☐ |
| E | [Q16](#q16) | ☐ | ☐ | ☐ |
| E | [Q32](#q32) | ☐ | ☐ | ☐ |
| E | [Q41](#q41) | ☐ | ☐ | ☐ |
| F | [Q4](#q4) | ☐ | ☐ | ☐ |
| F | [Q11](#q11) | ☐ | ☐ | ☐ |
| F | [Q30](#q30) | ☐ | ☐ | ☐ |
| F | [Q43](#q43) | ☐ | ☐ | ☐ |
| F | [Q44](#q44) | ☐ | ☐ | ☐ |
| F | [Q51](#q51) | ☐ | ☐ | ☐ |
| G | [Q6](#q6) | ☐ | ☐ | ☐ |
| G | [Q8](#q8) | ☐ | ☐ | ☐ |
| G | [Q31](#q31) | ☐ | ☐ | ☐ |
| G | [Q60](#q60) | ☐ | ☐ | ☐ |

---

# Group A — Hybrid networking & DNS (7)

<a id="q3"></a>

## Q3

A multi-national tech company has multiple VPCs assigned for each of its IT departments. VPC peering has been set up whenever intercommunication is needed between the VPCs. The solutions architect has been instructed to launch a new central database server that can be accessed by the other VPCs of the company using the database.tutorialsdojo.com domain name. This server should only be resolvable and accessible within the associated VPCs since only internal applications will be using the database.
Which of the following options should the solutions architect implement to meet the above requirements?

- **A.** Set up a private hosted zone with a domain name of tutorialsdojo.com and specify the VPCs that you want to associate with the hosted zone. Create an A record with a value of database.tutorialsdojo.com which maps to the Elastic IP address of the EC2 instance of your database server. Modify the enableDnsHostNames attribute of your VPC to true and the enableDnsSupport attribute to false
- **B.** Set up a public hosted zone with a domain name of tutorialsdojo.com and specify the VPCs that you want to associate with the hosted zone. Create an A record with a value of database.tutorialsdojo.com which maps to the IP address of the EC2 instance of your database server. Modify the enableDnsHostNames attribute of your VPC to true and the enableDnsSupport attribute to true
- **C.** Set up a private hosted zone with a domain name of tutorialsdojo.com and specify the VPCs that you want to associate with the hosted zone. Create an A record with a value of database.tutorialsdojo.com which maps to the IP address of the EC2 instance of your database server. Modify the enableDnsHostNames attribute of your VPC to true and the enableDnsSupport attribute to true
- **D.** Set up a public hosted zone with a domain name of tutorialsdojo.com and specify the VPCs that you want to associate with the hosted zone. Create a CNAME record with a value of database.tutorialsdojo.com which maps to the IP address of the EC2 instance of your database server. Modify the enableDnsHostNames attribute of your VPC to false and the enableDnsSupport attribute to false

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** resolvable only inside associated VPCs

⚠️ **Watch:** Public hosted zone exposes the name

🧠 **Rule:** Internal-only name → Route 53 private hosted zone associated with the VPCs.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC A ── peering ──┐
VPC B ── peering ──┼── database.tutorialsdojo.com
VPC C ── peering ──┘         (chỉ resolve/access NỘI BỘ, không public)
```

Yêu cầu chốt: domain **chỉ resolvable và accessible trong các VPC liên quan**, không lộ ra Internet. Anh chọn đúng **C**: private hosted zone + A record trỏ IP nội bộ của EC2 + `enableDnsHostNames=true` + `enableDnsSupport=true`.

#### Vì sao C đúng

- **Private hosted zone**: Route 53 chỉ trả lời DNS query cho domain này **từ bên trong các VPC được associate**, đúng yêu cầu "chỉ resolvable nội bộ".
- **A record trỏ IP (private) của EC2**: A record ánh xạ domain sang chính IP nội bộ trong VPC, không phải Elastic IP (Elastic IP là public, sẽ vi phạm yêu cầu "không truy cập được từ ngoài").
- **`enableDnsSupport=true`**: bắt buộc để Amazon-provided DNS resolver trong VPC hoạt động — nếu false, VPC không resolve được domain nào cả, kể cả private hosted zone.
- **`enableDnsHostNames=true`**: chỉ có tác dụng đầy đủ khi `enableDnsSupport` cũng true; cả hai cần bật cùng lúc.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì dùng **Elastic IP** — đây là public IPv4 address, có thể truy cập từ Internet, vi phạm ngay yêu cầu "chỉ nội bộ". Ngoài ra còn set `enableDnsSupport=false`, khiến VPC không resolve được domain.
- **B sai** vì dùng **public hosted zone** — public hosted zone trả lời DNS query từ cả Internet, không giới hạn trong VPC như yêu cầu.
- **D sai** vì vừa dùng **public hosted zone** (lộ domain ra ngoài), vừa dùng **CNAME trỏ vào IP** (CNAME phải trỏ vào một tên domain, không trỏ trực tiếp vào IP — sai kỹ thuật), lại còn set cả hai attribute VPC về false.

#### So sánh nhanh

| Đáp án | Loại hosted zone | Record | Giá trị record | 2 attribute VPC |
|---|---|---|---|---|
| **C (đúng)** | Private | A | IP nội bộ EC2 | true / true |
| A | Private | A | Elastic IP (public!) | true / **false** |
| B | Public | A | IP nội bộ EC2 | true / true |
| D | Public | CNAME | IP (sai cú pháp CNAME) | false / false |

#### Lưu ý thực tế

- `enableDnsHostNames` chỉ có hiệu lực khi `enableDnsSupport=true` — nếu chỉ set một trong hai, coi như DNS resolution trong VPC vẫn không hoạt động đầy đủ.
- CNAME record không bao giờ được trỏ trực tiếp vào một địa chỉ IP — chỉ trỏ vào một tên domain khác; muốn trỏ vào IP thì phải dùng A record (hoặc Alias record cho các AWS resource hỗ trợ).

#### Quy tắc nhớ cho thi

- **"Chỉ resolvable/accessible trong VPC"** → **Route 53 private hosted zone**, associate đúng các VPC cần
- **"Không muốn lộ ra Internet"** → tuyệt đối không dùng **Elastic IP** hay **public hosted zone**
- **Muốn DNS nội bộ VPC hoạt động** → cả **`enableDnsSupport`** và **`enableDnsHostNames`** phải là **true**
- **CNAME → trỏ domain, không trỏ IP**; muốn trỏ IP dùng **A record**

### TD explanation

In AWS, a hosted zone is a container for records, and records contain information about how you want to route traffic for a specific domain, such as tutorialsdojo.com, and its subdomains (portal.tutorialsdojo.com, database.tutorialsdojo.com). A hosted zone and the corresponding domain have the same name. There are two types of hosted zones:

– Public hosted zones contain records that specify how you want to route traffic on the internet.
– Private hosted zones contain records that specify how you want to route traffic in an Amazon VPC

A private hosted zone is a container that holds information about how you want Amazon Route 53 to respond to DNS queries for a domain and its subdomains within one or more VPCs that you create with the Amazon VPC service. Your VPC has attributes that determine whether your EC2 instance receives public DNS hostnames, and whether DNS resolution through the Amazon DNS server is supported.

enableDnsHostnames - Indicates whether the instances launched in the VPC get public DNS hostnames. If this attribute is true, instances in the VPC get public DNS hostnames, but only if the enableDnsSupport attribute is also set to true.
enableDnsSupport - Indicates whether the DNS resolution is supported for the VPC. If this attribute is false, the Amazon-provided DNS server in the VPC that resolves public DNS hostnames to IP addresses is not enabled. If this attribute is true, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC IPv4 network range plus two ( *.*.*.2 ) will succeed.
Hence, the option that says: Set up a private hosted zone with a domain name of tutorialsdojo.com and specify the VPCs that you want to associate with the hosted zone. Create an A record with a value of database.tutorialsdojo.com which maps to the IP address of the EC2 instance of your database server. Modify the enableDnsHostNames attribute of your VPC to true and the enableDnsSupport attribute to true is the correct answer.
The options that say:
1. Set up a public hosted zone with a domain name of tutorialsdojo.com and specify the VPCs that you want to associate with the hosted zone. Create an A record with a value of database.tutorialsdojo.com which maps to the IP address of the EC2 instance of your database server. Modify the enableDnsHostNames attribute of your VPC to true and the enableDnsSupport attribute to true
2. Set up a public hosted zone with a domain name of tutorialsdojo.com and specify the VPCs that you want to associate with the hosted zone. Create a CNAME record with a value of database.tutorialsdojo.com which maps to the IP address of the EC2 instance of your database server. Modify the enableDnsHostNames attribute of your VPC to false and the enableDnsSupport attribute to false
are incorrect because you have to create a private hosted zone and not a public one, since the database server will only be accessed by the associated VPCs and not publicly over the Internet. In addition, you have to create an A record for your database server and then set both the enableDnsHostNames and enableDnsSupport attributes to true.

The option that says: Set up a private hosted zone with a domain name of tutorialsdojo.com and specify the VPCs that you want to associate with the hosted zone. Create an A record with a value of database.tutorialsdojo.com which maps to the Elastic IP address of the EC2 instance of your database server. Modify the enableDnsHostNames attribute of your VPC to true and the enableDnsSupport attribute to false is incorrect. Even though it mentions the use of a private hosted zone, the configuration is incorrect since it is required to set both the enableDnsHostNames and enableDnsSupport attributes of your VPC to true. In addition, an Elastic IP address is a public IPv4 address, which is reachable from the Internet and hence, it violates the requirement that the database server should only be accessible within your associated VPCs.

References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html

Check out these Amazon VPC and Route 53 Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q9"></a>

## Q9

A tech company plans to host a website using an Amazon S3 bucket. The solutions architect created a new S3 bucket called “www.tutorialsdojo.com” in us-west-2 AWS region, enabled static website hosting, and uploaded the static web content files including the index.html file. The custom domain www.tutorialsdojo.com has been registered using Amazon Route 53 to be associated with the S3 bucket. The next day, a new Route 53 Alias record set was created which points to the S3 website endpoint: http://www.tutorialsdojo.com.s3-website-us-west-2.amazonaws.com. Upon testing, users cannot see any content on the bucket. Both the domains tutorialsdojo.com and www.tutorialsdojo.com do not work properly.
Which of the following is the MOST likely cause of this issue that the Architect should fix?

- **A.** The site does not work because you have not set a value for the error.html file, which is a required step.
- **B.** The site will not work because the URL does not include a file name at the end. This means that you need to use this URL instead: www.tutorialsdojo.com/index.html
- **C.** Route 53 is still propagating the domain name changes. Wait for another 12 hours and then try again.
- **D.** The S3 bucket does not have public read access which blocks the website visitors from seeing the content.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** S3 website endpoint; users see nothing

⚠️ **Watch:** Route 53 alias records were fine

🧠 **Rule:** S3 website 403 → bucket needs public read (bucket policy + Block Public Access off).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 bucket "www.tutorialsdojo.com" (static website hosting, us-west-2)
        │
Route 53 Alias record ──► S3 website endpoint (đã trỏ đúng!)
        │
     Users truy cập → KHÔNG THẤY GÌ (cả tutorialsdojo.com và www. đều lỗi)
```

Alias record đã được tạo đúng, trỏ đúng vào S3 website endpoint — vấn đề không nằm ở DNS. Anh chọn đúng **D**: bucket **thiếu public read access**.

#### Vì sao D đúng

S3 static website hosting **bắt buộc bucket phải cho phép public read** — đây là nguyên tắc cố định của dịch vụ này (khác với S3 dùng làm storage backend thông thường, nơi nên private theo mặc định). Nếu thiếu bucket policy cho phép `s3:GetObject` public (hoặc Block Public Access vẫn đang chặn), request từ browser tới S3 website endpoint sẽ bị **403 Forbidden**, khiến người dùng "không thấy nội dung gì" đúng như mô tả triệu chứng trong đề — dù DNS đã trỏ đúng chỗ.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì file `error.html` **không phải bước bắt buộc** khi enable static website hosting; nó chỉ dùng để custom trang lỗi 4xx, không ảnh hưởng đến khả năng truy cập trang chính.
- **B sai** vì S3 static website hosting **tự động phục vụ `index.html`** làm default document cho path gốc `/` — người dùng không cần gõ tên file cụ thể ở cuối URL.
- **C sai** vì Route 53 truyền lan (propagate) thay đổi DNS **trong khoảng 60 giây** trong điều kiện thông thường, không phải "chờ 12 giờ". Ngoài ra alias record trong đề vốn đã đúng, việc chờ thêm không giải quyết được gì.

#### So sánh nhanh

| Đáp án | Vấn đề nêu ra | Đúng bản chất lỗi? |
|---|---|---|
| **D (đúng)** | Bucket thiếu public read access | ✅ — đúng nguyên nhân gốc |
| A | Thiếu error.html | ❌ — không bắt buộc |
| B | Thiếu tên file cuối URL | ❌ — S3 tự phục vụ index.html |
| C | DNS propagation chậm | ❌ — Route 53 lan truyền trong ~60s |

#### Lưu ý thực tế

- Tên bucket phải **khớp chính xác** với tên record muốn route tới (ví dụ bucket `www.tutorialsdojo.com` cho record `www.tutorialsdojo.com`) — điều này đề đã làm đúng, không phải nguyên nhân lỗi ở đây.
- Muốn cho public read hoạt động, thường cần **tắt Block Public Access ở cấp bucket** (hoặc ít nhất phần liên quan tới bucket policy) VÀ có bucket policy `Allow s3:GetObject` cho principal `*`.

#### Quy tắc nhớ cho thi

- **"S3 static website, alias record đúng, user không thấy gì"** → nghĩ ngay đến **thiếu public read access / Block Public Access còn bật**
- **"Không truy cập được file cụ thể"** → S3 website hosting tự động serve **index document**, không cần gõ tên file
- **Route 53 propagation** hầu như **không phải nguyên nhân** trong các câu hỏi thi — DNS lan truyền rất nhanh (~60s)

### TD explanation

You can host a static website on Amazon Simple Storage Service (Amazon S3). On a static website, individual webpages include static content. They might also contain client-side scripts. To host a static website, you configure an Amazon S3 bucket for website hosting, and then upload your website content to the bucket. This bucket must have public read access. It is intentional that everyone in the world will have read access to this bucket.

When you configure an Amazon S3 bucket for website hosting, you must give the bucket the same name as the record that you want to use to route traffic to the bucket. For example, if you want to route traffic for example.com to an S3 bucket that is configured for website hosting, the name of the bucket must be example.com.
If you want to route traffic to an S3 bucket that is configured for website hosting but the name of the bucket doesn’t appear in the Alias Target list in the Amazon Route 53 console, check the following:

– The name of the bucket exactly matches the name of the record, such as tutorialsdojo.com or www.tutorialsdojo.com.
– The S3 bucket is correctly configured for website hosting.

In this scenario, the static S3 website does not work because the bucket does not have a public read access.
Therefore, the correct answer is: The S3 bucket does not have public read access which blocks the website visitors from seeing the content. This is the root cause why the static S3 website is inaccessible.
The option that says: The site does not work because you have not set a value for the error.html file, which is a required step is incorrect as the error.html is not required and won’t affect the availability of the static S3 website.
The option that says: The site will not work because the URL does not include a file name at the end. This means that you need to use this URL instead: www.tutorialsdojo.com/index.html is incorrect as it is not required to manually append the exact filename in S3.
The option that says: Route 53 is still propagating the domain name changes. Wait for another 12 hours and then try again is incorrect as the Route 53 domain name propagation does not take that long. Remember that Amazon Route 53 is designed to propagate updates you make to your DNS records to its worldwide network of authoritative DNS servers within 60 seconds under normal conditions.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RoutingToS3Bucket.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q35"></a>

## Q35

A company has just launched a new central employee registry application that contains all of the public employee registration information of each staff of the company. The application has a microservices architecture running in Docker in a single AWS Region. The management teams from other departments who have their servers located in different VPCs need to connect to the central repository application to continue their work. The Solutions Architect must ensure that the traffic to the application does not traverse the public Internet. The IT Security team must also be notified of any denied requests and be able to view the corresponding source IP.
How will the Architect implement the architecture of the new application given these circumstances?

- **A.** Use AWS Direct Connect to create a dedicated connection between the central VPC and each of the teams' VPCs. Enable the VPC Flow Logs on each VPC to capture rejected traffic requests, including the source IPs, that will be delivered to a CloudWatch Logs group. Set up an Amazon CloudWatch Logs subscription that streams the log data to the IT Security account.
- **B.** Set up an IPSec Tunnel between the central VPC and each of the teams' VPCs. Create VPC Flow Logs on each VPC to capture rejected traffic requests, including the source IPs, that will be delivered to an Amazon CloudWatch Logs group. Create a CloudWatch Logs subscription that streams the log data to the IT Security account.
- **C.** Link each of the teams' VPCs to the central VPC using VPC Peering. Create VPC Flow Logs on each VPC to capture rejected traffic requests, including the source IPs, that will be delivered to an Amazon CloudWatch Logs group. Set up a CloudWatch Logs subscription that streams the log data to the IT Security account.
- **D.** Set up a Transit VPC by using third-party marketplace VPN appliances running on an On-Demand Amazon EC2 instance that dynamically routes the VPN connections to the virtual private gateways (VGWs) attached to each VPC. Set up an AWS Config rule on each VPC to capture rejected traffic requests, including the source IPs, that will be delivered to an Amazon CloudWatch Logs group. Set up a CloudWatch Logs subscription that streams the log data to the IT Security account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** not over public internet; see denied source IPs

⚠️ **Watch:** Flow Logs capture REJECT + source IP; CloudTrail doesn't

🧠 **Rule:** Private connectivity → VPC peering; denied traffic → VPC Flow Logs → CloudWatch Logs metric filter.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Central VPC (employee registry, Docker microservices)
        ▲            ▲             ▲
   Team VPC A    Team VPC B    Team VPC C
Yêu cầu: (1) traffic KHÔNG qua public Internet
         (2) IT Security thấy denied requests + source IP
```

Anh chọn đúng **C — VPC Peering giữa central VPC và từng team VPC, VPC Flow Logs bắt REJECT + source IP → CloudWatch Logs → subscription gửi tới IT Security account**.

#### Vì sao C đúng

Hai yêu cầu tách biệt, mỗi phần khớp đúng công cụ:

- **Kết nối private, không qua Internet:** **VPC Peering** cho phép traffic giữa các VPC đi hoàn toàn trong mạng AWS, các instance "giao tiếp như cùng một network" — không đụng tới Internet Gateway hay đường truyền công khai.
- **Thấy denied request + source IP:** **VPC Flow Logs** ghi lại thông tin IP traffic đi/đến network interface, bao gồm cả traffic bị **REJECT** và **source IP** của nó — đúng chính xác yêu cầu giám sát.
- **Gửi cảnh báo tới team khác (IT Security account):** log được đẩy vào CloudWatch Logs group, sau đó dùng **CloudWatch Logs subscription** để stream dữ liệu log sang account của IT Security — không cần họ trực tiếp vào central account.

#### Vì sao các đáp án sai (distractor cần nhớ)

- **A (AWS Direct Connect giữa các VPC):** Direct Connect dùng để nối **on-premises datacenter với VPC**, không thể dùng để nối **VPC với VPC** — sai bản chất dịch vụ hoàn toàn cho use case này.
- **B (IPSec Tunnel):** IPSec Tunnel truyền dữ liệu **qua Internet công khai** (dù đã mã hóa) — vi phạm trực tiếp yêu cầu "traffic không được đi qua public Internet".
- **D (Transit VPC qua VPN appliance của bên thứ 3 + AWS Config):** VPN appliance cũng dùng Internet để truyền dữ liệu → vi phạm yêu cầu private. Thêm nữa, **AWS Config rule không có khả năng bắt được source IP** của traffic bị từ chối — đó là việc của VPC Flow Logs, không phải Config.

#### So sánh nhanh

| Đáp án | Kết nối | Qua Internet? | Bắt được denied + source IP? |
|---|---|---|---|
| **C. VPC Peering + Flow Logs (đúng)** | VPC-to-VPC private | Không | Có (Flow Logs) |
| A. Direct Connect | On-prem-to-VPC (sai use case) | Không (nhưng sai loại kết nối) | Có (Flow Logs) |
| B. IPSec Tunnel | VPN qua Internet | Có (vi phạm) | Có (Flow Logs) |
| D. Transit VPC (VPN appliance) | VPN qua Internet | Có (vi phạm) | Không (AWS Config không bắt IP) |

⚠️ **Lỗi lặp lại cần nhớ:** VPC Flow Logs là công cụ duy nhất trong 4 lựa chọn ghi được **source IP của traffic bị reject**; AWS CloudTrail hoặc AWS Config **không** làm được việc này — dễ nhầm vì cả hai đều nghe có vẻ "theo dõi/audit".

#### Quy tắc nhớ cho thi

- **"Kết nối riêng giữa nhiều VPC, không qua Internet"** → **VPC Peering** (hoặc Transit Gateway nếu số VPC lớn) — không phải Direct Connect (đó là cho on-premises) hay VPN/IPSec (đi qua Internet).
- **"Thấy denied traffic + source IP"** → luôn là **VPC Flow Logs**, không phải AWS Config hay CloudTrail.
- **"Gửi log sang account khác"** → **CloudWatch Logs subscription** (stream log data cross-account).
- Hễ thấy giải pháp có chữ **VPN/IPSec/Tunnel** mà đề yêu cầu "không qua public Internet" → gần như luôn là bẫy sai.

### TD explanation

A VPC peering connection is a networking connection between two VPCs that enables you to route traffic between them privately. Instances in either VPC can communicate with each other as if they are within the same network. You can create a VPC peering connection between your own VPCs, with a VPC in another AWS account, or with a VPC in a different AWS Region.

VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon CloudWatch Logs or Amazon S3. After you’ve created a flow log, you can retrieve and view its data in the chosen destination.
Flow logs can help you with a number of tasks, such as:
– Diagnosing overly restrictive security group rules
– Monitoring the traffic that is reaching your instance
– Determining the direction of the traffic to and from the network interfaces
Flow log data is collected outside of the path of your network traffic, and therefore does not affect network throughput or latency. You can create or delete flow logs without any risk of impact to network performance.
Hence, the correct answer is: Link each of the teams’ VPCs to the central VPC using VPC Peering. Create VPC Flow Logs on each VPC to capture rejected traffic requests, including the source IPs, that will be delivered to an Amazon CloudWatch Logs group. Set up a CloudWatch Logs subscription that streams the log data to the IT Security account.
The option that says: Set up an IPSec Tunnel between the central VPC and each of the teams’ VPCs. Create VPC Flow Logs on each VPC to capture rejected traffic requests, including the source IPs, that will be delivered to an Amazon CloudWatch Logs group. Create a CloudWatch Logs subscription that streams the log data to the IT Security account is incorrect. It is mentiond in the scenario that the traffic to the application must not traverse the public Internet. Since an IPSec tunnel uses the Internet to transfer data from your VPC to a specified destination, this solution is definitely incorrect.
The option that says: Use AWS Direct Connect to create a dedicated connection between the central VPC and each of the teams’ VPCs. Enable the VPC Flow Logs on each VPC to capture rejected traffic requests, including the source IPs, that will be delivered to a CloudWatch Logs group. Set up an Amazon CloudWatch Logs subscription that streams the log data to the IT Security account is incorrect. You cannot set up Direct Connect between different VPCs. AWS Direct Connect is primarily used to set up a dedicated connection between your on-premises data center and your Amazon VPC.
The option that says: Set up a Transit VPC by using third-party marketplace VPN appliances running on an On-Demand Amazon EC2 instance that dynamically routes the VPN connections to the virtual private gateways (VGWs) attached to each VPC. Set up an AWS Config rule on each VPC to capture rejected traffic requests, including the source IPs, that will be delivered to an Amazon CloudWatch Logs group. Set up a CloudWatch Logs subscription that streams the log data to the IT Security account is incorrect. An AWS Config rule is not capable of capturing the source IP of the incoming requests. A VPN appliance is using the public Internet to transfer data. Thus, it violates the requirement of ensuring that the data is securely within the AWS network.

References:
https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-peering.html
https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

Check out these Amazon VPC and VPC Peering Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/vpc-peering/

</details>

<a id="q39"></a>

## Q39

A company hosts its multi-tiered web application on a fleet of Auto Scaling Amazon EC2 instances spread across two Availability Zones. The Application Load Balancer is in the public subnets, and the EC2 instances are in the private subnets. After a few weeks of operations, the users are reporting that the web application is not working properly. Upon testing, the Solutions Architect found that the website is accessible and the login is successful. However, when the “find a nearby store” function is clicked on the website, the map loads only about 50% of the time when the page is refreshed. This function involves a third-party RESTful API call to a map provider. EC2 NAT instances are used for these outbound API calls.
Which of the following options is the MOST likely reason for this failure and the recommended solution?

- **A.** This error is caused by a failed NAT instance in one of the public subnets. Use NAT Gateways instead of EC2 NAT instances to ensure availability and scalability.
- **B.** This error is caused by an overloaded NAT instance in one of the subnets. Scale the EC2 NAT instances to larger-sized instances to ensure that they can handle the growing traffic.
- **C.** The error is caused by a failure in one of their availability zones in the VPC of the third-party provider. Contact the third-party provider support hotline and request for them to fix it.
- **D.** The subnets in which the application is hosted have a misconfigured Network ACL that blocks outbound traffic to the third-party provider. Update the network ACL to allow this connection and configure IAM permissions to restrict these changes in the future.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** map loads ~50% of time; NAT instances

⚠️ **Watch:** Relates to Q61: NAT GW lives in the public subnet

🧠 **Rule:** Intermittent outbound failure → one NAT instance failed → NAT Gateway per AZ.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ALB (public subnet)
   │
   ▼
EC2 app (private subnet)
   │  gọi API bên thứ 3 (map provider)
   ▼
NAT instance (đặt ở 1 AZ) ──► Internet
NAT instance (AZ khác)    ──► Internet
   │
   50% request thành công, 50% fail khi refresh
```

Yêu cầu: tìm nguyên nhân NHIỀU KHẢ NĂNG NHẤT khiến map load chỉ ~50% thời gian. Anh chọn đúng **A**: một NAT instance ở một AZ đã chết, và AWS không tự phục hồi NAT instance. Giải pháp là chuyển sang NAT Gateway để có tính sẵn sàng và khả năng mở rộng tốt hơn.

#### Vì sao A đúng

Có 2 AZ → 2 NAT instance, mỗi AZ dùng NAT riêng cho traffic outbound. Tỷ lệ lỗi đúng **50%** khớp hoàn hảo với "một trong hai NAT instance bị down" — traffic từ AZ có NAT chết sẽ luôn fail, traffic từ AZ còn lại luôn thành công. NAT instance là EC2 instance do khách hàng tự quản lý: nếu nó crash, AWS không tự động phát hiện và thay thế — phải tự giám sát và fix. NAT Gateway thì được AWS quản lý, có redundancy tích hợp trong từng AZ, tự scale bandwidth, nên khắc phục được cả vấn đề availability và vấn đề tự vận hành.

#### Vì sao các phương án khác sai

- **B (scale NAT instance lớn hơn vì overload):** overload sẽ gây **chậm/timeout không đều theo tải cao/thấp** (đỡ hơn giờ off-peak), không tạo ra tỷ lệ fail cố định ~50%. Tỷ lệ 50% ổn định là dấu hiệu của "1 trong 2 điểm route chết hẳn", không phải quá tải.
- **C (lỗi AZ của bên thứ 3, gọi hotline họ fix):** nếu AZ của map provider bị lỗi, traffic đáng lẽ phải được điều hướng tránh AZ đó (nhà cung cấp có HA riêng) — lỗi không liên quan gì tới việc "route qua NAT nào" trong VPC của mình, nên không giải thích được vì sao lỗi lại rơi đúng ~50%.
- **D (NACL block outbound):** NACL sai cấu hình sẽ block **toàn bộ** traffic outbound, không phải một nửa. Vì hiện tại vẫn có 50% request map load được, nghĩa là NACL đang cho phép traffic ra ngoài — NACL không phải nguyên nhân.

| Nguyên nhân giả định | Kiểu lỗi biểu hiện | Có khớp 50% cố định? |
|---|---|---|
| **A. Một NAT instance chết** | Tất cả request qua AZ đó fail | Có |
| B. NAT bị overload | Chậm/không đều theo tải | Không |
| C. Lỗi AZ nhà cung cấp | Ngẫu nhiên, không liên quan route trong VPC mình | Không |
| D. NACL sai | Chặn 100% | Không |

#### Lưu ý thực tế

⚠️ Liên quan tới câu Q61 (Anh trả lời sai): NAT Gateway phải được đặt trong **public subnet** (subnet có route tới Internet Gateway), route table của private subnet chỉ trỏ 0.0.0.0/0 tới NAT Gateway đó — không đặt NAT Gateway trong private subnet. Cùng chủ đề NAT ở hai câu, nhưng Q39 hỏi về "tại sao lỗi + hướng khắc phục chung", Q61 hỏi về "đặt NAT Gateway ở subnet nào".

#### Quy tắc nhớ cho thi

- **"Lỗi outbound intermittent đúng ~50%, có 2 AZ"** → một NAT instance ở một AZ đã chết → chuyển sang **NAT Gateway**.
- **"NAT instance"** → khách hàng tự quản lý, AWS không tự failover.
- **"NAT Gateway"** → AWS quản lý, có redundancy trong từng AZ, tự scale bandwidth.
- **"Lỗi 100% liên tục"** → nghĩ tới NACL/Security Group/routing sai hoàn toàn, không phải NAT instance chết một phần.

### TD explanation

You can use a NAT device to enable instances in a private subnet to connect to the Internet (for example, for software updates) or other AWS services, but prevent the Internet from initiating connections with the instances. A NAT device forwards traffic from the instances in the private subnet to the Internet or other AWS services, and then sends the response back to the instances. When traffic goes to the Internet, the source IPv4 address is replaced with the NAT device’s address, and similarly, when the response traffic goes to those instances, the NAT device translates the address back to those instances’ private IPv4 addresses.
You can either use a managed NAT device offered by AWS called a NAT gateway, or you can create your own NAT device in an EC2 instance, referred to here as a NAT instance. The bandwidth of NAT instances depends on the instance size – higher instances size will have higher bandwidth capacity. NAT instances are managed by the customer, so if the instance goes down, there could be a potential impact on the availability of your application. You have to manually check and fix the NAT instances.
AWS recommends NAT gateways because they provide better availability and bandwidth over NAT instances. The NAT gateway service is also a managed service that does not require your administration efforts. NAT Gateways are highly available. In each Availability Zone, they are implemented with redundancy. It is managed by AWS, so you do not have to perform maintenance or monitoring if it is UP. NAT gateways automatically scale in bandwidth, so you don’t have to choose instance types.
Check out the full comparison in the table below:

The correct answer is: This error is caused by a failed NAT instance in one of the public subnets. Use NAT Gateways instead of EC2 NAT instances to ensure availability and scalability. This is very likely as we have two subnets in the scenario and NAT instances reside in only one AZ. With a failure rate of 50%, one of the NAT instances must have been down. AWS does not automatically recover the failed NAT instances. AWS recommends using NAT gateways because they provide better availability and bandwidth. Even if NAT gateway is deployed on a single AZ, AWS implements redundancy to ensure that it is always available on that AZ.
The option that says: The subnets in which the application is hosted have a misconfigured Network ACL that blocks outbound traffic to the third-party provider. Update the network ACL to allow this connection and configure IAM permissions to restrict these changes in the future is incorrect. A misconfigured NACL would prevent the map function from working entirely, not intermittently. Since the map function loads 50% of the time, it indicates that the ACLs are configured correctly for internet access. Therefore, this is less likely to be the root cause.
The option that says: The error is caused by a failure in one of their availability zones in the VPC of the third-party provider. Contact the third-party provider support hotline and request for them to fix it is incorrect. If there is a failure on one availability zone of the third-party provider, the traffic should have stopped sending to that AZ, so this failure is primarily caused by a local failure in your VPC.
The option that says: This error is caused by an overloaded NAT instance in one of the subnets. Scale the EC2 NAT instances to larger-sized instances to ensure that they can handle the growing traffic is incorrect. If the NAT instances are overloaded, you will typically notice inconsistent performance or slowdown for the third-party requests. This failure should have been gone during off-peak hours. If the failure rate is 50% of the requests, it is most likely that one of the NAT instances is down.

References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

</details>

<a id="q52"></a>

## Q52

A multinational financial firm plans to do a multi-regional deployment of its cryptocurrency trading application that’s being heavily used in the US and in Europe. The containerized application uses Kubernetes and has Amazon DynamoDB Global Tables as a centralized database to store and sync the data from two regions.
The architecture has distributed computing resources with several public-facing Application Load Balancers (ALBs). The Network team of the firm manages the public DNS internally and wishes to make the application available through an apex domain for easier access. S3 Multi-Region Access Points are also used for object storage workloads and hosting static assets.
Which is the MOST operationally efficient solution that the Solutions Architect should implement to meet the above requirements?

- **A.** Launch an AWS Transit Gateway that targets specific ALBs on the required AWS Regions. Create a CNAME record in Amazon Route 53 that directly points your custom domain name to the DNS name assigned to the AWS Transit Gateway.
- **B.** Set up an AWS Transit Gateway with a multicast domain that targets specific ALBs on the required AWS Regions. Create a public record in Amazon Route 53 using the static IP address of the AWS Transit Gateway.
- **C.** Set up an AWS Global Accelerator, which has several endpoint groups that target specific endpoints and ALBs on the required AWS Regions. Create a public alias record in Amazon Route 53 that points your custom domain name to the DNS name assigned to your accelerator.
- **D.** Launch an AWS Global Accelerator with several endpoint groups that target the ALBs in all the relevant AWS Regions. Create an Amazon Route 53 Resolver Inbound Endpoint that points your custom domain name to the CNAME assigned to your accelerator.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** apex domain; multi-Region ALBs; operationally efficient

⚠️ **Watch:** CNAME can't be at the apex

🧠 **Rule:** Static anycast IPs across Regions → Global Accelerator + Route 53 alias at the apex.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Crypto trading app, multi-region (US + Europe)
Kubernetes containers + DynamoDB Global Tables (centralized DB)
Nhiều ALB public-facing ở các region
S3 Multi-Region Access Points cho static asset
Network team muốn expose qua APEX DOMAIN (root domain, ví dụ example.com)
Yêu cầu: MOST operationally efficient
```

Đáp án đúng: **C** — AWS Global Accelerator với nhiều endpoint group trỏ tới ALB ở các region, tạo Route 53 **alias record** (không phải CNAME) trỏ domain vào DNS name của accelerator. Anh chọn đúng C.

#### Vì sao C đúng

Từ khóa quyết định: **"apex domain"** + **"multi-region ALBs"** + **"operationally efficient"**. Global Accelerator dùng AWS global network với **static anycast IP** để route traffic tới endpoint gần nhất/khỏe nhất trong số nhiều ALB ở nhiều Region — đúng thiết kế cho multi-region traffic distribution với health check tự động, không cần Architect tự viết logic routing. Về phần domain: **Route 53 alias record** là extension riêng của Route 53, hoạt động giống CNAME nhưng **dùng được cho apex/root domain** (CNAME thì không) — đây là cách chuẩn để gắn custom domain vào DNS name của Global Accelerator ở cấp root domain.

#### Vì sao các phương án khác sai

- **A (Transit Gateway + CNAME ở apex):** sai hai lần — Transit Gateway **không phải công cụ để phân phối traffic tới nhiều ALB** (nó dùng để kết nối/route traffic giữa VPC, VPN, Direct Connect ở tầng network); và **CNAME record không thể dùng cho apex domain** trong Route 53 — phải dùng alias record.
- **B (Transit Gateway + multicast domain + record dùng static IP của Transit Gateway):** sai vai trò tương tự A, thêm sai nữa: **multicast domain** dùng để gửi 1 luồng data tới nhiều máy nhận đồng thời trong VPC (multicast giữa các subnet), không liên quan gì tới việc phân phối traffic HTTP tới ALB; Transit Gateway cũng **không có static IP address** cố định kiểu này để trỏ DNS record vào.
- **D (Global Accelerator đúng, nhưng dùng Route 53 Resolver Inbound Endpoint):** phần Global Accelerator đúng, nhưng **Resolver Inbound Endpoint chỉ dùng để cho phép DNS query từ on-premises network hoặc VPC khác gọi vào VPC của mình** — hoàn toàn không liên quan tới việc map custom domain vào accelerator; đây không phải cơ chế alias/CNAME domain.

| Phương án | Traffic distribution | DNS record ở apex | Đúng? |
|---|---|---|---|
| **C (đúng)** | Global Accelerator | Alias record | Có |
| A | Transit Gateway (sai vai trò) | CNAME (không hợp lệ ở apex) | Sai cả 2 |
| B | Transit Gateway + multicast (sai vai trò) | Static IP record (không có) | Sai cả 2 |
| D | Global Accelerator (đúng) | Resolver Inbound Endpoint (sai công cụ) | Sai phần DNS |

#### Lưu ý thực tế

⚠️ Quy tắc DNS cơ bản luôn xuất hiện trong đề SAP: **CNAME record không được đặt tại apex/root domain** (ví dụ `example.com`) theo chuẩn DNS (RFC), chỉ dùng được cho subdomain (`www.example.com`). Route 53 **alias record** là giải pháp riêng của AWS để lách hạn chế này, cho phép trỏ domain gốc tới AWS resource (Global Accelerator, CloudFront, ALB, S3 website...).

#### Quy tắc nhớ cho thi

- **"Apex/root domain trỏ vào AWS resource"** → **Route 53 alias record**, không phải CNAME.
- **"Static anycast IP, multi-region endpoint, health-based routing tới ALB/NLB/EC2"** → **AWS Global Accelerator**.
- **Transit Gateway** → kết nối network (VPC-to-VPC, VPN, Direct Connect), không phải load balancing traffic HTTP.
- **Route 53 Resolver Inbound Endpoint** → cho DNS query từ ngoài vào VPC, không liên quan custom domain mapping.

### TD explanation

AWS Global Accelerator is a service in which you create accelerators to improve the performance of your applications for local and global users. Depending on the type of accelerator you choose, you can gain additional benefits:

-With a standard accelerator, you can improve the availability of your internet applications that are used by a global audience. With a standard accelerator, Global Accelerator directs traffic over the AWS global network to endpoints in the nearest Region to the client.
-With a custom routing accelerator, you can map one or more users to a specific destination among many destinations.
For standard accelerators, Global Accelerator uses the AWS global network to route traffic to the optimal regional endpoint based on health, client location, and policies that you configure, which increases the availability of your applications. Endpoints for standard accelerators can be Network Load Balancers, Application Load Balancers, Amazon EC2 instances, or Elastic IP addresses that are located in one AWS Region or multiple Regions. The service reacts instantly to changes in health or configuration to ensure that internet traffic from clients is always directed to healthy endpoints.
Custom routing accelerators only support virtual private cloud (VPC) subnet endpoint types and route traffic to private IP addresses in that subnet.

In most scenarios, you can configure DNS to use your custom domain name (such as www.tutorialsdojo.com) with your accelerator instead of using the assigned static IP addresses or the default DNS name. First, using Amazon Route 53 or another DNS provider, create a domain name, and then add or update DNS records with your Global Accelerator IP addresses. Or you can associate your custom domain name with the DNS name for your accelerator. Complete the DNS configuration and wait for the changes to propagate over the internet. Now when a client makes a request using your custom domain name, the DNS server resolves it to the IP addresses in random order or to the DNS name for your accelerator.
To use your custom domain name with Global Accelerator when you use Route 53 as your DNS service, you create an alias record that points your custom domain name to the DNS name assigned to your accelerator. An alias record is a Route 53 extension to DNS. It’s similar to a CNAME record, but you can create an alias record both for the root domain, such as example.com, and for subdomains, such as www.tutorialsdojo.com.
Hence, the correct answer is: Set up an AWS Global Accelerator, which has several endpoint groups that target specific endpoints and ALBs on the required AWS Regions. Create a public alias record in Amazon Route 53 that points your custom domain name to the DNS name assigned to your accelerator.
The option that says: Set up an AWS Transit Gateway with a multicast domain that targets specific ALBs on the required AWS Regions. Create a public record in Amazon Route 53 using the static IP address of the AWS Transit Gateway is incorrect because an AWS Transit Gateway is not meant to be used to distribute traffic to multiple ALBs. In addition, a multicast domain is primarily used in delivering a single stream of data to multiple receiving computers simultaneously. Transit Gateway supports routing multicast traffic between subnets of attached VPCs and not ALBs. You have to use an AWS Global Accelerator instead since you can configure an accelerator to have several endpoint groups that point to multiple ALBs.
The option that says: Launch an AWS Transit Gateway that targets specific ALBs on the required AWS Regions. Create a CNAME record in Amazon Route 53 that directly points your custom domain name to the DNS name assigned to the AWS Transit Gateway is incorrect. As mentioned in the above rationale, an AWS Transit Gateway is not suitable to be used to integrate all the ALBs. Creating a CNAME record is also not right since the scenario explicitly mentioned that you have to use the apex domain. Remember that a CNAME record cannot be used for apex domain configuration in Amazon Route 53. You have to create a public alias record instead.
The option that says: Launch an AWS Global Accelerator with several endpoint groups that target the ALBs in all the relevant AWS Regions. Create an Amazon Route 53 Resolver Inbound Endpoint that points your custom domain name to the CNAME assigned to your accelerator is incorrect. Although the use of AWS Global Accelerator is a valid solution, creating a Route53 Resolver Inbound Endpoint is irrelevant. An Inbound Resolver endpoint simply allows DNS queries to your Amazon VPCs from your on-premises network or another VPC.

References:
https://aws.amazon.com/global-accelerator/
https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.mapping-your-custom-domain.html
https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html

Check out this AWS Global Accelerator Cheat Sheet:
https://tutorialsdojo.com/aws-global-accelerator/

</details>

<a id="q58"></a>

## Q58

A small company has several AWS accounts that are used by multiple teams. To centralize DNS record keeping, the company has created a private hosted zone in Amazon Route 53 on the main Account A. The new application and database servers are hosted on a VPC in Account B. The CNAME record set db.turotialsdojo.com has been created for the Amazon RDS endpoint on the private hosted zone in Amazon Route 53. Upon deployment, the application on the Amazon EC2 instances failed to start. The application logs indicate that the database endpoint db.turotialsdojo.com is not resolvable. However, the solutions architect can confirm that the Route 53 entry is configured correctly.
Which of the following options is the recommended solution for this issue? (Select TWO.)

- **A.** Create custom AMI for the Amazon EC2 instances that have an updated /etc/resolv.conf file containing the Amazon RDS endpoint to private IP address mapping.
- **B.** Create a VPC peering between the Account A VPC and Account B VPC. Configure the Amazon EC2 instances on Account B to use the DNS resolver IPs in Account A to resolve the Amazon RDS endpoint.
- **C.** On Account B, create a new private hosted zone in Amazon Route 53. Associate this zone to the private hosted zone in Account A to allow replication between the AWS accounts.
- **D.** On Account A, create an authorization to associate its private hosted zone to the new VPC in Account B.
- **E.** On Account B, associate the VPC to the private hosted zone in Account A. Delete the association authorization after the association is created.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D, E (you answered correctly)

🔑 **Key words:** cross-account VPC can't resolve PHZ record (Select TWO)

⚠️ **Watch:** ⚠️ Same concept you missed in Q27

🧠 **Rule:** Account A: create-vpc-association-authorization → Account B: associate-vpc-with-hosted-zone → delete authorization.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Account A (chủ PHZ)                      Account B (VPC chứa EC2 + RDS)
┌──────────────────────────┐             ┌──────────────────────────┐
│ Route 53 Private Hosted  │             │ EC2 app  ──► db.xxx.com  │
│ Zone: db.tutorialsdojo.com│            │   không resolve được!    │
└──────────────────────────┘             └──────────────────────────┘
```

CNAME record đúng, nhưng EC2 ở Account B không resolve được vì **VPC của Account B chưa được associate với PHZ của Account A** — PHZ chỉ trả lời DNS cho các VPC đã associate với nó. Đáp án đúng: **D + E** (Account A tạo authorization → Account B associate VPC → xoá authorization). Anh chọn đúng D, E.

#### Vì sao D và E đúng — quy trình 2 bước bắt buộc

Route 53 **không cho phép** dùng console để associate VPC khác account với PHZ; phải qua CLI/SDK/API theo đúng 2 bước:

```
Bước 1 (Account A – chủ PHZ):
    create-vpc-association-authorization
    → cấp quyền cho VPC của Account B được join vào PHZ

Bước 2 (Account B – chủ VPC):
    associate-vpc-with-hosted-zone
    → dùng authorization đó để chính thức associate

(Optional nhưng nên làm) Account A:
    delete-vpc-association-authorization
    → association vẫn giữ nguyên, chỉ chặn việc re-associate trong tương lai
```

**D đúng** vì đây là bước khởi tạo bắt buộc — không có authorization thì Account B không thể associate. **E đúng** vì đây là bước thực thi association thực sự, và dọn authorization sau khi dùng xong là best practice an toàn (không ảnh hưởng association đã tạo).

#### Từng đáp án sai vì đâu

- **A sai:** tạo custom AMI với mapping cứng RDS endpoint → IP trong `/etc/resolv.conf`. RDS private IP có thể đổi bất cứ lúc nào (failover, restart) → mapping tĩnh sẽ lỗi thời và gãy.
- **B sai:** VPC peering + trỏ EC2 dùng DNS resolver của Account A **không** giải quyết vấn đề, vì Route 53 ở Account A vốn không "biết" gì về RDS ở Account B — vấn đề là thiếu association với PHZ, không phải thiếu kết nối network.
- **C sai:** tạo PHZ mới ở Account B rồi "associate" với PHZ của Account A để replicate — Route 53 **không hỗ trợ** kiểu replication giữa hai private hosted zone ở hai account khác nhau.

| Đáp án | Cơ chế | Vấn đề |
|---|---|---|
| **D+E (đúng)** | create-vpc-association-authorization → associate-vpc-with-hosted-zone | Không |
| A | Static IP mapping trong AMI | RDS IP có thể đổi |
| B | VPC peering + trỏ DNS resolver | Không sửa được vấn đề gốc (PHZ chưa associate) |
| C | "Replicate" 2 PHZ | Route 53 không hỗ trợ |

#### ⚠️ Lỗi lặp lại (liên quan Q27)

Q27 cũng là bài cross-account private DNS nhưng dễ nhầm ở một điểm khác: khi có ~50 account cần share DNS, PHZ **không thể** "delegate" qua NS record như public hosted zone — vẫn phải dùng đúng cơ chế `create-vpc-association-authorization` + `associate-vpc-with-hosted-zone`, và tốt nhất tập trung PHZ ở 1 account trung tâm rồi associate VPC các account khác vào, không tạo peering hay NS delegation.

#### Quy tắc nhớ cho thi

- **Private hosted zone cross-account** → luôn 2 bước: **Account chủ PHZ tạo authorization** → **Account chủ VPC associate**.
- Route 53 console **không** làm được association cross-account — phải CLI/SDK/API.
- **Không** có "replication" giữa PHZ của 2 account khác nhau.
- **Không** hardcode IP của RDS/managed service vào file resolver — endpoint có thể đổi.

### TD explanation

You can use the Amazon Route 53 console to associate more VPCs with a private hosted zone if you created the hosted zone and the VPCs by using the same AWS account. Additionally, you can associate a VPC from one account with a private hosted zone in a different account.
If you want to associate VPCs that you created by using one account with a private hosted zone that you created by using a different account, you first must authorize the association. In addition, you can’t use the AWS console either to authorize the association or associate the VPCs with the hosted zone.
To associate an Amazon VPC and a private hosted zone that you created with different AWS accounts, perform the following procedure:

Using the account that created the hosted zone, authorize the association of the VPC with the private hosted zone by using one of the following methods:

-AWS CLI – using the create-vpc-association-authorization in the AWS CLI
-AWS SDK or AWS Tools for Windows PowerShell
-Amazon Route 53 API – Using the CreateVPCAssociationAuthorization API
Note the following:
– If you want to associate multiple VPCs that you created with one account with a hosted zone that you created with a different account, you must submit one authorization request for each VPC.
– When you authorize the association, you must specify the hosted zone ID, so the private hosted zone must already exist.
– You can’t use the Route 53 console either to authorize the association of a VPC with a private hosted zone or to make the association.

Using the account that created the VPC, associate the VPC with the hosted zone. As with authorizing the association, you can use the AWS SDK, Tools for Windows PowerShell, the AWS CLI, or the Route 53 API.
Optional but recommended – Delete the authorization to associate the VPC with the hosted zone. Deleting the authorization does not affect the association, it just prevents you from reassociating the VPC with the hosted zone in the future. If you want to reassociate the VPC with the hosted zone, you’ll need to repeat steps 1 and 2 of this procedure.

Therefore, the correct answers are:
-On Account A, create an authorization to associate its private hosted zone to the new VPC in Account B.
-On Account B, associate the VPC to the private hosted zone in Account A. Delete the association authorization after the association is created.
The option that says: Create a VPC peering between the Account A VPC and Account B VPC. Configure the Amazon EC2 instances on Account B to use the DNS resolver IPs in Account A to resolve the Amazon RDS endpoint is incorrect. This may be possible to configure, however, Route 53 in Account A has no knowledge of any RDS instance which are hosted on Account B. Therefore the EC2 instances still won’t be able to resolve the DB endpoint.
The option that says: Create custom AMI for the Amazon EC2 instances that have an updated /etc/resolv.conf file containing the Amazon RDS endpoint to private IP address mapping is incorrect. Creating a static mapping of the RDS endpoint to a private IP address is not recommended. The internal private IPs of RDS instances may change over time.
The option that says: On Account B, create a new private hosted zone in Amazon Route 53. Associate this zone to the private hosted zone in Account A to allow replication between the AWS accounts is incorrect. This is not possible as you can’t have replication between Route 53 in separate accounts.

References:
https://aws.amazon.com/premiumsupport/knowledge-center/private-hosted-zone-different-account/
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs-different-accounts.html

Check out the Amazon Route 53 Cheat Sheet:
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q70"></a>

## Q70

A government agency has multiple VPCs in various AWS regions across the United States that need to be linked up to an on-premises central office network in Washington, D.C. The central office requires inter-region VPC access over a private network that is dedicated to each region for enhanced security and more predictable data transfer performance. Your team is tasked to quickly build this network mesh and to minimize the management overhead to maintain these connections.
Which of the following options is the most secure, highly available, and durable solution that you should use to set up this kind of interconnectivity?

- **A.** Create a link aggregation group (LAG) in the central office network to aggregate multiple connections at a single AWS Direct Connect endpoint in order to treat them as a single, managed connection. Use AWS Direct Connect Gateway to achieve inter-region VPC access to all of your AWS resources. Create a virtual private gateway in each VPC and then create a public virtual interface for each AWS Direct Connect connection to the Direct Connect Gateway.
- **B.** Utilize AWS Direct Connect Gateway for inter-region VPC access. Create a virtual private gateway in each VPC, then create a private virtual interface for each AWS Direct Connect connection to the Direct Connect gateway.
- **C.** Implement a hub-and-spoke network topology in each region that routes all traffic through a network transit center using AWS Transit Gateway. Route traffic between VPCs and the on-premise network over AWS Site-to-Site VPN.
- **D.** Enable inter-region VPC peering which allows peering relationships to be established between VPCs across different AWS regions. This will ensure that the traffic will always stay on the global AWS backbone and will never traverse the public Internet.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** inter-Region VPC mesh over DX; low overhead

⚠️ **Watch:** ⚠️ Q36: VPN over DX needs a PUBLIC VIF; plain private access = private VIF

🧠 **Rule:** Many VPCs/Regions over DX → Direct Connect Gateway + private VIF + VGW per VPC.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises central office (Washington D.C.)
        │  1 Direct Connect connection
        ▼
   Direct Connect Gateway
        │
        ├── Private VIF ──► VGW (VPC #1, Region A)
        ├── Private VIF ──► VGW (VPC #2, Region B)
        └── Private VIF ──► VGW (VPC #3, Region C)

Yêu cầu: private, dedicated, predictable performance,
         nhiều VPC nhiều Region, ít management overhead
```

Chỉ truy cập **resource nằm trong VPC** (không dùng VPN qua Internet), nên chỉ cần **private virtual interface**. Đáp án đúng: **B**. Anh chọn đúng B.

#### Vì sao B đúng

**B đúng** vì Direct Connect Gateway cho phép một kết nối Direct Connect duy nhất từ on-premises "vươn tới" nhiều VPC ở nhiều Region khác nhau, mỗi VPC gắn một virtual private gateway (VGW) và một **private virtual interface (VIF)** riêng nối tới Direct Connect Gateway. Vì đích đến chỉ là resource **nằm trong VPC** (không cần truy cập public AWS service hay Internet), **private VIF** là loại VIF chính xác — nó traffic hoá route riêng cho VPC, giữ toàn bộ traffic trên kết nối dedicated/private của Direct Connect, đáp ứng đúng yêu cầu bảo mật + hiệu năng ổn định + giảm overhead (không cần thiết lập BGP session riêng cho từng VPC).

#### Từng đáp án sai vì đâu

- **A sai:** dùng **public virtual interface** thay vì private VIF — sai loại VIF vì mục tiêu chỉ là truy cập VPC resource, không cần public VIF (public VIF dùng để truy cập AWS public service/endpoint qua Direct Connect). Thêm LAG (Link Aggregation Group) vào đây cũng không liên quan gì đến yêu cầu bài — LAG chỉ là gộp nhiều kết nối DX vật lý thành 1 logical connection.
- **C sai:** dùng Transit Gateway + Site-to-Site VPN — mô hình hub-and-spoke này phù hợp khi công ty muốn tận dụng high-availability tự động và tối ưu license phần mềm VPN của bên thứ ba, nhưng **không đáp ứng** yêu cầu về "dedicated network" và "predictable data transfer performance" như đề đòi hỏi — VPN vẫn đi qua Internet dù được mã hóa.
- **D sai:** Inter-region VPC Peering đúng là traffic đi qua AWS global backbone (không ra Internet), nhưng đây là giải pháp **thủ công**, tốn nhiều công sức thiết lập/quản lý khi có nhiều VPC nhiều Region (mesh network phức tạp), và **không dedicated/highly available** như Direct Connect — không đáp ứng yêu cầu "minimize management overhead".

| Đáp án | Cơ chế | VIF/kết nối | Vấn đề |
|---|---|---|---|
| **B (đúng)** | DX Gateway + VGW mỗi VPC | Private VIF | Không |
| A | DX Gateway + LAG | Public VIF | Sai loại VIF; LAG không liên quan |
| C | Transit Gateway + Site-to-Site VPN | VPN qua Internet | Không dedicated, không predictable performance |
| D | Inter-region VPC Peering | Không qua DX | Nhiều overhead quản lý, không HA/dedicated |

#### ⚠️ Lỗi lặp lại (liên quan Q36)

Q36 hỏi tình huống ngược lại dễ gây nhầm lẫn: khi cần **mã hóa (encrypt)** traffic đi qua Direct Connect bằng site-to-site VPN (IPsec), phải dùng **PUBLIC VIF**, không dùng private VIF — vì VPN endpoint (Virtual Private Gateway) sử dụng **AWS public IP**, nên traffic VPN cần đi qua public VIF (dù vẫn nằm trên kết nối DX riêng, không ra Internet thật). Q70 thì khác: chỉ cần truy cập resource trong VPC, không có VPN/encryption nào ở đây — nên dùng **private VIF** là đúng. Ghi nhớ: **"chỉ truy cập VPC" → private VIF; "có VPN/IPsec chạy trên DX" → public VIF.**

#### Quy tắc nhớ cho thi

- **Nhiều VPC, nhiều Region, qua 1 kết nối Direct Connect** → **Direct Connect Gateway**.
- **Chỉ truy cập resource trong VPC** → **private VIF**. **Có VPN/IPsec chạy trên DX** → **public VIF** (vì VGW dùng AWS public IP).
- **LAG** chỉ là gộp nhiều physical DX connection thành 1 logical connection — không liên quan tới việc chọn loại VIF hay việc truy cập VPC.
- **"Dedicated + predictable performance"** → loại ngay các phương án dùng VPN qua Internet hoặc VPC Peering thủ công.

### TD explanation

AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS to achieve higher privacy benefits, additional data transfer bandwidth, and more predictable data transfer performance. Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections.
Using industry standard 802.1q VLANs, this dedicated connection can be partitioned into multiple virtual interfaces. Virtual interfaces can be reconfigured at any time to meet your changing needs. You can use an AWS Direct Connect gateway to connect your AWS Direct Connect connection over a private virtual interface to one or more VPCs in your account that are located in the same or different Regions. You associate a Direct Connect gateway with the virtual private gateway for the VPC. Then, create a private virtual interface for your AWS Direct Connect connection to the Direct Connect gateway. You can attach multiple private virtual interfaces to your Direct Connect gateway.
With Direct Connect Gateway, you no longer need to establish multiple BGP sessions for each VPC; this reduces your administrative workload as well as the load on your network devices.

Therefore, the correct answer is: Utilize AWS Direct Connect Gateway for inter-region VPC access. Create a virtual private gateway in each VPC, then create a private virtual interface for each AWS Direct Connect connection to the Direct Connect gateway.
The option that says: Create a link aggregation group (LAG) in the central office network to aggregate multiple connections at a single AWS Direct Connect endpoint in order to treat them as a single, managed connection. Use AWS Direct Connect Gateway to achieve inter-region VPC access to all of your AWS resources. Create a virtual private gateway in each VPC and then create a public virtual interface for each AWS Direct Connect connection to the Direct Connect Gateway is incorrect. You only need to create private virtual interfaces to the Direct Connect gateway since you are only connecting to resources inside a VPC. Using a link aggregation group (LAG) is also irrelevant in this scenario because it is just a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple connections at a single AWS Direct Connect endpoint, allowing you to treat them as a single, managed connection.
The option that says: Implement a hub-and-spoke network topology in each region that routes all traffic through a network transit center using AWS Transit Gateway. Route traffic between VPCs and the on-premise network over AWS Site-to-Site VPN is incorrect since the scenario requires a service that can provide a dedicated network between the VPCs and the on-premises network, as well as enhanced privacy and predictable data transfer performance. Simply using AWS Transit Gateway will not fulfill the conditions above. This option is best suited for customers who want to leverage AWS-provided, automated high availability network connectivity features and also optimize their investments in third-party product licensing such as VPN software.
The option that says: Enable inter-region VPC peering which allows peering relationships to be established between VPCs across different AWS regions. This will ensure that the traffic will always stay on the global AWS backbone and will never traverse the public internet is incorrect. This solution would require a lot of manual setup and management overhead to successfully build a functional, error-free inter-region VPC network compared with just using a Direct Connect Gateway. Although the Inter-Region VPC Peering provides a cost-effective way to share resources between regions or replicate data for geographic redundancy, its connections are not dedicated and highly available.

References:
https://aws.amazon.com/blogs/aws/new-aws-direct-connect-gateway-inter-region-vpc-access/
https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html
https://aws.amazon.com/answers/networking/aws-multiple-region-multi-vpc-connectivity/

Check out this AWS Direct Connect Cheat Sheet:
https://tutorialsdojo.com/aws-direct-connect/

</details>

---

# Group B — Security controls (10)

<a id="q1"></a>

## Q1

A company is planning to build its new customer relationship management (CRM) portal in AWS. The application architecture will be using a containerized microservices hosted on an Amazon ECS cluster. A Solutions Architect has been tasked to set up the architecture and comply with the AWS security best practice of granting the least privilege. The architecture should also support the use of security groups and standard network monitoring tools at the container level to comply with the company’s strict IT security policies.
Which of the following provides the MOST secure configuration for the CRM portal?

- **A.** Use the awsvpc network mode in the task definition in your Amazon ECS Cluster. Attach security groups to the ECS tasks then use IAM roles for tasks to access other resources.
- **B.** Use the awsvpc network mode in the task definition in your Amazon ECS Cluster. Attach security groups to the ECS tasks then pass IAM credentials into the container at launch time to access other AWS resources.
- **C.** Use AWS App Runner to run the containerized application instead to improve security and reduce operational overhead. Select VPC and security groups accordingly for deployment. Add IAM credentials to the environment variables when launching the service.
- **D.** Use the bridge network mode in the task definition in your Amazon ECS Cluster. Attach security groups to Amazon EC2 instances then use IAM roles for EC2 instances to access other resources.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** least privilege; SGs + network monitoring at container level

⚠️ **Watch:** bridge/host mode can't attach SGs per task

🧠 **Rule:** Per-task SG + ENI → awsvpc mode + IAM task roles.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ECS Cluster
┌─────────────────────────────────────────┐
│  Task (container) ── cần SG riêng       │
│  Task (container) ── cần network log    │
│                                          │
│  Yêu cầu: least privilege + SG + monitor│
│           TẠI MỨC CONTAINER              │
└─────────────────────────────────────────┘
```

Yêu cầu then chốt: security group và network-monitoring tool phải áp dụng **ở cấp container/task**, không phải cấp EC2 instance, và credentials phải theo nguyên tắc least privilege. Anh chọn đúng **A**: `awsvpc` network mode + security group gắn vào ECS task + IAM roles for tasks.

#### Vì sao A đúng

`awsvpc` là network mode duy nhất cấp cho **mỗi task một ENI (elastic network interface) và một private IP riêng**. Vì mỗi task có ENI riêng:

- Có thể gắn **security group trực tiếp vào task** (không phải vào EC2 instance) → đúng yêu cầu "SG ở cấp container".
- Có thể dùng **VPC Flow Logs** trên ENI đó → đúng yêu cầu "network monitoring tool ở cấp container".
- Dùng **IAM roles for tasks** để cấp quyền cho từng task riêng biệt, không phải share role của cả EC2 instance → đúng "least privilege".

#### Vì sao từng đáp án sai bị loại

- **B sai** vì tuy dùng đúng `awsvpc` + SG ở task, nhưng lại **truyền IAM credentials trực tiếp vào container qua biến môi trường/launch time** — đây là rủi ro bảo mật (credentials tĩnh, dễ lộ, không tự xoay vòng), vi phạm least privilege và best practice.
- **C sai** vì App Runner tuy giảm operational overhead nhưng **nhúng IAM credentials vào environment variables** — cùng lỗi bảo mật như B, không được khuyến nghị dù dịch vụ khác nhau.
- **D sai** vì dùng `bridge` mode — đây là network mode mặc định của Docker, chạy trên **virtual network nội bộ của EC2 instance**. Với `bridge`, security group chỉ gắn được vào **EC2 instance** (áp dụng chung cho mọi task chạy trên instance đó), không tách riêng theo từng task được.

#### So sánh nhanh các network mode ECS

| Mode | ENI riêng cho task? | Gắn SG ở đâu? | Phù hợp yêu cầu này? |
|---|---|---|---|
| **awsvpc** | Có | Task | ✅ Đúng |
| bridge | Không (dùng Docker virtual network) | EC2 instance | ❌ |
| host | Không (map trực tiếp cổng EC2) | EC2 instance | ❌ |
| none | Không có kết nối ngoài | — | ❌ |

#### Quy tắc nhớ cho thi

- **"SG + network monitoring ở cấp container/task"** → **`awsvpc` mode** (task có ENI riêng)
- **"IAM permission cho container"** → luôn là **IAM roles for tasks**, KHÔNG BAO GIỜ là credentials nhúng vào env var/container image
- **"bridge/host mode"** → SG chỉ gắn được vào EC2 instance, không phải task → sai khi đề hỏi "granular per container"

### TD explanation

Task definitions are split into separate parts: the task family, the IAM task role, the network mode, container definitions, volumes, task placement constraints, and launch types. The family and container definitions are required in a task definition, while task role, network mode, volumes, task placement constraints, and launch type are optional.
You can configure various Docker networking modes that will be used by containers in your ECS task. The valid values are none, bridge, awsvpc, and host. The default Docker network mode is bridge.
With IAM roles for Amazon ECS tasks, you can specify an IAM role that can be used by the containers in a task. Applications must sign their AWS API requests with AWS credentials, and this feature provides a strategy for managing credentials for your applications to use, similar to the way that Amazon EC2 instance profiles provide credentials to EC2 instances. Instead of creating and distributing your AWS credentials to the containers or using the EC2 instance’s role, you can associate an IAM role with an ECS task definition or RunTask API operation. The applications in the task’s containers can then use the AWS SDK or CLI to make API requests to authorized AWS services.

If the network mode is set to none, the task’s containers do not have external connectivity, and port mappings can’t be specified in the container definition.
If the network mode is bridge, the task utilizes Docker’s built-in virtual network which runs inside each container instance.
If the network mode is host, the task bypasses Docker’s built-in virtual network and maps container ports directly to the EC2 instance’s network interface directly. In this mode, you can’t run multiple instantiations of the same task on a single container instance when port mappings are used.
If the network mode is awsvpc, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration when you create a service or run a task with the task definition. When you use this network mode in your task definitions, every task that is launched from that task definition gets its own elastic network interface (ENI) and a primary private IP address. The task networking feature simplifies container networking and gives you more control over how containerized applications communicate with each other and other services within your VPCs.
Task networking also provides greater security for your containers by allowing you to use security groups and network monitoring tools at a more granular level within your tasks. Because each task gets its own ENI, you can also take advantage of other Amazon EC2 networking features like VPC Flow Logs so that you can monitor traffic to and from your tasks. Additionally, containers that belong to the same task can communicate over the localhost interface. A task can only have one ENI associated with it at a given time.
Hence, the correct answer is: Use the awsvpc network mode in the task definition in your Amazon ECS Cluster. Attach security groups to the ECS tasks then use IAM roles for tasks to access other resources.
The option that says: Use the bridge network mode in the task definition in your Amazon ECS Cluster. Attach security groups to Amazon EC2 instances then use IAM roles for EC2 instances to access other resources is incorrect because you won’t be able to attach security groups to your ECS tasks using this network mode type. This will only use the Docker’s built-in virtual network which runs inside each container instance. You have to use the awsvpc network mode instead to allow you to use security groups and network monitoring tools at a more granular level within your tasks. Moreover, if you are using the awsvpc network mode, you should attach the security group to the ECS task and not to the EC2 instance.
The option that says: Use AWS App Runner to run the containerized application instead to improve security and reduce operational overhead. Select VPC and security groups accordingly for deployment. Add IAM credentials to the environment variables when launching the service is incorrect. This is possible as you can deploy containerized workloads on AWS App Runner. However, it is not recommended to put sensitive IAM credentials on the environment variables when running the service.
The option that says: Use the awsvpc network mode in the task definition in your Amazon ECS Cluster. Attach security groups to the ECS tasks then pass IAM credentials into the container at launch time to access other AWS resources is incorrect. Although it uses the correct network mode, you have to use an IAM Role instead. It is a security risk to pass the IAM credentials into the container as it could be potentially exposed.

References:
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#network_mode

Check out this Amazon ECS Cheat Sheet:
https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

</details>

<a id="q7"></a>

## Q7

A company runs a sports web portal that covers the latest cricket news in Australia. The solutions architect manages the main AWS account, which has resources in multiple AWS regions. The web portal is hosted on a fleet of on-demand Amazon EC2 instances and an Amazon RDS database, which are also deployed to other AWS regions. The IT Security Compliance Officer has given the solutions architect the task of developing a reliable and durable logging solution to track changes made to all EC2, IAM, and RDS resources in all AWS regions. The solution must ensure the integrity and confidentiality of the log data. The company already uses AWS Key Management Service to encrypt data at rest across its AWS environment.
Which of the following solutions would be the best option to choose?

- **A.** Create a new trail in AWS CloudTrail with the global services option selected, and assign it an existing Amazon S3 bucket to store the logs. Create S3 ACLs and enable Multi-Factor Authentication (MFA) delete on the S3 bucket storing your logs.
- **B.** Create a new trail in AWS CloudTrail and assign it a new Amazon S3 bucket to store the logs. Configure AWS SNS to send delivery notifications to your management system. Secure the S3 bucket that stores your logs using IAM roles and S3 bucket policies.
- **C.** Create three new AWS CloudTrail trails, each with its own Amazon S3 bucket to store the logs: one for the AWS Management console, one for AWS SDKs, and one for command-line tools. Then create IAM roles and S3 bucket policies for the S3 buckets storing your logs.
- **D.** Create a new trail in AWS CloudTrail with the global services option selected, and create one new Amazon S3 bucket to store the logs. Create IAM roles, S3 bucket policies, and enable Multi Factor Authentication (MFA) Delete on the S3 bucket storing your logs.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** all Regions; EC2/IAM/RDS changes; log integrity + confidentiality

⚠️ **Watch:** IAM events need global services option

🧠 **Rule:** CloudTrail multi-Region + global services + KMS + MFA Delete + log file validation.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Main account
├── EC2 + RDS trải nhiều Region
├── IAM (global service)
└── Yêu cầu: log MỌI thay đổi trên MỌI Region
             + log data phải TOÀN VẸN (integrity) và BẢO MẬT (confidentiality)
```

Anh chọn đúng **D**: CloudTrail trail với **global services option** bật + **1 S3 bucket mới** + IAM roles/bucket policy + **MFA Delete**.

#### Vì sao D đúng

Bốn thành phần trong D giải quyết đúng bốn khía cạnh của yêu cầu:

- **Global services option (`IncludeGlobalServiceEvents`)**: IAM là global service — events của IAM chỉ được ghi vào trail nào có bật flag này. Thiếu flag này = mất log IAM hoàn toàn.
- **Một S3 bucket MỚI**: bucket mới đảm bảo không ai khác đã có quyền truy cập từ trước — giữ **confidentiality**.
- **IAM roles + S3 bucket policy**: kiểm soát chặt ai được đọc/viết log — cũng phục vụ confidentiality.
- **MFA Delete**: yêu cầu xác thực MFA trước khi xoá vĩnh viễn object/version hoặc đổi versioning state → bảo vệ **integrity** của log, chống xoá log để che giấu hành vi.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì dùng một **bucket đã tồn tại** (existing S3 bucket) — bucket cũ có thể đã có người khác truy cập từ trước, không đảm bảo confidentiality cho log mới. Ngoài ra dùng **S3 ACL** thay vì IAM roles, kém chặt chẽ hơn.
- **B sai** vì **không bật global services option** — thiếu flag này thì các sự kiện IAM (một yêu cầu rõ trong đề: "track changes... to all EC2, IAM, and RDS resources") sẽ không được ghi log ở bất kỳ Region nào.
- **C sai** vì tạo **3 trail riêng** (console/SDK/CLI) với 3 bucket riêng — vừa không cần thiết (một trail multi-Region + global option đã đủ), vừa **cũng không bật global services option**, và làm tăng độ phức tạp quản lý vô ích.

#### So sánh nhanh

| Đáp án | Global services option | Số bucket | Bảo vệ integrity | Bảo vệ confidentiality |
|---|---|---|---|---|
| **D (đúng)** | ✅ Bật | 1 (mới) | MFA Delete | IAM roles + bucket policy |
| A | ✅ Bật | 1 (đã có sẵn) | MFA Delete | S3 ACL (yếu hơn) + bucket cũ |
| B | ❌ Không | 1 (mới) | SNS chỉ để thông báo, không bảo vệ integrity | IAM roles |
| C | ❌ Không | 3 | — | IAM roles nhưng dàn trải, phức tạp |

#### Lưu ý thực tế

- CloudTrail còn có **log file validation** (dùng digest file + hash chain) để chứng minh log không bị chỉnh sửa — đây cũng là cơ chế bảo vệ integrity phổ biến trong các câu hỏi tương tự, dù không xuất hiện trong đáp án đúng của câu này (MFA Delete đã đủ để đạt điểm "integrity" theo TD).

#### Quy tắc nhớ cho thi

- **"Track IAM changes / mọi Region"** → luôn cần **CloudTrail với global services option bật**, quên flag này là mất log IAM
- **"Log integrity"** → nghĩ đến **MFA Delete** hoặc **log file validation**
- **"Log confidentiality"** → dùng **bucket MỚI** (không phải bucket có sẵn) + **IAM roles/bucket policy**, tránh S3 ACL khi có lựa chọn tốt hơn
- **Nhiều trail/nhiều bucket** không đồng nghĩa với an toàn hơn — thường là dấu hiệu đáp án gây nhiễu, phức tạp hoá không cần thiết

### TD explanation

For most services, events are recorded in the region where the action occurred in its respective AWS CloudTrail. For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53, events are delivered to any trail that includes global services (IncludeGlobalServiceEvents flag). AWS CloudTrail service should be your top choice for the scenarios where the application is tracking the changes made by any AWS service, resource, or API.

AWS Identity and Access Management (IAM) is integrated with AWS CloudTrail, a service that logs AWS events made by or on behalf of your AWS account. CloudTrail logs AWS API calls and also AWS sign-in events, and collects this event information in files that are delivered to Amazon S3 buckets.
Hence, the correct answer is: Create a new trail in AWS CloudTrail with the global services option selected, and create one new Amazon S3 bucket to store the logs. Create IAM roles, S3 bucket policies, and enable Multi Factor Authentication (MFA) Delete on the S3 bucket storing your logs. It uses AWS CloudTrail with the (includeGlobalServiceEvents flag) Global Option enabled, a single new S3 bucket, and IAM Roles so that it has confidentiality, and MFA on Delete on the S3 bucket so that it maintains data integrity.
The option that says: Create a new trail in AWS CloudTrail with the global services option selected, and assign it an existing Amazon S3 bucket to store the logs. Create S3 ACLs and enable Multi-Factor Authentication (MFA) delete on the S3 bucket storing your logs is incorrect. As an existing S3 bucket is used, it may already be accessible by the user, simply not maintaining confidentiality, and it is not using IAM roles.
The option that says: Create three new AWS CloudTrail trails, each with its own Amazon S3 bucket to store the logs: one for the AWS Management console, one for AWS SDKs, and one for command-line tools. Then create IAM roles and S3 bucket policies for the S3 buckets storing your logs is incorrect. Although it uses AWS CloudTrail, the Global Option is not enabled, and three S3 buckets are not needed.
The option that says: Create a new trail in AWS CloudTrail and assign it a new Amazon S3 bucket to store the logs. Configure AWS SNS to send delivery notifications to your management system. Secure the S3 bucket that stores your logs using IAM roles and S3 bucket policies is incorrect. Although it uses AWS CloudTrail, the Global Option is not just enabled.
References:
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events
https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html

Check out these AWS CloudTrail and IAM Cheat Sheets:
https://tutorialsdojo.com/aws-cloudtrail/
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q23"></a>

## Q23

A fintech startup has developed a cloud-based payment processing system that accepts credit card payments as well as cryptocurrencies such as Bitcoin, Ripple, and the likes. The system is deployed in AWS which uses EC2, DynamoDB, S3, and CloudFront to process the payments. Since they are accepting credit card information from the users, they are required to be compliant with the Payment Card Industry Data Security Standard (PCI DSS). On the recent 3rd-party audit, it was found that the credit card numbers are not properly encrypted and hence, their system failed the PCI DSS compliance test. You were hired by the fintech startup to solve this issue so they can release the product in the market as soon as possible. In addition, you also have to improve performance by increasing the proportion of your viewer requests that are served from CloudFront edge caches instead of going to your origin servers for content. 
In this scenario, what is the best option to protect and encrypt the sensitive credit card information of the users and to improve the cache hit ratio of your CloudFront distribution?

- **A.** Configure the CloudFront distribution to use Signed URLs. Configure your origin to add a Cache-Control max-age directive to your objects, and specify the longest practical value for max-age to increase your cache hit ratio.
- **B.** Create an origin access control (OAC) and add it to the CloudFront distribution. Configure your origin to add User-Agent and Host headers to your objects to increase your cache hit ratio.
- **C.** Add a custom SSL in the CloudFront distribution. Configure your origin to add User-Agent and Host headers to your objects to increase your cache hit ratio.
- **D.** Configure the CloudFront distribution to enforce secure end-to-end connections to origin servers by using HTTPS and field-level encryption. Configure your origin to add a Cache-Control max-age directive to your objects, and specify the longest practical value for max-age to increase your cache hit ratio.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** protect credit card field; raise cache hit ratio

⚠️ **Watch:** max-age only helps cacheable static content (it was a distractor in Q17)

🧠 **Rule:** Sensitive form field → CloudFront field-level encryption + HTTPS to origin; hit ratio → Cache-Control max-age.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
User ──POST(credit card)──► CloudFront ──► Origin (payment system)
                                │
                                └─ cần: (1) mã hóa field credit card
                                        (2) tăng cache hit ratio
Yêu cầu PCI DSS: số credit card đang KHÔNG được mã hóa đúng cách → fail audit
```

Anh chọn đúng **D — CloudFront field-level encryption + HTTPS end-to-end, cộng với Cache-Control max-age để tăng cache hit ratio**.

#### Vì sao D đúng

Đây là bài có **2 yêu cầu độc lập**, đáp án đúng phải giải quyết cả hai:

1. **Bảo vệ field credit card cụ thể:** CloudFront **field-level encryption** cho phép mã hóa riêng các field nhạy cảm (tối đa 10 field) trong request POST, ngay tại edge, và dữ liệu vẫn được mã hóa xuyên suốt cho tới khi tới đúng ứng dụng có private key giải mã. Kết hợp với HTTPS end-to-end tới origin → thỏa yêu cầu PCI DSS về mã hóa dữ liệu thẻ khi truyền và cả trong lúc xử lý.
2. **Tăng cache hit ratio:** cấu hình origin trả **Cache-Control max-age** dài nhất có thể cho các object tĩnh (ảnh, CSS, JS…) → CloudFront giữ cache lâu hơn, giảm số lần phải quay lại origin.

#### Vì sao các đáp án sai (đều là distractor về mã hóa)

- **A (Signed URLs + max-age):** Signed URL chỉ kiểm soát **ai được truy cập** nội dung (private content), hoàn toàn không mã hóa dữ liệu bên trong request — không giải quyết được vấn đề credit card bị lộ.
- **B (OAC + custom headers):** Origin Access Control (OAC) dùng để **hạn chế truy cập trực tiếp vào S3** (chỉ cho CloudFront truy cập), không liên quan đến mã hóa field dữ liệu người dùng nhập vào. Thêm User-Agent/Host header cũng không tăng cache hit ratio theo đúng cơ chế TTL.
- **C (custom SSL + custom headers):** Custom SSL certificate chỉ đảm bảo kết nối HTTPS end-to-end an toàn ở tầng transport, nhưng **không mã hóa riêng field cụ thể** — nếu origin/log bị lộ, dữ liệu thẻ vẫn ở dạng plaintext sau khi giải mã TLS. Vẫn thiếu field-level encryption.

#### So sánh nhanh

| Cơ chế | Mục đích | Có mã hóa field cụ thể? |
|---|---|---|
| **Field-level encryption + HTTPS (D)** | Bảo vệ dữ liệu nhạy cảm end-to-end | Có |
| Signed URL (A) | Kiểm soát ai truy cập nội dung | Không |
| OAC (B) | Chặn truy cập S3 trực tiếp | Không |
| Custom SSL (C) | Mã hóa toàn kênh transport | Không (không tách riêng field) |

⚠️ **Lỗi lặp lại:** `Cache-Control max-age` từng là **distractor sai** trong Q17 (vì đó là request đăng nhập động, không cacheable). Ở Q23 nó lại là **phần đúng** vì áp dụng cho object tĩnh cần tăng cache hit ratio — cùng một khái niệm nhưng đúng/sai tùy theo loại nội dung (dynamic login request vs static object).

#### Quy tắc nhớ cho thi

- **"Mã hóa field dữ liệu nhạy cảm (credit card, SSN…) trong request"** → **CloudFront field-level encryption**.
- **"Tăng cache hit ratio"** → **Cache-Control max-age dài nhất khả thi** — nhưng chỉ hợp lý với **nội dung tĩnh**, không phải request đăng nhập/động.
- **OAC** → chỉ để bảo vệ S3 origin, không liên quan mã hóa dữ liệu người dùng.
- **Signed URL/Cookie** → kiểm soát quyền truy cập, không phải công cụ mã hóa.

### TD explanation

Field-level encryption adds an additional layer of security, along with HTTPS, that lets you protect specific data throughout system processing so that only certain applications can see it. Field-level encryption allows you to securely upload user-submitted sensitive information to your web servers. The sensitive information provided by your clients is encrypted at the edge closer to the user and remains encrypted throughout your entire application stack, ensuring that only applications that need the data—and have the credentials to decrypt it—are able to do so.

To use field-level encryption, you configure your CloudFront distribution to specify the set of fields in POST requests that you want to be encrypted, and the public key to use to encrypt them. You can encrypt up to 10 data fields in a request. Hence, the correct answer for this scenario is the option that says: Configure the CloudFront distribution to enforce secure end-to-end connections to origin servers by using HTTPS and field-level encryption. Configure your origin to add a Cache-Control max-age directive to your objects, and specify the longest practical value for max-age to increase your cache hit ratio.
You can improve performance by increasing the proportion of your viewer requests that are served from CloudFront edge caches instead of going to your origin servers for content; that is, by improving the cache hit ratio for your distribution. To increase your cache hit ratio, you can configure your origin to add a Cache-Control max-age directive to your objects, and specify the longest practical value for max-age. The shorter the cache duration, the more frequently CloudFront forwards another request to your origin to determine whether the object has changed and, if so, to get the latest version.
The option that says: Add a custom SSL in the CloudFront distribution. Configure your origin to add User-Agent and Host headers to your objects to increase your cache hit ratio is incorrect. Although it provides secure end-to-end connections to origin servers, it is better to add field-level encryption to protect the credit card information.
The option that says: Configure the CloudFront distribution to use Signed URLs. Configure your origin to add a Cache-Control max-age directive to your objects, and specify the longest practical value for max-age to increase your cache hit ratio is incorrect because a Signed URL provides a way to distribute private content but it doesn’t encrypt the sensitive credit card information.
The option that says: Create an Origin Access Control (OAC) and add it to the CloudFront distribution. Configure your origin to add User-Agent and Host headers to your objects to increase your cache hit ratio is incorrect because OAC is mainly used to restrict access to objects in S3 bucket, but not provide encryption to specific fields.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html#field-level-encryption-setting-up
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

<a id="q34"></a>

## Q34

A multinational financial company has a suite of web applications hosted in multiple VPCs in various AWS regions. As part of their security compliance, the company’s Solutions Architect has been tasked to set up a logging solution to track all of the changes made to their AWS resources in all regions, which host their enterprise accounting systems. The company is using different AWS services such as Amazon EC2 instances, Amazon S3 buckets, CloudFront web distributions, and AWS IAM. The logging solution must ensure the security, integrity, and durability of your log data in order to pass the compliance requirements. In addition, it should provide an event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command-line tools, and API calls. 
In this scenario, which of the following options is the best solution to use?

- **A.** Create a new AWS CloudTrail trail in a new S3 bucket using the AWS CLI and also pass both the –is-multi-region-trail and –include-global-service-events parameters then encrypt log files using KMS encryption. Enable Multi-Factor Authentication (MFA) Delete on the S3 bucket and ensure that only authorized users can access the logs by configuring the bucket policies.
- **B.** Create a new AWS CloudTrail trail in a new S3 bucket using the AWS CLI and also pass the –no-include-global-service-events and –is-multi-region-trail parameter then encrypt log files using KMS encryption. Enable Multi-Factor Authentication (MFA) Delete on the S3 bucket and ensure that only authorized users can access the logs by configuring the bucket policies.
- **C.** Create a new Amazon CloudWatch trail in a new S3 bucket using the AWS CLI and also pass both the –is-multi-region-trail and –include-global-service-events parameters then encrypt log files using KMS encryption. Enable Multi-Factor Authentication (MFA) Delete on the S3 bucket and ensure that only authorized users can access the logs by configuring the bucket policies.
- **D.** Create a new Amazon CloudWatch trail in a new S3 bucket using the AWS CLI and also pass the –include-global-service-events parameter then encrypt log files using KMS encryption. Enable Multi-Factor Authentication (MFA) Delete on the S3 bucket and ensure that only authorized users can access the logs by configuring the bucket policies.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** integrity of logs; account activity history

⚠️ **Watch:** Same as Q7

🧠 **Rule:** CloudTrail --is-multi-region-trail + --include-global-service-events + KMS + MFA Delete.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhiều VPC, nhiều region: EC2, S3, CloudFront (global), IAM (global)
        │
        ▼  cần log toàn bộ account activity, đủ integrity + durability
??? trail ── --is-multi-region-trail ── --include-global-service-events
        │
        ▼
S3 bucket + KMS encryption + MFA Delete + bucket policy
```

Anh chọn đúng **A — CloudTrail trail với cả `--is-multi-region-trail` và `--include-global-service-events`, mã hóa KMS, MFA Delete trên S3**.

#### Vì sao A đúng

Yêu cầu là "event history of account activity, bao gồm Console/SDK/CLI/API calls" — đây chính xác là định nghĩa của **AWS CloudTrail** (không phải CloudWatch, vốn chỉ theo dõi metric/log ứng dụng, không phải API call history).

Hai flag bắt buộc phải có đồng thời:

- **`--is-multi-region-trail`**: gom log từ **tất cả region** — bắt buộc vì công ty có VPC ở "various AWS regions".
- **`--include-global-service-events`**: bắt buộc để bắt được hoạt động của **global services** như IAM, Route 53, AWS WAF, CloudFront — các dịch vụ không gắn với một region cụ thể. Thiếu flag này thì trail multi-region vẫn **bỏ lọt** hoạt động IAM/CloudFront mà đề bài yêu cầu theo dõi.

Cộng thêm **mã hóa KMS** + **MFA Delete** trên S3 bucket chứa log → đúng yêu cầu "security, integrity, and durability" cho compliance.

#### Vì sao các đáp án sai (distractor cần nhớ)

- **C, D (dùng "Amazon CloudWatch trail"):** Không có khái niệm "CloudWatch trail" — trail là khái niệm của **CloudTrail**, không phải CloudWatch. CloudWatch theo dõi metric/log ứng dụng, không ghi lại lịch sử API call của account.
- **D (thiếu `--is-multi-region-trail`):** Ngoài lỗi "CloudWatch trail", D còn thiếu hẳn tham số multi-region — chỉ dùng `--include-global-service-events` một mình thì log của các region khác (ngoài region tạo trail) sẽ không được ghi lại.
- **B (`--no-include-global-service-events`):** Đây là flag **ngược nghĩa** — nó chủ động **loại bỏ** sự kiện từ global service (như IAM) khỏi log, trực tiếp vi phạm yêu cầu theo dõi IAM của đề bài.

#### So sánh nhanh

| Đáp án | Dịch vụ | Multi-region? | Global service events? |
|---|---|---|---|
| **A (đúng)** | CloudTrail | Có | Có (include) |
| B | CloudTrail | Có | Không (no-include, sai) |
| C | "CloudWatch trail" (không tồn tại) | Có | Có |
| D | "CloudWatch trail" (không tồn tại) | Không | Có |

#### Quy tắc nhớ cho thi

- **"Event history of account activity / API call log"** → luôn là **AWS CloudTrail**, không phải CloudWatch.
- **Nhiều region + có dùng global service (IAM, CloudFront, Route 53, WAF)** → phải bật **cả hai** flag: `--is-multi-region-trail` **và** `--include-global-service-events`.
- Cẩn thận với flag có chữ **"no-"** ở đầu (`--no-include-global-service-events`) — dễ đọc lướt và hiểu nhầm là "có bật".
- **MFA Delete + KMS encryption trên S3 log bucket** = combo chuẩn cho yêu cầu "integrity + durability" của log compliance.

### TD explanation

The accounting firm requires a secure and durable logging solution that will track all of the activities of all AWS resources (such as EC2, S3, CloudFront, and IAM) on all regions. CloudTrail can be used for this case with multi-region trail enabled. However, CloudTrail will only cover the activities of the regional services (EC2, S3, RDS etc.) and not for global services such as IAM, CloudFront, AWS WAF, and Route 53.

The option that says: Create a new AWS CloudTrail trail in a new S3 bucket using the AWS CLI and also pass both the –is-multi-region-trail and –include-global-service-events parameters then encrypt log files using KMS encryption. Enable Multi-Factor Authentication (MFA) Delete on the S3 bucket and ensure that only authorized users can access the logs by configuring the bucket policies is correct because it provides security, integrity, and durability to your log data. In addition, it has the -include-global-service-events parameter enabled which will also include activity from global services such as IAM, Route 53, AWS WAF, and CloudFront.
The option that says: Create a new Amazon CloudWatch trail in a new S3 bucket using the AWS CLI and also pass both the –is-multi-region-trail and –include-global-service-events parameters then encrypt log files using KMS encryption. Enable Multi-Factor Authentication (MFA) Delete on the S3 bucket and ensure that only authorized users can access the logs by configuring the bucket policies is incorrect because you need to use CloudTrail instead of CloudWatch.
The option that says: Create a new Amazon CloudWatch trail in a new S3 bucket using the AWS CLI and also pass the –include-global-service-events parameter then encrypt log files using KMS encryption. Enable Multi-Factor Authentication (MFA) Delete on the S3 bucket and ensure that only authorized users can access the logs by configuring the bucket policies is incorrect because you need to use CloudTrail instead of CloudWatch. In addition, the –is-multi-region-trail parameter is also missing in this setup.
The option that says: Create a new AWS CloudTrail trail in a new S3 bucket using the AWS CLI and also pass the –no-include-global-service-events and –is-multi-region-trail parameter then encrypt log files using KMS encryption. Enable Multi-Factor Authentication (MFA) Delete on the S3 bucket and ensure that only authorized users can access the logs by configuring the bucket policies is incorrect. The –is-multi-region-trail is not enough as you also need to add the –include-global-service-events parameter to track the global service events. The –no-include-global-service-events parameter actually prevents CloudTrail from publishing events from global services such as IAM to the log files.

References:
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events
https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli.html

Check out this AWS CloudTrail Cheat Sheet:
https://tutorialsdojo.com/aws-cloudtrail/

</details>

<a id="q46"></a>

## Q46

A media company has a suite of internet-facing web applications hosted in US West (N. California) region in AWS. The architecture is composed of several On-Demand Amazon EC2 instances behind an Application Load Balancer, which is configured to use public SSL/TLS certificates. The Application Load Balancer also enables incoming HTTPS traffic through the fully qualified domain names (FQDNs) of the applications for SSL termination. A Solutions Architect has been instructed to upgrade the corporate web applications to a multi-region architecture that uses various AWS Regions such as ap-southeast-2, ca-central-1, eu-west-3, and so forth.
Which of the following approach should the Architect implement to ensure that all HTTPS services will continue to work without interruption?

- **A.** In each new AWS Region, request for SSL/TLS certificates using the AWS Certificate Manager for each FQDN. Associate the new certificates to the corresponding Application Load Balancer of the same AWS Region.
- **B.** Use the AWS KMS in the US West (N. California) region to request for SSL/TLS certificates for each FQDN which will be used to all regions. Associate the new certificates to the new Application Load Balancer on each new AWS Region that the Architect will add.
- **C.** In each new AWS Region, request for SSL/TLS certificates using AWS KMS for each FQDN. Associate the new certificates to the corresponding Application Load Balancer of the same AWS Region.
- **D.** Use the AWS Certificate Manager service in the US West (N. California) region to request for SSL/TLS certificates for each FQDN which will be used to all regions. Associate the new certificates to the new Application Load Balancer on each new AWS Region that the Architect will add.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** multi-Region HTTPS without interruption

⚠️ **Watch:** ACM certs are Regional (except us-east-1 for CloudFront)

🧠 **Rule:** New Region ALB → request ACM cert in that Region.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
US West (N. California): ALB + HTTPS (SSL/TLS cert) cho nhiều FQDN
Mở rộng multi-region: ap-southeast-2, ca-central-1, eu-west-3, ...
Yêu cầu: HTTPS phải hoạt động LIÊN TỤC, không đứt ở mọi region mới
```

Đáp án đúng: **A** — ở MỖI region mới, request cert ACM riêng cho từng FQDN, gắn cert đó vào ALB của đúng region đó. Anh chọn đúng A.

#### Vì sao A đúng

Nguyên tắc cốt lõi: **chứng chỉ ACM gắn với Application Load Balancer là resource theo Region** — không giống với chứng chỉ dùng cho CloudFront (chỉ CloudFront mới cho phép request cert ở us-east-1 và dùng chung cho phân phối toàn cầu). Vì ở đây service đích là **ALB**, nên với mỗi Region mới triển khai, phải **request cert ACM mới trong đúng Region đó**, rồi gắn vào ALB của Region đó. Đây là cách duy nhất đảm bảo HTTPS hoạt động không gián đoạn ở tất cả các Region.

#### Vì sao các phương án khác sai

- **B (AWS KMS ở N. California, dùng chung cho mọi region, gắn vào ALB mới):** sai công cụ — **KMS dùng để mã hóa dữ liệu (data encryption key), không phải dịch vụ cấp SSL/TLS certificate**. ACM mới là dịch vụ đúng cho việc này.
- **C (KMS ở mỗi region, gắn vào ALB tương ứng):** đúng ý tưởng "mỗi region request riêng" nhưng lại sai công cụ — vẫn dùng KMS thay vì ACM, nên vẫn không tạo ra được SSL/TLS certificate hợp lệ để gắn vào ALB.
- **D (ACM ở N. California, dùng 1 cert cho tất cả region, gắn vào ALB mới ở mọi region):** đúng công cụ (ACM) nhưng sai phạm vi sử dụng — cert ACM chỉ **dùng chung được nhiều region khi gắn vào CloudFront** (vì CloudFront phân phối cert đó ra khắp các edge location toàn cầu); còn khi gắn trực tiếp vào ALB, **mỗi Region phải có cert riêng được request tại Region đó**.

| Phương án | Dịch vụ dùng | Cert theo region riêng? | Đúng? |
|---|---|---|---|
| **A (đúng)** | ACM | Có, mỗi region request riêng | Có |
| B | KMS | Không (dùng chung 1 cert) | Sai công cụ + sai phạm vi |
| C | KMS | Có (nhưng sai công cụ) | Sai công cụ |
| D | ACM | Không (dùng chung 1 cert cho ALB) | Sai phạm vi |

#### Lưu ý thực tế

⚠️ Ngoại lệ duy nhất của quy tắc "ACM cert theo Region" là khi cert gắn vào **CloudFront** — lúc đó phải request cert tại **us-east-1 (N. Virginia)**, và CloudFront tự phân phối cert đó tới mọi edge location toàn cầu, không cần request lại ở các Region khác.

#### Quy tắc nhớ cho thi

- **"SSL/TLS certificate"** → luôn nghĩ tới **ACM**, không phải KMS.
- **"Gắn cert vào ALB/NLB ở nhiều Region"** → phải request cert **riêng cho mỗi Region**.
- **"Gắn cert vào CloudFront"** → request cert duy nhất tại **us-east-1**, dùng chung cho toàn cầu.
- **KMS** → chỉ dùng cho mã hóa dữ liệu (encryption keys), không tạo SSL/TLS certificate.

### TD explanation

AWS Certificate Manager is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources. SSL/TLS certificates are used to secure network communications and establish the identity of websites over the Internet as well as resources on private networks. AWS Certificate Manager removes the time-consuming manual process of purchasing, uploading, and renewing SSL/TLS certificates.
With AWS Certificate Manager, you can quickly request a certificate, deploy it on ACM-integrated AWS resources, such as Elastic Load Balancers, Amazon CloudFront distributions, and APIs on API Gateway, and let AWS Certificate Manager handle certificate renewals. It also enables you to create private certificates for your internal resources and manage the certificate lifecycle centrally. Public and private certificates provisioned through AWS Certificate Manager for use with ACM-integrated services are free. You pay only for the AWS resources you create to run your application. With AWS Certificate Manager Private Certificate Authority, you pay monthly for the operation of the private CA and for the private certificates you issue.

You can use the same SSL certificate from ACM in more than one AWS Region but it depends on whether you’re using Elastic Load Balancing or Amazon CloudFront. To use a certificate with Elastic Load Balancing for the same site (the same fully qualified domain name, or FQDN, or set of FQDNs) in a different Region, you must request a new certificate for each Region in which you plan to use it. To use an ACM certificate with Amazon CloudFront, you must request the certificate in the US East (N. Virginia) region. ACM certificates in this region that are associated with a CloudFront distribution are distributed to all the geographic locations configured for that distribution.
Hence, the correct answer is the option that says: In each new AWS Region, request for SSL/TLS certificates using the AWS Certificate Manager for each FQDN. Associate the new certificates to the corresponding Application Load Balancer of the same AWS Region.
The option that says: In each new AWS Region, request for SSL/TLS certificates using AWS KMS for each FQDN. Associate the new certificates to the corresponding Application Load Balancer of the same AWS Region is incorrect because AWS KMS is not the right service to use to generate the SSL/TLS certificates. You have to utilize ACM instead.
The option that says: Use the AWS KMS in the US West (N. California) region to request for SSL/TLS certificates for each FQDN which will be used to all regions. Associate the new certificates to the new Application Load Balancer on each new AWS Region that the Architect will add is incorrect. You have to use the AWS Certificate Manager (ACM) service to generate the certificates and not AWS KMS as this service is primarily used for data encryption. Moreover, you have to associate the certificates that were generated from the same AWS Region where the load balancer is launched.
The option that says: Use the AWS Certificate Manager service in the US West (N. California) region to request for SSL/TLS certificates for each FQDN which will be used to all regions. Associate the new certificates to the new Application Load Balancer on each new AWS Region that the Architect will add is incorrect. You can only use the same SSL certificate from ACM in more than one AWS Region if you are attaching it to your CloudFront distribution only, and not to your Application Load Balancer. To use a certificate with Elastic Load Balancing for the same site (the same fully qualified domain name, or FQDN, or set of FQDNs) in a different Region, you must request a new certificate for each Region in which you plan to use it.

References:
https://aws.amazon.com/certificate-manager/faqs/
https://aws.amazon.com/premiumsupport/knowledge-center/associate-acm-certificate-alb-nlb/
https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-add-or-delete-listeners.html#add-listener-console

Check out these AWS Certificate Manager and Elastic Load Balancer Cheat Sheets:
https://tutorialsdojo.com/aws-certificate-manager/
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

</details>

<a id="q50"></a>

## Q50

A top university has launched its serverless online portal using Lambda and API Gateway in AWS that enables its students to enroll, manage their class schedules, and see their grades online. After a few weeks, the portal abruptly stopped working and lost all of its data. The university hired an external cybersecurity consultant and based on the investigation, the outage was due to an SQL injection vulnerability on the portal’s login page in which the attacker simply injected the malicious SQL code. You also need to track historical changes to the rules and metrics associated with your firewall. 
Which of the following is the most suitable and cost-effective solution to avoid another SQL Injection attack against their infrastructure in AWS?

- **A.** Use AWS WAF to add a web access control list (web ACL) in front of the Lambda functions to block requests that contain malicious SQL code. Use AWS Firewall Manager, to track changes to your web access control lists (web ACLs) such as the creation and deletion of rules including the updates to the WAF rule configurations.
- **B.** Use AWS WAF to add a web access control list (web ACL) in front of the API Gateway to block requests that contain malicious SQL code. Use AWS Config to track changes to your web access control lists (web ACLs) such as the creation and deletion of rules including the updates to the WAF rule configurations.
- **C.** Block the IP address of the attacker in the Network Access Control List of your VPC and then set up a CloudFront distribution. Set up AWS WAF to add a web access control list (web ACL) in front of the CloudFront distribution to block requests that contain malicious SQL code. Use AWS Config to track changes to your web access control lists (web ACLs) such as the creation and deletion of rules including the updates to the WAF rule configurations.
- **D.** Create a new Application Load Balancer (ALB) and set up AWS WAF in the load balancer. Place the API Gateway behind the ALB and configure a web access control list (web ACL) in front of the ALB to block requests that contain malicious SQL code. Use AWS Firewall Manager to track changes to your web access control lists (web ACLs) such as the creation and deletion of rules including the updates to the WAF rule configurations.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** SQL injection on API Gateway; track rule changes

⚠️ **Watch:** Shield = DDoS, not SQLi

🧠 **Rule:** SQLi → WAF web ACL on API Gateway; change history → Config.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Serverless portal: Lambda + API Gateway
Bị SQL Injection ở login page → mất toàn bộ dữ liệu
Yêu cầu: chặn SQLi tiếp diễn + TRACK lịch sử thay đổi rules/metrics của firewall
         MOST cost-effective
```

Đáp án đúng: **B** — AWS WAF web ACL đặt trước API Gateway để chặn SQLi, dùng AWS Config để track thay đổi WAF rule. Anh chọn đúng B.

#### Vì sao B đúng

Hai phần yêu cầu, hai công cụ đúng: **(1)** chặn SQL injection → **AWS WAF** là firewall tầng ứng dụng, có sẵn rule pattern cho SQLi/XSS, gắn được trực tiếp vào **API Gateway** — nơi thực sự nhận request từ client (Lambda phía sau không expose trực tiếp ra internet để gắn WAF). **(2)** "track historical changes to rules and metrics" → **AWS Config** ghi lại và theo dõi thay đổi cấu hình tài nguyên, bao gồm việc tạo/xóa rule và update rule configuration của web ACL — đúng khớp yêu cầu "track lịch sử thay đổi" trong đề.

#### Vì sao các phương án khác sai

- **A (WAF trước Lambda functions, dùng Firewall Manager để track):** sai vị trí đặt WAF — WAF gắn trực tiếp vào **API Gateway**, không gắn trực tiếp vào Lambda function; và **Firewall Manager dùng để quản lý firewall tập trung qua nhiều AWS account trong Organization**, không phải công cụ track lịch sử thay đổi rule — AWS Config mới đúng việc này.
- **C (Block IP kẻ tấn công ở NACL + dựng CloudFront + WAF trước CloudFront + Config):** thêm CloudFront là **không cần thiết và tốn thêm chi phí** — đề không yêu cầu scale toàn cầu/CDN, chỉ cần chặn SQLi tại điểm vào là API Gateway; việc chặn 1 IP cụ thể ở NACL cũng không giải quyết gốc vấn đề (kẻ tấn công đổi IP khác vẫn injection được).
- **D (Tạo mới ALB, đặt API Gateway sau ALB, WAF ở ALB, dùng Firewall Manager):** tạo thêm ALB là **chi phí phát sinh không cần thiết** (API Gateway không cần ALB đứng trước để gắn WAF — WAF gắn trực tiếp vào API Gateway được); Firewall Manager cũng sai vai trò như phương án A.

| Phương án | WAF đặt ở đâu | Track thay đổi rule | Thêm chi phí không cần thiết? |
|---|---|---|---|
| **B (đúng)** | API Gateway | AWS Config | Không |
| A | Lambda (sai vị trí) | Firewall Manager (sai) | — |
| C | CloudFront | AWS Config | Có (CloudFront không cần) |
| D | ALB mới | Firewall Manager (sai) | Có (ALB mới không cần) |

#### Lưu ý thực tế

⚠️ Phân biệt rõ: **AWS Firewall Manager** = quản lý policy WAF/Shield tập trung **qua nhiều account trong AWS Organizations**; **AWS Config** = theo dõi lịch sử thay đổi cấu hình của một resource cụ thể (ví dụ rule của 1 web ACL). Đề hỏi "track historical changes to the rules" của **một** firewall — đúng là việc của Config, không phải Firewall Manager.

#### Quy tắc nhớ cho thi

- **"SQL injection / XSS trên web app dùng API Gateway"** → **AWS WAF web ACL gắn trực tiếp vào API Gateway**.
- **"Track lịch sử thay đổi rule/config của 1 resource"** → **AWS Config**.
- **"Quản lý firewall tập trung nhiều account trong Organization"** → **AWS Firewall Manager** (không phải Config).
- Thêm CloudFront hoặc ALB chỉ khi đề thật sự cần CDN/global scale hoặc load balancing — nếu không, đó là chi phí thừa, loại ngay khi thấy "cost-effective".

### TD explanation

AWS WAF is a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. With AWS Config, you can track changes to WAF web access control lists (web ACLs). For example, you can record the creation and deletion of rules and rule actions, as well as updates to WAF rule configurations.

AWS WAF gives you control over which traffic to allow or block to your web applications by defining customizable web security rules. You can use AWS WAF to create custom rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that are designed for your specific application. New rules can be deployed within minutes, letting you respond quickly to changing traffic patterns. Also, AWS WAF includes a full-featured API that you can use to automate the creation, deployment, and maintenance of web security rules.
In this scenario, the best option is to deploy WAF in front of the API Gateway. Hence the correct answer is the option that says: Use AWS WAF to add a web access control list (web ACL) in front of the API Gateway to block requests that contain malicious SQL code. Use AWS Config to track changes to your web access control lists (web ACLs) such as the creation and deletion of rules including the updates to the WAF rule configurations.
The option that says: Use AWS WAF to add a web access control list (web ACL) in front of the Lambda functions to block requests that contain malicious SQL code. Use AWS Firewall Manager, to track changes to your web access control lists (web ACLs) such as the creation and deletion of rules including the updates to the WAF rule configurations is incorrect because you have to use AWS WAF in front of the API Gateway and not directly to the Lambda functions. AWS Firewall Manager is primarily used to manage your Firewall across multiple AWS accounts under your AWS Organizations and hence, it is not suitable for tracking changes to WAF web access control lists. You should use AWS Config instead.
The option that says: Block the IP address of the attacker in the Network Access Control List of your VPC and then set up a CloudFront distribution. Set up AWS WAF to add a web access control list (web ACL) in front of the CloudFront distribution to block requests that contain malicious SQL code. Use AWS Config to track changes to your web access control lists (web ACLs) such as the creation and deletion of rules including the updates to the WAF rule configurations is incorrect. Even though it is valid to use AWS WAF with CloudFront, it entails an additional and unnecessary cost to launch a CloudFront distribution for this scenario. There is no requirement that the serverless online portal should be scalable and be accessible around the globe hence, a CloudFront distribution is not necessary.
The option that says: Create a new Application Load Balancer (ALB) and set up AWS WAF in the load balancer. Place the API Gateway behind the ALB and configure a web access control list (web ACL) in front of the ALB to block requests that contain malicious SQL code. Use AWS Firewall Manager to track changes to your web access control lists (web ACLs) such as the creation and deletion of rules including the updates to the WAF rule configurations is incorrect. Launching a new Application Load Balancer entails additional cost and is not cost-effective. In addition, AWS Firewall manager is primarily used to manage your Firewall across multiple AWS accounts under your AWS Organizations. Using AWS Config is much more suitable for tracking changes to WAF web access control lists.

References:
https://aws.amazon.com/waf/
https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html

Check out this AWS WAF Cheat Sheet:
https://tutorialsdojo.com/aws-waf/

</details>

<a id="q54"></a>

## Q54

A leading financial company is planning to launch its Node.js application with an Amazon RDS MariaDB database to serve its clients worldwide. The application will run on both on-premises servers as well as Reserved EC2 instances. To comply with the company’s strict security policy, the database credentials must be encrypted both at rest and in transit. These credentials will be used by the application servers to connect to the database. The Solutions Architect is tasked to manage all of the aspects of the application architecture and production deployment. 
How should the Architect automate the deployment process of the application in the MOST secure manner?

- **A.** Upload the database credentials with a Secure String data type in AWS Systems Manager Parameter Store. Install the AWS SSM agent on all servers. Set up a new IAM role that enables access and decryption of the database credentials from SSM Parameter Store. Associate this role to all on-premises servers and EC2 instances. Use Elastic Beanstalk to host and manage the application on both on-premises servers and EC2 instances. Deploy the succeeding application revisions to AWS and on-premises servers using Elastic Beanstalk.
- **B.** Upload the database credentials with key rotation in AWS Secrets Manager. Install the AWS SSM agent on all servers. Set up a new IAM role that enables access and decryption of the database credentials from SSM Parameter Store. Associate this role to all on-premises servers and EC2 instances. Use Elastic Beanstalk to host and manage the application on both on-premises servers and EC2 instances. Deploy the succeeding application revisions to AWS and on-premises servers using Elastic Beanstalk.
- **C.** Upload the database credentials with a Secure String data type in AWS Systems Manager Parameter Store. Install the AWS SSM agent on all servers. Set up a new IAM role that enables access and decryption of the database credentials from SSM Parameter Store. Associate this role to the EC2 instances. Create an IAM Service Role that will be associated with the on-premises servers. Deploy the application packages to the EC2 instances and on-premises servers using AWS CodeDeploy.
- **D.** Upload the database credentials with a Secure String data type in AWS Systems Manager Parameter Store. Install the AWS SSM agent on all servers. Set up a new IAM role that enables access and decryption of the database credentials from SSM Parameter Store. Attach this IAM policy to the instance profile for CodeDeploy-managed EC2 instances. Associate the same policy as well to the on-premises instances. Using AWS CodeDeploy, launch the application packages to the Amazon EC2 instances and on-premises servers.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** DB creds encrypted at rest + in transit; automated deploy

⚠️ **Watch:** ⚠️ Q74: when ROTATION is required → Secrets Manager, not Parameter Store

🧠 **Rule:** Plain secret storage → Parameter Store SecureString + IAM role + KMS decrypt.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises servers                  EC2 instances (Reserved)
        │                                     │
        └──────────► SSM Parameter Store ◄────┘
                (SecureString, DB credentials)
                          │
        IAM role riêng cho từng loại tài nguyên:
        - EC2        → instance role
        - On-premises → IAM Service Role (hybrid activation)
                          │
                  Deploy bằng AWS CodeDeploy
                (chạy được cả trên EC2 + on-prem)
```

Yêu cầu: credentials mã hóa **at rest + in transit**, deploy tự động lên **cả EC2 và on-premises**. Anh chọn đúng **C**.

#### Vì sao C đúng

**C đúng** vì đáp ứng đủ 2 điều kiện khó nhất của đề:

1. **Mã hóa credentials:** SecureString trong Parameter Store dùng KMS để mã hóa at rest; kết nối tới SSM API qua HTTPS nên at rest + in transit đều được đáp ứng.
2. **Deploy lên cả EC2 và on-premises:** chỉ **AWS CodeDeploy** làm được việc này. Muốn on-premises server dùng được SSM, phải cài SSM agent và gán một **IAM Service Role** (dành riêng cho hybrid activation) — khác với IAM role gán cho EC2 instance (đi qua instance profile). Đây là điểm phân biệt C với các đáp án khác.

#### Từng đáp án sai vì đâu

- **A sai:** dùng Elastic Beanstalk để host & deploy trên on-premises — Elastic Beanstalk chỉ quản lý được EC2, không deploy được lên máy chủ vật lý ngoài AWS.
- **B sai:** giống lỗi của A (vẫn dùng Elastic Beanstalk cho on-premises), lại còn đổi credentials store thành Secrets Manager nhưng vẫn giữ nguyên phần IAM role tham chiếu Parameter Store — không nhất quán, và không giải quyết được vấn đề deploy on-premises.
- **D sai:** gán **IAM Policy** trực tiếp vào instance profile/on-premises instance thay vì dùng **IAM Role**. Muốn instance (hoặc SSM hybrid activation) lấy được quyền decrypt từ Parameter Store, phải đi qua một IAM Role được assume, không phải attach Policy trực tiếp kiểu đó.

| Đáp án | Credentials store | Deploy được on-premises? | Vấn đề |
|---|---|---|---|
| **C (đúng)** | Parameter Store SecureString | Có, qua CodeDeploy + Service Role | Không |
| A | Parameter Store SecureString | Không (Elastic Beanstalk) | Sai công cụ deploy |
| B | Secrets Manager | Không (Elastic Beanstalk) | Sai công cụ deploy |
| D | Parameter Store SecureString | Có (CodeDeploy) | Dùng Policy thay vì Role |

#### ⚠️ Lỗi lặp lại (liên quan Q74)

Q74 hỏi ngược lại: khi đề yêu cầu **"key rotation" / "lifecycle management"** cho credentials trong ECS Fargate, đáp án đúng là **Secrets Manager**, không phải Parameter Store — vì Parameter Store không có rotation built-in. Ở Q54, đề **không** đòi rotation, chỉ đòi mã hóa + IAM role, nên Parameter Store SecureString vẫn là lựa chọn hợp lý (rẻ hơn, đủ dùng). Đừng suy ra "cứ thấy DB credentials là chọn Secrets Manager" — phải đọc kỹ từ khóa "rotation" có xuất hiện hay không.

#### Quy tắc nhớ cho thi

- **Không có "rotation"** → Parameter Store SecureString đủ dùng, rẻ hơn Secrets Manager.
- **Có "rotation" / "lifecycle management"** → Secrets Manager.
- **Deploy lên cả EC2 và on-premises** → CodeDeploy (Elastic Beanstalk KHÔNG hỗ trợ on-premises).
- **Cấp quyền cho service/instance** → luôn là IAM Role, không phải IAM Policy gán trực tiếp cho instance.
- On-premises server tham gia SSM hybrid environment → cần một **IAM Service Role** riêng (khác EC2 instance role).

### TD explanation

AWS Systems Manager Parameter Store provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, and license codes as parameter values. You can store values as plain text or encrypted data. You can then reference values by using the unique name that you specified when you created the parameter. Highly scalable, available, and durable, Parameter Store is backed by the AWS Cloud.
Servers and virtual machines (VMs) in a hybrid environment require an IAM role to communicate with the Systems Manager service. The role grants AssumeRole trust to the Systems Manager service. You only need to create the service role for a hybrid environment once for each AWS account.
Users in your company or organization who will use Systems Manager on your hybrid machines must be granted permission in IAM to call the SSM API.

Service role: A service role is an AWS Identity and Access Management (IAM) that grants permissions to an AWS service so that the service can access AWS resources. Only a few Systems Manager scenarios require a service role. When you create a service role for Systems Manager, you choose the permissions to grant in order for it to access or interact with other AWS resources.
Service-linked role: A service-linked role is predefined by Systems Manager and includes all the permissions that the service requires to call other AWS services on your behalf.
If you plan to use Systems Manager to manage on-premises servers and virtual machines (VMs) in what is called a hybrid environment, you must create an IAM role for those resources to communicate with the Systems Manager service.
Hence, the correct answer is: Upload the database credentials with a Secure String data type in AWS Systems Manager Parameter Store. Install the AWS SSM agent on all servers. Set up a new IAM role that enables access and decryption of the database credentials from SSM Parameter Store. Associate this role to the EC2 instances. Create an IAM Service Role that will be associated with the on-premises servers. Deploy the application packages to the EC2 instances and on-premises servers using AWS CodeDeploy.
The option that says: Upload the database credentials with a Secure String data type in AWS Systems Manager Parameter Store. Install the AWS SSM agent on all servers. Set up a new IAM role that enables access and decryption of the database credentials from SSM Parameter Store. Associate this role to all on-premises servers and EC2 instances. Use Elastic Beanstalk to host and manage the application on both on-premises servers and EC2 instances. Deploy the succeeding application revisions to AWS and on-premises servers using Elastic Beanstalk is incorrect. You can’t deploy an application to your on-premises servers using Elastic Beanstalk. This is only applicable to your Amazon EC2 instances.
The option that says: Upload the database credentials with a Secure String data type in AWS Systems Manager Parameter Store. Install the AWS SSM agent on all servers. Set up a new IAM role that enables access and decryption of the database credentials from SSM Parameter Store. Attach this IAM policy to the instance profile for CodeDeploy-managed EC2 instances. Associate the same policy as well to the on-premises instances. Using AWS CodeDeploy, launch the application packages to the Amazon EC2 instances and on-premises servers is incorrect. You have to use an IAM Role and not an IAM Policy to grant access to AWS Systems Manager Parameter Store.
The option that says: Upload the database credentials with key rotation in AWS Secrets Manager. Install the AWS SSM agent on all servers. Set up a new IAM role that enables access and decryption of the database credentials from SSM Parameter Store. Associate this role to all on-premises servers and EC2 instances. Use Elastic Beanstalk to host and manage the application on both on-premises servers and EC2 instances. Deploy the succeeding application revisions to AWS and on-premises servers using Elastic Beanstalk is incorrect. Although you can store the database credentials to AWS Secrets Manager, you still can’t deploy an application to your on-premises servers using Elastic Beanstalk.

References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-service-role.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-service-role.html

Check out this AWS Systems Manager Cheat Sheet:
https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q56"></a>

## Q56

A company has launched a company-wide bug bounty program to find and patch up security vulnerabilities in your web applications as well as the underlying cloud resources. As the solutions architect, you are focused on checking system vulnerabilities on AWS resources for DDoS attacks. Due to budget constraints, the company cannot afford to enable AWS Shield Advanced to prevent higher-level attacks.
Which of the following are the best techniques to help mitigate Distributed Denial of Service (DDoS) attacks for cloud infrastructure hosted in AWS? (Select TWO.)

- **A.** Use Reserved EC2 instances to ensure that each instance has the maximum performance possible. Use AWS WAF to protect your web applications from common web exploits that could affect application availability.
- **B.** Add multiple Elastic Network Interfaces to each EC2 instance and use Enhanced Networking to increase the network bandwidth.
- **C.** Use S3 as a POSIX-compliant storage instead of EBS Volumes for storing data. Install the SSM agent to all of your instances and use AWS Systems Manager Patch Manager to automatically patch your instances.
- **D.** Use an Amazon CloudFront distribution for both static and dynamic content of your web applications. Add CloudWatch alerts to automatically look and notify the Operations team for high CPUUtilization and NetworkIn metrics, as well as to trigger Auto Scaling of your EC2 instances.
- **E.** Use an Application Load Balancer (ALB) to reduce the risk of overloading your application by distributing traffic across many backend instances. Integrate AWS WAF and the ALB to protect your web applications from common web exploits that could affect application availability.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D, E (you answered correctly)

🔑 **Key words:** DDoS mitigation without Shield Advanced (Select TWO)

⚠️ **Watch:** Relates to Q22 (NACL + Shield)

🧠 **Rule:** CloudFront + ALB + WAF + Auto Scaling + CloudWatch alarms.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Internet
   │  (DDoS attack, không có Shield Advanced)
   ▼
Amazon CloudFront (static + dynamic content)
   │  chỉ nhận kết nối TCP hợp lệ, chặn SYN flood/UDP reflection
   ▼
Application Load Balancer  ── + AWS WAF (chặn SQLi, XSS)
   │  phân tải qua nhiều backend instance
   ▼
EC2 fleet (Auto Scaling, kích hoạt bởi CloudWatch alarms
           trên CPUUtilization / NetworkIn)
```

Yêu cầu: giảm thiểu DDoS mà **không có Shield Advanced** (Select TWO). Anh chọn đúng **D, E**.

#### Vì sao D và E đúng

**D đúng** vì hai kỹ thuật kết hợp: **CloudFront** chỉ chuyển tiếp các kết nối TCP well-formed lên origin, tự loại bỏ SYN flood/UDP reflection trước khi chạm tới hạ tầng của anh; còn **CloudWatch alarm + Auto Scaling** đảm bảo khi traffic tăng đột biến (dù là DDoS hay flash crowd) thì fleet EC2 tự phình ra để chịu tải, giữ ứng dụng available.

**E đúng** vì **ALB** phân traffic ra nhiều backend instance nên một điểm không bị "gánh" hết traffic tấn công, và ALB tự scale theo traffic; tích hợp thêm **AWS WAF** để chặn các pattern tấn công tầng ứng dụng (SQLi, XSS) — đây chính là các attack vector Shield Advanced không xử lý (Shield chỉ lo network/transport layer), nên WAF là bù đắp hợp lý khi không có Shield Advanced.

Hai đáp án tạo thành **một giải pháp phòng thủ nhiều lớp**: CloudFront ở edge (network layer) + ALB/WAF ở gần origin (application layer) + Auto Scaling để hấp thụ tải dư.

#### Mỗi đáp án sai vì đâu

- **A sai:** Reserved Instance chỉ là mô hình thanh toán, **không** tăng hiệu năng CPU/network so với On-Demand cùng loại — không giúp gì cho việc chống DDoS.
- **B sai:** thêm ENI + Enhanced Networking chỉ tăng băng thông network, nhưng CPU của instance vẫn bị request DDoS làm bão hòa → app vẫn treo, không giải quyết gốc vấn đề.
- **C sai:** đổi EBS sang S3 để lưu data là bài toán scalability lưu trữ, không liên quan DDoS; hơn nữa **S3 không phải POSIX-compliant** — chi tiết sai kỹ thuật rõ ràng trong đáp án.

| Đáp án | Lớp bảo vệ | Vấn đề với DDoS |
|---|---|---|
| **D (đúng)** | Edge (CloudFront) + Auto Scaling | Không |
| **E (đúng)** | ALB + WAF (application layer) | Không |
| A | Compute pricing model | Không tăng performance |
| B | Network throughput | CPU vẫn bão hòa |
| C | Storage service | Không liên quan; sai fact về S3 |

#### Quy tắc nhớ cho thi

- **Không có Shield Advanced, cần chống DDoS** → CloudFront (edge, chặn SYN/UDP flood) + ALB/WAF (application layer) + Auto Scaling + CloudWatch alarms.
- **"Reserved Instance"** không bao giờ là câu trả lời cho vấn đề performance/DDoS — chỉ là giá.
- **S3 không phải POSIX-compliant** — nếu thấy option nói vậy, loại ngay.
- Thêm ENI/Enhanced Networking chỉ giải quyết network bandwidth, không giải quyết CPU saturation.

### TD explanation

The following options are the correct answers in this scenario as they can help mitigate the effects of DDoS attacks:
– Use an Amazon CloudFront distribution for both static and dynamic content of your web applications. Add CloudWatch alerts to automatically look and notify the Operations team for high CPUUtilization and NetworkIn metrics, as well as to trigger Auto Scaling of your EC2 instances.
– Use an Application Load Balancer (ALB) to reduce the risk of overloading your application by distributing traffic across many backend instances. Integrate AWS WAF and the ALB to protect your web applications from common web exploits that could affect application availability.
Amazon CloudFront is a content delivery network (CDN) service that can be used to deliver your entire website, including static, dynamic, streaming, and interactive content. Persistent TCP connections and variable time-to-live (TTL) can be used to accelerate delivery of content, even if it cannot be cached at an edge location. This allows you to use Amazon CloudFront to protect your web application, even if you are not serving static content. Amazon CloudFront only accepts well-formed connections to prevent many common DDoS attacks like SYN floods and UDP reflection attacks from reaching your origin.

Larger DDoS attacks can exceed the size of a single Amazon EC2 instance. To mitigate these attacks, you will want to consider options for load balancing excess traffic. With Elastic Load Balancing (ELB), you can reduce the risk of overloading your application by distributing traffic across many backend instances. ELB can scale automatically, allowing you to manage larger volumes of unanticipated traffic, like flash crowds or DDoS attacks.
Another way to deal with application layer attacks is to operate at scale. In the case of web applications, you can use ELB to distribute traffic to many Amazon EC2 instances that are overprovisioned or configured to auto scale for the purpose of serving surges of traffic, whether it is the result of a flash crowd or an application layer DDoS attack. Amazon CloudWatch alarms are used to initiate Auto Scaling, which automatically scales the size of your Amazon EC2 fleet in response to events that you define. This protects application availability even when dealing with an unexpected volume of requests.
The option that says: Use S3 as a POSIX-compliant storage instead of EBS Volumes for storing data. Install the SSM agent to all of your instances and use AWS Systems Manager Patch Manager to automatically patch your instances is incorrect because using S3 instead of EBS Volumes is mainly for addressing scalability to your storage requirements and not for avoiding DDoS attacks. In addition, Amazon S3 is not a POSIX-compliant storage.
The option that says: Add multiple Elastic Network Interfaces to each EC2 instance and use Enhanced Networking to increase the network bandwidth is incorrect. Even if you add multiple ENIs and are using Enhanced Networking to increase the network throughput of the instances, the CPU of the instance will be saturated with the DDoS requests which will cause the application to be unresponsive.
The option that says: Use Reserved EC2 instances to ensure that each instance has the maximum performance possible. Use AWS WAF to protect your web applications from common web exploits that could affect application availability is incorrect because using Reserved EC2 instances does not provide any additional computing performance compared to other EC2 types.

References:
https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html
https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html
https://d0.awsstatic.com/whitepapers/DDoS_White_Paper_June2015.pdf

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

Best practices on DDoS Attack Mitigation:
https://youtu.be/HnoZS5jj7pk

</details>

<a id="q59"></a>

## Q59

A global financial company is launching its new trading platform in AWS which allows people to buy and sell their bitcoin, ethereum, ripple, and other cryptocurrencies, as well as access to various financial reports. To meet the anti-money laundering and counter-terrorist financing (AML/CFT) measures compliance, all report files of the trading platform must not be accessible in certain countries which are listed in the Financial Action Task Force (FATF) list of non-cooperative countries or territories. You were given a task to ensure that the company complies with this requirement to avoid hefty monetary penalties. 
In this scenario, what is the best way to satisfy this security requirement in AWS while still delivering content to users around the globe with lower latency?

- **A.** Deploy the trading platform using Elastic Beanstalk and deny all incoming traffic from the IP addresses of the blacklisted countries in the Network Access Control List (ACL) of the VPC.
- **B.** Use Route 53 with a Geolocation routing policy that blocks all traffic from the blacklisted countries.
- **C.** Create a CloudFront distribution with Geo-Restriction enabled to block all of the blacklisted countries from accessing the trading platform.
- **D.** Use Route 53 with a Geoproximity routing policy that blocks all traffic from the blacklisted countries.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** block sanctioned countries; low latency globally

⚠️ **Watch:** Route 53 geolocation doesn't block

🧠 **Rule:** Country block → CloudFront geo restriction (or WAF geo match).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users toàn cầu ──► CloudFront distribution (edge locations, low latency)
                        │
                    Geo-Restriction ENABLED
                        │
              ┌─────────┴─────────┐
       Allowed countries      FATF blacklist countries
       → serve content        → BLOCK truy cập report files
```

Yêu cầu: chặn các nước trong FATF blacklist truy cập report files, **đồng thời** vẫn phải phục vụ người dùng toàn cầu với **latency thấp**. Đáp án đúng: **C**. Anh chọn đúng C.

#### Vì sao C đúng

**C đúng** vì CloudFront **Geo-Restriction (geoblocking)** vừa giải quyết đúng yêu cầu bảo mật (chặn truy cập ở cấp quốc gia dựa trên whitelist/blacklist) **vừa giữ nguyên lợi ích low-latency** của CDN — CloudFront vẫn phục vụ các country được phép qua edge location gần nhất. Đây là tính năng tích hợp sẵn trong CloudFront distribution, không cần thêm hạ tầng ngoài.

#### Từng đáp án sai vì đâu

- **A sai:** chặn IP của từng blacklisted country trong VPC Network ACL — về lý thuyết có thể làm nhưng đòi hỏi maintain danh sách IP range khổng lồ, thay đổi liên tục, rất nhiều công sức và không phải giải pháp được recommend cho geoblocking cấp quốc gia.
- **B sai:** Route 53 **Geolocation routing policy** chỉ dùng để **định tuyến traffic dựa theo vị trí user** (đưa user đến resource gần nhất/khu vực phù hợp) — nó không có khả năng "chặn" truy cập, và Route 53 chỉ làm DNS resolution, không cung cấp low-latency content delivery như CloudFront.
- **D sai:** Route 53 **Geoproximity routing policy** dùng để định tuyến dựa theo **vị trí của resource** (và dịch traffic giữa các resource ở vị trí khác nhau) — sai mục đích hoàn toàn, không liên quan đến việc chặn quốc gia, và cũng không cung cấp low-latency delivery.

| Đáp án | Cơ chế | Chặn được quốc gia? | Cung cấp low-latency? |
|---|---|---|---|
| **C (đúng)** | CloudFront Geo-Restriction | Có | Có |
| A | VPC NACL theo IP | Có (nhưng cực nhiều công sức) | Không |
| B | Route 53 Geolocation | Không (chỉ routing) | Không |
| D | Route 53 Geoproximity | Không (chỉ routing theo resource) | Không |

#### Quy tắc nhớ cho thi

- **"Block/chặn theo quốc gia"** → CloudFront **Geo-Restriction** (hoặc AWS WAF geo match) — không phải Route 53.
- **Route 53 Geolocation** = route theo vị trí **user**; **Geoproximity** = route theo vị trí **resource** — cả hai chỉ routing, không block.
- Route 53 chỉ làm DNS resolution, **không** cung cấp low-latency content delivery như CloudFront.
- Thấy "block theo IP range của cả 1 quốc gia trong NACL" → luôn là bẫy tốn công, có công cụ chuyên dụng hơn (CloudFront/WAF).

### TD explanation

You can use geo restriction – also known as geoblocking – to prevent users in specific geographic locations from accessing content that you’re distributing through a CloudFront web distribution. To use geo restriction, you have two options:

Use the CloudFront geo restriction feature. Use this option to restrict access to all of the files that are associated with a distribution and to restrict access at the country level.
Use a third-party geolocation service. Use this option to restrict access to a subset of the files that are associated with a distribution or to restrict access at a finer granularity than the country level.

When a user requests your content, CloudFront typically serves the requested content regardless of where the user is located. If you need to prevent users in specific countries from accessing your content, you can use the CloudFront geo restriction feature to do one of the following:

Allow your users to access your content only if they’re in one of the countries on a whitelist of approved countries.
Prevent your users from accessing your content if they’re in one of the countries on a blacklist of banned countries.

For example, if a request comes from a country where, for copyright reasons, you are not authorized to distribute your content, you can use CloudFront geo restriction to block the request.
Hence, the option that says: Create a CloudFront distribution with Geo-Restriction enabled to block all of the blacklisted countries from accessing the trading platform is correct. CloudFront can provide the users low-latency access to the files as well as block certain countries on the FTAF list.
The option that says: Deploy the trading platform using Elastic Beanstalk and deny all incoming traffic from the IP addresses of the blacklisted countries in the Network Access Control List (ACL) of the VPC is incorrect. Blocking all of the IP addresses of each blacklisted country in the Network Access Control List entails a lot of work and is not a recommended way to accomplish the task. Using CloudFront geo restriction feature is a better solution for this.
The following options are incorrect because Route 53 only provides Domain Name Resolution and sends the requests based on the configured entries. It does not provide low-latency access to users around the globe, unlike CloudFront.
Use Route 53 with a Geolocation routing policy that blocks all traffic from the blacklisted countries.
Use Route 53 with a Geoproximity routing policy that blocks all traffic from the blacklisted countries.
Geolocation routing policy is used when you want to route traffic based on the location of your users while Geoproximity routing policy is for scenarios where you want to route traffic based on the location of your resources and, optionally, shift traffic from resources on one location to resources in another.

Reference:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

Latency Routing vs Geoproximity Routing vs Geolocation Routing:
https://tutorialsdojo.com/aws-cheat-sheet-latency-routing-vs-geoproximity-routing-vs-geolocation-routing/

Comparison of AWS Services Cheat Sheets:
https://tutorialsdojo.com/comparison-of-aws-services-for-udemy-students/

</details>

<a id="q67"></a>

## Q67

A company runs a Flight Deals web application which is currently hosted on their on-premises data center. The website hosts high-resolution photos of top tourist destinations in the world and uses a third-party payment platform to accept payments. Recently, the company heavily invested in their global marketing campaign and there is a high probability that the incoming traffic to their Flight Deals website will increase in the coming days. Due to a tight deadline, the company does not have the time to fully migrate the website to the AWS cloud. A set of security rules that block common attack patterns, such as SQL injection and cross-site scripting should also be implemented to improve website security. 
Which of the following options will maintain the website’s functionality despite the massive amount of incoming traffic?

- **A.** Use the AWS Application Migration Service to easily migrate the website from your on-premises data center to your VPC. Create an Auto Scaling group to automatically scale the web tier based on the incoming traffic. Deploy AWS WAF on the Amazon CloudFront distribution to protect the website from common web attacks.
- **B.** Use CloudFront to cache and distribute the high resolution images and other static assets of the website. Deploy AWS WAF on the Amazon CloudFront distribution to protect the website from common web attacks.
- **C.** Generate an AMI based on the existing Flight Deals website. Launch  the AMI to a fleet of EC2 instances with Auto Scaling group enabled, for it to automatically scale up or scale down based on the incoming traffic. Place these EC2 instances behind an ALB which can balance traffic between the web servers in the on-premises data center and the web servers hosted in AWS.
- **D.** Create and configure an S3 bucket as a static website hosting. Move the web domain of the website from your on-premises data center to Route 53 then route the newly created S3 bucket as the origin. Enable Amazon S3 server-side encryption with AWS Key Management Service managed keys.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** massive traffic of hi-res images; block SQLi/XSS

⚠️ **Watch:** WAF on CloudFront protects at the edge

🧠 **Rule:** Static assets → CloudFront; common web attacks → WAF on CloudFront.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises data center                     AWS
┌────────────────────────┐
│ Flight Deals website    │
│ - high-res photos       │      CloudFront distribution
│ - dynamic (payment)     │  ◄── cache static assets (photos)
│ - deadline gấp,          │      │
│   không kịp migrate      │      └── AWS WAF (chặn SQLi, XSS)
└────────────────────────┘                    │
        ▲ origin (custom origin: web server on-prem)
        └──────────────────────────────────────┘
```

Yêu cầu: traffic tăng mạnh do marketing campaign, **không đủ thời gian** migrate hẳn lên AWS, cần chặn SQLi/XSS. Đáp án đúng: **B**. Anh chọn đúng B.

#### Vì sao B đúng

**B đúng** vì đây là giải pháp **không cần migrate** — CloudFront hỗ trợ **custom origin**, tức là trỏ thẳng về web server on-premises hiện tại mà không cần thay đổi hạ tầng backend. CloudFront sẽ cache các file ảnh độ phân giải cao (static assets), giảm tải rất nhiều cho origin on-premises trong lúc traffic tăng đột biến, đồng thời mang lại tốc độ tải trang nhanh hơn cho người dùng toàn cầu. Gắn **AWS WAF** trực tiếp trên CloudFront distribution giải quyết đúng yêu cầu chặn SQL injection/XSS mà không cần triển khai thêm hạ tầng hay quản lý SSL/reverse proxy riêng.

#### Từng đáp án sai vì đâu

- **A sai:** dùng AWS Application Migration Service để migrate hẳn website lên VPC — đúng về mặt kỹ thuật (scale tốt hơn) nhưng **sai về ràng buộc thời gian**: đề nói rõ công ty không có thời gian để migrate đầy đủ trước deadline.
- **C sai:** đây là mô hình hybrid với EC2 + ALB cân bằng traffic giữa on-prem và AWS — nhưng thiếu điều kiện tiên quyết là kết nối riêng (**Direct Connect hoặc VPN**) giữa on-prem và VPC, mà đề không hề đề cập tới hạ tầng này. Ngoài ra, ứng dụng phục vụ người dùng toàn cầu nên CloudFront vẫn phù hợp hơn ALB đơn thuần.
- **D sai:** chuyển hẳn sang S3 static website hosting — nhưng website này là **dynamic** (có payment/booking), không thể host như static site trên S3; đổi cả domain sang Route 53 cũng tốn thời gian, đi ngược lại ràng buộc "deadline gấp".

| Đáp án | Cách tiếp cận | Vấn đề |
|---|---|---|
| **B (đúng)** | CloudFront (custom origin) + WAF, giữ nguyên backend on-prem | Không |
| A | Migrate app + Auto Scaling + WAF | Không đủ thời gian migrate |
| C | ALB cân bằng on-prem + AWS | Thiếu Direct Connect/VPN; sai công cụ cho global traffic |
| D | S3 static hosting + Route 53 | Website là dynamic, không host được trên S3 static |

#### Quy tắc nhớ cho thi

- **"Không đủ thời gian migrate" + "traffic tăng mạnh"** → CloudFront với **custom origin** trỏ về hạ tầng hiện tại, không cần đổi backend.
- **AWS WAF gắn trên CloudFront/ALB/API Gateway** để chặn SQLi/XSS — không cần software/DNS/SSL setup thêm.
- Muốn load balance giữa on-premises và AWS qua ALB → phải có **Direct Connect hoặc VPN** trước, nếu đề không nói có thì loại phương án này.
- Website **dynamic** (payment, booking, login...) → không thể host tĩnh trên S3 static website.

### TD explanation

Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you’re serving with CloudFront, the user is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.
AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources. AWS WAF gives you control over how traffic reaches your applications by enabling you to create security rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that filter out specific traffic patterns you define. You can get started quickly using Managed Rules for AWS WAF, a pre-configured set of rules managed by AWS or AWS Marketplace Sellers. The Managed Rules for WAF address issues like the OWASP Top 10 security risks. These rules are regularly updated as new issues emerge. AWS WAF includes a full-featured API that you can use to automate the creation, deployment, and maintenance of security rules.

AWS WAF is easy to deploy and protect applications deployed on either Amazon CloudFront as part of your CDN solution, the Application Load Balancer that fronts all your origin servers, or Amazon API Gateway for your APIs. There is no additional software to deploy, DNS configuration, SSL/TLS certificate to manage, or need for a reverse proxy setup. With AWS Firewall Manager integration, you can centrally define and manage your rules, and reuse them across all the web applications that you need to protect.
Hence, the option that says: Use CloudFront to cache and distribute the high resolution images and other static assets of the website. Deploy AWS WAF on the Amazon CloudFront distribution to protect the website from common web attacks is correct because CloudFront will provide the scalability the website needs without doing major infrastructure changes. You can create a CloudFront distribution using a custom origin. Each distribution will can point to an S3 or to a custom origin. A custom origin is an HTTP server, for example, a web server. The HTTP server can be an Amazon Elastic Compute Cloud (Amazon EC2) instance or an HTTP server that you manage privately (like an on-premises web server). Take note that the website has a lot of high-resolution images which can easily be cached using CloudFront to alleviate the massive incoming traffic going to the on-premises web server and also provide a faster page load time for the web visitors.
The option that says: Use the AWS Application Migration Service to easily migrate the website from your on-premises data center to your VPC. Create an Auto Scaling group to automatically scale the web tier based on the incoming traffic. Deploy AWS WAF on the Amazon CloudFront distribution to protect the website from common web attacks is incorrect as migrating to AWS would be time-consuming compared with simply using CloudFront. Although this option can provide a more scalable solution, the scenario says that the company does not have ample time to do the migration.
The option that says: Create and configure an S3 bucket as a static website hosting. Move the web domain of the website from your on-premises data center to Route53 then route the newly created S3 bucket as the origin. Enable Amazon S3 server-side encryption with AWS Key Management Service managed keys is incorrect because the website is a dynamic website that accepts payments and bookings. Migrating your web domain to Route 53 may also take some time.
The option that says: Generate an AMI based on the existing Flight Deals website. Launch the AMI to a fleet of EC2 instances with Auto Scaling group enabled, for it to automatically scale up or scale down based on the incoming traffic. Place these EC2 instances behind an ALB which can balance traffic between the web servers in the on-premises data center and the web servers hosted in AWS is incorrect because it didn’t mention any existing AWS Direct Connect or VPN connection. Although an Application Load Balancer can load balance the traffic between the EC2 instances in AWS Cloud and web servers located in the on-premises data center, your systems should be connected via Direct Connect or VPN connection first. In addition, the application seems to be used around the world because the company launched a global marketing campaign. Hence, CloudFront is a more suitable option for this scenario.

References:
https://aws.amazon.com/cloudfront/
https://aws.amazon.com/waf/
https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

</details>

---

# Group C — Ops: patching, monitoring, troubleshooting (8)

<a id="q2"></a>

## Q2

A company needs a deployment solution for its application that is hosted on the AWS cloud. The company has the following requirements for the application: 
– The instances must have 500GB worth of static dataset that is accessible for the application upon boot up.
– The instances must be able to scale-out or scale-in depending on the traffic load of the application.
– The Development team must have a quick and automated way to deploy their code updates several times during the day.
– Security patches for the vulnerabilities on the operating system (OS) must be installed within 48 hours of release.
Which of the following solutions should the Solutions Architect implement to meet the company requirements while being cost-effective?

- **A.** Create an Auto Scaling group of EC2 instances using the Amazon Linux AMI. Install the application on the EC2 instances. Write a user data script that will download the 500 GB static dataset from an Amazon S3 bucket. Use AWS Systems Manager to install the OS patches as soon as they are released. Deploy the new version of the application to the instances using AWS CodeDeploy.
- **B.** Install OS patches and create a new AMI using AWS Systems Manager. Use this new AMI for the Auto Scaling group of EC2 instances and replace the existing instances. Create a scheduled batch job that will run every night to deploy the new application version and install the OS patches. Mount an Amazon EFS volume containing the static dataset on the instances upon boot up.
- **C.** Install OS patches and create a new AMI using AWS Systems Manager. Use this new AMI for the Auto Scaling group of EC2 instances and replace the existing instances. Deploy the new version of the application to the instances using AWS CodeDeploy. Mount an Amazon EFS volume containing the static dataset on the instances upon boot up.
- **D.** Create an Auto Scaling group of EC2 instances using the Amazon Linux AMI. Install the application on the EC2 instances. Replace the existing instances as soon as AWS releases a new Amazon Linux AMI version. Write a user data script that will download the 500 GB static dataset from an Amazon S3 bucket. Deploy the new version of the application to the instances using AWS CodeDeploy.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** several deploys/day; OS patches within 48h; cost-effective

⚠️ **Watch:** Linked to Q13/Q53 (patch groups) — patching is your weak side

🧠 **Rule:** Immutable patching → SSM builds patched AMI → replace ASG instances; app via CodeDeploy.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Yêu cầu:
  – 500GB static dataset, đọc được ngay khi boot
  – Auto Scaling (scale-out/scale-in)
  – Deploy code NHIỀU LẦN/ngày
  – OS patch trong vòng 48h
  – Cost-effective
```

Đề có 4 yêu cầu chồng nhau: dữ liệu dùng chung cho nhiều instance, deploy liên tục, patch nhanh, và rẻ. Anh chọn đúng **C**: AMI đã patch sẵn (SSM) thay instance trong ASG + CodeDeploy cho app + EFS cho dataset.

#### Vì sao C đúng

Ba cơ chế trong C giải quyết đúng ba yêu cầu khác nhau, không xung đột nhau:

- **AMI patch qua SSM + thay instance trong ASG**: patch OS được áp dụng "immutable" — tạo AMI mới đã vá lỗi, rồi launch template dùng AMI đó thay thế instance cũ. Đáp ứng khung "trong 48h" vì SSM tự động hoá bước tạo AMI, không chờ theo lịch cứng.
- **AWS CodeDeploy**: tách riêng khỏi vòng patch OS, cho phép Dev team đẩy code **nhiều lần/ngày** độc lập với chu kỳ patch — đúng yêu cầu "quick and automated, several times a day".
- **Amazon EFS**: một file system NFS **dùng chung cho mọi instance trong ASG**, mount lúc boot — khi scale-out, instance mới chỉ cần mount EFS, không cần copy lại 500GB. Rẻ hơn gắn 500GB EBS riêng cho từng instance.

#### Vì sao từng đáp án sai bị loại

- **B sai (batch job ban đêm)**: batch job chạy 1 lần/đêm để deploy code **không đáp ứng "several times a day"** — Dev team cần deploy nhiều lần trong ngày, không thể chờ đến đêm.
- **A sai (S3 + user data script download)**: S3 để lưu 500GB thì rẻ, nhưng mỗi instance phải **tải lại 500GB vào EBS cục bộ khi boot** → tốn thời gian boot, và phải gắn EBS volume lớn cho từng instance → tốn kém hơn EFS chia sẻ.
- **D sai (chờ AMI mới của Amazon Linux)**: AWS phát hành Amazon Linux AMI mới theo chu kỳ **vài tuần đến vài tháng**, không đảm bảo patch trong 48h theo yêu cầu.

⚠️ Lỗi lặp lại: đây liên quan cùng chủ đề patch OS như **Q13/Q53** (SSM Patch Manager) mà Anh trả lời sai — ở Q13/Q53 vấn đề là cần **2 Patch Group + 2 Maintenance Window không chồng lịch** để tránh reboot đồng loạt. Ở Q2 này bài toán khác: dùng SSM để **build AMI đã patch** rồi thay instance (immutable patching), không phải patch instance đang chạy tại chỗ. Cùng dịch vụ SSM nhưng hai cách dùng khác nhau — cần phân biệt rõ.

#### So sánh nhanh

| Đáp án | Patch OS | Deploy code | Dataset |
|---|---|---|---|
| **C (đúng)** | AMI mới (SSM) → thay instance | CodeDeploy, nhiều lần/ngày | EFS chia sẻ |
| A | SSM patch tại chỗ | CodeDeploy | S3 → tải vào EBS mỗi instance |
| B | AMI mới (SSM) → thay instance | Batch job đêm | EFS chia sẻ |
| D | Chờ AMI Amazon Linux mới (chậm) | CodeDeploy | S3 → tải vào EBS mỗi instance |

#### Quy tắc nhớ cho thi

- **"Nhiều instance cùng cần 1 bộ dữ liệu lớn, share được"** → **EFS**, không phải mỗi instance tự tải từ S3
- **"Deploy code nhiều lần/ngày"** → cần cơ chế **on-demand** (CodeDeploy), loại ngay các đáp án dùng **batch/cron theo lịch cố định**
- **"Patch OS nhanh, trong X giờ"** → **SSM build AMI mới rồi thay instance (immutable)**, không chờ AMI chính thức của AWS
- **Patch tại chỗ (Patch Manager + Maintenance Window) vs patch bằng AMI mới** là hai kỹ thuật khác nhau — đọc kỹ đề để biết nên dùng cái nào

### TD explanation

AWS Systems Manager Patch Manager automates the process of patching managed instances with both security-related and other types of updates. You can use Patch Manager to apply patches for both operating systems and applications. You can use Patch Manager to install Service Packs on Windows instances and perform minor version upgrades on Linux instances.
Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches. You can install patches on a regular basis by scheduling patching to run as a Systems Manager maintenance window task.
AWS Systems Manager Automation simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources. Automation enables you to do the following:
– Build automations to configure and manage instances and AWS resources.
– Create custom runbooks or use pre-defined runbooks maintained by AWS.
– Receive notifications about Automation tasks and runbooks by using Amazon EventBridge.
– Monitor Automation progress and details by using the AWS Systems Manager console.
AWS Systems Manager Automation provides several runbooks with pre-defined steps that you can use to perform common tasks like restarting one or more EC2 instances or creating an Amazon Machine Image (AMI). A Systems Manager Automation runbook defines the actions that Systems Manager performs on your managed instances and other AWS resources when an automation runs. A runbook contains one or more steps that run in sequential order. Each step is built around a single action. Output from one step can be used as input in a later step.

Amazon Elastic File System (Amazon EFS) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. Amazon EFS has a simple web services interface that allows you to create and configure file systems quickly and easily. With Amazon EFS, you pay only for the storage used by your file system and there is no minimum fee or setup cost. Amazon EFS oﬀers two storage classes, Standard and Infrequent Access. The Standard storage class is used to store frequently accessed files. The Infrequent Access (IA) storage class is a lower-cost storage class that’s designed for storing long-lived, infrequently accessed ﬁles cost-eﬀectively.
Amazon Elastic File System presents a standard file-system interface that supports full file-system access semantics. Using Network File System (NFS) version 4.1 (NFSv4.1), you can mount your Amazon EFS file system on any Amazon Elastic Compute Cloud (Amazon EC2) Linux-based instance. After your system is mounted, you can work with the files and directories just as you do with a local file system.
Therefore, the correct answer is: Install OS patches and create a new AMI using AWS Systems Manager. Use this new AMI for the Auto Scaling group of EC2 instances and replace the existing instances. Deploy the new version of the application to the instances using AWS CodeDeploy. Mount an Amazon EFS volume containing the static dataset on the instances upon boot up.
The option that says: Install OS patches and create a new AMI using AWS Systems Manager. Use this new AMI for the Auto Scaling group of EC2 instances and replace the existing instances. Create a scheduled batch job that will run every night to deploy the new application version and install the OS patches. Mount an Amazon EFS volume containing the static dataset on the instances upon boot up is incorrect. The OS patches can be installed every night, but it is not suitable for the application deployment. A batch job is not suitable for the application deployment as the Developers must deploy several times during the day.
The option that says: Create an Auto Scaling group of EC2 instances using the Amazon Linux AMI. Install the application on the EC2 instances. Write a user data script that will download the 500 GB static dataset from an Amazon S3 bucket. Use AWS Systems Manager to install the OS patches as soon as they are released. Deploy the new version of the application to the instances using AWS CodeDeploy is incorrect. Although Amazon S3 may seem more cost-effective than Amazon EFS in storing static contents, the Amazon EC2 instances will have to download the dataset on its local EBS volume. Attaching 500GB EBS volumes on each of the EC2 instances is more expensive compared to just using a single EFS volume mounted on all EC2 instances at boot up.
The option that says: Create an Auto Scaling group of EC2 instances using the Amazon Linux AMI. Install the application on the EC2 instances. Replace the existing instances as soon as AWS releases a new Amazon Linux AMI version. Write a user data script that will download the 500 GB static dataset from an Amazon S3 bucket. Deploy the new version of the application to the instances using AWS CodeDeploy is incorrect. The Amazon Linux AMI is patched for security vulnerabilities and OS minor versions. However, each new version usually takes weeks or months depending on Amazon’s release cycle.

References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html
https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html

Check out these AWS Systems Manager and Amazon EFS Cheat Sheets:
https://tutorialsdojo.com/aws-systems-manager/
https://tutorialsdojo.com/amazon-efs/

</details>

<a id="q15"></a>

## Q15

An online media streaming startup has deployed hundreds of containerized microservices using Amazon Elastic Container Service (Amazon ECS) with AWS Fargate. As new features roll out, the number of running ECS tasks steadily increases. The engineering team wants to proactively prevent service disruptions due to hitting resource limits. Specifically, the team needs to be alerted when the number of concurrently running Fargate vCPUs exceeds 75% of the service quota’s maximum limit.
A solutions architect must design a solution that sends a notification when the threshold is reached. The company also has plans to use ECS Anywhere to run and manage container-based applications in its on-premises data center to optimize its cloud workloads.
Which of the following is the MOST operationally efficient solution that meets these requirements?

- **A.** Use Amazon CloudWatch Container Insights to monitor ECS clusters and tasks. Create a custom CloudWatch dashboard that displays the current Fargate task count and the account limit. Set up a CloudWatch alarm based on a custom metric that calculates the percentage of tasks used.
- **B.** Use Amazon CloudWatch to monitor service quotas published in the AWS/Usage metric namespace. Set up an alarm when the math expression metricId/SERVICE_QUOTA(metricId)*100 is greater than 75. Configure Amazon SNS to send notifications to the operations team.
- **C.** Use Amazon CloudWatch to monitor the sample count metric for each service in the ECS cluster. Create an alarm based on the math expression sample count/SERVICE_QUOTA(service)*100 when it exceeds 75. Use Amazon Simple Notification Service (Amazon SNS) to notify the operations team.
- **D.** Use AWS Service Quotas to request an increase in the Fargate task limit to 200% of the current limit. Configure AWS Health Dashboard to monitor for quota-related issues and use Amazon EventBridge to trigger an AWS Lambda function that sends notifications via Amazon SNS when the usage reaches 75% of the new limit.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** notify at quota threshold; operationally efficient

⚠️ **Watch:** Trusted Advisor checks fewer quotas + needs polling

🧠 **Rule:** Quota alarm → CloudWatch AWS/Usage + SERVICE_QUOTA() math expression + SNS.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ECS + Fargate ── vCPU đang tăng dần theo số task
        │
   Muốn: cảnh báo khi vCPU dùng > 75% service quota
        │
   Tiêu chí: MOST operationally efficient
```

Anh chọn đúng **B**: CloudWatch giám sát metric namespace **`AWS/Usage`** + alarm dùng math expression **`metricId/SERVICE_QUOTA(metricId)*100 > 75`** + SNS báo team.

#### Vì sao B đúng

AWS **tự động publish** usage metrics của nhiều service quota (bao gồm Fargate vCPU) vào namespace có sẵn **`AWS/Usage`** — không cần code, không cần custom metric:

```
metricId (vCPU đang dùng)
──────────────────────────── × 100  >  75  ──► trigger alarm ──► SNS
SERVICE_QUOTA(metricId) (quota tối đa)
```

`SERVICE_QUOTA()` là hàm built-in của CloudWatch alarm math, tự lấy giá trị quota hiện tại của resource tương ứng — không cần tự tra cứu hay hardcode số quota. Đây là cách **ít công sức nhất** để đạt yêu cầu, đúng tiêu chí "operationally efficient".

#### Vì sao từng đáp án sai bị loại

- **A sai** vì yêu cầu **custom CloudWatch dashboard + custom metric** để tự tính phần trăm task đã dùng — AWS đã cung cấp sẵn dữ liệu này qua `AWS/Usage`, dùng custom metric là làm lại việc không cần thiết, tốn công vận hành hơn.
- **C sai** vì dùng **sample count metric** — đây là số lượng request/invocation, **không đại diện cho việc dùng quota vCPU**; công thức `sample count/SERVICE_QUOTA(service)` không phản ánh đúng số vCPU đang chạy.
- **D sai** vì tập trung vào **tăng quota lên 200%** thay vì **giám sát** mức dùng hiện tại — không đáp ứng đúng yêu cầu đề bài (cảnh báo ở 75%, không phải tăng giới hạn). Ngoài ra AWS Health Dashboard chủ yếu dùng để thông báo **reactive** về sự cố dịch vụ/quota, không phải công cụ proactive monitor % sử dụng.

#### So sánh nhanh

| Đáp án | Nguồn metric | Custom effort | Đúng ý nghĩa "dùng bao nhiêu % quota"? |
|---|---|---|---|
| **B (đúng)** | `AWS/Usage` (built-in) | Không cần custom metric | ✅ |
| A | Custom dashboard/metric | Cao | Có nhưng tốn công |
| C | Sample count (request count) | Trung bình | ❌ Sai ý nghĩa metric |
| D | Tăng quota + AWS Health | — | ❌ Không phải giám sát % dùng |

#### Lưu ý thực tế

- Không phải mọi service quota đều có metric trong `AWS/Usage` — chỉ những quota được AWS publish mới dùng được cách này; nếu quota không có trong namespace này thì mới cần cân nhắc custom metric hoặc Trusted Advisor.
- Việc đề nhắc đến "kế hoạch dùng ECS Anywhere trong tương lai" chỉ là thông tin bối cảnh (liên quan Q8), không ảnh hưởng đến logic chọn đáp án của câu này.

#### Quy tắc nhớ cho thi

- **"Cảnh báo khi dùng gần tới service quota"** → **CloudWatch `AWS/Usage` namespace + `SERVICE_QUOTA()` math expression**, không tự tạo custom metric nếu AWS đã có sẵn
- **"Sample count"** → chỉ đại diện cho **số lượng request/data point**, không đại diện cho mức sử dụng resource (vCPU, storage...)
- **"Operationally efficient"** trong đề SAP-C02 → luôn ưu tiên đáp án dùng **tính năng built-in của AWS** hơn build custom solution

### TD explanation

Amazon CloudWatch is a robust monitoring and observability service from Amazon Web Services (AWS). It collects and tracks performance metrics and log files, allowing for real-time analysis of application behavior. With the ability to set alarms for specific performance thresholds, CloudWatch enables quick responses to issues, enhancing system reliability. By providing valuable data and insights, it helps you monitor application health and optimize resource utilization efficiently.
Service Quotas are limits on the number of resources or operations that can be created or performed within an AWS account. These quotas exist to prevent accidental over-provisioning and to ensure service stability, and they can often be increased upon request to accommodate growing application needs.
Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging service that enables the sending of messages, alerts, and notifications from applications to subscribers or other applications. It supports multiple protocols and can be used to fan out messages to large numbers of recipients, making it ideal for building distributed systems and microservices architectures.
CloudWatch Alarms is a valuable feature of Amazon CloudWatch that allows users to respond automatically when monitored metrics cross predefined thresholds. You can set thresholds for various performance indicators, and when these are reached, exceeded, or dropped below, CloudWatch Alarms can send notifications or trigger automated actions to help maintain system performance effectively.

Amazon Web Services (AWS) offers metrics on service quota usage through CloudWatch in the AWS/Usage namespace, including data on the Fargate vCPU utilization. To effectively monitor this usage, a CloudWatch alarm can be created using the expression: metricid/SERVICE_QUOTA(metricid)*100. Here, metricid is an alias that represents the vCPU count metric in Fargate. SERVICE_QUOTA() is a built-in CloudWatch function that retrieves the service quota for a specific resource. This function can be used to monitor and alert when the usage for a particular resource approaches its service quota limit. For example, when you want to monitor Fargate vCPUs, SERVICE_QUOTA(metricid) will give you the maximum value allowed by the service, which can then be used to set up alerts or perform further calculations, like determining when you’re approaching 75% of the allowed quota.
Setting the alarm to trigger when usage exceeds 75 serves as a proactive measure, alerting the operations team via an Amazon Simple Notification Service (SNS) topic.
This solution is efficient as it utilizes AWS services to minimize complexity and avoid custom metrics. Additionally, it provides real-time monitoring, enabling timely actions to prevent service disruptions. By implementing this strategy, the engineering team can effectively manage resource limits and ensure smooth operations.
Hence, the correct answer is: Use Amazon CloudWatch to monitor service quotas published in the AWS/Usage metric namespace. Set up an alarm when the math expression metricId/SERVICE_QUOTA(metricId)*100 is greater than 75. Configure Amazon SNS to send notifications to the operations team.
The option that says: Use Amazon CloudWatch to monitor the sample count metric for each service in the ECS cluster. Create an alarm based on the math expression sample count/SERVICE_QUOTA(service)*100 when it exceeds 75. Use Amazon Simple Notification Service (Amazon SNS) to notify the operations team is incorrect because it primarily focuses on the sample count metric, which monitors the count of requests or invocations in the ECS cluster. The sample count does not directly represent the quota usage or the number of running ECS tasks.
The option that says: Use AWS Service Quotas to request an increase in the Fargate task limit to 200% of the current limit. Configure AWS Health Dashboard to monitor for quota-related issues and use Amazon EventBridge to trigger an AWS Lambda function that sends notifications via Amazon SNS when the usage reaches 75% of the new limit is incorrect because it focuses on increasing the quota rather than monitoring it. While increasing the quota might be helpful, it doesn’t address the requirement to monitor and notify when reaching 75% of the limit. Additionally, AWS Health is not designed for proactive monitoring of approaching quota limits; it’s typically used for reactive notifications about service health and quota-related issues.
The option that says: Use Amazon CloudWatch Container Insights to monitor ECS clusters and tasks. Create a custom CloudWatch dashboard that displays the current Fargate task count and the account limit. Set up a CloudWatch alarm based on a custom metric that calculates the percentage of tasks used is incorrect because it only focuses on creating a custom dashboard and metric, which requires additional effort and configuration to track the percentage of tasks used manually. AWS typically provides built-in metrics through the AWS/Usage namespace, making it unnecessary to create custom metrics for this use case. While this approach could work, it is less efficient and requires more maintenance than leveraging native AWS Service Quotas integration with CloudWatch.

References:
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.html#:~:text=(Optional)%20To%20set,Create%20alarm.
https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html

Check out the following Cheat Sheets:
https://tutorialsdojo.com/amazon-sns/
https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/
https://tutorialsdojo.com/amazon-cloudwatch/

</details>

<a id="q18"></a>

## Q18

A media company uses the AWS Cloud to process and convert its video collection. An Auto Scaling group of Amazon EC2 instances processes the videos and scales based on the number of messages in an Amazon Simple Queue Service (SQS) queue. These SQS messages contain links to the videos, each taking about 20-40 minutes to process.
The management has set a redrive policy on the SQS queue to send failed messages to a dead-letter queue. The visibility timeout has been set to 1 hour, and the maxReceiveCount has been set to 1. When there are messages on the dead-letter queue, an Amazon CloudWatch alarm has been set up to notify the development team.
Within a few days of operation, the dead-letter queue received several videos that failed to process. The developers did not find any operational errors in the application logs and confirmed that no videos exceeded the expected processing time. Upon examining the CloudTrail logs, the team noted that the application was making repeated ReceiveMessage API calls in quick succession for specific videos, indicating retry attempts.
Which of the following options should the solutions architect implement to help solve the above problem?

- **A.** Configure a higher delivery delay setting on the Amazon SQS queue. This will give time for the consumers more time to pick up the messages on the SQS queue.
- **B.** Reconfigure the SQS redrive policy and set maxReceiveCount to 10. This will allow the consumers to retry the messages before sending them to the dead-letter queue.
- **C.** Update the visibility timeout for the Amazon SQS queue to 2 hours to solve this problem.
- **D.** The videos were not processed because the Amazon EC2 scale-up process takes too long. Set a minimum number of EC2 instances on the Auto Scaling group to solve this.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** repeated ReceiveMessage; retries; DLQ

⚠️ **Watch:** Visibility timeout also plausible — read which symptom

🧠 **Rule:** Messages hit DLQ too early → raise redrive maxReceiveCount.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
SQS queue ──► EC2 ASG xử lý video (20-40 phút/video)
     │
   Visibility timeout = 1 giờ
   maxReceiveCount = 1  ← chỉ cần fail nhận 1 lần là vào DLQ ngay
     │
   CloudTrail log: ReceiveMessage bị gọi LẶP LẠI liên tục, nhanh (retry)
     │
   Không có lỗi app, video không quá thời gian xử lý → vẫn rơi vào DLQ
```

Mấu chốt: log CloudTrail cho thấy **retry ReceiveMessage liên tục, nhanh** — không phải do quá visibility timeout hay do lỗi xử lý app. Anh chọn đúng **B**: tăng `maxReceiveCount` lên **10**.

#### Vì sao B đúng

`maxReceiveCount = 1` nghĩa là: **chỉ một lần** nhận message thất bại (network glitch, dependency timeout, hoặc bất kỳ lỗi tạm thời nào trong lúc receive) là message **bị đẩy ngay vào DLQ**, dù chưa hề được xử lý thật. Đây khớp chính xác với triệu chứng "repeated ReceiveMessage API calls in quick succession" — hệ thống đang **retry rất nhanh rồi rơi vào DLQ ngay lập tức** chứ không phải do timeout xử lý (20-40 phút xử lý << 1 giờ visibility timeout, nên timeout không phải vấn đề). Tăng `maxReceiveCount` lên 10 cho phép hệ thống **thử lại nhiều lần hơn** trước khi coi message là "không xử lý được", giảm false-positive đẩy vào DLQ.

#### Vì sao từng đáp án sai bị loại

- **C sai** vì visibility timeout hiện tại (1 giờ) **đã lớn hơn nhiều** so với thời gian xử lý thực tế (20-40 phút) — đề đã xác nhận rõ "no videos exceeded the expected processing time". Tăng thêm timeout lên 2 giờ không giải quyết được nguyên nhân thật (đang là do maxReceiveCount quá thấp, không phải do hết giờ).
- **D sai** vì Auto Scaling group **đã scale theo số message trong queue** — vấn đề không nằm ở tốc độ scale-up của EC2, mà nằm ở cấu hình redrive policy đẩy message vào DLQ quá sớm. Đặt minimum instance cố định cũng đi ngược "cost-effective" của kiến trúc ASG theo tải.
- **A sai** vì **delivery delay** chỉ ảnh hưởng đến message **mới được gửi vào queue sau này**, không ảnh hưởng gì đến message đã ở trong queue, đã được consumer nhận và đang bị retry — không giải quyết được vấn đề hiện tại.

#### So sánh nhanh

| Đáp án | Thay đổi | Có khớp với triệu chứng "retry nhanh, rơi DLQ sớm"? |
|---|---|---|
| **B (đúng)** | `maxReceiveCount`: 1 → 10 | ✅ — cho phép nhiều lần retry trước khi vào DLQ |
| C | Visibility timeout: 1h → 2h | ❌ — timeout hiện tại đã đủ, không phải nguyên nhân |
| D | Set min EC2 instance | ❌ — không liên quan tới nguyên nhân retry/DLQ |
| A | Tăng delivery delay | ❌ — chỉ ảnh hưởng message mới, không phải message đang retry |

#### Lưu ý thực tế

- `maxReceiveCount = 1` là cấu hình rất "nhạy" — bất kỳ lỗi thoáng qua (network blip, throttle) đều đủ khiến message rơi DLQ ngay ở lần đầu, dù bản chất message hoàn toàn xử lý được. Đây là bẫy phổ biến trong các câu SQS/DLQ.
- Việc phân biệt "do hết visibility timeout" (message bị nhận lại vì consumer chưa xử lý xong) và "do vượt maxReceiveCount" (message bị đẩy DLQ vì retry quá số lần cho phép) là kỹ năng đọc log CloudTrail/triệu chứng cần luyện — log cho thấy retry "liên tục và nhanh" chứ không phải "sau đúng 1 giờ" mới là tín hiệu cho maxReceiveCount, không phải visibility timeout.

#### Quy tắc nhớ cho thi

- **"Retry liên tục, message rơi DLQ sớm dù xử lý không quá lâu"** → kiểm tra **`maxReceiveCount`** trước — có thể đang set quá thấp (ví dụ 1)
- **"Message rơi DLQ vì bị nhận lại NGAY SAU KHI hết visibility timeout"** → mới là dấu hiệu cần tăng **visibility timeout**
- **Delivery delay** → chỉ ảnh hưởng message **mới gửi vào queue**, không cứu được message đang bị retry

### TD explanation

Amazon SQS supports dead-letter queues (DLQ), which other queues (source queues) can target for messages that can’t be processed (consumed) successfully. Dead-letter queues are useful for debugging your application or messaging system because they let you isolate unconsumed messages to determine why their processing doesn’t succeed.
Occasionally, producers and consumers might fail to interpret aspects of the protocol that they use to communicate, causing message corruption or loss. Also, the consumer’s hardware errors might corrupt message payload. If a message can’t be consumed successfully, you can send it to a dead-letter queue (DLQ). Dead-letter queues let you isolate problematic messages to determine why they are failing.

The Maximum receives value determines when a message will be sent to the DLQ. If the ReceiveCount for a message exceeds the maximum receive count for the queue, Amazon SQS moves the message to the associated DLQ (with its original message ID).
As you redrive your messages, the redrive status will show you the most recent message redrive status for your dead-letter queue.
The redrive policy specifies the source queue, the dead-letter queue, and the conditions under which Amazon SQS moves messages from the former to the latter if the consumer of the source queue fails to process a message a specified number of times. The maxReceiveCount is the number of times a consumer tries receiving a message from a queue without deleting it before being moved to the dead-letter queue. Setting the maxReceiveCount to a low value, such as 1, would result in any failure to receive a message to cause the message to be moved to the dead-letter queue. Such failures include network errors and client dependency errors.
The redrive allow policy specifies which source queues can access the dead-letter queue. This policy applies to a potential dead-letter queue. You can choose whether to allow all source queues, allow specific source queues, or deny all source queues. The default is to allow all source queues to use the dead-letter queue.
Therefore, the correct answer is: Reconfigure the SQS redrive policy and set maxReceiveCount to 10. This will allow the consumers to retry the message from the dead-letter queue. This setting ensures that any message that failed to be processed will be sent back to the queue to be picked up by other consumers and re-processed.
The option that says: The videos were not processed because the Amazon EC2 scale-up process takes too long. Set a minimum number of EC2 instances on the Auto Scaling group to solve this is incorrect. The Auto Scaling group responds to the number of messages on the queue, setting a fixed minimum number of instances is not cost-effective when there are no messages on the SQS queue.
The option that says: Update the visibility timeout for the Amazon SQS queue to 2 hours to solve this problem is incorrect. This option will have negligible effect and would only make sense if messages are taking longer to process than the current timeout (1 hour). However, as mentioned in the scenario, no video processing exceeds the expected time of 20-40 minutes. The current visibility timeout should already provide sufficient time for the messages to be processed without becoming visible again for reprocessing.
The option that says: Configure a higher delivery delay setting on the Amazon SQS queue. This will give time for the consumers more time to pick up the messages on the SQS queue is incorrect. This setting does not affect the videos that were already on the queue, picked up for processing, but failed to process completely.

References:
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html
https://aws.amazon.com/blogs/compute/introducing-amazon-simple-queue-service-dead-letter-queue-redrive-to-source-queues/

Check out these Amazon SQS and AWS Auto Scaling Cheat Sheets:
https://tutorialsdojo.com/amazon-sqs/
https://tutorialsdojo.com/aws-auto-scaling/

</details>

<a id="q20"></a>

## Q20

An accounting firm hosts a mix of Windows and Linux Amazon EC2 instances in its AWS account. The solutions architect has been tasked with conducting a monthly performance check on all production instances. There are more than 200 On-Demand EC2 instances running in its production environment, and it is required to ensure that each instance has a logging feature that collects various system details such as memory usage, disk space, and other metrics. The system logs will be analyzed using AWS Analytics tools, and the results will be stored in an Amazon S3 bucket. The team currently uses an AWS Systems Manager Automation runbook for routine instance patching and maintenance.
Which of the following is the most efficient way to collect and analyze logs from the instances with minimal effort?

- **A.** Set up and install AWS Inspector Agent on each On-Demand EC2 instance, which will collect and push data to Amazon CloudWatch Logs periodically. Set up a CloudWatch dashboard to properly analyze the log data of all instances.
- **B.** Enable the Traffic Mirroring feature and install AWS CDK on each On-Demand EC2 instance. Create a custom daemon script that would collect and push data to Amazon CloudWatch Logs periodically. Set up CloudWatch detailed monitoring and use CloudWatch Logs Insights to analyze the log data of all instances.
- **C.** Set up and install the Systems Manager Agent (SSM Agent) on each On-Demand EC2 instance, which will automatically collect and push data to Amazon CloudWatch Logs. Analyze the log data with CloudWatch Logs Insights.
- **D.** Set up and configure a unified Amazon CloudWatch Logs agent in each On-Demand EC2 instance that will automatically collect and push data to CloudWatch Logs. Analyze the log data with CloudWatch Logs Insights.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** collect + analyze EC2 logs; minimal effort

⚠️ **Watch:** Kinesis/Athena pipelines = more effort

🧠 **Rule:** EC2 logs → unified CloudWatch agent + Logs Insights.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
200+ EC2 On-Demand (Windows + Linux)
        │  cần log: memory, disk, metrics khác
        ▼
  ??? agent  ──►  CloudWatch Logs  ──►  AWS Analytics  ──►  S3
Yêu cầu: hiệu quả nhất, NỖ LỰC CÀI ĐẶT/QUẢN LÝ tối thiểu
```

Anh chọn đúng **D — cài unified CloudWatch Logs agent trên từng instance, phân tích bằng CloudWatch Logs Insights**.

#### Vì sao D đúng

Từ khóa "memory usage, disk space" là các **metric nằm bên trong OS (in-guest)** mà CloudWatch mặc định không thu thập được (CloudWatch chỉ có metric ở tầng hypervisor như CPUUtilization, NetworkIn/Out). Muốn lấy được các số liệu "bên trong" máy — cả Windows và Linux — thì phải cài **unified CloudWatch agent**, vì agent này:

- Thu cả log và metric chỉ với **một agent duy nhất** (so với agent cũ chỉ thu log).
- Hỗ trợ Windows Server (agent cũ không hỗ trợ tốt).
- Cho hiệu năng tốt hơn.

Sau khi log về CloudWatch Logs, dùng **CloudWatch Logs Insights** để query nhanh bằng ngôn ngữ truy vấn chuyên dụng — đúng nghĩa "phân tích" với "nỗ lực tối thiểu", không cần dựng thêm pipeline.

#### Vì sao các đáp án sai (distractor cần nhớ)

- **A (Inspector Agent + CloudWatch dashboard):** Inspector là dịch vụ **đánh giá lỗ hổng bảo mật/network exposure**, không thu thập memory/disk metric. Dashboard chỉ để hiển thị trực quan, không phải công cụ phân tích log — sai cả agent và cách phân tích.
- **B (Traffic Mirroring + AWS CDK + custom daemon):** Traffic Mirroring chỉ sao chép network traffic ở tầng ENI, không liên quan log hệ thống. Phải tự viết daemon script và cài CDK trên 200+ máy — cực kỳ tốn công, ngược hẳn yêu cầu "minimal effort". Bật thêm CloudWatch detailed monitoring cũng không cần thiết, tốn phí.
- **C (SSM Agent):** SSM Agent dùng để **quản lý/patch/run command** trên instance (giống runbook Automation mà công ty đang dùng), không tự động thu thập và đẩy log hệ thống lên CloudWatch Logs như CloudWatch agent. Muốn xem log bằng SSM thường phải kết nối thủ công vào từng máy — tốn thời gian hơn.

#### So sánh nhanh

| Giải pháp | Thu memory/disk? | Hỗ trợ Windows? | Công cụ phân tích |
|---|---|---|---|
| **Unified CloudWatch agent (D)** | Có | Có | Logs Insights |
| SSM Agent (C) | Không tự động | Có | Thủ công/kết nối máy |
| Inspector Agent (A) | Không (chỉ security) | Có | Dashboard (không hợp) |
| Traffic Mirroring + daemon (B) | Chỉ qua script tự viết | Tùy code | Logs Insights (nhưng quá cồng kềnh) |

#### Quy tắc nhớ cho thi

- **"Metric bên trong OS (memory, disk, custom app metric)"** → **unified CloudWatch agent**, không phải CloudWatch mặc định.
- **"Phân tích/query log nhanh, ít công cụ"** → **CloudWatch Logs Insights**.
- **SSM Agent** = quản lý/patch/automation, không phải công cụ logging chính.
- **Inspector** = quét lỗ hổng bảo mật, không đo hiệu năng hệ thống.

### TD explanation

To collect logs from your Amazon EC2 instances and on-premises servers into CloudWatch Logs, AWS offers both a new unified CloudWatch agent and an older CloudWatch Logs agent. It is recommended to use the unified CloudWatch agent, which has the following advantages:

– You can collect both logs and advanced metrics with the installation and configuration of just one agent.
– The unified agent enables the collection of logs from servers running Windows Server.
– If you are using the agent to collect CloudWatch metrics, the unified agent also enables the collection of additional system metrics, for in-guest visibility.
– The unified agent provides better performance.

CloudWatch Logs Insights enables you to interactively search and analyze your log data in Amazon CloudWatch Logs. You can perform queries to help you quickly and effectively respond to operational issues. If an issue occurs, you can use CloudWatch Logs Insights to identify potential causes and validate deployed fixes.
CloudWatch Logs Insights includes a purpose-built query language with a few simple but powerful commands. CloudWatch Logs Insights provides sample queries, command descriptions, query autocompletion, and log field discovery to help you get started quickly. Sample queries are included for several types of AWS service logs.
Hence, the correct answer is: Set up and configure a unified Amazon CloudWatch Logs agent in each On-Demand EC2 instance that will automatically collect and push data to CloudWatch Logs. Analyze the log data with CloudWatch Logs Insights.
The option that says: Enable the Traffic Mirroring feature and install AWS CDK on each On-Demand EC2 instance. Create a custom daemon script that would collect and push data to Amazon CloudWatch Logs periodically. Set up CloudWatch detailed monitoring and use CloudWatch Logs Insights to analyze the log data of all instances is incorrect. Although this is a valid solution, this entails a lot of effort to implement, as you have to allocate time to install the AWS CDK to each instance and develop a custom monitoring solution. Traffic Mirroring is simply an Amazon VPC feature that you can use to copy network traffic from an elastic network interface of Amazon EC2 instances. As per the scenario, you are specifically looking for a solution that can be implemented with minimal effort. In addition, it is unnecessary and not cost-efficient to enable detailed monitoring in CloudWatch in order to meet the requirements, since this can be done using CloudWatch Logs.

The option that says: Set up and install the Systems Manager Agent (SSM Agent) on each On-Demand EC2 instance, which will automatically collect and push data to Amazon CloudWatch Logs. Analyze the log data with CloudWatch Logs Insights is incorrect. Although this is also a valid solution, it is more efficient to use a CloudWatch agent than an SSM agent. Manually connecting to an instance to view log files and troubleshoot an issue with an SSM Agent is time-consuming. Hence, for more efficient instance monitoring, you can use the CloudWatch Agent instead to send the log data to Amazon CloudWatch Logs.
The option that says: Set up and install AWS Inspector Agent on each On-Demand EC2 instance, which will collect and push data to Amazon CloudWatch Logs periodically. Set up a CloudWatch dashboard to properly analyze the log data of all instances is incorrect. AWS Inspector is simply a security assessment service that only helps you check for unintended network accessibility of your EC2 instances and for vulnerabilities on those EC2 instances. Furthermore, setting up an Amazon CloudWatch dashboard is not suitable since it’s primarily used for scenarios where you have to monitor your resources in a single view, even those resources that are spread across different AWS Regions. It is better to use CloudWatch Logs Insights instead since it enables you to interactively search and analyze your log data.

References:
https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-ssm-agent.html
https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html

Check out this Amazon CloudWatch Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudwatch/

CloudWatch Agent vs SSM Agent vs Custom Daemon Scripts
https://tutorialsdojo.com/cloudwatch-agent-vs-ssm-agent-vs-custom-daemon-scripts/

</details>

<a id="q24"></a>

## Q24

The department of education just recently decided to leverage the AWS cloud infrastructure to supplement its current on-premises network. They are building a new learning portal that teaches kids basic computer science concepts and provides innovative gamified courses for teenagers where they can gain higher rankings, power-ups and badges. A Solutions Architect is instructed to build a highly available cloud infrastructure in AWS with multiple Availability Zones. The department wants to increase the application’s reliability and gain actionable insights using application logs. A Solutions Architect needs to aggregate logs, automate log analysis for errors and immediately notify the IT Operations team when errors breached a certain threshold.
Which of the following is the MOST suitable solution that the Architect should implement?

- **A.** Download and install the Amazon Managed Service for Prometheus in the on-premises servers and send the logs to AWS Lambda to turn log data into numerical metrics that identify and measure application errors. Write the processed metrics back to the time series database in Prometheus. Create a CloudWatch Alarm that monitors the metric and immediately notifies the IT Operations team for any issues.
- **B.** Download and install the Amazon CloudWatch agent in the on-premises servers and send the logs to Amazon EventBridge. Create a metric filter in CloudWatch to turn log data into numerical metrics to identify and measure application errors. Use Amazon Athena to monitor the metric filter and immediately notify the IT Operations team for any issues.
- **C.** Download and install the Amazon Kinesis agent in the on-premises servers and send the logs to Amazon CloudWatch Logs. Create a metric filter in CloudWatch to turn log data into numerical metrics to identify and measure application errors. Use Amazon QuickSight to monitor the metric filter in CloudWatch and immediately notify the IT Operations team for any issues.
- **D.** Download and install the Amazon CloudWatch agent in the on-premises servers and send the logs to Amazon CloudWatch Logs. Create a metric filter in CloudWatch to turn log data into numerical metrics to identify and measure application errors. Create a CloudWatch Alarm that monitors the metric filter and immediately notify the IT Operations team for any issues.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** on-prem logs; error threshold → notify

⚠️ **Watch:** Unified CloudWatch agent works on-prem too

🧠 **Rule:** Logs → CloudWatch agent → metric filter → alarm → SNS.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises servers (learning portal)
       │  logs
       ▼
  ??? agent  ──►  CloudWatch Logs  ──►  metric filter  ──►  alarm  ──►  IT Ops
Yêu cầu: aggregate log + tự động phân tích lỗi + báo ngay khi vượt threshold
```

Anh chọn đúng **D — CloudWatch agent (on-prem) → CloudWatch Logs → metric filter → CloudWatch Alarm → thông báo IT Ops**.

#### Vì sao D đúng

Đây là chuỗi xử lý log kinh điển của CloudWatch, đủ 3 bước:

1. **Thu log từ on-premises:** CloudWatch agent **hỗ trợ cài trên on-premises servers**, không chỉ EC2 — gửi log về CloudWatch Logs.
2. **Biến log thành số liệu đo được:** **metric filter** trong CloudWatch Logs quét các pattern/term trong log (ví dụ "ERROR") và chuyển thành **numerical metric** để có thể graph hoặc đặt alarm.
3. **Báo ngay khi vượt ngưỡng:** **CloudWatch Alarm** theo dõi metric filter đó, khi vượt threshold thì trigger action (ví dụ gửi SNS) để báo IT Ops ngay lập tức.

#### Vì sao các đáp án sai (distractor cần nhớ)

- **B (gửi log tới EventBridge + Athena):** Log hệ thống phải gửi tới **CloudWatch Logs**, không phải EventBridge (EventBridge là event bus cho sự kiện rời rạc, không phải nơi lưu/aggregate log). Athena dùng để query dữ liệu có cấu trúc (thường trên S3), không phải công cụ để "monitor metric filter" và cảnh báo theo threshold — đó là việc của CloudWatch Alarm.
- **C (Kinesis agent + QuickSight):** Phải dùng **CloudWatch agent** để đẩy log vào CloudWatch Logs, không phải Kinesis agent (Kinesis dùng cho streaming pipeline khác, không tích hợp trực tiếp kiểu này). QuickSight là công cụ **visualize/BI**, không phải công cụ theo dõi ngưỡng và gửi cảnh báo real-time.
- **A (Amazon Managed Service for Prometheus + Lambda tự viết):** Yêu cầu phải tự viết Lambda để chuyển log thành metric rồi ghi ngược lại time series DB — quá phức tạp và không cần thiết khi CloudWatch metric filter đã làm sẵn việc này. Prometheus phù hợp hơn cho **container metrics**, không phải use case log on-premises đơn giản này.

#### So sánh nhanh

| Giải pháp | Agent đúng cho on-prem? | Biến log → metric | Cảnh báo threshold |
|---|---|---|---|
| **CloudWatch agent + metric filter + Alarm (D)** | Có | metric filter | CloudWatch Alarm |
| Kinesis agent + QuickSight (C) | Sai agent | metric filter (đúng phần này) | QuickSight (sai) |
| CloudWatch agent + EventBridge + Athena (B) | Đúng agent, sai đích gửi log | metric filter (đúng) | Athena (sai) |
| Prometheus + Lambda tự viết (A) | Đúng nhưng thừa công | Tự code (không cần) | CloudWatch Alarm (đúng phần cuối) |

#### Quy tắc nhớ cho thi

- **"On-premises servers cần gửi log về AWS"** → **unified CloudWatch agent** hỗ trợ cả on-prem, không chỉ EC2.
- **"Biến log thành số liệu đo được, đặt ngưỡng cảnh báo"** → **CloudWatch metric filter + CloudWatch Alarm**, không phải Athena/QuickSight (những cái đó dùng để phân tích/hiển thị, không phải cảnh báo real-time).
- **EventBridge** = event bus cho sự kiện, không phải nơi lưu trữ log thô.
- Thấy "container metrics" mới nghĩ tới **Prometheus**; log server thông thường thì CloudWatch agent là đủ.

### TD explanation

Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications. The CloudWatch home page automatically displays metrics about every AWS service you use. You can additionally create custom dashboards to display metrics about your custom applications and display custom collections of metrics that you choose.

After the CloudWatch Logs agent begins publishing log data to Amazon CloudWatch, you can begin searching and filtering the log data by creating one or more metric filters. Metric filters define the terms and patterns to look for in log data as it is sent to CloudWatch Logs. CloudWatch Logs uses these metric filters to turn log data into numerical CloudWatch metrics that you can graph or set an alarm on. You can use any type of CloudWatch statistic, including percentile statistics when viewing these metrics or setting alarms.
You can create alarms that watch metrics and send notifications or automatically make changes to the resources you are monitoring when a threshold is breached. For example, you can monitor the CPU usage and disk reads and writes of your Amazon EC2 instances and then use this data to determine whether you should launch additional instances to handle the increased load. You can also use this data to stop under-used instances to save money. With CloudWatch, you gain system-wide visibility into resource utilization, application performance, and operational health.
Hence, the correct answer is: Download and install the Amazon CloudWatch agent in the on-premises servers and send the logs to Amazon CloudWatch Logs. Create a metric filter in CloudWatch to turn log data into numerical metrics to identify and measure application errors. Create a CloudWatch Alarm that monitors the metric filter and immediately notify the IT Operations team for any issues.
The option that says: Download and install the Amazon Kinesis agent in the on-premises servers and send the logs to Amazon CloudWatch Logs. Create a metric filter in CloudWatch to turn log data into numerical metrics to identify and measure application errors. Use Amazon QuickSight to monitor the metric filter in CloudWatch and immediately notify the IT Operations team for any issues is incorrect. You have to use an Amazon CloudWatch agent instead of an Amazon Kinesis agent to send the logs to Amazon CloudWatch Logs. It is also better to use CloudWatch Alarms to monitor the metric filter than to use Amazon QuickSight.
The option that says: Download and install the Amazon Managed Service for Prometheus in the on-premises servers and send the logs to AWS Lambda to turn log data into numerical metrics that identify and measure application errors. Write the processed metrics back to the time series database in Prometheus. Create a CloudWatch Alarm that monitors the metric and immediately notifies the IT Operations team for any issues is incorrect. Amazon Managed Service for Prometheus is a serverless, Prometheus-compatible monitoring service for container metrics. You don’t have to create a custom Lambda function to process the logs. Amazon Managed Service for Prometheus is integrated with CloudWatch to monitor metrics and Logs.
The option that says: Download and install the Amazon CloudWatch agent in the on-premises servers and send the logs to Amazon EventBridge. Create a metric filter in CloudWatch to turn log data into numerical metrics to identify and measure application errors. Use Amazon Athena to monitor the metric filter and immediately notify the IT Operations team for any issues is incorrect. You have to send the logs to CloudWatch Logs and not CloudWatch Events. It is also better to use CloudWatch Alarm to monitor the metric filter and immediately notify the IT Operations team for any issues.

References:
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-premise.html
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html
https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringPolicyExamples.html

Check out this Amazon CloudWatch Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudwatch/

</details>

<a id="q37"></a>

## Q37

An IT consulting company has multiple AWS accounts for its teams and departments that have been grouped into several organizational units (OUs) using AWS Organizations. The lead solutions architect received a report from the security team that there was a suspected breach in one of the environments wherein a third-party AWS account was suddenly added to the AWS Organization without any prior approval. The external account has high-level access privileges to the accounts that the company owns. Fortunately, no detrimental action was performed yet. 
Which of the following actions should the solutions architect take to properly set up a monitoring system that notifies for any changes to the company AWS accounts? (Select TWO.)

- **A.** Set up a CloudWatch Dashboard to monitor any changes to your organizations and create an SNS topic that would send you a notification.
- **B.** Configure AWS Control Tower to manage and monitor all child accounts under the organization. Use Amazon Inspector to analyze any possible breach and notify the administrators using AWS SNS.
- **C.** Create a trail in Amazon CloudTrail to capture all API calls to your AWS Organizations, including calls from the AWS Organizations console and from code calls to the AWS Organizations APIs. Use Amazon EventBridge and SNS to raise events when administrator-specified actions occur in an organization and send a notification to you.
- **D.** Monitor all changes to your organization using Systems Manager and use Amazon EventBridge to notify you of any new activity to your account.
- **E.** Use AWS Config to monitor the compliance of your AWS Organizations. Set up an SNS Topic or Amazon EventBridge that will send alerts to you for any changes.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, E (you answered correctly)

🔑 **Key words:** detect changes to AWS Organizations (Select TWO)

⚠️ **Watch:** GuardDuty/Inspector ≠ change tracking

🧠 **Rule:** Org change alerts → CloudTrail + EventBridge/SNS and Config + SNS/EventBridge.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations (nhiều OU)
        │
        ▼  third-party account bị thêm vào KHÔNG được phê duyệt
??? giám sát mọi thay đổi trong Organizations, báo ngay
```

Anh chọn đúng **C, E — CloudTrail (capture API calls tới Organizations) + EventBridge/SNS, VÀ AWS Config (compliance) + SNS/EventBridge**.

#### Vì sao C và E đúng (kết hợp thành MỘT giải pháp)

Bài yêu cầu Select TWO nhưng cả hai lựa chọn đúng cùng phục vụ mục tiêu "phát hiện thay đổi + thông báo", theo hai góc nhìn bổ trợ nhau:

- **C — CloudTrail + EventBridge + SNS:** AWS Organizations tích hợp với CloudTrail để ghi lại **mọi API call** tới Organizations (từ console hoặc code). Khi có action nhạy cảm như "thêm account mới vào Organization", EventBridge có thể bắt sự kiện này (dựa trên CloudTrail) và trigger SNS gửi thông báo ngay — đây là góc nhìn **real-time event-driven**.
- **E — AWS Config + SNS/EventBridge:** AWS Config hỗ trợ **multi-account, multi-region aggregation**, cho phép admin trung tâm theo dõi **compliance** của cấu hình trên toàn Organization. Đây là góc nhìn **giám sát trạng thái/compliance liên tục**, bổ sung cho việc chỉ bắt sự kiện tức thời của CloudTrail.

Hai công cụ này không thay thế nhau — CloudTrail bắt "hành động xảy ra", Config theo dõi "trạng thái cấu hình có đúng chuẩn không" — kết hợp lại mới đủ để vừa phát hiện ngay khi account lạ được thêm, vừa theo dõi được sai lệch cấu hình lâu dài.

#### Vì sao các đáp án sai (distractor cần nhớ)

- **A (CloudWatch Dashboard + SNS):** CloudWatch Dashboard chỉ để **hiển thị trực quan** resource, không phải công cụ theo dõi cấu hình Organizations và không tự phát hiện được việc thêm account mới.
- **B (Control Tower + Amazon Inspector + SNS):** Control Tower có thể gửi log tới CloudWatch/CloudTrail để giám sát account, nhưng **Amazon Inspector** là dịch vụ **quét lỗ hổng vulnerability trên workload** (EC2, container...), hoàn toàn không liên quan đến việc phát hiện thay đổi cấu trúc tổ chức (thêm/xóa account).
- **D (Systems Manager + EventBridge):** Systems Manager dùng để **quản lý EC2/on-premises servers ở scale**, không có khả năng theo dõi cấu hình của AWS Organizations.

#### So sánh nhanh

| Công cụ | Bắt được API call/action tức thời? | Theo dõi compliance liên tục? | Phù hợp use case Organizations? |
|---|---|---|---|
| **CloudTrail + EventBridge (C)** | Có | Không (đó là việc của Config) | Có |
| **AWS Config (E)** | Không trực tiếp | Có | Có |
| CloudWatch Dashboard (A) | Không | Không | Không |
| Control Tower + Inspector (B) | Một phần (qua Control Tower) | Không (Inspector = vulnerability, không phải config) | Không đủ |
| Systems Manager (D) | Không | Không | Không (SSM quản lý EC2, không quản lý Organizations) |

#### Quy tắc nhớ cho thi

- **"Phát hiện thay đổi cấu trúc AWS Organizations (thêm/xóa account, thay đổi OU)"** → **CloudTrail + EventBridge/SNS**.
- **"Theo dõi compliance cấu hình trên nhiều account/region"** → **AWS Config với multi-account aggregator**.
- **Amazon Inspector** = vulnerability scanning cho workload, không liên quan tới việc giám sát Organizations.
- **Systems Manager / CloudWatch Dashboard** = quản lý & hiển thị resource, không phải công cụ giám sát cấu trúc tổ chức.

### TD explanation

AWS Organizations can work with CloudWatch Events to raise events when administrator-specified actions occur in an organization. For example, because of the sensitivity of such actions, most administrators would want to be warned every time someone creates a new account in the organization or when an administrator of a member account attempts to leave the organization. You can configure CloudWatch Events rules that look for these actions and then send the generated events to administrator-defined targets. Targets can be an Amazon SNS topic that emails or text messages its subscribers. Combining this with Amazon CloudTrail, you can set an event to trigger whenever a matching API call is received.
Multi-account, multi-region data aggregation in AWS Config enables you to aggregate AWS Config data from multiple accounts and regions into a single account. Multi-account, multi-region data aggregation is useful for central IT administrators to monitor compliance for multiple AWS accounts in the enterprise. An aggregator is a new resource type in AWS Config that collects AWS Config data from multiple source accounts and regions. Create an aggregator in the Region where you want to see the aggregated AWS Config data. While creating an aggregator, you can choose to add either individual account IDs or your organization.

Therefore, the following options are the correct answers:
– Create a trail in Amazon CloudTrail to capture all API calls to your AWS Organizations, including calls from the AWS Organizations console and from code calls to the AWS Organizations APIs. Use Amazon EventBridge and SNS to raise events when administrator-specified actions occur in an organization and send a notification to you.

– Use AWS Config to monitor the compliance of your AWS Organizations. Set up an SNS Topic or Amazon EventBridge that will send alerts to you for any changes.

The option that says: Monitor all changes to your organization using Systems Manager and use Amazon EventBridge to notify you of any new activity to your account is incorrect. AWS Systems Manager is a collection of capabilities for configuring and managing your Amazon EC2 instances, on-premises servers and virtual machines, and other AWS resources at scale. This can’t be used to monitor the changes to the setup of AWS Organizations.
The option that says: Setting up a CloudWatch Dashboard to monitor any changes to your organizations and creating an SNS topic that would send you a notification is incorrect because a CloudWatch Dashboard is primarily used to monitor your AWS resources and not the configuration of your AWS Organizations. Although you can enable sharing of all CloudWatch Events across all accounts in your organization, this can’t be used to monitor if there is a new AWS account added to your AWS Organizations. Most of the time, the Amazon EventBridge service is primarily used to monitor your AWS resources and the applications you run on AWS in real-time.
The option that says: Configure AWS Control Tower to manage and monitor all child accounts under the organization. Use Amazon Inspector to analyze any possible breach and notify the administrators using AWS SNS is incorrect. AWS Control Tower can send logs to CloudWatch and CloudTrail for monitoring AWS accounts in the organization. However, Amazon Inspector is used as an automated vulnerability management service that continually scans AWS workloads for software vulnerabilities, not for monitoring events on individual AWS accounts.

References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_monitoring.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_cwe.html
https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-config.html

Check out these AWS Organizations and AWS Config Cheat Sheets:
https://tutorialsdojo.com/aws-organizations/
https://tutorialsdojo.com/multi-account-multi-region-data-aggregation-on-aws-config/

</details>

<a id="q45"></a>

## Q45

A company is developing an online voting application for a photo competition. The infrastructure is deployed in AWS using CloudFormation. The application accepts high-quality images of each contestant and stores them in S3 then records the information about the image as well as the contestant’s profile in RDS. After the competition, the CloudFormation stack is not used anymore, and to save costs, the stack can be terminated. The manager instructed the solutions architect to back up the RDS database and the S3 bucket so the data can still be used even after the CloudFormation template is deleted.
Which of the following options is the MOST suitable solution to fulfill this requirement?

- **A.** Set the DeletionPolicy to retain on both the RDS and S3 resource types on the CloudFormation template.
- **B.** Set the DeletionPolicy for the RDS instance to snapshot and then enable S3 bucket replication on the source bucket to a destination bucket to maintain a copy of all the S3 objects.
- **C.** Set the DeletionPolicy on the S3 bucket to snapshot.
- **D.** Set the DeletionPolicy on the RDS resource to snapshot and set the S3 bucket to retain.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** delete stack but keep RDS + S3 data

⚠️ **Watch:** Don't rely on defaults — set DeletionPolicy explicitly per resource

🧠 **Rule:** DeletionPolicy: Snapshot for RDS, Retain for S3.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
CloudFormation stack: RDS (thông tin contestant) + S3 (ảnh chất lượng cao)
Sau cuộc thi → xóa stack để tiết kiệm chi phí
Yêu cầu: dữ liệu vẫn dùng được SAU KHI stack bị xóa
```

Đáp án đúng: **D** — set `DeletionPolicy: Snapshot` cho RDS, `DeletionPolicy: Retain` cho S3. Anh chọn đúng D.

#### Vì sao D đúng

`DeletionPolicy` là attribute gắn trực tiếp trên từng resource trong template CloudFormation, quyết định điều gì xảy ra với resource đó khi stack bị xóa. Có 3 loại: **Delete** (mặc định nếu không set gì), **Retain** (giữ nguyên resource, không xóa), **Snapshot** (chụp snapshot rồi mới xóa resource gốc). Với RDS, chọn **Snapshot** là hợp lý nhất vì snapshot là hình thức backup chuẩn của RDS — dữ liệu được lưu lại dưới dạng snapshot độc lập, có thể restore thành instance mới sau này, đồng thời instance RDS gốc (đang tốn tiền theo giờ) vẫn bị xóa đúng như mong muốn "tiết kiệm chi phí". Với S3, chọn **Retain** là đúng vì S3 bucket + object không "chụp lại" theo kiểu snapshot — retain giữ nguyên bucket và toàn bộ ảnh, không bị xóa theo stack.

#### Vì sao các phương án khác sai

- **A (Retain cho cả RDS và S3):** sai ở phần RDS — nếu Retain, CloudFormation sẽ **giữ RDS instance tiếp tục chạy** (không xóa, không snapshot) → vẫn tốn chi phí chạy DB hàng giờ, không đạt mục tiêu "tiết kiệm chi phí" của bài toán.
- **B (Snapshot cho RDS + S3 replication sang bucket khác):** vẫn snapshot RDS đúng, nhưng phần S3 sai hướng — dùng replication để copy sang bucket đích **không ngăn được việc bucket gốc bị xóa khi xóa stack** (nếu bucket gốc không có DeletionPolicy retain); giải pháp vòng vo và tốn thêm chi phí lưu trữ ở bucket phụ trong khi chỉ cần set Retain trực tiếp trên bucket gốc.
- **C (Snapshot cho S3):** `Snapshot` **không áp dụng được cho resource type S3** — S3 bucket chỉ hỗ trợ Delete hoặc Retain, không có khái niệm snapshot theo CloudFormation DeletionPolicy.

| Phương án | RDS DeletionPolicy | S3 DeletionPolicy | Kết quả |
|---|---|---|---|
| **D (đúng)** | Snapshot | Retain | Dữ liệu giữ, chi phí RDS ngừng |
| A | Retain | Retain | RDS vẫn chạy → tốn tiền |
| B | Snapshot | (Delete + replication ngoài) | Vòng vo, không chắc giữ bucket gốc |
| C | (không nêu) | Snapshot (không hợp lệ) | Sai loại resource |

#### Quy tắc nhớ cho thi

- **RDS** cần backup dữ liệu → `DeletionPolicy: Snapshot`.
- **S3, EC2, nested stack** cần giữ nguyên tài nguyên → `DeletionPolicy: Retain`.
- Không set `DeletionPolicy` → CloudFormation **xóa mặc định (Delete)** khi xóa stack — luôn set rõ nếu cần giữ dữ liệu.
- `Snapshot` chỉ áp dụng cho các resource type hỗ trợ snapshot (RDS, EBS, ElastiCache, Redshift…), không áp dụng cho S3.

### TD explanation

With the DeletionPolicy attribute you can preserve, and in some cases, backup a resource when its stack is deleted. You specify a DeletionPolicy attribute for each resource that you want to control. If a resource has no DeletionPolicy attribute, AWS CloudFormation deletes the resource by default.
This capability also applies to stack update operations that lead to resources being deleted from stacks. For example, if you remove the resource from the stack template, and then update the stack with the template. This capability doesn’t apply to resources whose physical instance is replaced during stack update operations. For example, if you edit a resource’s properties such that CloudFormation replaces that resource during a stack update.
To keep a resource when its stack is deleted, specify Retain for that resource. You can use retain for any resource. For example, you can retain a nested stack, Amazon S3 bucket, or EC2 instance so that you can continue to use or modify those resources after you delete their stacks.
There are 3 types of DeletionPolicy Options:

Delete
Retain
Snapshot

For Delete, CloudFormation deletes the resource and all its contents if applicable during stack deletion. For Retain, CloudFormation keeps the resource without deleting the resource or its contents when its stack is deleted. For Snapshot, CloudFormation creates a snapshot of the resource before deleting it.

Therefore the correct answer is: Set the DeletionPolicy on the RDS resource to snapshot and set the S3 bucket to retain. It correctly sets the DeletionPolicy of retain on S3 bucket and snapshot on RDS instance.
The option that says: Set the DeletionPolicy for the RDS instance to snapshot and then enable S3 bucket replication on the source bucket to a destination bucket to maintain a copy of all the S3 objects is incorrect. Even if the images are backed up to another bucket, the original bucket would be deleted if the CloudFormation stack is deleted. Although this option is valid, it is certainly not the most suitable solution because you don’t need to back up the data to another region in the first place. You simply have to set the DeletionPolicy of the S3 bucket to retain.
The option that says: Set the DeletionPolicy to retain on both the RDS and S3 resource types on the CloudFormation template is incorrect. The DeletionPolicy attribute for RDS should be set to Snapshot and not Retain because with the snapshot option, the backup of the RDS instance would be stored in the form of snapshots. With the retain option, CloudFormation will keep the RDS instance running.
The option that says: Set the DeletionPolicy on the S3 bucket to snapshot is incorrect because the DeletionPolicy of the S3 bucket should be retained, not snapshot.

References:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html
https://aws.amazon.com/premiumsupport/knowledge-center/delete-cf-stack-retain-resources/

Check out this AWS CloudFormation Cheat Sheet:
https://tutorialsdojo.com/aws-cloudformation/

</details>

<a id="q49"></a>

## Q49

A company plans to decommission its legacy web application that is hosted in AWS. It is composed of an Auto Scaling group of Amazon EC2 instances and an Application Load Balancer (ALB). The new application is built on a new framework. The solutions architect has been tasked with setting up a new serverless architecture that comprises AWS Lambda, Amazon API Gateway, and Amazon DynamoDB. In addition, it is required to build a CI/CD pipeline to automate the build process and to support gradual deployments. The team initially tried an all-at-once deployment strategy, but it could not deliver the gradual rollout the business requires.




Which is the most suitable way to build, test, and deploy the new architecture in AWS?

- **A.** Set up a CI/CD pipeline using AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline to build the CI/CD pipeline, then use AWS Systems Manager Automation to automate the build process and support gradual deployments.
- **B.** Use the AWS Serverless Application Repository to organize related components, share configuration such as memory and timeouts between resources, and deploy all related resources together as a single, versioned entity.
- **C.** Use AWS Elastic Beanstalk to deploy the application.
- **D.** Use AWS Serverless Application Model (AWS SAM) and set up AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline to build a CI/CD pipeline.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** serverless CI/CD; gradual deployments

⚠️ **Watch:** all-at-once rejected

🧠 **Rule:** Serverless + canary/linear → SAM + CodePipeline/CodeBuild/CodeDeploy.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Legacy app: ASG EC2 + ALB → sắp decommission
New app: AWS Lambda + API Gateway + DynamoDB (serverless)
Đã thử "all-at-once deployment" → KHÔNG đạt gradual rollout
Yêu cầu: build/test/deploy kiến trúc mới, có CI/CD, hỗ trợ GRADUAL DEPLOYMENT
```

Đáp án đúng: **D** — dùng AWS SAM để định nghĩa kiến trúc serverless, kết hợp CodeBuild + CodeDeploy + CodePipeline làm CI/CD. Anh chọn đúng D.

#### Vì sao D đúng

Hai yêu cầu cốt lõi: **(1)** kiến trúc là serverless (Lambda/API Gateway/DynamoDB) nên cần công cụ build/deploy chuyên cho serverless — đó là **AWS SAM**, một extension của CloudFormation, có SAM CLI để build/test/deploy. **(2)** cần **gradual deployment** (canary/linear) thay cho all-at-once đã thất bại — SAM tích hợp trực tiếp với **CodeDeploy** để hỗ trợ các chiến lược deploy dần (canary, linear) cho Lambda alias/version, còn CodeBuild/CodePipeline lo phần build và orchestrate pipeline tự động.

#### Vì sao các phương án khác sai

- **A (CodeBuild/CodeDeploy/CodePipeline + Systems Manager Automation cho gradual deploy):** sai vai trò của Systems Manager Automation — SSM Automation dùng để **chạy runbook quản lý/tự động hoá tác vụ trên EC2 instance** (patch, restart, config...), **không phải công cụ để build và deploy ứng dụng Lambda** theo kiểu gradual rollout.
- **B (AWS Serverless Application Repository):** SAR chỉ là một **repository/marketplace** để chia sẻ và tổ chức các serverless application components có sẵn (share config như memory, timeout giữa resource) — nó **không tự làm CI/CD**, cần thêm nhiều công cụ khác mới hoàn chỉnh; giải pháp này thiếu (incomplete).
- **C (Elastic Beanstalk):** Elastic Beanstalk được thiết kế để deploy và quản lý ứng dụng chạy trên **EC2 instance**, không phù hợp cho kiến trúc serverless dựa trên Lambda.

| Phương án | Phù hợp serverless? | Hỗ trợ gradual deploy? |
|---|---|---|
| **D (đúng)** | Có (SAM) | Có (CodeDeploy canary/linear cho Lambda) |
| A | Có (CodeDeploy) | Sai — SSM Automation không phải công cụ deploy app |
| B | Có (nhưng chỉ là repo) | Không — thiếu cả pipeline |
| C | Không (Elastic Beanstalk cho EC2) | — |

#### Lưu ý thực tế

⚠️ Việc đề nói "team initially tried all-at-once… could not deliver gradual rollout" là gợi ý loại trừ mọi phương án không nhắc tới cơ chế deploy dần cho Lambda cụ thể — chỉ SAM + CodeDeploy mới có traffic-shifting config (Canary10Percent5Minutes, Linear10PercentEvery1Minute…) built-in cho Lambda alias.

#### Quy tắc nhớ cho thi

- **Serverless (Lambda/API Gateway) build/deploy** → **AWS SAM**.
- **Gradual/canary deployment cho Lambda** → **CodeDeploy** (không phải SSM Automation).
- **Elastic Beanstalk** → dành cho app chạy trên EC2, không phải kiến trúc serverless thuần.
- **Serverless Application Repository (SAR)** → chỉ là nơi chia sẻ/organize component, không thay được CI/CD pipeline.

### TD explanation

The AWS Serverless Application Model (AWS SAM) is an open-source framework that you can use to build serverless applications on AWS. It consists of the AWS SAM template specification that you use to define your serverless applications, and the AWS SAM command-line interface (AWS SAM CLI) that you use to build, test, and deploy your serverless applications.

Because AWS SAM is an extension of AWS CloudFormation, you get the reliable deployment capabilities of AWS CloudFormation. You can define resources by using AWS CloudFormation in your AWS SAM template. Also, you can use the full suite of resources, intrinsic functions, and other template features that are available in AWS CloudFormation.
You can use AWS SAM with a suite of AWS tools for building serverless applications. To build a deployment pipeline for your serverless applications, you can use CodeBuild, CodeDeploy, and CodePipeline. To deploy your serverless application, you can use the Jenkins plugin, and you can use Stackery.io’s toolkit to build production-ready applications.
Hence, the correct answer is: Use AWS Serverless Application Model (AWS SAM) and set up AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline to build a CI/CD pipeline.
The option that says: Use AWS Elastic Beanstalk to deploy the application is incorrect because AWS Elastic Beanstalk is designed for deploying and managing applications on EC2 instances, not for serverless applications like Lambda.
The option that says: Set up a CI/CD pipeline using AWS CodeBuild, AWS CodeDeploy, and AWS CodePipeline to build the CI/CD pipeline, then use AWS Systems Manager Automation to automate the build process and support gradual deployments is incorrect. Systems Manager Automation is primarily designed to configure and manage instances with custom runbooks or pre-defined runbooks maintained by AWS, not for building and deploying serverless applications on AWS Lambda.
The option that says: Use the AWS Serverless Application Repository to organize related components, share configuration such as memory and timeouts between resources, and deploy all related resources together as a single, versioned entity is incorrect. AWS Serverless Application Repository is just a managed repository for serverless applications. This solution is incomplete, as you will need other AWS tools to build and deploy your application.

References:
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html

Check out this AWS Serverless Application Model Cheat Sheet:
https://tutorialsdojo.com/aws-serverless-application-model-sam/

</details>

---

# Group D — Multi-account governance & cost (8)

<a id="q19"></a>

## Q19

A media company hosts its entire infrastructure on the AWS cloud. There is a requirement to copy information to or from the shared resources from another AWS account. The solutions architect has to provide the other account access to several AWS resources, such as Amazon S3, AWS KMS, and Amazon OpenSearch Service, in the form of a list of AWS account ID numbers. In addition, the user in the other account should still work in the trusted account, and there is no need to give up the user permissions in place of the role permissions. The solutions architect must also set up a solution that continuously assesses, audits, and monitors the policy configurations. 
Which of the following is the MOST suitable type of policy that should be used in this scenario?

- **A.** Set up cross-account access with a user-based policy configuration. Use AWS Config rules to periodically audit changes to the IAM policy and monitor the compliance of the configuration.
- **B.** Set up a service-linked role with a service control policy. Use AWS Systems Manager rules to periodically audit changes to the IAM policy and monitor the compliance of the configuration.
- **C.** Set up a service-linked role with an identity-based policy. Use AWS Systems Manager rules to periodically audit changes to the IAM policy and monitor the compliance of the configuration.
- **D.** Set up cross-account access with a resource-based Policy. Use AWS Config rules to periodically audit changes to the IAM policy and monitor the compliance of the configuration.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** keep user perms (no role switch); audit policies

⚠️ **Watch:** Role assumption gives up user perms

🧠 **Rule:** Cross-account without giving up perms → resource-based policy + Config rules to audit.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Trusted Account (chủ resource)          Account khác (được cấp quyền)
┌─────────────────────────┐             ┌─────────────────────────┐
│ S3 / KMS / OpenSearch    │  ◄────────  │ User vẫn giữ quyền cũ    │
└─────────────────────────┘   truy cập   │ trong trusted account   │
                                          └─────────────────────────┘
Yêu cầu:
  - cấp quyền theo list account ID
  - user KHÔNG cần "đánh đổi" quyền cũ để lấy quyền mới (không assume role)
  - phải audit + monitor cấu hình policy liên tục
```

Anh chọn đúng **D — Cross-account access bằng resource-based policy + AWS Config rules**.

#### Vì sao D đúng

Từ khóa quyết định là "user vẫn tiếp tục làm việc trong trusted account, không cần đánh đổi user permissions lấy role permissions" — đây chính là điểm khác biệt lớn nhất giữa **resource-based policy** và **role (identity-based) assumption**:

- Khi **assume role** để cross-account, user phải tạm "bỏ" quyền hiện tại, chuyển sang bộ quyền của role → không thể vừa làm việc ở account cũ vừa truy cập account mới cùng lúc.
- Với **resource-based policy** (đính trực tiếp vào S3 bucket, KMS key, OpenSearch domain...), policy liệt kê rõ **AWS account ID** nào được phép truy cập. User vẫn giữ nguyên identity và quyền ở trusted account, đồng thời có thêm quyền truy cập resource ở account khác — đúng nhu cầu "copy dữ liệu qua lại giữa hai account".
- Yêu cầu audit/monitor liên tục → **AWS Config rules**, vì Config là dịch vụ chuyên "assess, audit, evaluate configuration" của resource, đúng với việc theo dõi thay đổi policy.

#### Vì sao các đáp án sai (distractor cần nhớ)

- **A (user-based policy + Config):** User-based policy chỉ gắn quyền vào một IAM user cụ thể, không gắn vào resource → không thể liệt kê "AWS account ID nào được truy cập resource này". Sai bản chất loại policy cần dùng.
- **B (service-linked role + SCP + Systems Manager):** Service-linked role là role đặc biệt được AWS service tự tạo để gọi service khác giùm mình (ví dụ Auto Scaling gọi EC2), không phải cơ chế cấp quyền cross-account cho người dùng. SCP thuộc AWS Organizations, dùng để giới hạn quyền tối đa trong toàn tổ chức, không phải cấp quyền truy cập resource cụ thể. Và Systems Manager không audit config — đó là việc của Config.
- **C (service-linked role + identity-based policy + Systems Manager):** Cùng lỗi service-linked role như B, cộng thêm identity-based policy vẫn là gắn vào role/user (đòi hỏi assume role → mất quyền cũ), và vẫn sai dịch vụ audit (Systems Manager thay vì Config).

#### So sánh nhanh

| Cách cấp quyền | Gắn vào đâu | User có mất quyền cũ không | Audit config |
|---|---|---|---|
| **Resource-based policy (D)** | Resource (S3, KMS, OpenSearch…) | Không | AWS Config |
| Identity-based policy qua role | Role (phải assume) | Có (tạm thời) | — |
| User-based policy | IAM user | — (nhưng không map theo resource) | — |
| Service control policy (SCP) | Toàn Organization | Không áp dụng cho case này | — |

⚠️ **Lỗi lặp lại:** Ở Q12 anh từng lẫn giữa AWS Config và một dịch vụ khác cho việc "audit/kiểm tra compliance" (Config Managed Rule cho AMI). Nguyên tắc chung: **"assess/audit/evaluate configuration của resource"** luôn trỏ về **AWS Config**, dù đó là policy IAM (Q19) hay AMI compliance (Q12).

#### Quy tắc nhớ cho thi

- **"Cross-account, không muốn mất quyền hiện tại / không assume role"** → **resource-based policy**.
- **"Audit/giám sát liên tục cấu hình resource"** → **AWS Config rules**, không phải Systems Manager hay CloudWatch Dashboard.
- **Service-linked role** ≠ cơ chế chia sẻ quyền cross-account cho người dùng — nó là role nội bộ của một AWS service.
- **SCP** = giới hạn quyền toàn Organization (deny-by-default guardrail), không phải cấp quyền truy cập tài nguyên cụ thể.

### TD explanation

For some AWS services, you can grant cross-account access to your resources. To do this, you attach a policy directly to the resource that you want to share, instead of using a role as a proxy. The resource that you want to share must support resource-based policies. Unlike a user-based policy, a resource-based policy specifies who (in the form of a list of AWS account ID numbers) can access that resource.
Cross-account access with a resource-based policy has some advantages over a role. With a resource that is accessed through a resource-based policy, the user still works in the trusted account and does not have to give up his or her user permissions in place of the role permissions. In other words, the user continues to have access to resources in the trusted account at the same time as he or she has access to the resource in the trusting account. This is useful for tasks such as copying information to or from the shared resource in the other account.

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations.
Hence, the correct answer is: Set up cross-account access with a resource-based Policy. Use AWS Config rules to periodically audit changes to the IAM policy and monitor the compliance of the configuration.
The option that says: Set up cross-account access with a user-based policy. configuration. Use AWS Config rules to periodically audit changes to the IAM policy and monitor the compliance of the configuration is incorrect because a user-based policy only maps the access to a certain IAM user and not to a certain AWS resource.
The option that says: Set up a service-linked role with an identity-based policy. Use AWS Systems Manager rules to periodically audit changes to the IAM policy and monitor the compliance of the configuration is incorrect because a service-linked role is just a unique type of IAM role that is linked directly to an AWS service. In addition, it is the AWS Config service, and not the AWS Systems Manager, that enables you to assess, audit, and evaluate the configurations of your AWS resources.
The option that says: Set up a service-linked role with a service control policy. Use AWS Systems Manager rules to periodically audit changes to the IAM policy and monitor the compliance of the configuration is incorrect because a service control policy is primarily used in AWS Organizations and not for cross-account access. Service-linked roles are predefined by the service and include all the permissions that the service requires to call other AWS services on your behalf. This is not suitable for providing access to your resources to other AWS accounts, unlike cross-account access. You should also use AWS Config, and not AWS Systems Manager, to periodically audit changes to the IAM policy.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html
https://aws.amazon.com/config/

Check out this AWS Config Cheat Sheet:
https://tutorialsdojo.com/aws-config/

</details>

<a id="q33"></a>

## Q33

A company is modernizing its on-premises system by migrating it to AWS. The system will be hosted on Amazon EC2 instances managed by Amazon Elastic Kubernetes Service (Amazon EKS) and use Amazon RDS for MySQL as the database. The system has predictable schedules of high usage, especially during sales events and holiday seasons. A recent cost‑optimization review using the AWS Well‑Architected Tool highlighted the strict need to minimize compute costs during peak-demand surges.
What pricing options should the company consider when selecting the MOST cost-optimized solution?

- **A.** Acquire Compute Savings Plans for the EC2 nodes of the EKS cluster to be used for regular traffic. Scale the node cluster with On-Demand Capacity Reservations during peak demands. Handle the predicted database load with a 1-year No Upfront Reserved Instance and increase database read replicas on scheduled high usage.
- **B.** Purchase Compute Savings Plans for the EC2 nodes of the EKS cluster to be used for regular traffic. Scale the node cluster with Spot instances during peak demands. Handle the predicted database load with a 1-year All Upfront Reserved Instance and vertically scale up the DB instance on scheduled high usage.
- **C.** Acquire EC2 Instance Savings Plans for the EC2 nodes of the EKS cluster to be used for regular traffic. Scale the node cluster with On-Demand Instances during peak demands. Handle the predicted database load with a 1-year Partial Upfront Reserved Instance and vertically scale up the DB instance on scheduled high usage.
- **D.** Purchase Standard Reserved Instances for the EC2 nodes of the EKS cluster to be used for regular traffic. Scale the node cluster with Dedicated Instances during peak demands. Handle the predicted database load with a 1-year All Upfront Reserved Instance.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** EKS steady + unpredictable peaks; minimize compute cost

⚠️ **Watch:** EC2 Instance Savings Plans lock to family/Region

🧠 **Rule:** Baseline → Compute Savings Plans; spikes → Spot; steady DB → RI.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EKS trên EC2 nodes           RDS MySQL
     │                            │
Tải nền (steady)             Tải nền (predictable)
     │                            │
Tải cao đột biến (sale/holiday, dự đoán được lịch)
Yêu cầu: MINIMIZE COMPUTE COST khi peak-demand
```

Anh chọn đúng **B — Compute Savings Plans (baseline) + Spot Instances (peak) + RDS 1-year All Upfront RI + vertical scale up DB theo lịch**.

#### Vì sao B đúng

Bài có 2 loại tải khác nhau cần 2 chiến lược pricing khác nhau:

- **Tải nền ổn định (EKS nodes cho traffic thường xuyên)** → **Compute Savings Plans**: giảm giá tới 66%, linh hoạt áp dụng cho **nhiều instance family và cả EC2/Fargate/Lambda** — phù hợp môi trường Kubernetes có thể đổi loại node.
- **Tải đột biến, có lịch dự đoán (sale/holiday)** → **Spot Instances**: tận dụng capacity dư thừa với giá rẻ nhất trong các lựa chọn, giảm chi phí compute đáng kể khi cần scale ngang tạm thời cho node cluster.
- **Database tải dự đoán được** → **1-year All Upfront Reserved Instance**: vì tải database có thể lập kế hoạch trước, trả toàn bộ upfront cho mức chiết khấu **lớn nhất** trong các hình thức RI.
- **Vertical scale up DB theo lịch**: vì lịch cao điểm biết trước, có thể lên kế hoạch tăng resource cho DB đúng thời điểm mà không cần tự động scale phức tạp.

#### Vì sao các đáp án sai (distractor cần nhớ)

- **A (Compute SP + On-Demand Capacity Reservations + No Upfront RI + read replica):** On-Demand Capacity Reservations chỉ **đảm bảo có capacity sẵn**, không mang lại **chiết khấu giá** — không giúp "minimize cost" cho phần peak. No Upfront RI cũng cho mức giảm giá **thấp nhất** trong 3 loại upfront (No/Partial/All) — không tối ưu chi phí nhất cho tải dự đoán được.
- **C (EC2 Instance Savings Plans + On-Demand peak + Partial Upfront RI + vertical scale):** EC2 Instance Savings Plans khóa vào **một instance family/region cụ thể**, giảm tính linh hoạt hơn Compute Savings Plans. Scale peak bằng **On-Demand** đắt hơn Spot rất nhiều. Partial Upfront RI cho chiết khấu **thấp hơn** All Upfront.
- **D (Standard RI + Dedicated Instances peak + All Upfront RI):** **Dedicated Instances** chạy trên hardware dành riêng cho một khách hàng — đắt hơn instance chia sẻ/Spot, thường dùng vì lý do compliance chứ không phải để tối ưu chi phí — sai chiến lược cho phần peak.

#### So sánh nhanh

| Đáp án | Baseline compute | Peak compute | Database RI upfront |
|---|---|---|---|
| **B. Compute SP + Spot (đúng)** | Compute Savings Plans | Spot (rẻ nhất) | All Upfront (giảm nhiều nhất) |
| A. Compute SP + Capacity Reservation | Compute Savings Plans | Capacity Reservation (không giảm giá) | No Upfront (giảm ít nhất) |
| C. EC2 Instance SP + On-Demand | Kém linh hoạt hơn Compute SP | On-Demand (đắt) | Partial Upfront (giảm trung bình) |
| D. Standard RI + Dedicated | RI thường | Dedicated (rất đắt) | All Upfront (đúng phần DB) |

#### Quy tắc nhớ cho thi

- **"Tải nền ổn định trên EKS/nhiều instance family, cần linh hoạt"** → **Compute Savings Plans** (không phải EC2 Instance Savings Plans, vốn khóa family/region).
- **"Tải đột biến, chấp nhận rủi ro bị reclaim, muốn rẻ nhất"** → **Spot Instances**, không phải On-Demand hay Capacity Reservation (Capacity Reservation chỉ đảm bảo có máy, không giảm giá).
- **"Database tải dự đoán trước, muốn giảm giá tối đa"** → **1-year All Upfront RI** (All > Partial > No Upfront về mức chiết khấu).
- **Dedicated Instances** = compliance/hardware riêng, không phải công cụ tối ưu chi phí.

### TD explanation

AWS offers multiple purchasing options such as Savings Plans, Reserved Instances, and Spot Instances to allow customers to optimize their workloads in terms of cost. There are also multiple services that can be used when monitoring usage and cost to help in this analysis, such as AWS Pricing Calculator, AWS Cost Explorer, and AWS Budgets.
For EC2 usage, EC2 Instance Savings Plans offer the highest savings (up to 72%) and are applied to a specific instance within a chosen region. Compute Savings Plans offer slightly lower savings (up to 66%) but provide more flexibility as they apply to any instance family and can cover usage across different services like EC2, Fargate, and Lambda. For use cases when there is an increase in load during certain periods, Spot instances can be a cost-effective solution. These instances provide flexibility and allow using spare EC2 capacity at a significant discount.

For the database instance, paying for an entire Reserved Instance term (1 year) with an upfront payment provides a large discount compared with other payment options. Since the usage is predictable, database sizing can also be planned beforehand. Vertical scaling, or scaling up, adds resources to a server. This is an effective way to handle high traffic during sales events and holiday seasons. Scaling up the database can be scheduled to handle the increased load.
Hence, the correct answer is: Purchase Compute Savings Plans for the EC2 nodes of the EKS cluster to be used for regular traffic. Scale the node cluster with Spot instances during peak demands. Handle the predicted database load with a 1-year All Upfront Reserved Instance and vertically scale up the DB instance on scheduled high usage.
The option that says: Acquire EC2 Instance Savings Plans for the EC2 nodes of the EKS cluster to be used for regular traffic. Scale the node cluster with On-Demand Instances during peak demands. Handle the predicted database load with a 1-year Partial Upfront Reserved Instance and vertically scale up the DB instance on scheduled high usage is incorrect. While EC2 Instance Savings Plans do offer a discount over On-Demand pricing, these only apply to a specific instance family and will limit the flexibility of changing instance types. This option suggests scaling with On-Demand Instances, which are more expensive than Spot instances. Moreover, using a 1-year Partial Upfront Reserved Instance for the database can offer some cost savings, but not as much savings as an All Upfront Reserved Instance.
The option that says: Acquire Compute Savings Plans for the EC2 nodes of the EKS cluster to be used for regular traffic. Scale the node cluster with On-Demand Capacity Reservations during peak demands. Handle the predicted database load with a 1-year No Upfront Reserved Instance and increase database read replicas on scheduled high usage is incorrect. Using On-Demand Capacity Reservations to handle increased load ensures the required capacity is available when needed, but this does not just provide any cost savings. Moreover, using No-Upfront Reserved Instances for the database offers a smaller discount than an Upfront payment.
The option that says: Purchase Standard Reserved Instances for the EC2 nodes of the EKS cluster to be used for regular traffic. Scale the node cluster with Dedicated Instances during peak demands. Handle the predicted database load with a 1-year All Upfront Reserved Instance is incorrect. Dedicated Instances run on hardware dedicated to a single customer and are more expensive than shared or Spot instances, often used for compliance reasons rather than cost optimization.

References:
https://aws.amazon.com/savingsplans/
https://aws.amazon.com/aws-cost-management/aws-cost-optimization/reserved-instances/

Check out this AWS Savings Plan Cheat Sheet:
https://tutorialsdojo.com/aws-savings-plan/

</details>

<a id="q38"></a>

## Q38

A company uses computer simulations for modeling weather patterns in a certain country. The simulations generate terabytes of data, which is stored in a MySQL 8.0 database that runs in an Amazon EC2 instance. A Ruby on Rails application is hosted on a separate EC2 instance to process the data. The current database size is 16 TiB and is expected to grow as more complex simulations are created continuously. The facility wants to re-architect its infrastructure to be highly scalable and highly available as they need to run the application reliably 24×7.
Which of the following is the MOST cost-effective solution that can satisfy the above requirements?

- **A.** Purchase Reserved Amazon EC2 instances for the application instance and database instances to save costs. Create an EC2 Auto Scaling group with Multi-AZ configuration behind a load balancer for the application tier. Implement a “source-replica” setup for your database tier. Use Logical Volume Management on the database instances to easily attach new EBS volumes and expand the file system.
- **B.** Convert the application tier to Lambda@Edge functions for high availability, scalability, and cost-effectiveness. Migrate the MySQL database to an Amazon RDS MySQL instance with Multi-AZ enabled. Enable storage autoscaling on the RDS instance.
- **C.** Configure your application tier to run on an Auto Scaling group of smaller sized EC2 instances behind an Application Load Balancer. Purchase Reserved EC2 instances for fixed capacity and let the Auto Scaling instances run on demand. Migrate the MySQL database to Amazon Aurora. Create a read-replica on another Availability Zone of the Aurora instance for high availability.
- **D.** Configure your application tier to run on an Auto Scaling group of smaller sized EC2 instances behind an Application Load Balancer. Purchase reserved EC2 instances for fixed capacity and let the Auto Scaling instances run on demand. Migrate the MySQL database to an Amazon RDS MySQL instance with Multi-AZ enabled. Adjust the RDS Storage volume manually as demand increases.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** 24×7 HPC app; data growing; most cost-effective

⚠️ **Watch:** All On-Demand or all Spot for a 24×7 baseline

🧠 **Rule:** Steady baseline → Reserved; bursts → Auto Scaling On-Demand; shared growing data → EFS/S3.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 (Ruby on Rails app) ──► EC2 (MySQL 8.0, 16 TiB, đang tăng)
Yêu cầu: re-architect HA + scalable, chạy 24×7, MOST COST-EFFECTIVE
```

Anh chọn đúng **C — ASG (smaller EC2) + ALB, Reserved Instances cho baseline + On-Demand cho phần scale, migrate sang Aurora + read-replica AZ khác**.

#### Vì sao C đúng

Bài có 2 tầng cần tối ưu riêng:

- **Tầng application:** chạy 24×7 liên tục nên có phần tải **cố định (baseline)** — dùng **Reserved Instances** cho phần này để có chiết khấu, còn phần **biến động** thì để **Auto Scaling group chạy On-Demand**, kết hợp cả hai giúp tối ưu chi phí mà vẫn co giãn theo tải. ALB đứng trước để cân bằng tải.
- **Tầng database:** dữ liệu 16 TiB và tiếp tục tăng, tự vận hành MySQL trên EC2 sẽ ngày càng khó scale — migrate sang **Amazon Aurora**, storage tự động scale tới 128 TiB mà **chỉ trả tiền cho phần dùng thực tế**, không cần tự quản lý resize. Thêm **một read-replica ở AZ khác** để đảm bảo HA — đủ để failover nhanh khi primary lỗi, không cần nhiều hơn (tránh dư thừa chi phí).

#### Vì sao các đáp án sai (distractor cần nhớ)

- **A (Reserved cho cả app+DB, tự quản lý MySQL trên EC2, LVM để mở rộng volume):** Vẫn tự vận hành **MySQL trên EC2** ("source-replica" tự dựng) — tốn nhiều công quản lý (backup, patch, replication), và phải **thủ công** gắn thêm EBS volume + mở rộng filesystem mỗi khi dữ liệu tăng — không scalable tự động như Aurora.
- **B (Lambda@Edge cho app tier + RDS MySQL Multi-AZ storage autoscaling):** Lambda@Edge dùng để tùy biến nội dung CloudFront **gần user toàn cầu** — bài không nói ứng dụng phục vụ user toàn cầu, dùng Lambda@Edge ở đây là sai ngữ cảnh (mô hình phù hợp hơn là container hóa app rồi chạy trên ECS, không phải Lambda@Edge). RDS MySQL cũng có storage autoscaling nhưng giới hạn thấp hơn Aurora và kém tối ưu cho dữ liệu simulation rất lớn.
- **D (giống C nhưng RDS MySQL Multi-AZ + tự điều chỉnh storage thủ công):** Phải **"adjust the RDS Storage volume manually"** — đi ngược lại khả năng auto-scaling mà RDS/Aurora đã hỗ trợ sẵn, tạo thêm công vận hành không cần thiết so với Aurora (tự scale mặc định).

#### So sánh nhanh

| Đáp án | Compute (app) | Database | Storage scale |
|---|---|---|---|
| **C. RI + On-Demand ASG + Aurora (đúng)** | Reserved (baseline) + On-Demand (biến động) | Aurora | Tự động, trả theo dùng |
| A. Toàn Reserved + tự vận hành MySQL | Reserved, ASG multi-AZ | MySQL tự quản lý trên EC2 | Thủ công (LVM + EBS) |
| B. Lambda@Edge + RDS MySQL | Lambda@Edge (sai ngữ cảnh) | RDS MySQL Multi-AZ | Autoscaling (giới hạn hơn Aurora) |
| D. RI + On-Demand + RDS MySQL thủ công | Reserved + On-Demand (đúng) | RDS MySQL Multi-AZ | Thủ công (sai, RDS đã hỗ trợ autoscaling) |

#### Quy tắc nhớ cho thi

- **"Chạy 24×7, có baseline load ổn định + phần biến động"** → **Reserved Instances (baseline) + Auto Scaling On-Demand (biến động)**, không phải toàn Reserved hay toàn On-Demand.
- **"Dữ liệu MySQL rất lớn, tiếp tục tăng, cần tự scale storage"** → **Amazon Aurora** (tự scale tới 128 TiB, trả theo dùng), tốt hơn tự vận hành MySQL trên EC2 hoặc RDS MySQL thông thường.
- **Lambda@Edge** chỉ hợp lý khi có yêu cầu rõ ràng về **người dùng toàn cầu / tùy biến nội dung tại edge** — không phải "converter" mặc định cho mọi app tier.
- Thấy cụm **"adjust/manually"** trong đáp án khi dịch vụ đã có tính năng tự động tương ứng → thường là dấu hiệu đáp án sai.

### TD explanation

You can launch and automatically scale a fleet of On-Demand Instances and Spot Instances within a single Auto Scaling group. In addition to receiving discounts for using Spot Instances, you can use Reserved Instances or a Savings Plan to receive discounted rates of the regular On-Demand Instance pricing. All of these factors combined help you to optimize your cost savings for Amazon EC2 instances, while making sure that you obtain the desired scale and performance for your application.

Amazon Aurora storage automatically scales with the data in your cluster volume. As your data grows, your cluster volume storage expands up to a maximum of 128 tebibytes (TiB). Even though an Aurora cluster volume can scale up in size to many tebibytes, you are only charged for the space that you use in the volume. The mechanism for determining billed storage space depends on the version of your Aurora cluster. Aurora stores copies of the data in a DB cluster across multiple Availability Zones in a single AWS Region. Aurora stores these copies regardless of whether the instances in the DB cluster span multiple Availability Zones. However, you still need to create a read-replica for the high availability of the Aurora DB instance. A single read-replica is enough to quickly recover the database in case the primary instance fails.
Therefore, the correct answer is: Configure your application tier to run on an Auto Scaling group of smaller sized EC2 instances behind an Application Load Balancer. Purchase Reserved EC2 instances for fixed capacity and let the Auto Scaling instances to run on demand. Migrate the MySQL database to Amazon Aurora. Create a read-replica on another Availability Zone of the Aurora instance for high-availability.
The option that says: Purchase Reserved Amazon EC2 instances for the application instance and database instances to save costs. Create an EC2 Auto Scaling group with Multi-AZ configuration behind a load balancer for the application tier. Implement a “source-replica” setup for your database tier. Use Logical Volume Management on the database instances to easily attach new EBS volumes and expand the file system is incorrect because running your own MySQL server on an EC2 instance entails significant management overhead. This is not scalable because you need to manually resize and configure the EC2 instance as you will eventually need more compute or storage capacity in the future. A better solution is to use Amazon Aurora instead.
The option that says: Convert the application tier to Lambda@Edge functions for high availability, scalability, and cost-effectiveness. Migrate the MySQL database to an Amazon RDS MySQL instance with Multi-AZ enabled. Enable storage autoscaling on the RDS instance is incorrect. Although it is true that MySQL RDS instances can support storage autoscaling for up to 64TiB, using Lambda@Edge to run the application is not warranted. Lambda@Edge is just an extension of AWS Lambda that customizes the content of what Amazon CloudFront delivers. It is not stated in the scenario that the application is used globally. This would be a viable option if you convert your application to Docker-based containers and run them on Amazon ECS.
The option that says: Configure your application tier to run on an Auto Scaling group of smaller sized EC2 instances behind an Application Load Balancer. Purchase reserved EC2 instances for fixed capacity and let the Auto Scaling instances to run on demand. Migrate the MySQL database to an Amazon RDS MySQL instance with Multi-AZ enabled. Adjust the RDS Storage volume manually as demand increases is incorrect. You don’t have to manually adjust storage volume because storage auto-scaling is supported by Amazon RDS. You just have to enable the storage auto-scaling option. Amazon Aurora as it automatically scales disk storage by default.

References:
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html
https://aws.amazon.com/about-aws/whats-new/2019/05/amazon-rds-mysql-mariadb-postgresql-64tib-support/
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html

Check out this Amazon RDS Cheat Sheet:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q48"></a>

## Q48

A company has created multiple accounts in AWS to support the rapid growth of its cloud services. The multiple accounts are used to separate its various departments such as finance, human resources, engineering, and many others. Each account is managed by a Systems Administrator who has root access for that specific account only. There is a requirement to centrally manage policies across multiple AWS accounts by allowing or denying particular AWS services for individual accounts, or for groups of accounts. The team evaluated AWS Proton for centralized governance but found it introduced more complexity than needed for simple service restrictions.
Which is the most suitable solution that should be implemented with the LEAST amount of complexity?

- **A.** Use AWS Organizations and Service Control Policies to control the list of AWS services that can be used by each member account.
- **B.** Set up AWS Organizations and Organizational Units (OU) to connect all AWS accounts of each department. Create a custom IAM Policy to allow or deny the use of certain AWS services for each account.
- **C.** Connect all departments by setting up cross-account access to each of the AWS accounts of the company. Create and attach IAM policies to your resources based on their respective departments to control access.
- **D.** Provide access to externally authenticated users via Identity Federation. Set up an IAM role to specify permissions for users from each department whose identity is federated from your organization or a third-party identity provider.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** allow/deny services per account; least complexity

⚠️ **Watch:** IAM per account = no central control

🧠 **Rule:** Restrict services per account/OU → Organizations SCPs.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhiều AWS account (finance, HR, engineering, ...)
Mỗi account có 1 Systems Administrator có root access — CHỈ trong account đó
Yêu cầu: quản lý TẬP TRUNG service nào được/không được dùng
          per account hoặc per nhóm account, LEAST COMPLEXITY
```

Đáp án đúng: **A** — dùng AWS Organizations + Service Control Policies (SCP) để kiểm soát danh sách service được dùng ở từng member account. Anh chọn đúng A.

#### Vì sao A đúng

Từ khóa quyết định: **"centrally manage"**, **"allow/deny service theo account hoặc nhóm account (OU)"**, **"least complexity"**. SCP là công cụ duy nhất trong danh sách được thiết kế đúng cho việc này: SCP gắn vào root/OU/account, áp dụng lên **mọi IAM user, group, role — kể cả root identity** của account đó, cho phép whitelist hoặc blacklist service ở mức tổ chức mà không cần chỉnh IAM policy riêng lẻ ở từng account. Đây chính là cơ chế governance tập trung với độ phức tạp thấp nhất trong các lựa chọn.

#### Vì sao các phương án khác sai

- **B (Organizations + OU, nhưng dùng IAM Policy để allow/deny service):** đúng phần dùng Organizations/OU để nhóm account, nhưng sai công cụ kiểm soát — **IAM Policy chỉ gắn được vào user/group/role và không thể restrict root identity** của account; để chặn/permit service ở cấp account hoặc OU phải dùng SCP, không phải IAM Policy thông thường.
- **C (cross-account access + IAM policy theo từng resource):** đây là cách làm thủ công, tốn nhiều công thiết lập cho **mỗi cặp account** — hoàn toàn ngược với yêu cầu "least complexity" khi có nhiều account; cross-account access phù hợp hơn khi chỉ có 1–2 account, không phải giải pháp quản lý tập trung nhiều account.
- **D (Identity Federation + IAM role cho user liên kết):** giải quyết vấn đề **authentication** (ai đăng nhập, dùng identity provider nào), không giải quyết vấn đề **governance service nào được dùng ở account nào** — lạc đề so với yêu cầu chính của bài toán.

| Phương án | Cơ chế nhóm account | Công cụ allow/deny service | Đúng mục tiêu? |
|---|---|---|---|
| **A (đúng)** | Organizations | SCP | Có, ít phức tạp nhất |
| B | Organizations + OU | IAM Policy (sai, không chặn root) | Sai công cụ |
| C | Cross-account access | IAM Policy theo resource | Quá phức tạp cho nhiều account |
| D | Identity Federation | IAM role | Lạc đề (authentication, không phải governance) |

#### Lưu ý thực tế

⚠️ Liên quan Q40 (Anh trả lời sai): SCP có tính **kế thừa (inheritance)** — SCP gắn ở root/OU cha sẽ áp dụng xuống mọi OU/account con, và **Deny ở cấp cao hơn luôn thắng Allow ở cấp thấp hơn**. Vì vậy khi thiết kế SCP tập trung như câu này, cần đặt đúng cấp (root/OU) để tránh vô tình chặn cả những account cần được phép tạm thời (ví dụ account mới sáp nhập).

#### Quy tắc nhớ cho thi

- **"Allow/deny AWS service theo account hoặc nhóm account, tập trung, ít phức tạp"** → **AWS Organizations + SCP**.
- **IAM Policy** không thể restrict root identity của account — SCP thì có thể.
- **Cross-account access** hợp lý cho vài account, không hợp lý khi số account lớn (nhiều cấu hình lặp lại).
- **Identity Federation** là bài toán "ai đăng nhập", khác với "service nào được phép dùng" (SCP).

### TD explanation

AWS Organizations offers policy-based management for multiple AWS accounts. With Organizations, you can create groups of accounts, automate account creation, and apply and manage policies for those groups. Organizations enables you to centrally manage policies across multiple accounts, without requiring custom scripts and manual processes. It allows you to create Service Control Policies (SCPs) that centrally control AWS service use across multiple AWS accounts.
Remember that AWS Organizations does not replace associating IAM policies with users, groups, and roles within an AWS account. Hence, you still need to set up appropriate IAM policies for your root and member accounts.

IAM policies let you allow or deny access to AWS services (such as Amazon S3), individual AWS resources (such as a specific S3 bucket), or individual API actions (such as s3:CreateBucket). An IAM policy can be applied only to IAM users, groups, or roles, and it can never restrict the root identity of the AWS account.
By contrast, AWS Organizations lets you use service control policies (SCPs) to allow or deny access to particular AWS services for individual AWS accounts, or for groups of accounts within an organizational unit (OU). The specified actions from an attached SCP affect all IAM users, groups, and roles for an account, including the root account identity.
When you apply an SCP to an OU or an individual AWS account, you choose to either enable (whitelist), or disable (blacklist) the specified AWS service. Access to any service that isn’t explicitly allowed by the SCPs associated with an account, its parent OUs, or the master account is denied to the AWS accounts or OUs associated with the SCP. When an SCP is applied to an OU, it is inherited by all of the AWS accounts in that OU.
Hence, the correct answer is: Use AWS Organizations and Service Control Policies to control the list of AWS services that can be used by each member account.
The option that says: Setting up AWS Organizations and Organizational Units (OU) to connect all AWS accounts of each department and creating a custom IAM Policy to allow or deny the use of certain AWS services for each account is incorrect. Although it is correct to use AWS Organizations, this option is incorrect about IAM Policy. It is the Service Control Policy (SCP) that enables you to allow or deny the use of certain AWS services for each account, and not the IAM Policy.
The option that says: Connecting all departments by setting up cross-account access to each of the AWS accounts of the company, then creating and attaching IAM policies to your resources based on their respective departments to control access is incorrect. Although you can set up cross-account access to each department, this entails a lot of configuration compared with using AWS Organizations and Service Control Policies (SCPs). Cross-account access would be a more suitable choice if you only have two accounts to manage, but not for multiple accounts.
The option that says: Providing access to externally authenticated users via Identity Federation and setting up an IAM role to specify permissions for users from each department whose identity is federated from your organization or a third-party identity provider is incorrect. This option is primarily focused on the Identity Federation authentication setup for your AWS accounts but not the IAM policy management for multiple AWS accounts. A combination of AWS Organizations and Service Control Policies (SCPs) is a better choice compared to this option.

References:
https://aws.amazon.com/organizations/
https://aws.amazon.com/premiumsupport/knowledge-center/iam-policy-service-control-policy/
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html

Check out this AWS Organizations Cheat Sheet:
https://tutorialsdojo.com/aws-organizations/

</details>

<a id="q63"></a>

## Q63

An IT consultancy company has multiple offices located in San Francisco, Frankfurt, Tokyo, and Manila. The company is using AWS Organizations to easily manage its several AWS accounts which are being used by its regional offices and subsidiaries. A new AWS account was recently added to a specific organizational unit (OU) which is responsible for the overall systems administration. The solutions architect noticed that the account is using a root-created Amazon ECS Cluster with an attached service-linked role. For regulatory purposes, the solutions architect created a custom SCP that would deny the new account from performing certain actions in relation to using ECS. However, after applying the policy, the new account could still perform the actions that it was supposed to be restricted from doing. 
Which of the following is the most likely reason for this problem?

- **A.** The ECS service is being run outside the jurisdiction of the organization. SCPs affect only the principals that are managed by accounts that are part of the organization.
- **B.** There is an SCP attached to a higher-level OU that permits the actions of the service-linked role. This permission would therefore be inherited by the current OU, and override the SCP placed by the administrator.
- **C.** The default SCP grants all permissions attached to every root, OU, and account. To apply stricter permissions, this policy is required to be modified.
- **D.** SCPs do not affect any service-linked role. Service-linked roles enable other AWS services to integrate with AWS Organizations and can't be restricted by SCPs.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** SCP denies ECS actions but still allowed

⚠️ **Watch:** SCPs also don't affect the management account

🧠 **Rule:** SCPs don't restrict service-linked roles.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Organization root
   │
   OU "Systems Administration"
   │
   AWS Account mới
   │
   ├── Amazon ECS Cluster (root-created)
   │        │
   │        └── Service-linked role (tự ECS tạo, để tích hợp với AWS Organizations/service khác)
   │
   └── SCP mới: DENY một số hành động liên quan ECS
        → Vẫn KHÔNG chặn được! Vì sao?
```

Solutions Architect tạo SCP deny cho account mới, nhưng account vẫn thực hiện được các action bị deny liên quan ECS. Đáp án đúng: **D**. Anh chọn đúng D.

#### Vì sao D đúng

**D đúng** vì đây là một exception được AWS Organizations document rõ: **SCP không bao giờ ảnh hưởng tới service-linked role**. Service-linked role được thiết kế để một AWS service (ở đây là ECS) tự thao tác/tích hợp với các service khác (bao gồm cả Organizations) mà không phụ thuộc vào permission của user/role thông thường — nên dù SCP có deny action nào ở cấp account/OU, service-linked role vẫn hoạt động bình thường, không bị filter qua SCP.

#### Từng đáp án sai vì đâu

- **A sai:** đề không nói ECS chạy "ngoài jurisdiction" của organization — service-linked role được tạo **trong chính account của organization** (do root/account đó tạo), nên Principal ở đây vẫn thuộc organization. Ngoài ra option này đánh tráo khái niệm: đề hỏi account bị deny action, không phải "service" bị deny.
- **B sai:** dù giả sử có SCP Allow ở OU cao hơn cho service-linked role, thì khi account tạo một SCP **Deny** mới, explicit Deny luôn override Allow (theo quy tắc filter permission của SCP) — nên nếu đây thực sự là do IAM permission bình thường, SCP Deny mới vẫn phải có tác dụng. Việc "vẫn cho phép" không xuất phát từ việc bị inherit Allow, mà từ việc SCP hoàn toàn không áp dụng lên service-linked role.
- **C sai:** đúng là có SCP mặc định `FullAWSAccess` gán cho mọi root/OU/account cho phép tất cả — nhưng đề đã nói rõ administrator **đã tạo một Deny SCP mới**, tức là đã "sửa" policy theo đúng ý C đề xuất rồi. Option này không giải thích được tại sao Deny mới vẫn không có hiệu lực.

| Đáp án | Giải thích | Vấn đề |
|---|---|---|
| **D (đúng)** | SCP không áp dụng lên service-linked role | Không |
| A | ECS "ngoài" organization | Sai — service-linked role được tạo trong account của org |
| B | SCP Allow ở OU cao hơn override | Sai — explicit Deny luôn thắng Allow theo cơ chế SCP |
| C | Default SCP chưa bị sửa | Sai — đề đã nói administrator tạo Deny SCP rồi |

#### ⚠️ Lỗi lặp lại (liên quan Q40)

Q40 là một bài SCP khác dễ nhầm: khi SCP **Deny** được gán ở **root** của Organization, **mọi OU con** (bao gồm cả OU tạm/onboarding) đều **inherit** deny đó — một Allow SCP ở OU con **không** override được Deny ở root. Q63 và Q40 đều xoay quanh nguyên tắc "explicit Deny luôn thắng, và luôn evaluate theo toàn bộ chuỗi từ root xuống account", nhưng Q63 thêm một exception riêng: **service-linked role nằm ngoài phạm vi ảnh hưởng của SCP hoàn toàn**, dù SCP đó đặt ở đâu trong cây OU.

#### Quy tắc nhớ cho thi

- **SCP không ảnh hưởng service-linked role** — dù Deny đặt ở root, OU, hay account trực tiếp.
- **Explicit Deny trong SCP luôn override Allow** (bao gồm cả default `FullAWSAccess`), bất kể Deny đặt ở cấp nào trong cây.
- SCP **không** cấp permission — nó chỉ filter permission mà IAM policy đã cấp; nhưng service-linked role thì miễn khỏi filter này.
- Đề nói "account vẫn làm được hành động dù có Deny SCP, và liên quan tới service-linked role" → nghĩ ngay tới exception này, không đi vòng qua OU inheritance hay default SCP.

### TD explanation

Users and roles must still be granted permissions using IAM permission policies attached to them or to groups. The SCPs filter the permissions granted by such policies, and the user can’t perform any actions that the applicable SCPs don’t allow. Actions allowed by the SCPs can be used if they are granted to the user or role by one or more IAM permission policies.

When you attach SCPs to the root, OUs, or directly to accounts, all policies that affect a given account are evaluated together using the same rules that govern IAM permission policies:
– Any action that has an explicit Deny in an SCP can’t be delegated to users or roles in the affected accounts. An explicit Deny statement overrides any Allow that other SCPs might grant.
– Any action that has an explicit Allow in an SCP (such as the default “*” SCP or by any other SCP that calls out a specific service or action) can be delegated to users and roles in the affected accounts.
– Any action that isn’t explicitly allowed by an SCP is implicitly denied and can’t be delegated to users or roles in the affected accounts.
By default, an SCP named FullAWSAccess is attached to every root, OU, and account. This default SCP allows all actions and all services. So in a new organization, until you start creating or manipulating the SCPs, all of your existing IAM permissions continue to operate as they did. As soon as you apply a new or modified SCP to a root or OU that contains an account, the permissions that your users have in that account become filtered by the SCP. Permissions that used to work might now be denied if they’re not allowed by the SCP at every level of the hierarchy down to the specified account.
As stated in the documentation of AWS Organizations, SCPs DO NOT affect any service-linked role. Service-linked roles enable other AWS services to integrate with AWS Organizations and can’t be restricted by SCPs.

The option that says: The default SCP grants all permissions attached to every root, OU, and account. To apply stricter permissions, this policy is required to be modified is incorrect. The scenario already implied that the administrator created a Deny policy. By default, an SCP named FullAWSAccess is attached to every root, OU, and account. This default SCP allows all actions and all services. However, you specify a Deny policy if you want to create a blacklist that blocks all access to the specified services and actions. The explicit Deny on specific actions in the blacklist policy overrides the Allow in any other policy, such as the one in the default SCP.
The option that says: There is an SCP attached to a higher-level OU that permits the actions of the service-linked role. This permission would therefore be inherited by the current OU, and override the SCP placed by the administrator is incorrect because even if a higher-level OU has an SCP attached with an Allow policy for the service, the current set up should still have restricted access to the service. Creating and attaching a new Deny SCP to the new account’s OU will not be affected by the pre-existing Allow policy in the same OU.
The option that says: The ECS service is being run outside the jurisdiction of the organization. SCPs affect only the principals that are managed by accounts that are part of the organization is incorrect because the service-linked role must have been created within the organization, most notably by the root account of the organization. It also does not make sense if we make the assumption that the service is indeed outside of the organization’s jurisdiction because the Principal element of a policy specifies which entity will have limited permissions. But the scenario tells us that it should be the new account that is denied certain actions, not the service itself.

References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html

Service Control Policies (SCP) vs IAM Policies:
https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/

Comparison of AWS Services Cheat Sheets:
https://tutorialsdojo.com/comparison-of-aws-services/

</details>

<a id="q66"></a>

## Q66

A multinational consumer goods corporation structured their AWS accounts to use AWS Organizations, which consolidates payment of their multiple AWS accounts for their various Business Units (BU’s) namely Beauty products, Baby products, Health products, and Home Care products unit. One of their Solutions Architects for the Baby products business unit has purchased 10 Reserved Instances for their new Supply Chain application which will go live 3 months from now. However, they do not want their Reserved Instance (RI) discounts to be shared by the other business units.
Which of the following options is the most suitable solution for this scenario?

- **A.** Since the Baby product business unit is part of an AWS Organization, the Reserved Instances will always be shared across other member accounts. There is no way to disable this setting.
- **B.** Turn off the Reserved Instance (RI) sharing on the master account for all of the member accounts in the Baby products business unit.
- **C.** Remove the AWS account of the Baby products business unit out of the AWS Organization.
- **D.** Set the Reserved Instance (RI) sharing to private on the AWS account of the Baby products business unit.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** don't share RI discounts with other BUs

⚠️ **Watch:** RIs can't be moved between accounts

🧠 **Rule:** Turn off RI/Savings Plans discount sharing for those accounts in the management account.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations (Consolidated Billing)
   │
   ├── Beauty products account
   ├── Baby products account   ── mua 10 RI, KHÔNG muốn share discount
   ├── Health products account
   └── Home Care products account

Mặc định: RI discount được SHARE cho TẤT CẢ account trong Organization
Yêu cầu: Baby products muốn giữ riêng RI discount của mình
```

Đáp án đúng: **B** — tắt RI sharing ở **management/master account** cho các member account thuộc Baby products BU. Anh chọn đúng B.

#### Vì sao B đúng

**B đúng** vì consolidated billing coi tất cả account trong Organization như một account để tính billing, nên theo default, RI hourly cost-benefit **luôn được chia sẻ** cho account khác có instance phù hợp. Cách chính thức để ngăn việc này là trên **payer/master account**, vào Billing and Cost Management console → Preferences → **turn off Reserved Instance discount sharing** cho các member account cụ thể. Đây là setting nằm ở cấp master account, không phải ở account thành viên.

#### Từng đáp án sai vì đâu

- **A sai (chính là điều anh không chọn nhưng dễ nhầm):** đây là câu tuyên bố sai hoàn toàn — AWS **có** cung cấp cơ chế tắt RI sharing, không phải "always shared, no way to disable".
- **C sai:** remove account khỏi Organization là giải pháp quá "nặng tay" — sẽ mất luôn các lợi ích khác của consolidated billing (ví dụ volume discount, gộp free tier...) chỉ để giải quyết một vấn đề về RI sharing, trong khi có cách đơn giản hơn (tắt sharing) ngay trong Organization.
- **D sai:** "set RI sharing to private" — đây là chi tiết **không tồn tại** trong Billing Console. Không có tùy chọn "private" cho RI/Savings Plans discount sharing, và quan trọng hơn, member account **không có quyền** tự tắt RI sharing của chính nó — quyền này chỉ thuộc về payer/master account.

| Đáp án | Hành động | Vấn đề |
|---|---|---|
| **B (đúng)** | Master account tắt RI sharing cho account Baby products | Không |
| A | Tuyên bố "không thể tắt" | Sai fact |
| C | Remove account khỏi Organization | Quá cực đoan, mất lợi ích consolidated billing khác |
| D | "Set to private" ở account con | Setting không tồn tại; sai cấp thực hiện |

#### Quy tắc nhớ cho thi

- **RI/Savings Plans discount sharing** mặc định áp dụng cho **toàn bộ** account trong Organization (qua consolidated billing).
- Chỉ **management/payer account** mới tắt được RI sharing cho một hoặc nhiều member account — member account tự nó không có quyền này.
- **Không có** tùy chọn "private" trong Billing preferences — chỉ có on/off cho RI discount sharing.
- Reserved Instances **không di chuyển được** giữa account (không "move" RI sang account khác) — chỉ có thể kiểm soát việc **share hay không share** hourly benefit.

### TD explanation

For billing purposes, the consolidated billing feature of AWS Organizations treats all the accounts in the organization as one account. This means that all accounts in the organization can receive the hourly cost-benefit of Reserved Instances that are purchased by any other account. In the payer account, you can turn off Reserved Instance discount sharing on the Preferences page on the Billing and Cost Management console.
The master account of an organization can turn off Reserved Instance (RI) sharing for member accounts in that organization. This means that Reserved Instances are not shared between that member account and other member accounts. You can change this preference multiple times. Each estimated bill is computed using the last set of preferences. However, take note that turning off Reserved Instance sharing can result in a higher monthly bill.

Hence, the correct answer is: Turn off the Reserved Instance (RI) sharing on the master account for all of the member accounts in the Baby products business unit.
The option that says: Set the Reserved Instance (RI) sharing to private on the AWS account of the Baby products business unit is incorrect because there is no “private” option in the RI and Savings Plan discount sharing settings in the Billing Management Console. By default, the member account doesn’t have the capability to turn off RI sharing on their account.
The option that says: Remove the AWS account of the Baby products business unit out of the AWS Organization is incorrect because removing the Baby products business unit account from the AWS Organization is not the optimal solution to prevent the other account from sharing its RI discounts. You can simply turn off the Reserved Instance discount sharing in the payer account.
The option that says: Since the Baby product business unit is part of an AWS Organization, the Reserved Instances will always be shared across other member accounts. There is no way to disable this setting is incorrect because this statement is false. There is certainly a way to disable the current setting by simply turning off RI sharing.

References:
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html
https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off-process.html

Check out this AWS Billing and Cost Management Cheat Sheet:
https://tutorialsdojo.com/aws-billing-and-cost-management/

</details>

<a id="q71"></a>

## Q71

A company is hosting a multi-tier web application in AWS. It is composed of an Application Load Balancer and Amazon EC2 instances across three Availability Zones. During peak load, its stateless web servers operate at 95% utilization. The current configuration relies on a fixed capacity model rather than a dynamic scaling policy, which limits its ability to respond quickly to sudden traffic surges and AZ failures. The system is set up to use Reserved Instances to handle the steady-state load and On-Demand Instances to handle the peak load. The manager instructed the team to review the current architecture and make the necessary changes to improve the system. 
Which of the following provides the most cost-effective architecture to allow the application to recover quickly in the event that an Availability Zone is unavailable during peak load?

- **A.** Use a combination of Reserved and On-Demand instances on each AZ to handle both the steady state and peak load.
- **B.** Launch an Auto Scaling group of Reserved instances on each AZ to handle the peak load. Retain the current setup for handling the steady state load.
- **C.** Launch a Spot Fleet using a diversified allocation strategy, with Auto Scaling enabled on each AZ to handle the peak load instead of On-Demand instances. Retain the current setup for handling the steady state load.
- **D.** Use a combination of Spot and On-Demand instances on each AZ to handle both the steady state and peak load.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** recover from AZ loss at peak; most cost-effective

⚠️ **Watch:** Spot diversified reduces AZ/pool interruption risk

🧠 **Rule:** Peak capacity cheaply + resilient → Spot Fleet diversified allocation + Auto Scaling per AZ.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ALB
 │
 ├── AZ-1: EC2 (Reserved) ─┐
 ├── AZ-2: EC2 (Reserved) ─┼─ steady-state load (fixed capacity)
 └── AZ-3: EC2 (Reserved) ─┘

Peak load hiện tại: On-Demand instances, KHÔNG có dynamic scaling
   → 95% utilization, không phản ứng nhanh khi 1 AZ down lúc peak

Yêu cầu: cost-effective NHẤT + recover NHANH khi mất 1 AZ lúc peak
```

Giữ nguyên phần steady-state (Reserved), chỉ cải tiến phần **peak load**. Đáp án đúng: **C**. Anh chọn đúng C.

#### Vì sao C đúng

**C đúng** vì kết hợp hai yếu tố: **Spot Fleet với diversified allocation strategy** và **Auto Scaling trên mỗi AZ**. Spot instance rẻ hơn hẳn On-Demand/Reserved, giải quyết bài toán "cost-effective nhất" cho phần peak load (vốn không cần chạy 24/7). "Diversified allocation strategy" là best practice để tăng khả năng Spot request được fulfill khi có outage ở 1 AZ — bằng cách trải request qua nhiều AZ (mỗi AZ dùng subnet riêng) và nhiều instance pool, nên khi 1 AZ gặp sự cố, capacity ở các AZ khác vẫn tiếp tục phục vụ ngay, đúng yêu cầu "recover quickly". Auto Scaling group đảm bảo capacity luôn co giãn theo tải thực tế trên từng AZ.

#### Từng đáp án sai vì đâu

- **A sai:** kết hợp Reserved + On-Demand trên mỗi AZ — không dùng Auto Scaling nên vẫn giữ mô hình fixed capacity, không phản ứng nhanh được khi traffic surge hoặc mất AZ; Reserved cũng đắt hơn Spot cho phần tải không liên tục (peak).
- **B sai:** dùng Auto Scaling nhưng lại gắn với **Reserved Instances** cho peak load — Reserved chỉ tối ưu cho tải ổn định dài hạn (đã dùng đúng cho steady-state), dùng RI cho peak load (không liên tục) sẽ đắt hơn Spot một cách không cần thiết.
- **D sai:** kết hợp Spot + On-Demand nhưng **không đề cập Auto Scaling** — thiếu chính yếu tố cho phép hệ thống tự động co giãn/phục hồi nhanh khi 1 AZ down lúc peak; đề yêu cầu rõ khả năng "recover quickly", không có Auto Scaling thì không đạt được.

| Đáp án | Compute cho peak | Auto Scaling? | Vấn đề |
|---|---|---|---|
| **C (đúng)** | Spot Fleet (diversified) | Có, theo từng AZ | Không |
| A | Reserved + On-Demand | Không | Fixed capacity, không recover nhanh |
| B | Reserved | Có | RI đắt hơn Spot cho tải không liên tục |
| D | Spot + On-Demand | Không | Thiếu Auto Scaling |

#### Quy tắc nhớ cho thi

- **Peak load, không liên tục, cần rẻ nhất** → **Spot Instances/Spot Fleet**, không phải Reserved (Reserved dành cho tải ổn định/dài hạn).
- **Muốn tăng khả năng chịu lỗi khi 1 AZ down với Spot** → **diversified allocation strategy** (nhiều AZ, nhiều subnet, nhiều instance pool).
- **"Recover quickly" / phản ứng nhanh với traffic surge** → luôn cần **Auto Scaling group**; đáp án thiếu Auto Scaling nên loại ngay.
- Giữ nguyên phần đã đúng (steady-state dùng Reserved) — chỉ thay đổi phần đề bài chỉ ra là có vấn đề (peak load, fixed capacity).

### TD explanation

The scenario requires a cost-effective architecture to allow the application to recover quickly. Hence, using an Auto Scaling group is a must to handle the peak load and improve both the availability and scalability of the application.
Setting up a diversified allocation strategy for your Spot Fleet is a best practice to increase the chances that a spot request can be fulfilled by EC2 capacity in the event of an outage in one of the Availability Zones. You can include each AZ available to you in the launch specification. And instead of using the same subnet each time, use three unique subnets (each mapping to a different AZ).

Hence, the correct answer is: Launch a Spot Fleet using a diversified allocation strategy, with Auto Scaling enabled on each AZ to handle the peak load instead of On-Demand instances. Retain the current setup for handling the steady state load. The Spot instances are the most cost-effective for handling the temporary peak loads of the application.
The option that says: Launch an Auto Scaling group of Reserved instances on each AZ to handle the peak load. Retain the current setup for handling the steady state load is incorrect because even though it uses Auto Scaling, Reserved Instances cost more than Spot instances, so it is just more suitable to use the latter to handle the peak load.
The following options are incorrect because they did not mention the use of Auto Scaling Groups, which is a primary requirement for this architecture:
– Use a combination of Spot and On-Demand instances on each AZ to handle both the steady state and peak load.
– Use a combination of Reserved and On-Demand instances on each AZ to handle both the steady state and peak load.

References:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-examples.html#fleet-config5
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html
https://github.com/awsdocs/amazon-ec2-user-guide/pull/56

Check out this AWS Billing and Cost Management Cheat Sheet:
https://tutorialsdojo.com/aws-billing-and-cost-management/

</details>

<a id="q75"></a>

## Q75

A company wants to host its internal web application in AWS. The front-end uses Docker containers, and it connects to a MySQL instance as the backend database. The company plans to use AWS-managed container services to reduce the overhead of managing the servers. The application should allow employees to access company documents, which are accessed frequently for the first 3 months and then rarely after that. As part of the company policy, these documents must be retained for at least five years. Because this is an internal web application, the company wants to have the lowest possible cost.
Which of the following implementations is the most cost-effective solution?

- **A.** Deploy the Docker containers using Amazon Elastic Kubernetes Service (Amazon EKS) with auto-scaling enabled. Use Amazon EC2 Spot instances for the EKS cluster to further reduce costs. Use On-Demand instances for the Amazon RDS database and its read replicas. Create an encrypted Amazon S3 bucket to store the company documents. Create a bucket lifecycle policy that will move the documents to S3 Glacier after three months and will delete objects older than five years.
- **B.** Deploy the Docker containers using Amazon Elastic Container Service (Amazon ECS) with Amazon EC2 Spot Instances. Ensure that Spot Instance draining is enabled on the ECS agent config. Use Reserved instance for the Amazon RDS database and its read replicas. Create an encrypted Amazon S3 bucket to store the company documents. Create a bucket lifecycle policy that will move the documents to S3 Glacier after three months and will delete objects older than five years.
- **C.** Deploy the Docker containers using Amazon Elastic Container Service (Amazon ECS) with Amazon EC2 Spot Instances. Use Amazon Aurora Serverless v2 for the MySQL backend. Create an encrypted Amazon EBS volume on the EC2 hosts that is shared with the containers to store the company documents. Set up a cron job that will delete the files after five years.
- **D.** Deploy the Docker containers using Amazon Elastic Container Service (Amazon ECS) with Amazon EC2 On-Demand instances. Use On-Demand instances as well for the Amazon RDS database and its read replicas. Create an Amazon EFS volume that is mounted on the EC2 instances to store the company documents. Create a cron job that will copy the documents to Amazon S3 Glacier after three months and then create a bucket lifecycle policy that will delete objects older than five years.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** internal app; docs hot 3 months, retain 5 years; lowest cost

⚠️ **Watch:** Spot draining needed to avoid dropped tasks

🧠 **Rule:** ECS on Spot (draining) + RDS RI + S3 lifecycle → Glacier.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Internal web app
   │
   Front-end: Docker containers ──► Amazon ECS (managed container service)
   │            │
   │            └── EC2 Spot Instances (rẻ) + Spot draining enabled
   │
   Backend: MySQL ──► Amazon RDS + read replicas
   │            └── Reserved Instances (chạy liên tục, dự đoán được)
   │
   Company documents:
   │   - Hot 3 tháng đầu, rồi rarely accessed
   │   - Phải giữ ít nhất 5 năm
   │            │
   │            └── Amazon S3 (encrypted) + Lifecycle policy:
   │                  → move to Glacier sau 3 tháng
   │                  → delete sau 5 năm
```

Yêu cầu: dùng AWS-managed container service, lowest cost nhất. Đáp án đúng: **B**. Anh chọn đúng B.

#### Vì sao B đúng

**B đúng** vì kết hợp 3 lựa chọn rẻ nhất cho từng phần đúng bản chất workload:

1. **ECS + EC2 Spot Instances** cho compute container — Spot rẻ hơn hẳn On-Demand, phù hợp vì đây là internal app (chấp nhận được rủi ro gián đoạn ngắn). **Spot Instance draining phải enable** để ECS nhận signal 2 phút cảnh báo trước khi Spot bị thu hồi, chuyển instance vào trạng thái DRAINING, dừng nhận task mới và di task đang PENDING sang instance khác — tránh downtime khi Spot bị terminate.
2. **RDS Reserved Instance** cho MySQL — vì database chạy liên tục 24/7 (steady-state, dự đoán được), Reserved rẻ hơn On-Demand cho use case này.
3. **S3 + lifecycle policy** cho company documents — đúng khớp pattern "hot 3 tháng rồi rarely accessed, giữ 5 năm": transition sang Glacier sau 3 tháng (giảm chi phí lưu trữ) và expiration action tự xóa sau 5 năm (đáp ứng compliance retention, không cần quản lý thủ công).

#### Từng đáp án sai vì đâu

- **A sai:** dùng **EKS** thay ECS — EKS phức tạp/tốn phí hơn ECS cho cùng nhu cầu (EKS có phí cluster riêng, cần quản lý control plane nhiều hơn), trong khi đề chỉ cần "AWS-managed container service" đơn giản; dùng **On-Demand cho RDS** thay vì Reserved cũng đắt hơn không cần thiết cho tải liên tục dự đoán được.
- **C sai:** dùng **Aurora Serverless v2** cho backend — có thể đắt hơn RDS Reserved cho workload dự đoán được/liên tục (Serverless phù hợp hơn cho tải biến động); lưu company documents trên **EBS volume chia sẻ trên EC2 host** tốn thêm dung lượng đĩa không cần thiết, đắt hơn S3; dùng **cron job để tự xóa file sau 5 năm** thiếu độ tin cậy/tự động hóa so với S3 lifecycle policy (không có cơ chế transition sang storage rẻ hơn ở giữa chu kỳ).
- **D sai:** dùng **On-Demand cho cả ECS và RDS** — đắt nhất trong 4 đáp án vì bỏ lỡ cả 2 cơ hội tiết kiệm (Spot cho compute, Reserved cho DB); lưu document trên **EFS** đắt hơn S3 đáng kể cho cùng nhu cầu lưu trữ; phải tự viết **cron job để copy sang Glacier** thay vì dùng lifecycle policy có sẵn — thêm overhead vận hành không cần thiết.

| Đáp án | Compute | Database | Storage | Vấn đề |
|---|---|---|---|---|
| **B (đúng)** | ECS + Spot (draining) | RDS Reserved | S3 + lifecycle | Không |
| A | EKS + Spot | RDS On-Demand | S3 + lifecycle | EKS phức tạp/đắt hơn; RDS On-Demand đắt hơn Reserved |
| C | ECS + Spot | Aurora Serverless v2 | EBS + cron xóa | Aurora Serverless đắt hơn cho tải liên tục; EBS đắt, cron thiếu tự động |
| D | ECS + On-Demand | RDS On-Demand | EFS + cron copy Glacier | Đắt nhất; EFS đắt hơn S3; thiếu lifecycle tự động |

#### Quy tắc nhớ cho thi

- **AWS-managed container service, đơn giản, ít overhead** → **ECS** thường rẻ/gọn hơn EKS khi không cần tính năng Kubernetes đặc thù.
- **Compute không cần liên tục 24/7, chấp nhận gián đoạn ngắn** → **EC2 Spot**, kèm bắt buộc **Spot Instance draining** khi dùng với ECS.
- **Database chạy liên tục, tải dự đoán được** → **RDS Reserved Instance** rẻ hơn On-Demand/Aurora Serverless.
- **File hot rồi rarely accessed, có yêu cầu retention theo compliance** → **S3 + Lifecycle policy** (transition + expiration), không dùng EBS/EFS và không tự viết cron job để làm việc mà lifecycle policy đã làm sẵn.

### TD explanation

A Spot Instance is an unused Amazon EC2 instance that is available for less than the On-Demand price. Because Spot Instances enable you to request unused EC2 instances at steep discounts, you can lower your Amazon EC2 costs significantly. The hourly price for a Spot Instance is called a Spot price. The Spot price of each instance type in each Availability Zone is set by Amazon EC2, and adjusted gradually based on the long-term supply of and demand for Spot Instances. You can register Spot Instances to your Amazon ECS clusters. Amazon EC2 terminates, stops, or hibernates your Spot Instance when the Spot price exceeds the maximum price for your request or capacity is no longer available. Amazon EC2 provides a Spot Instance interruption notice, which gives the instance a two-minute warning before it is interrupted. If Amazon ECS Spot Instance draining is enabled on the instance, ECS receives the Spot Instance interruption notice and places the instance in DRAINING status.

When a container instance is set to DRAINING, Amazon ECS prevents new tasks from being scheduled for placement on the container instance. Service tasks on the draining container instance that are in the PENDING state are stopped immediately. If there are container instances in the cluster that are available, replacement service tasks are started on them. Spot Instance draining is disabled by default and must be manually enabled by adding the line ECS_ENABLE_SPOT_INSTANCE_DRAINING=true on your /etc/ecs/ecs.config file.
S3 Lifecycle helps you store objects cost-effectively throughout their lifecycle by transitioning them to lower-cost storage classes or deleting expired objects on your behalf. To manage the lifecycle of your objects, create an S3 Lifecycle configuration for your bucket. An S3 Lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of objects. There are two types of actions:
– Transition – These actions define when objects transition to another storage class. For example, you might transition objects to the S3 Standard-IA storage class 30 days after creating them, or archive objects to the S3 Glacier Flexible Retrieval storage class one year after creating them.
– Expiration actions – These actions define when objects expire. Amazon S3 deletes expired objects on your behalf. For example, you might expire objects after being stored for a regulatory compliance period.
Therefore, the correct answer is: Deploy the Docker containers using Amazon Elastic Container Service (Amazon ECS) with Amazon EC2 Spot Instances. Ensure that Spot Instance draining is enabled on the ECS agent config. Use Reserved instance for the Amazon RDS database and its read replicas. Create an encrypted Amazon S3 bucket to store the company documents. Create a bucket lifecycle policy that will move the documents to S3 Glacier after three months and will delete objects older than five years. This solution combines cost-effective compute (Spot Instances), predictable database pricing (RDS Reserved Instances), and optimal storage lifecycle management (S3 + Glacier + lifecycle policy). This setup minimizes operational overhead while meeting retention and access requirements.
The option that says: Deploy the Docker containers using Amazon Elastic Container Service (Amazon ECS) with Amazon EC2 Spot Instances. Use Amazon Aurora Serverless v2 for the MySQL backend. Create an encrypted Amazon EBS volume on the EC2 hosts that is shared with the containers to store the company documents. Set up a cron job that will delete the files after five years is incorrect. Storing company documents on the EC2 instances will require more disk space on instances, which is unnecessary and expensive. Aurora Serverless v2 may be more expensive than RDS Reserved for predictable workloads. Also, using cron jobs for retention pimarily lacks the automation and durability of S3 lifecycle policies.
The option that says:  Deploy the Docker containers using Amazon Elastic Container Service (Amazon ECS) with Amazon EC2 On-Demand instances. Use On-Demand instances as well for the Amazon RDS database and its read replicas. Create an Amazon EFS volume that is mounted on the EC2 instances to store the company documents. Create a cron job that will copy the documents to Amazon S3 Glacier after three months and then create a bucket lifecycle policy that will delete objects older than five years is incorrect. This is possible, however, using EFS volumes is typically more expensive than just storing the files on Amazon S3 in the first place.
The option that says: Deploy the Docker containers using Amazon Elastic Kubernetes Service (Amazon EKS) with auto-scaling enabled. Use Amazon EC2 Spot instances for the EKS cluster to further reduce costs. Use On-Demand instances for the Amazon RDS database and its read replicas. Create an encrypted Amazon S3 bucket to store the company documents. Create a bucket lifecycle policy that will move the documents to S3 Glacier after three months and will delete objects older than five years is incorrect. This option is also possible, however, using on-demand instances for continuously running RDS instances is expensive. You can save costs by using Reserved instances for Amazon RDS.

References:
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-spot.html
https://aws.amazon.com/ec2/spot/containers-for-less/get-started/
https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html

Check out this Amazon ECS Cheat Sheet:
https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

</details>

---

# Group E — Resilience / DR / performance (3)

<a id="q16"></a>

## Q16

A tech startup is planning to launch a new global mobile marketplace using AWS Amplify and AWS Mobile Hub. To lower the latency, the backend APIs will be launched to multiple AWS regions to process the sales and financial transactions in the region closest to the users. The solutions architect is instructed to design the system architecture to ensure that the transactions made in one region are automatically replicated to other regions. In the coming months ahead, it is expected that the marketplace will have millions of users across North America, South America, Europe, and Asia. The team considered Amazon Keyspaces for its wide‑column store capabilities, but it would have required more operational effort to manage cross‑region replication.
Which of the following is the most scalable, cost-effective, and highly available architecture that should be implemented?

- **A.** Create Amazon S3 buckets in all required regions. Store the individual transactions in the S3 bucket in the local region. Replicate the transactions between regions using S3 Cross-Region Replication.
- **B.** Use a combination of AWS Control Tower and Amazon Connect to launch and centrally manage multiple Amazon DynamoDB tables in various AWS Regions. In each local region, store the individual transactions to a DynamoDB replica table in the same region.
- **C.** Create a Global Amazon DynamoDB table with replica tables across several AWS regions that you prefer. In each local region, store the individual transactions to a DynamoDB replica table in the same region. Any changes made in one of the replica tables will automatically be replicated across all other tables.
- **D.** In each local region, store the individual transactions to an Amazon DynamoDB table. Set up an AWS Lambda function to read recent writes from the table, and replay the data to DynamoDB tables in all other regions.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** multi-Region transactions; Keyspaces too much effort

⚠️ **Watch:** Aurora Global = single writer Region

🧠 **Rule:** Multi-Region active-active NoSQL → DynamoDB global tables.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
North America     South America     Europe     Asia
     │                  │              │           │
   Backend API (nhiều region, gần user để giảm latency)
     │                  │              │           │
     └──────── transaction ghi 1 region PHẢI tự replicate sang region khác ────────┘
```

Millions user, cần **replicate transaction giữa các Region tự động**, scalable + HA + cost-effective. Anh chọn đúng **C**: **Global DynamoDB table** với replica table ở nhiều Region.

#### Vì sao C đúng

Global Tables là DynamoDB **multi-Region, multi-master**:

- Viết vào replica table ở bất kỳ Region nào → **tự động replicate** sang tất cả Region khác (dùng DynamoDB Streams bên dưới), không cần code riêng để đồng bộ.
- Vẫn giữ **local read/write** ở Region gần user nhất → latency thấp đúng mục tiêu ban đầu.
- Chịu được cả khi 1 Region bị sự cố/cô lập — các Region khác vẫn hoạt động → đúng "highly available".
- Scale tự động theo traffic của DynamoDB gốc → phù hợp "millions of users", "scalable".

#### Vì sao từng đáp án sai bị loại

- **D sai** vì dùng **Lambda function tự đọc recent writes rồi replay** sang các table Region khác — đây là replication **tự viết tay**, không scale được khi có triệu user (một Lambda function phải xử lý toàn bộ khối lượng ghi khổng lồ), và không đáng tin cậy như cơ chế Global Tables có sẵn.
- **B sai** vì **AWS Control Tower** (thiết lập/quản trị multi-account) và **Amazon Connect** (contact center) **không có chức năng gì để tạo hoặc quản lý DynamoDB Global Table** — hai dịch vụ này hoàn toàn sai mục đích trong ngữ cảnh này.
- **A sai** vì **Amazon S3** không phải thiết kế cho workload **transactional, real-time** — S3 Cross-Region Replication có độ trễ và phù hợp cho object storage (ảnh, file, backup...), không phù hợp lưu và đồng bộ giao dịch tài chính cần tính nhất quán và tốc độ.

#### So sánh nhanh

| Đáp án | Dịch vụ chính | Cơ chế replicate | Scale cho triệu user? |
|---|---|---|---|
| **C (đúng)** | DynamoDB Global Tables | Tự động, built-in (Streams) | ✅ |
| D | DynamoDB + Lambda tự viết | Custom, thủ công | ❌ Không scale, dễ nghẽn |
| B | DynamoDB (nhưng dùng sai tool quản lý) | Không rõ, Control Tower/Connect không hỗ trợ | ❌ |
| A | S3 Cross-Region Replication | Object replication, có độ trễ | ❌ Không hợp transaction |

#### Lưu ý thực tế

- Đề có nhắc tới **Amazon Keyspaces** (Cassandra-compatible) như một lựa chọn cân nhắc nhưng bị loại vì "tốn operational effort hơn để quản lý cross-Region replication" — đây là chi tiết củng cố hướng chọn DynamoDB Global Tables, không phải một đáp án trắc nghiệm thật.
- Aurora Global Database thường bị nhắc tới trong các câu tương tự nhưng có đặc điểm **chỉ 1 Region là writer chính** (primary), các Region khác chủ yếu để đọc — khác với yêu cầu ở đây là ghi transaction **ở mọi Region cùng lúc** (multi-master).

#### Quy tắc nhớ cho thi

- **"Multi-Region, ghi ở nhiều nơi, tự động đồng bộ"** → **DynamoDB Global Tables** (multi-master)
- **"Chỉ 1 Region ghi chính, các Region khác đọc"** → cân nhắc **Aurora Global Database** (không phải multi-master)
- **Amazon S3 Cross-Region Replication** → chỉ dùng cho **object storage**, không dùng cho **transactional workload**
- **Tự viết Lambda để replicate dữ liệu giữa Region** → hầu như luôn là đáp án sai khi đã có dịch vụ managed thay thế (Global Tables, DMS...)

### TD explanation

Global Tables builds upon DynamoDB’s global footprint to provide you with a fully managed, multi-region, and multi-master database that provides fast, local, read and write performance for massively scaled, global applications. Global Tables replicates your Amazon DynamoDB tables automatically across your choice of AWS regions.
Global Tables eliminates the difficult work of replicating data between regions and resolving update conflicts, enabling you to focus on your application’s business logic. In addition, Global Tables enables your applications to stay highly available even in the unlikely event of isolation or degradation of an entire region.

Hence, the correct answer is: Create a Global Amazon DynamoDB table with replica tables across several AWS regions that you prefer. In each local region, store the individual transactions to a DynamoDB replica table in the same region. Any changes made in one of the replica tables will automatically be replicated across all other tables.
The option that says: In each local region, store the individual transactions to an Amazon DynamoDB table. Set up an AWS Lambda function to read recent writes from the table, and replay the data to DynamoDB tables in all other regions is incorrect. Using an AWS Lambda function to replicate all data across regions is not a scalable solution. Remember that there will be millions of customers who will use the mobile app around the world, and this entails a lot of replication and compute capacity for a single Lambda function. In this scenario, the best solution is to use Global DynamoDB tables with the DynamoDB Stream option enabled to automatically handle the replication process.
The option that says: Use a combination of AWS Control Tower and Amazon Connect to launch and centrally manage multiple Amazon DynamoDB tables in various AWS Regions. In each local region, store the individual transactions to a DynamoDB replica table in the same region is incorrect. Amazon Connect is just an easy-to-use omnichannel cloud contact center that helps companies provide superior customer service at a lower cost, while AWS Control Tower just offers the easiest way to set up and govern a new, secure, multi-account AWS environment. You can’t use these two services to set up a Global DynamoDB Table.
The option that says: Create Amazon S3 buckets in all required regions. Store the individual transactions to the S3 bucket in the local region. Replicate the transactions between regions using S3 Cross-Region Replication is incorrect because Amazon S3 is not designed for transactional workloads. While S3 Cross-Region Replication can replicate objects across buckets in different regions, it’s not suitable for handling real-time, transactional data.

References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_HowItWorks.html
https://aws.amazon.com/dynamodb/global-tables/

Check out this Amazon DynamoDB Cheat Sheet:
https://tutorialsdojo.com/amazon-dynamodb/

</details>

<a id="q32"></a>

## Q32

A logistics company plans to host its web application on AWS to allow customers to track their shipping worldwide. The web application will have a multi-tier setup – Amazon EC2 instances for running the web and application layer, Amazon S3 bucket for hosting the static content, and a NoSQL database. The company plans to provision the resources in the us-east-1 region. The company also wants to have a second site hosted on us-west-1 region for disaster recovery. The second site must have the same copy of data from the primary site and the failover should be as quick as possible when the primary region becomes unavailable. Failing back to the primary region should be done automatically once it becomes available again.
Which of the following solutions should the Solutions Architect implement to meet the company requirements?

- **A.** Create the same resources of Auto Scaling group of EC2 instances for web and application tiers on both regions using AWS CloudFormation StackSets. Enable Amazon S3 cross-Region on the S3 bucket to asynchronously replicate the contents to the secondary region. Create Amazon Route 53 DNS zone entries with a failover routing policy and set the us-west-1 region as the secondary site. For the database tier, create a DynamoDB global table spanning both regions.
- **B.** Create the same resources of Auto Scaling group of EC2 instances for web and application tiers on both regions using AWS CloudFormation StackSets. Enable Amazon S3 cross-Region on the S3 bucket to asynchronously replicate the contents to the secondary region. Create Amazon Route 53 DNS zone entries with a failover routing policy and set the us-west-1 region as the secondary site. For the database tier, create an Amazon Aurora global database spanning the two regions.
- **C.** Provision the same Auto Scaling group of EC2 instances for web and application tiers in both regions using AWS Service Catalog. Enable Amazon S3 cross-Region on the S3 bucket to asynchronously replicate the contents to the secondary region. Ensure that Amazon Route 53 health check is enabled on the primary region and update the public DNS zone entry with the secondary region in case of an outage. For the database tier, create an Amazon RDS for MySQL and enable cross-region replication to create a read-replica on the secondary region.
- **D.** Create the same resources of Auto Scaling group of EC2 instances for web and application tiers on both regions using AWS CloudFormation StackSets. Enable Amazon S3 cross-Region on the S3 bucket to asynchronously replicate the contents to the secondary region. Create an Amazon CloudFront distribution. Set the S3 bucket as the origin for static files and multi-origins for the web and application tiers. For the database tier, create an Amazon DynamoDB table in each region and regularly backup to an Amazon S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** fast failover; automatic failback

⚠️ **Watch:** Route 53 failover records fail back automatically when primary is healthy

🧠 **Rule:** Warm standby: StackSets in both Regions + S3 CRR + Route 53 failover routing.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
us-east-1 (primary)                     us-west-1 (DR site)
┌───────────────────────┐               ┌───────────────────────┐
│ EC2 (web+app) ASG      │  StackSets    │ EC2 (web+app) ASG      │
│ S3 bucket               │──CRR────────►│ S3 bucket (replica)     │
│ NoSQL DB                │  ??? cách    │ NoSQL DB (đồng bộ)      │
└───────────────────────┘               └───────────────────────┘
Yêu cầu: failover NHANH nhất + failback TỰ ĐỘNG khi primary phục hồi
```

Anh chọn đúng **A — CloudFormation StackSets (2 region) + S3 CRR + Route 53 failover routing policy + DynamoDB global table**.

#### Vì sao A đúng

Đây là mô hình **warm standby**, mỗi thành phần khớp một yêu cầu:

- **CloudFormation StackSets**: triển khai đồng bộ cùng resource (ASG web/app) ở cả hai region, chỉ cần một template quản lý cả hai — nhất quán, không lệch cấu hình giữa 2 site.
- **S3 Cross-Region Replication (CRR)**: tự động sao chép nội dung tĩnh sang region phụ.
- **Route 53 failover routing policy**: đúng chính xác yêu cầu "failover nhanh nhất khi primary down và **tự động failback** khi primary healthy lại" — đây là cơ chế mặc định của failover routing policy (health check + tự chuyển đổi cả hai chiều).
- **DynamoDB global table**: vì hệ thống dùng **NoSQL database**, global table cho phép **đọc/viết multi-active** ở cả hai region, tự động đồng bộ dữ liệu hai chiều — có sẵn bản sao mới nhất ở cả hai site, đúng yêu cầu "same copy of data".

#### Vì sao các đáp án sai (distractor cần nhớ)

- **B (giống A nhưng dùng Aurora global database):** Đề bài nêu rõ database là **NoSQL**, nên phải dùng **DynamoDB global table**, không phải Aurora (Aurora là relational/SQL). Sai loại database cho use case.
- **C (Service Catalog + Route 53 health check + cập nhật DNS thủ công + RDS MySQL read-replica):** Phải **cập nhật public DNS zone thủ công** khi có outage — vi phạm yêu cầu "failover nhanh nhất" (con người can thiệp = chậm và không tự động). Đồng thời dùng RDS MySQL (SQL) thay vì NoSQL, và read-replica chỉ đọc, cần thao tác promote thủ công khi failover — không tự động.
- **D (CloudFront multi-origin + DynamoDB backup/restore qua S3):** Backup/restore từ S3 có **độ trễ (delay)**, không đảm bảo "same copy of data" theo thời gian thực như global table — nếu primary down, dữ liệu restore có thể đã cũ. CloudFront multi-origin cũng không phải cơ chế failover chuẩn cho toàn bộ web/app tier so với ALB + Route 53 failover.

#### So sánh nhanh

| Đáp án | Database | Failover DNS | Failback tự động? |
|---|---|---|---|
| **A. DynamoDB global table (đúng)** | NoSQL (đúng loại) | Route 53 failover | Có |
| B. Aurora global database | SQL (sai loại) | Route 53 failover | Có |
| C. RDS MySQL read-replica | SQL (sai loại) | Cập nhật DNS thủ công | Không |
| D. DynamoDB + S3 backup/restore | NoSQL nhưng có delay | CloudFront multi-origin | Không rõ, chậm |

#### Quy tắc nhớ cho thi

- **"NoSQL database cần đồng bộ nhiều region, đọc/viết cả hai nơi"** → **DynamoDB global table**, không phải Aurora global database (đó là cho SQL).
- **"Failover nhanh + failback tự động"** → **Route 53 failover routing policy với health check**, không phải cập nhật DNS zone thủ công.
- **CloudFormation StackSets** → công cụ chuẩn để triển khai đồng nhất resource across regions/accounts.
- Backup/restore qua S3 luôn có **độ trễ (delay)** — không phù hợp khi cần "same copy of data" real-time.

### TD explanation

AWS CloudFormation helps AWS customers implement an Infrastructure as Code model. Instead of setting up their environments and applications by hand, they build a template and use it to create all of the necessary resources, collectively known as a CloudFormation stack. This model removes opportunities for manual error, increases efficiency, and ensures consistent configurations over time.
With Amazon CloudFormation StackSets you can define an AWS resource configuration in a CloudFormation template and then roll it out across multiple AWS accounts and/or Regions with a couple of clicks. You can use this to set up a baseline level of AWS functionality that addresses the cross-account and cross-region scenarios. Once you have set this up, you can easily expand coverage to additional accounts and regions.
Amazon S3 Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. Buckets that are configured for object replication can be owned by the same AWS account or by different accounts. The objects may be replicated to a single destination bucket or multiple destination buckets. Destination buckets can be in different AWS Regions or within the same Region as the source bucket. Amazon S3 Cross-Region Replication (CRR) is used to copy objects across Amazon S3 buckets in different AWS Regions. CRR is helpful if you want to meet compliance requirements such as the need to have a copy of your data on another location.
Amazon DynamoDB global tables provide you with a fully managed, multi-region and multi-active database that delivers fast, local, read and write performance for massively scaled, global applications. Global tables replicate your DynamoDB tables automatically across your choice of AWS Regions. Global tables eliminate the difficult work of replicating data between Regions and resolving update conflicts, enabling you to focus on your application’s business logic. In addition, global tables enable your applications to stay highly available even in the unlikely event of isolation or degradation of an entire Region.

Therefore, the correct answer is: Create the same resources of Auto Scaling group of EC2 instances for web and application tiers on both regions using AWS CloudFormation StackSets. Enable Amazon S3 cross-Region on the S3 bucket to asynchronously replicate the contents to the secondary region. Create Amazon Route 53 DNS zone entries with a failover routing policy and set the us-west-1 region as the secondary site. For the database tier, create a DynamoDB global table spanning both regions.
The option that says: Create the same resources of Auto Scaling group of EC2 instances for web and application tiers on both regions using AWS CloudFormation StackSets. Enable Amazon S3 cross-Region on the S3 bucket to asynchronously replicate the contents to the secondary region. Create Amazon Route 53 DNS zone entries with a failover routing policy and set the us-west-1 region as the secondary site. For the database tier, create an Amazon Aurora global database spanning the two regions is incorrect. The application is designed for a NoSQL database so a DynamoDB global table is recommended for this, not an Amazon Aurora global database.
The option that says: Provision the same Auto Scaling group of EC2 instances for web and application tiers in both regions using AWS Service Catalog. Enable Amazon S3 cross-Region on the S3 bucket to asynchronously replicate the contents to the secondary region. Ensure that Amazon Route 53 health check is enabled on the primary region and update the public DNS zone entry with the secondary region in case of an outage. For the database tier, create an Amazon RDS for MySQL and enable cross-region replication to create a read-replica on the secondary region is incorrect. You don’t have to manually update the public DNS zone entry with the secondary region, you just have to configure the failover routing policy in Route 53 to automatically failover to the secondary site and vice versa. MySQL is not recommended as the application is designed for a NoSQL database.
The option that says: Create the same resources of Auto Scaling group of EC2 instances for web and application tiers on both regions using AWS CloudFormation StackSets. Enable Amazon S3 cross-Region on the S3 bucket to asynchronously replicate the contents to the secondary region. Create an Amazon CloudFront distribution. Set the S3 bucket as the origin for static files and multi-origins for the web and application tiers. For the database tier, create an Amazon DynamoDB table in each region and regularly backup to an Amazon S3 bucket is incorrect. You can’t reliably sync DynamoDB tables on two regions with just backups from S3. There will be a delay on the backup and restore. You should use DynamoDB global tables instead.

References:
https://aws.amazon.com/blogs/aws/use-cloudformation-stacksets-to-provision-resources-across-multiple-aws-accounts-and-regions/
https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html
https://aws.amazon.com/dynamodb/global-tables/

Check out these Amazon S3, Amazon DynamoDB, and CloudFormation StackSet Cheat Sheets:
https://tutorialsdojo.com/amazon-dynamodb/
https://tutorialsdojo.com/amazon-s3/
https://tutorialsdojo.com/aws-cloudformation-stacksets-and-nested-stacks/

</details>

<a id="q41"></a>

## Q41

A company currently hosts its online immigration system on one large Amazon EC2 instance with attached EBS volumes to store all of the applicants’ data. The registration system accepts the information from the user including documents and photos and then performs automated verification and processing to check if the applicant is eligible for immigration. The immigration system becomes unavailable at times when there is a surge of applicants using the system. The existing architecture needs improvement as it takes a long time for the system to complete the processing and the attached EBS volumes are not enough to store the ever-growing data being uploaded by the users. 
Which of the following options is the recommended option to achieve high availability and more scalable data storage?

- **A.** Upgrade to EBS with Provisioned IOPS as your main storage service and change your architecture to use an SQS queue to distribute the tasks to a group of EC2 instances. Use Auto Scaling to dynamically increase or decrease the group of EC2 instances depending on the length of the SQS queue.
- **B.** Use EBS with Provisioned IOPS to store files, SNS to distribute tasks to a group of EC2 instances working in parallel, and Auto Scaling to dynamically size the group of EC2 instances depending on the number of SNS notifications. Use CloudFormation to replicate your architecture to another region.
- **C.** Use SNS to distribute the tasks to a group of EC2 instances. Use Auto Scaling to dynamically increase or decrease the group of EC2 instances depending on the length of the SQS queue.
- **D.** Upgrade your architecture to use an S3 bucket with cross-region replication (CRR) enabled, as the storage service. Set up an SQS queue to distribute the tasks to a group of EC2 instances with Auto Scaling to dynamically increase or decrease the group of EC2 instances depending on the length of the SQS queue. Use CloudFormation to replicate your architecture to another region.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** slow processing; EBS too small; HA + scalable storage

⚠️ **Watch:** Bigger EBS = still single-AZ

🧠 **Rule:** S3 (CRR) storage + SQS + ASG workers.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Trước:
User upload docs/photos ──► 1 EC2 lớn ──► EBS volume
                              (xử lý xác minh nhập cư)
Vấn đề:
- EBS không co giãn kịp, dung lượng ngày càng đầy
- Chỉ 1 EC2 → khi surge, hệ thống down, xử lý chậm

Yêu cầu: HIGH AVAILABILITY + STORAGE CO GIÃN được
```

Đáp án đúng: **D** — S3 (có Cross-Region Replication) làm storage + SQS phân phối task + Auto Scaling group EC2 worker + CloudFormation replicate sang region khác. Anh chọn đúng D.

#### Vì sao D đúng

D giải quyết đúng cả hai vấn đề gốc:
- **Storage:** S3 gần như không giới hạn dung lượng, độ bền cao (11 số 9), CRR giúp có bản sao ở region khác → thay thế hoàn toàn EBS (vốn gắn cứng vào 1 EC2, giới hạn kích thước, không share được).
- **Compute/HA:** SQS làm hàng đợi giữa bước nhận file và bước xử lý → tách rời (decouple) request đến từ khả năng xử lý; Auto Scaling group theo độ dài queue → co giãn theo lượng task tồn đọng, không còn phụ thuộc 1 instance duy nhất.
- CloudFormation replicate kiến trúc sang region khác → hỗ trợ DR/multi-region, khớp với yêu cầu "high availability" ở mức kiến trúc rộng hơn.

#### Vì sao các phương án khác sai

- **A (EBS Provisioned IOPS + SQS + ASG):** vẫn dùng EBS làm storage chính — EBS **không co giãn/durable ngang S3**, và mỗi EC2 trong ASG phải có EBS riêng, dữ liệu không đồng bộ giữa các volume → không giải quyết được vấn đề "dữ liệu ngày càng lớn, cần scale storage".
- **B (EBS + SNS phân phối task + ASG theo số SNS notification):** hai lỗi — vẫn dùng EBS làm storage chính (sai như A), và dùng **SNS** để phân phối task cho ASG là sai mô hình; SNS là pub/sub broadcast, không giữ hàng đợi công việc để worker lấy dần như SQS.
- **C (SNS phân phối task, scale theo SQS queue length):** mâu thuẫn nội tại — nói dùng SNS phân phối task nhưng lại scale theo độ dài SQS queue (không có SQS nào được thiết lập ở đây); về bản chất SNS không phù hợp làm cơ chế phân việc cho worker pool.

| Phương án | Storage | Cơ chế phân task | Đúng mô hình? |
|---|---|---|---|
| **D (đúng)** | S3 + CRR | SQS → ASG | Có |
| A | EBS PIOPS | SQS → ASG | Storage sai |
| B | EBS PIOPS | SNS → ASG | Storage sai + phân task sai |
| C | (không nêu) | SNS, nhưng scale theo SQS | Mâu thuẫn, phân task sai |

#### Quy tắc nhớ cho thi

- **"Dữ liệu ngày càng lớn, cần storage co giãn, durable"** → **Amazon S3**, không phải EBS (dù có Provisioned IOPS).
- **"Phân phối task cho nhóm EC2 worker, Auto Scaling theo độ dài hàng đợi"** → **SQS**, không phải SNS.
- **SNS** = pub/sub broadcast (nhiều subscriber nhận cùng message); **SQS** = hàng đợi công việc (1 message được 1 worker xử lý).
- **"Cần replicate kiến trúc sang region khác"** → CloudFormation stack ở region mới, kết hợp S3 CRR cho dữ liệu.

### TD explanation

In this scenario, you need to overhaul the existing immigration service to upgrade its storage and computing capacity. Since EBS Volumes can only provide limited storage capacity and are not scalable, you should use S3 instead. The system goes down at times when there is a surge of requests which indicates that the existing large EC2 instance could not handle the requests any longer. In this case, you should implement a highly-available architecture and a queueing system with SQS and Auto Scaling.

The option that says: Upgrade your architecture to use an S3 bucket with cross-region replication (CRR) enabled, as the storage service. Set up an SQS queue to distribute the tasks to a group of EC2 instances with Auto Scaling to dynamically increase or decrease the group of EC2 instances depending on the length of the SQS queue. Use CloudFormation to replicate your architecture to another region is correct. This option provides high availability and scalable data storage with S3. Auto-scaling of EC2 instances reduces the overall processing time and SQS helps in distributing the tasks to a group of EC2 instances.
The option that says: Use EBS with Provisioned IOPS to store files, SNS to distribute tasks to a group of EC2 instances working in parallel, and Auto Scaling to dynamically size the group of EC2 instances depending on the number of SNS notifications. Use CloudFormation to replicate your architecture to another region is incorrect because EBS is not an easily scalable and durable storage solution compared to Amazon S3. Using SQS is more suitable in distributing the tasks to an Auto Scaling group of EC2 instances and not SNS.
The option that says: Use SNS to distribute the tasks to a group of EC2 instances. Use Auto Scaling to dynamically increase or decrease the group of EC2 instances depending on the length of the SQS queue is incorrect because SNS is not a valid choice in this scenario. Using SQS is more suitable in distributing the tasks to an Auto Scaling group of EC2 instances and not SNS.
The option that says: Upgrade to EBS with Provisioned IOPS as your main storage service and change your architecture to use an SQS queue to distribute the tasks to a group of EC2 instances. Use Auto Scaling to dynamically increase or decrease the group of EC2 instances depending on the length of the SQS queue is incorrect. Having a large EBS volume attached to each of the EC2 instance of the auto-scaling group is not economical. And it will be hard to sync the growing data across these EBS volumes. You should use S3 instead.

References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

---

# Group F — Serverless & app architecture (6)

<a id="q4"></a>

## Q4

A company has several IoT-enabled devices and sells it to customers around the globe. Every 5 minutes, each IoT device sends back a data file that includes the device status and other information to an Amazon S3 bucket. The company already uses AWS IoT SiteWise to monitor device health in real time, but the data files are still processed in a nightly batch. Every midnight, a Python cron job runs from an Amazon EC2 instance to read and process each data file in the S3 bucket and load the values into a designated Amazon RDS database. The cron job takes about 10 minutes to process a day’s worth of data. After each data file is processed, it is eventually deleted from the S3 bucket. The company wants to expedite the process and access the processed data on the RDS as soon as possible.
Which of the following actions should be implemented to achieve this requirement with the LEAST amount of effort?

- **A.** Convert the Python script cron job to an AWS Lambda function. Configure AWS CloudTrail to log data events of the S3 bucket. Set up an Amazon EventBridge rule to trigger the Lambda function whenever an upload event on the S3 bucket occurs.
- **B.** Increase the EC2 instance size and spawn more instances to speed up the processing of the data files. Set the Python script cron job schedule to a 1-minute interval to further improve the access time.
- **C.** Convert the Python script cron job to an AWS Lambda function. Create an Amazon EventBridge rule scheduled at 1-minute intervals and trigger the Lambda function. Create parallel Amazon CloudWatch rules that trigger the same Lambda function to further reduce the processing time.
- **D.** Convert the Python script cron job to an AWS Lambda function. Configure the S3 bucket event notifications to trigger the Lambda function whenever an object is uploaded to the bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** cron script per day; process ASAP; least effort

⚠️ **Watch:** SQS + EC2 poller = more effort

🧠 **Rule:** Process on upload → S3 event notification → Lambda.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
IoT device ──(mỗi 5 phút)──► S3 bucket ──(hiện tại: cron EC2 chạy MỖI ĐÊM)──► RDS
                                                     │
                                     Muốn: xử lý ASAP, ít công sức nhất
```

Yêu cầu: chuyển từ xử lý batch ban đêm sang xử lý **gần real-time**, với **ít effort nhất**. Anh chọn đúng **D**: chuyển cron script thành Lambda + **S3 event notification** trigger trực tiếp khi có object mới.

#### Vì sao D đúng

S3 event notification là cơ chế **built-in của S3**, không cần thêm dịch vụ trung gian:

```
Object upload vào S3 bucket
        │
        ▼ (S3 tự phát event, thường trong vài giây)
   Lambda function được trigger
        │
        ▼
   Xử lý + ghi vào RDS ngay
```

Đây là cách **ít bước cấu hình nhất** để đạt "xử lý ngay khi file được tạo" — không cần polling, không cần dịch vụ log riêng.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì dùng **CloudTrail data events + EventBridge** để bắt sự kiện upload — về logic vẫn trigger được Lambda, nhưng đây là cách **nhiều bước hơn hẳn** so với dùng trực tiếp S3 event notification (phải bật CloudTrail data events, tạo rule EventBridge...) — không tối ưu "least effort".
- **B sai** vì tăng size/số EC2 instance và giảm interval cron xuống 1 phút — cron **tối thiểu chỉ chạy được mỗi 1 phút**, và nhiều instance có thể **xử lý trùng cùng 1 file** (race condition), không đáng tin cậy.
- **C sai** vì EventBridge **scheduled rule tối thiểu cũng chỉ 1-phút interval** (không thể nhanh hơn), và thêm CloudWatch rule song song để "giảm thời gian xử lý" là **giải pháp phức tạp, tốn effort**, không giải quyết được gốc vấn đề (vẫn là polling theo lịch, không phải theo event).

#### So sánh nhanh

| Đáp án | Cơ chế trigger | Độ trễ | Effort cấu hình |
|---|---|---|---|
| **D (đúng)** | S3 event notification → Lambda | Vài giây | Thấp nhất |
| A | CloudTrail data events + EventBridge → Lambda | Vài giây~phút | Nhiều bước hơn |
| B | Cron 1 phút trên nhiều EC2 | ≥1 phút, dễ trùng | Tốn kém, kém tin cậy |
| C | EventBridge scheduled 1 phút + CloudWatch song song | ≥1 phút | Phức tạp |

#### Quy tắc nhớ cho thi

- **"Xử lý ngay khi file lên S3, ít effort nhất"** → **S3 event notification → Lambda trực tiếp**, không cần CloudTrail/EventBridge trung gian
- **"Scheduled rule / cron interval nhỏ nhất"** → nhớ **EventBridge scheduled rule tối thiểu là 1 phút** — nếu đề cần nhanh hơn, đáp án đó tự động sai
- **CloudTrail data events + EventBridge** chỉ nên chọn khi đề **yêu cầu rõ** phải audit qua CloudTrail hoặc cần log API call chi tiết, không phải khi chỉ cần trigger đơn giản

### TD explanation

The Amazon S3 notification feature enables you to receive notifications when certain events happen in your bucket. To enable notifications, you must first add a notification configuration that identifies the events you want Amazon S3 to publish and the destinations where you want Amazon S3 to send the notifications. You store this configuration in the notification subresource that is associated with a bucket. Amazon S3 event notifications are designed to be delivered at least once. Typically, event notifications are delivered in seconds but can sometimes take a minute or longer.

Currently, Amazon S3 can publish notifications for the following events:
New object created events — Amazon S3 supports multiple APIs to create objects. You can request a notification when only a specific API is used (for example, s3:ObjectCreated:Put), or you can use a wildcard (for example, s3:ObjectCreated:*) to request a notification when an object is created regardless of the API used.
Object removal events — Amazon S3 supports deletes of versioned and unversioned objects. For information about object versioning, see Object Versioning and Using versioning.
Restore object events — Amazon S3 supports the restoration of objects archived to the S3 Glacier storage classes. Your request to be notified of object restoration completion by using s3:ObjectRestore:Completed. You use s3:ObjectRestore:Post to request notification of the initiation of a restore.
Reduced Redundancy Storage (RRS) object lost events — Amazon S3 sends a notification message when it detects that an object of the RRS storage class has been lost.
Replication events — Amazon S3 sends event notifications for replication configurations that have S3 Replication Time Control (S3 RTC) enabled. It sends these notifications when an object fails replication, when an object exceeds the 15-minute threshold, when an object is replicated after the 15-minute threshold, and when an object is no longer tracked by replication metrics. It publishes a second event when that object replicates to the destination Region.
Enabling notifications is a bucket-level operation; that is, you store notification configuration information in the notification subresource associated with a bucket. After creating or changing the bucket notification configuration, typically you need to wait 5 minutes for the changes to take effect. Amazon S3 supports the following destinations where it can publish events: Amazon Simple Notification Service (Amazon SNS) topic, Amazon Simple Queue Service (Amazon SQS) queue, and AWS Lambda.
Hence, the correct answer is: Convert the Python script cron job to an AWS Lambda function. Configure the S3 bucket event notifications to trigger the Lambda function whenever an object is uploaded to the bucket because this provides the best processing and access time. Each of the data files will be processed almost immediately once uploaded to the S3 bucket.
The option that says: Increase the EC2 instance size and spawn more instances to speed up the processing of the data files. Set the Python script cron job schedule to a 1-minute interval to further improve the access time is incorrect. This solution is unreliable since the Amazon EC2 instances can process the same data file at the same time, and because of the limitations of cron, the minimum interval for processing is only 1 minute.
The option that says: Convert the Python script cron job to an AWS Lambda function. Configure AWS CloudTrail to log data events of the S3 bucket. Set up an Amazon EventBridge rule to trigger the Lambda function whenever an upload event on the S3 bucket occurs is incorrect. Although this is possible, you do not have to use CloudTrail and Amazon EventBridge to satisfy the given requirement. This solution entails a lot of steps. You can simply use the Amazon S3 event notification feature that can trigger the Lambda function directly.
The option that says: Convert the Python script cron job to an AWS Lambda function. Create an Amazon EventBridge rule scheduled at 1-minute intervals and trigger the Lambda function. Create parallel Amazon CloudWatch rules that trigger the same Lambda function to further reduce the processing time is incorrect. The scheduled Amazon EventBridge rule can only have a minimum of 1-minute intervals. Using Amazon S3 Event notifications as triggers will result in near-real-time processing of the data files.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html
https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html#with-s3-example-configure-event-source
https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q11"></a>

## Q11

A company develops new android and iOS mobile apps. The company is considering storing user customization data in AWS. This would provide a more uniform cross-platform experience to their users using multiple mobile devices to access their apps. The preference data for each user is estimated to be 4 KB in size. Additionally, 3 million customers are expected to use the application on a regular basis, using their social login accounts for easier user authentication. 
How should the Solutions Architect design a highly available, cost-effective, scalable, and secure solution to meet the above requirements?

- **A.** Create an RDS MySQL instance with multiple read replicas in 2 availability zones to store the user preference data. The mobile application will then query the user preferences from the read replicas. Finally, utilize MySQL's user management and access privilege system to handle the security and access credentials of the users.
- **B.** Provision a table in DynamoDB containing an item for each user having the necessary attributes to hold the user preferences. The mobile app will query the user preferences directly from the table. Use STS, Web Identity Federation, and DynamoDB's Fine-Grained Access Control for authentication and authorization.
- **C.** Have the user preference data stored in S3, and set up a DynamoDB table with an item for each user and an item attribute referencing the user's S3 object. The mobile app will retrieve the S3 URL from DynamoDB and then access the S3 object directly utilizing STS, Web identity Federation, and S3 Access Points.
- **D.** Launch an RDS MySQL instance in 2 availability zones to contain the user preference data. Deploy a public-facing application on a server in front of the database which will manage authentication and access controls.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** 4 KB prefs; 3M users; social login; HA + cheap

⚠️ **Watch:** Same concept you missed in Q65/Q21 — web identity federation

🧠 **Rule:** Per-user data + social login → DynamoDB + web identity federation (STS) + fine-grained IAM.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Mobile app (Android/iOS) ── social login (Facebook/Google/...) ──► ?
        │
   3 triệu users, mỗi user ~4KB preference data
        │
   Yêu cầu: HA + cost-effective + scalable + secure
```

Điểm mấu chốt là **social login** — đây là tín hiệu trực tiếp cho **Web Identity Federation**. Anh chọn đúng **B**: DynamoDB table (mỗi user 1 item) + **STS + Web Identity Federation + DynamoDB Fine-Grained Access Control**.

#### Vì sao B đúng

- **DynamoDB**: dữ liệu 4KB/user, đơn giản dạng key-value, không có quan hệ phức tạp → phù hợp NoSQL, scale tự động theo triệu user, trả tiền theo dùng — đúng "scalable + cost-effective" hơn RDS.
- **Web Identity Federation + STS**: khi user đăng nhập bằng social login (Facebook/Google/OIDC), app không cần tự quản lý user identity — nhận token từ IdP rồi đổi qua STS để lấy **temporary security credentials** ánh xạ vào một IAM role.
- **DynamoDB Fine-Grained Access Control**: dùng policy variables (`${www.amazon.com:user_id}` hoặc tương đương) để mỗi user chỉ đọc/viết được **đúng item của chính họ** trong table chung — đảm bảo "secure" ở mức item, không cần backend server riêng để enforce.

#### Vì sao từng đáp án sai bị loại

- **C sai** vì lưu data ở **S3 + DynamoDB tham chiếu URL** — cách này khuyến nghị dùng khi dữ liệu **lớn** cần tách metadata (DynamoDB) và nội dung (S3); ở đây mỗi user chỉ 4KB, quá nhỏ để cần tách, chỉ làm phức tạp thêm. Ngoài ra phương án này **không dùng DynamoDB Fine-Grained Access Control**, và S3 Access Points không cần thiết trong ngữ cảnh này.
- **A sai** vì RDS MySQL (dù có nhiều read replica) **kém scalable và cost-effective hơn DynamoDB** ở quy mô 3 triệu user. Ngoài ra dùng "MySQL's user management" để authen/author user cuối là sai mô hình — MySQL user management là để quản lý user truy cập database, không phải để authen end-user của app.
- **D sai** cùng lý do RDS kém scalable/cost-effective hơn DynamoDB ở quy mô này; thêm nữa phải tự dựng **application server riêng để quản lý auth/access**, tốn thêm effort vận hành so với dùng STS + Fine-Grained Access Control có sẵn.

⚠️ Cùng chủ đề đã sai ở **Q65/Q21** (web identity federation) — điểm chung cần nhớ: hễ thấy **"social login"** (Facebook, Google, Amazon, OIDC) trong đề, nghĩ ngay đến **Web Identity Federation + STS**, không phải Cognito User Pools (khi chưa nêu rõ) và không phải tự viết auth server.

#### So sánh nhanh

| Đáp án | Database | Auth mechanism | Phù hợp 4KB/user, 3M users? |
|---|---|---|---|
| **B (đúng)** | DynamoDB | STS + Web Identity Federation + Fine-Grained Access | ✅ |
| C | S3 + DynamoDB (metadata) | STS + Web Identity Federation + S3 Access Points | Thừa phức tạp cho data nhỏ |
| A | RDS MySQL + read replica | MySQL user management | Kém scale/cost |
| D | RDS MySQL | App server tự viết | Kém scale/cost, tốn effort |

#### Quy tắc nhớ cho thi

- **"Social login" (Facebook/Google/Amazon/OIDC)** → **Web Identity Federation + STS**
- **Dữ liệu nhỏ, mỗi user 1 item, cần scale tới triệu user, rẻ** → **DynamoDB**, không phải RDS
- **Muốn mỗi user chỉ truy cập đúng item của mình trong 1 table chung** → **DynamoDB Fine-Grained Access Control**
- **S3 + DynamoDB kết hợp** chỉ hợp lý khi dữ liệu **lớn** (ảnh, file...), không hợp lý cho data vài KB

### TD explanation

Take note that the question mentioned the use of social media logins. With web identity federation, you don’t need to create custom sign-in code or manage your own user identities. Instead, users of your app can sign in using a well-known identity provider (IdP) —such as Login with Amazon, Facebook, Google, or any other OpenID Connect (OIDC)-compatible IdP, receive an authentication token, and then exchange that token for temporary security credentials in AWS that map to an IAM role with permissions to use the resources in your AWS account. Using an IdP helps you keep your AWS account secure, because you don’t have to embed and distribute long-term security credentials with your application.

The option that says: Provision a table in DynamoDB containing an item for each user having the necessary attributes to hold the user preferences. The mobile app will query the user preferences directly from the table. Use STS, Web Identity Federation, and DynamoDB’s Fine Grained Access Control for authentication and authorization is correct because it uses DynamoDB for scalability and cost-efficiency. It uses federated access using Web Identity Provider, and uses fine-grained access privileges for authenticating the access.
The option that says: Have the user preference data stored in S3, and set up a DynamoDB table with an item for each user and an item attribute referencing the user’s S3 object. The mobile app will retrieve the S3 URL from DynamoDB and then access the S3 object directly utilizing STS, Web identity Federation, and S3 Access Points is incorrect because it doesn’t use DynamoDB’s built-in Fine-Grained Access Control for authentication and authorization feature. Additionally, using Amazon S3 bucket with DynamoDB is recommended for storing large data with the metadata stored on DynamoDB. The user preference data is only 4KB in size which can be stored effectively in a DynamoDB table. The use of S3 Access points is not necessary because these are just unique hostnames that enforce distinct permissions and network controls for any request made through the access point.
The option that says: Launch an RDS MySQL instance in 2 availability zones to contain the user preference data. Deploy a public-facing application on a server in front of the database which will manage authentication and access controls is incorrect because RDS MySQL is not as scalable and cost-effective as DynamoDB.
The option that says: Create an RDS MySQL instance with multiple read replicas in 2 availability zones to store the user preference data. The mobile application will then query the user preferences from the read replicas. Finally, utilize MySQL’s user management and access privilege system to handle the security and access credentials of the users is incorrect because RDS MySQL is not as scalable and cost-effective as DynamoDB. Additionally, the user management and access privilege system for RDS cannot be used for controlling access.
References:
https://aws.amazon.com/dynamodb/developer-resources
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-use-s3-too.html
https://developer.amazon.com/blogs/appstore/post/TxZR5F5K6QINFQ/storing-user-preference-in-amazon-dynamodb-using-the-aws-sdk-for-android

Check out this Amazon DynamoDB Cheat Sheet:
https://tutorialsdojo.com/amazon-dynamodb/

</details>

<a id="q30"></a>

## Q30

A print media company has a popular web application hosted on an on-premises network that allows anyone around the globe to search its back catalog and retrieve individual newspaper pages. The company scanned the old newspapers into PNG image format and used Optical Character Recognition (OCR) software to automatically convert images to a text file. The license of the OCR software will expire soon, and the news organization decided to move to AWS and produce a scalable, durable, and highly available architecture. 




Which is the best option to achieve this requirement?

- **A.** Create a new Amazon S3 bucket to store and serve the scanned image files using an Amazon CloudFront web distribution. Launch a new AWS Elastic Beanstalk environment to host the website across multiple Availability Zones and set up an Amazon OpenSearch Service for query processing, which the website can use. Use Amazon Textract to detect and recognize text from scanned old newspapers.
- **B.** Create a new AWS CloudFormation template which has EBS-backed Amazon EC2 instances with an Application Load Balancer in front. Install and run an NGINX web server and an open source search application. Store the images to Amazon EBS volumes with Amazon Data Lifecycle Manager configured, and which automatically attach new volumes to the EC2 instances as required.
- **C.** Store the images in an Amazon S3 bucket and prepare a separate bucket to host the static website. Utilize Amazon Kendra to intelligently search and select the images stored in S3. Set up a lifecycle policy to move the selected images to Glacier after 3 months, and if needed, use Amazon Athena to query the archives.
- **D.** Use Amazon S3 Intelligent-Tiering storage class to store and serve the scanned files. Migrate the on-premises web application as well as the Optical Character Recognition (OCR) software to an Auto Scaling group of Spot Amazon EC2 Instances across multiple Availability Zones with an Application Load Balancer to balance the incoming load. Use Amazon Rekognition to detect and recognize text from the scanned old newspapers.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** OCR license expiring; scalable, durable, HA

⚠️ **Watch:** EC2 OCR software = keep license problem

🧠 **Rule:** Images → S3 + CloudFront; OCR → Textract; web → Elastic Beanstalk multi-AZ.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises: PNG scan cũ + OCR software (license sắp hết)
        │
        ▼  di chuyển lên AWS
S3 (ảnh + web tĩnh) ──CloudFront──► user toàn cầu
        │
        ▼
Elastic Beanstalk (web multi-AZ) ──► OpenSearch Service (query)
        │
        ▼
Textract (OCR thay license cũ)
Yêu cầu: scalable, durable, highly available — không phụ thuộc OCR license cũ
```

Anh chọn đúng **A — S3 + CloudFront lưu/serve ảnh, Elastic Beanstalk multi-AZ host web, OpenSearch Service cho tìm kiếm, Textract thay OCR cũ**.

#### Vì sao A đúng

Bài yêu cầu thay license OCR sắp hết bằng dịch vụ AWS, đồng thời đảm bảo scalable/durable/HA — mỗi thành phần trong A khớp đúng một tiêu chí:

- **S3 + CloudFront** cho ảnh: S3 có độ bền (durability) rất cao và scale tự động, CloudFront phân phối toàn cầu nhanh — đúng nghĩa "durable, scalable" thay cho việc tự quản lý storage.
- **Elastic Beanstalk multi-AZ**: host website với **nhiều Availability Zone** → high availability.
- **OpenSearch Service**: xử lý query tìm kiếm bài báo cũ — dịch vụ search managed, tự scale theo dữ liệu/traffic.
- **Textract**: thay thế trực tiếp phần mềm OCR sắp hết license — Textract không chỉ OCR đơn giản mà còn hiểu form/table, đúng nhu cầu "chuyển ảnh scan thành text".

#### Vì sao các đáp án sai (distractor cần nhớ)

- **B (CloudFormation + EBS-backed EC2 + NGINX + open source search):** Lưu ảnh trên **EBS volume** không durable/scalable như S3 — EBS gắn với một AZ, phải tự quản lý Data Lifecycle Manager để gắn thêm volume, tốn công vận hành hơn nhiều so với S3 fully-managed.
- **C (S3 + Kendra + Glacier + Athena):** **Kendra không làm OCR** — Kendra là dịch vụ tìm kiếm ngữ nghĩa trên text đã có sẵn, không tự đọc được ảnh PNG (cần OCR trước). Thêm nữa, lifecycle chuyển ảnh vào Glacier dựa trên tuổi/tag, không thể "chỉ chuyển các ảnh được Kendra chọn" — sai logic lifecycle. Glacier còn gây delay khi cần phục vụ công khai ngay.
- **D (S3 Intelligent-Tiering + giữ nguyên OCR software cũ + Rekognition):** Vẫn giữ **OCR software cũ sắp hết license** — không giải quyết đúng vấn đề gốc của bài. Rekognition chủ yếu dùng cho nhận diện ảnh/video (object, face...), không phải công cụ OCR chuyên dụng như Textract cho việc trích xuất text từ scan cũ.

#### So sánh nhanh

| Đáp án | Thay OCR cũ? | Lưu ảnh | Search |
|---|---|---|---|
| **A. Textract + S3 + OpenSearch (đúng)** | Có (Textract) | S3 (durable) | OpenSearch |
| B. EBS + open-source search | Có nhưng thủ công | EBS (kém durable, tốn công) | tự cài |
| C. Kendra + Glacier | Không (Kendra không OCR ảnh) | S3 + Glacier (delay) | Kendra |
| D. Rekognition + license cũ | Không (vẫn giữ OCR cũ) | S3 Intelligent-Tiering | — |

#### Quy tắc nhớ cho thi

- **"OCR/trích xuất text từ ảnh scan, form, table"** → **Amazon Textract**, không phải Rekognition (nhận diện ảnh) hay Kendra (search trên text có sẵn).
- **"Lưu file scan/ảnh scalable + durable"** → **S3**, tránh EBS cho use case này.
- **"Tìm kiếm nội dung/documents"** → **Amazon OpenSearch Service** hoặc Kendra, nhưng Kendra cần text đã có sẵn (không tự OCR).
- Thấy "license sắp hết, cần giải pháp managed thay thế" → loại ngay đáp án nào vẫn giữ nguyên software cũ.

### TD explanation

Amazon OpenSearch Service simplifies the deployment, operation, and scaling of OpenSearch, a widely used open-source search and analytics engine. It provides robust security features, ensures high availability and data durability, and offers direct access to the OpenSearch API.
With Amazon OpenSearch Service, you can quickly add rich search capabilities to your website or application. You don’t need to become a search expert or worry about hardware provisioning, setup, and maintenance. With a few clicks in the AWS Management Console, you can create a search domain and upload the data that you want to make searchable, and Amazon OpenSearch Service will automatically provision the required resources and deploy a highly-tuned search index.
You can easily change your search parameters, fine-tune search relevance, and apply new settings at any time. As your volume of data and traffic fluctuates, Amazon OpenSearch Service seamlessly scales to meet your needs.
Amazon Textract is a machine learning (ML) service that automatically extracts text, handwriting, and data from scanned documents. It goes beyond simple optical character recognition (OCR) to identify, understand, and extract data from forms and tables.
Amazon Textract makes it easy to add document text detection and analysis to your applications. Using Amazon Textract, customers can:
– Detect typed and handwritten text in a variety of documents, including financial reports, medical records, and tax forms.
– Extract text, forms, and tables from documents with structured data, using the Amazon Textract Document Analysis API.
– Specify and extract information from documents using the Queries feature within the Amazon Textract Analyze Document API.
– Process invoices and receipts with the AnalyzeExpense API.
– Process ID documents such as driver’s licenses and passports issued by the U.S. government using the AnalyzeID API.

Hence, the correct answer is: Create a new Amazon S3 bucket to store and serve the scanned image files using an Amazon CloudFront web distribution. Launch a new AWS Elastic Beanstalk environment to host the website across multiple Availability Zones and set up an Amazon OpenSearch Service for query processing, which the website can use. Use Amazon Textract to detect and recognize text from scanned old newspapers. It satisfies the requirement given in the scenario, i.e., it uses S3 to store the images instead of the commercial product, which will be decommissioned soon. More importantly, it uses Amazon OpenSearch Service for query processing, and in addition, it uses a Multi-AZ implementation, which provides high availability. It is also correct to use Amazon Textract to detect and recognize text from scanned old newspapers.
The option that says: Create a new AWS CloudFormation template which has EBS-backed Amazon EC2 instances with an Application Load Balancer in front. Install and run an NGINX web server and an open source search application. Store the images to Amazon EBS volumes with Amazon Data Lifecycle Manager configured, and which automatically attach new volumes to the EC2 instances as required is incorrect. An EBS volume is not a scalable nor a durable solution compared with S3. In addition, it is not as cost-effective compared to S3 since it typically entails maintenance overhead, unlike the fully managed storage service provided by S3.
The option that says: Store the images in an Amazon S3 bucket and prepare a separate bucket to host the static website. Utilize Amazon Kendra to intelligently search and select the images stored in S3. Set up a lifecycle policy to move the selected images to Glacier after 3 months, and if needed, use Amazon Athena to query the archives is incorrect. Amazon Kendra cannot search PNG images because it does not perform OCR and requires pre‑extracted text. Lifecycle policies cannot move only the images selected by a Kendra query as they operate on object age or tags, not on search results. Amazon Athena cannot query PNG images as it only works on structured data like CSV or JSON. Storing images in Glacier introduces retrieval delays that are unacceptable for a public newspaper archive
The option that says: Use Amazon S3 Intelligent-Tiering storage class to store and serve the scanned files. Migrate the on-premises web application as well as the Optical Character Recognition (OCR) software to an Auto Scaling group of Spot Amazon EC2 Instances across multiple Availability Zones with an Application Load Balancer to balance the incoming load. Use Amazon Rekognition to detect and recognize text from the scanned old newspapers is incorrect. Even though it properly uses S3 for durable and scalable storage, it still uses the Optical Character Recognition (OCR) software, which will be decommissioned soon. It is better to use Amazon OpenSearch Service instead.

References:
https://docs.aws.amazon.com/opensearch-service/
https://docs.aws.amazon.com/textract/latest/dg/what-is.html
https://docs.aws.amazon.com/textract/latest/dg/how-it-works-documents.html

Check out these Amazon OpenSearch Service and Amazon Textract Cheat Sheets:
https://tutorialsdojo.com/amazon-opensearch-service/
https://tutorialsdojo.com/amazon-textract/

</details>

<a id="q43"></a>

## Q43

A startup develops Internet-Of-Things (IoT) devices that provide health monitoring for dogs and cats which is integrated into their collars. The startup has an engineering team to build a smart pet collar that collects biometric information of the pet every second and then sends it to a web portal through a POST API request. The Solutions Architect has been tasked to set up the API services and the web portal that will accept and process the biometric data as well as provide complete trends and health reports to pet owners around the globe. The portal should be highly durable, available, and scalable with an additional feature for showing real-time biometric data analytics and monitoring. 
Which of the following is the best architecture that the Solutions Architect should implement to meet the above requirement?

- **A.** 1. Create an Amazon SQS queue to collect the incoming biometric data. 2. Analyze the data from SQS with Amazon Kinesis. 3. Store the results to an Amazon RDS for MySQL database.
- **B.** 1. Launch an Amazon Elastic MapReduce instance to collect the incoming biometrics data. 2. Use Amazon Kinesis to analyze the data. 3. Save the results to an Amazon DynamoDB table.
- **C.** 1. Use Amazon Kinesis Data Streams to collect the incoming biometric data. 2. Analyze the data using Amazon Kinesis and show the results in a real-time dashboard. 3. Set up a simple data aggregation process and pass the results to Amazon S3. 4. Store the data to Amazon Redshift, configured with automated backups, to handle complex analytics.
- **D.** 1. Create an Amazon S3 bucket to collect the incoming biometric data from the smart pet collar. 2.  Use Amazon Data Pipeline to run a data analysis task in the S3 bucket every day. 3.  Use Amazon Redshift as the online analytic processing (OLAP) database for the web portal.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** real-time biometric analytics

⚠️ **Watch:** SQS/Firehose aren't real-time analytics

🧠 **Rule:** Real-time streams → Kinesis Data Streams + real-time analytics dashboard.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Vòng cổ IoT (chó/mèo) ──mỗi giây──► POST API biometric data
                                        │
                              cần: durable + available + scalable
                              + REAL-TIME analytics/dashboard
                                        │
                              lưu trữ lâu dài để phân tích phức tạp
```

Đáp án đúng: **C** — Kinesis Data Streams thu thập → Kinesis phân tích + dashboard real-time → aggregate rồi đẩy vào S3 → Redshift (có automated backup) cho complex analytics. Anh chọn đúng C.

#### Vì sao C đúng

Từ khóa quyết định là **"real-time biometric data analytics and monitoring"**. Kinesis Data Streams sinh ra chính cho use-case này: thu nhận luồng dữ liệu liên tục tốc độ cao (per-second từ hàng loạt vòng cổ), rồi Kinesis Applications (KCL) xử lý ngay để đổ vào **real-time dashboard**. Sau khi có kết quả real-time, mới tổng hợp và đẩy dữ liệu xuống S3, rồi từ đó vào Redshift để phục vụ các báo cáo/phân tích phức tạp hơn (trend theo thời gian dài) — đúng kiến trúc streaming ingestion → real-time layer → batch/OLAP layer.

#### Vì sao các phương án khác sai

- **A (SQS → Kinesis → RDS MySQL):** SQS **không phù hợp nhận luồng liên tục tốc độ cao** kiểu này — SQS là hàng đợi message rời rạc cho worker xử lý, không có khái niệm "real-time dashboard" hay ordered stream. RDS MySQL cũng không phải lựa chọn cho phân tích lớn.
- **B (EMR nhận data → Kinesis phân tích → DynamoDB):** sai ngay bước đầu — **EMR không dùng để "collect" luồng dữ liệu đến**, EMR là cluster xử lý big data theo batch/Spark job trên dữ liệu đã có sẵn, không phải điểm nhận request trực tiếp từ thiết bị.
- **D (S3 nhận data → Data Pipeline chạy phân tích mỗi ngày → Redshift OLAP):** đây là mô hình **batch hàng ngày**, hoàn toàn không đáp ứng yêu cầu "real-time" — dữ liệu chỉ được phân tích 1 lần/ngày, không có real-time dashboard.

| Phương án | Điểm nhận data | Có real-time analytics? |
|---|---|---|
| **C (đúng)** | Kinesis Data Streams | Có (Kinesis + dashboard) |
| A | SQS | Không (SQS không stream) |
| B | EMR (sai vai trò) | Không (EMR không nhận trực tiếp) |
| D | S3, batch/ngày | Không (chỉ 1 lần/ngày) |

#### Lưu ý thực tế

📝 Ghi chú kỹ thuật: trong thực tế thường dùng thêm **Kinesis Data Firehose** để tự động đẩy dữ liệu đã tổng hợp từ Kinesis Data Streams vào S3 (thay vì code tay), nhưng TD explanation không nhắc Firehose — vẫn giữ nguyên đáp án C theo đúng nội dung đề đưa ra.

#### Quy tắc nhớ cho thi

- **"Real-time analytics/dashboard trên luồng dữ liệu liên tục"** → **Kinesis Data Streams**.
- **SQS** = hàng đợi việc rời rạc, không phải kênh nhận luồng streaming liên tục.
- **EMR** = cluster xử lý dữ liệu đã có, không phải điểm ingest trực tiếp từ thiết bị.
- **"Complex analytics dài hạn"** → S3 (data lake) rồi Redshift (OLAP), tách riêng khỏi lớp real-time.

### TD explanation

Amazon Kinesis Data Streams enable you to build custom applications that process or analyze streaming data for specialized needs. Kinesis Data Streams can continuously capture and store terabytes of data per hour from hundreds of thousands of sources such as website clickstreams, financial transactions, social media feeds, IT logs, and location-tracking events. With the Kinesis Client Library (KCL), you can build Kinesis Applications and use streaming data to power real-time dashboards, generate alerts, implement dynamic pricing and advertising, and more. You can also emit data from Kinesis Data Streams to other AWS services such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon EMR, and AWS Lambda.

Kinesis Data Streams can be used to collect log and event data from sources such as servers, desktops, and mobile devices. You can then build Kinesis Applications to continuously process the data, generate metrics, power live dashboards, and emit aggregated data into stores such as Amazon S3.
You can have your Kinesis Applications run real-time analytics on high frequency event data such as sensor data collected by Kinesis Data Streams, which enables you to gain insights from your data at a frequency of minutes instead of hours or days.
Hence, the following option is the correct answer as Amazon Kinesis is the one used here to collect the streaming data:
1. Use Amazon Kinesis Data Streams to collect the incoming biometric data.
2. Analyze the data using Amazon Kinesis and show the results in a real-time dashboard.
3. Set up a simple data aggregation process and pass the results to Amazon S3.
4. Store the data to Amazon Redshift, configured with automated backups, to handle complex analytics.
The following option is incorrect because S3, Data Pipeline, and Redshift do not provide real-time data analytics:
1. Create an Amazon S3 bucket to collect the incoming biometric data from the smart pet collar.
2. Use Amazon Data Pipeline to run a data analysis task in the S3 bucket every day.
3. Use Amazon Redshift as the online analytic processing (OLAP) database for the web portal.
The following option is incorrect because an SQS queue is not appropriate to use to accept all of the incoming biometric data. You should use Amazon Kinesis instead:
1. Create an Amazon SQS queue to collect the incoming biometric data.
2. Analyze the data from SQS with Amazon Kinesis.
3. Store the results to an Amazon RDS for MySQL database.
The following option is incorrect because just like in the above, it does not use Amazon Kinesis to accept the incoming data:
1. Launch an Amazon Elastic MapReduce instance to collect the incoming biometrics data.
2. Use Amazon Kinesis to analyze the data.
3. Save the results to an Amazon DynamoDB table.

References:
https://aws.amazon.com/kinesis/data-streams/details/
https://docs.aws.amazon.com/streams/latest/dev/introduction.html

Check out this Amazon Kinesis Cheat Sheet:
https://tutorialsdojo.com/amazon-kinesis/

</details>

<a id="q44"></a>

## Q44

A tech company will soon launch a new smartwatch that will collect statistics and usage information from its users. The solutions architect was tasked to design a data storage and retrieval solution for the receiving application. The application is expected to ingest millions of records per minute from its worldwide user base. For the storage requirements:


Each record is less than 4KB in size.




Data must be stored durably.




Data must be stored for 120 days only, then it can be deleted.




Data must have low latency retrieval time.


For running the application for a year, the estimated storage requirement is around 10-15 TB.
Which of the following options is the recommended storage solution while being the most cost-effective?

- **A.** Configure the application to ingest the records and store each record on a dedicated Amazon S3 bucket. Ensure that a unique filename is set for each object. Create an S3 bucket lifecycle policy to expire objects that are older than 120 days.
- **B.** Configure the application to receive the records and store the records to Amazon Aurora Serverless. Write an AWS Lambda function that runs a query to delete records older than 120 days. Schedule the function to run every night.
- **C.** Use Amazon Managed Streaming for Apache Kafka (MSK) to ingest and store the records. Set a custom data retention period of 120 days for the Kafka topic. Send the streamed data to an Amazon S3 bucket for added durability.
- **D.** Configure the application to receive the records and set the storage to a DynamoDB table. Configure proper scaling on the DynamoDB table and enable the DynamoDB table Time to Live (TTL) setting to delete records after 120 days.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** keep 120 days then delete; low latency; 10–15 TB

⚠️ **Watch:** S3 lifecycle has higher-latency retrieval for record lookups

🧠 **Rule:** Auto-expiring low-latency records → DynamoDB + TTL.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Smartwatch ──millions records/phút──► storage
Mỗi record < 4KB | phải durable | giữ 120 ngày rồi xóa
Yêu cầu: LOW LATENCY retrieval | ~10-15 TB/năm | cost-effective
```

Đáp án đúng: **D** — DynamoDB table + TTL để tự xóa record sau 120 ngày. Anh chọn đúng D.

#### Vì sao D đúng

Hai từ khóa quyết định: **"low latency retrieval"** và **"tự xóa sau 120 ngày"**. DynamoDB là NoSQL key-value/document, độ trễ đọc/viết tính bằng milliseconds — khớp "low latency". TTL (Time to Live) cho phép gắn timestamp hết hạn trên từng item; DynamoDB tự quét và xóa item hết hạn ở background **không tốn write throughput** → tự động, cost-effective, không cần Lambda/cron riêng để dọn dữ liệu cũ. Kết hợp on-demand hoặc auto scaling cho throughput phù hợp với "millions of records per minute".

#### Vì sao các phương án khác sai

- **A (S3 + lifecycle policy expire 120 ngày):** lifecycle policy xóa object đúng sau 120 ngày, nhưng S3 **không tối ưu cho truy vấn record đơn lẻ với latency thấp** kiểu key-value tra cứu nhanh — mỗi record là 1 object riêng, việc list/lookup không nhanh như DynamoDB.
- **B (Aurora Serverless + Lambda cron xóa mỗi đêm):** Aurora Serverless chỉ tiết kiệm chi phí khi có **khoảng nghỉ (idle)** để scale-to-0/thấp; ở đây dữ liệu đổ vào liên tục 24/7 nên DB luôn phải chạy ở mức cao → mất lợi ích cost-saving của serverless. Việc xóa bằng Lambda cron mỗi đêm cũng tốn thêm query/compute, kém hơn TTL tự động của DynamoDB.
- **C (MSK ingest/lưu, retention 120 ngày, đẩy sang S3):** Kafka/MSK tối ưu cho streaming pipeline, không phải nơi lưu trữ chính có **truy vấn tra cứu low-latency lâu dài**; thêm bước gửi ra S3 để "durability" chỉ làm tăng chi phí và độ phức tạp không cần thiết so với yêu cầu đề ra.

| Phương án | Tự xóa sau 120 ngày | Low-latency lookup | Cost-effective ở tải liên tục |
|---|---|---|---|
| **D. DynamoDB + TTL** | Có, miễn phí | Có | Có |
| A. S3 lifecycle | Có | Không (object lookup) | Có (nhưng sai latency) |
| B. Aurora Serverless | Cần cron riêng | Có | Không (DB luôn chạy) |
| C. MSK + S3 | Có (retention) | Không tối ưu | Kém hơn |

#### Quy tắc nhớ cho thi

- **"Tự xóa dữ liệu sau N ngày, không tốn write throughput"** → **DynamoDB TTL**.
- **"Low latency lookup theo key, khối lượng lớn record nhỏ"** → DynamoDB, không phải S3.
- **Aurora Serverless tiết kiệm chi phí** chỉ khi có khoảng thời gian idle để scale down — tải liên tục 24/7 thì mất lợi thế đó.
- **MSK/Kafka** = streaming pipeline, không phải nơi lưu trữ chính cho truy vấn nhanh dài hạn.

### TD explanation

Amazon DynamoDB Time to Live (TTL) allows you to define a per-item timestamp to determine when an item is no longer needed. Shortly after the date and time of the specified timestamp, DynamoDB deletes the item from your table without consuming any write throughput. TTL is provided at no extra cost as a means to reduce stored data volumes by retaining only the items that remain current for your workload’s needs.
TTL is useful if you store items that lose relevance after a specific time. The following are example TTL use cases:
-Remove user or sensor data after one year of inactivity in an application.
-Archive expired items to an Amazon S3 data lake via Amazon DynamoDB Streams and AWS Lambda.
-Retain sensitive data for a certain amount of time according to contractual or regulatory obligations.
When enabling TTL on a DynamoDB table, you must identify a specific attribute name that the service will look for when determining if an item is eligible for expiration. After you enable TTL on a table, a per-partition scanner background process automatically and continuously evaluates the expiry status of items in the table.
The scanner background process compares the current time, in Unix epoch time format in seconds, to the value stored in the user-defined attribute of an item. If the attribute is a Number data type, the attribute’s value is a timestamp in Unix epoch time format in seconds, and the timestamp value is older than the current time but not five years older or more (in order to avoid a possible accidental deletion due to a malformed TTL value), then the item is set to expire.

Therefore, the correct answer is: Configure the application to receive the records and set the storage to a DynamoDB table. Configure proper scaling on the DynamoDB table and enable the DynamoDB table Time to Live (TTL) setting to delete records after 120 days. DynamoDB has a feature to delete items after a defined timestamp. This is cost-effective because it does not consume any write throughput.
The option that says: Use Amazon Managed Streaming for Apache Kafka (MSK) to ingest and store the records. Set a custom data retention period of 120 days for the Kafka topic. Send the streamed data to an Amazon S3 bucket for added durability is incorrect because it may not be the most efficient or cost-effective solution. While Amazon MSK is capable of ingesting and storing large volumes of data in real-time, it’s not optimized for low-latency data retrieval, which is a key requirement in the scenario. Moreover, the additional step of sending the streamed data to an Amazon S3 bucket for added durability might be unnecessary and could incur additional costs.
The option that says: Configure the application to receive the records and store the records to Amazon Aurora Serverless. Write an AWS Lambda function that runs a query to delete records older than 120 days. Schedule the function to run every night is incorrect. Since the application will constantly receive records, you won’t get the cost-effectiveness benefit of using Amazon Aurora Serverless. The DB will constantly be running anyway.
The option that says: Configure the application to ingest the records and store each record on a dedicated Amazon S3 bucket. Ensure that a unique filename is set for each object. Create an S3 bucket lifecycle policy to expire objects that are older than 120 days is incorrect. This is possible; however, it does not meet the low-latency retrieval time for the records.

References:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/howitworks-ttl.html
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-how-to.html

Check out these Amazon DynamoDB and Amazon Kinesis Cheat Sheets:
https://tutorialsdojo.com/amazon-dynamodb/
https://tutorialsdojo.com/amazon-kinesis/

</details>

<a id="q51"></a>

## Q51

A company uses Lightweight Directory Access Protocol (LDAP) for its employee authentication and authorization. The company plans to release a mobile app that can be installed on employee’s smartphones. The mobile application will allow users to have federated access to AWS resources. Due to strict security and compliance requirements, the mobile application must use a custom-built solution for user authentication. It must also use IAM roles for granting user permissions to AWS resources. The Solutions Architect was tasked to create a solution that meets these requirements.
Which of the following options should the Solutions Architect implement to enable authentication and authorization for the application? (Select TWO.)

- **A.** Build a custom OpenID Connect-compatible solution for the user authentication functionality. Use Amazon Cognito Identity Pools for authorizing access to AWS resources.
- **B.** Build a custom SAML-compatible solution for user authentication. Leverage AWS IAM Identity Center for authorizing access to AWS resources.
- **C.** Build a custom LDAP connector using Amazon API Gateway with AWS Lambda function for user authentication. Use Amazon DynamoDB to store user authorization tokens. Write another Lambda function that will validate user authorization requests based on the token stored on DynamoDB.
- **D.** Build a custom SAML-compatible solution to handle authentication and authorization. Configure the solution to use LDAP for user authentication and use SAML assertion to perform authorization to the IAM identity provider.
- **E.** Build a custom OpenID Connect-compatible solution in combination with AWS IAM Identity Center to create authentication and authorization functionality for the application.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D (you answered correctly)

🔑 **Key words:** custom auth + IAM roles for AWS access (Select TWO)

⚠️ **Watch:** Cognito user pools not allowed here

🧠 **Rule:** Custom OIDC IdP + Cognito identity pools, or custom SAML IdP (LDAP) + IAM SAML provider.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Công ty đang dùng LDAP để xác thực nhân viên
Ra mobile app: cần FEDERATED ACCESS vào AWS resources
Yêu cầu bắt buộc:
  - Custom-built solution cho user authentication
  - Dùng IAM roles để cấp quyền
(Select TWO)
```

Đáp án đúng: **A và D**. Anh chọn đúng cả hai.

#### Vì sao A và D đúng — hai giải pháp độc lập, cùng thỏa yêu cầu

Đề yêu cầu 2 lựa chọn **riêng biệt, mỗi lựa chọn tự nó là một giải pháp hoàn chỉnh** (không phải ghép 2 phần của 1 giải pháp như một số câu multi-select khác):

- **A — Custom OpenID Connect (OIDC) + Cognito Identity Pools:** tự xây IdP tương thích OpenID Connect để xác thực user (custom-built, đúng yêu cầu). Sau khi user có token từ IdP này, **Cognito Identity Pools** đổi token đó thành **temporary AWS credentials gắn với IAM role** — đúng yêu cầu "dùng IAM roles cấp quyền". Cognito Identity Pool hỗ trợ cả user đã login (qua OIDC provider được khai báo trong IAM) và user ẩn danh.
- **D — Custom SAML-compatible solution, dùng LDAP để xác thực, SAML assertion để lấy quyền:** tự xây SAML IdP (custom-built), IdP này gọi vào **hệ thống LDAP hiện có của công ty** để xác thực user — tận dụng đúng hạ tầng LDAP đã có. Sau xác thực, SAML assertion được gửi tới **IAM identity provider (SAML 2.0)** để đổi ra quyền truy cập AWS thông qua **IAM role** — đúng cả 2 yêu cầu "custom auth" và "IAM roles".

#### Vì sao các phương án còn lại sai

- **B (custom SAML + AWS IAM Identity Center để cấp quyền):** IAM Identity Center (SSO) **chỉ hỗ trợ single sign-on cho các business application qua web browser**, không thiết kế cho **mobile app** gọi trực tiếp — sai kênh truy cập so với yêu cầu đề ("mobile app installed on smartphones").
- **C (custom LDAP connector qua API Gateway + Lambda, lưu authorization token trong DynamoDB vĩnh viễn):** sai thực hành bảo mật — **không nên lưu authorization token vĩnh viễn trong DynamoDB**; token chỉ nên được sinh ra khi xác thực và lưu tạm trong thời gian session, không phải lưu trữ lâu dài như dữ liệu thường.
- **E (custom OpenID Connect + AWS IAM Identity Center):** sai vì **IAM Identity Center chỉ hỗ trợ ứng dụng dựa trên SAML 2.0**, không tương thích với giải pháp OpenID Connect — kết hợp này không hoạt động được.

| Phương án | Auth (custom) | Cấp quyền AWS | Vấn đề |
|---|---|---|---|
| **A (đúng)** | OIDC tự xây | Cognito Identity Pools | Không có |
| **D (đúng)** | SAML tự xây (dựa trên LDAP) | IAM SAML provider + IAM role | Không có |
| B | SAML tự xây | IAM Identity Center | Chỉ hỗ trợ web browser, không hợp mobile |
| C | LDAP connector custom | DynamoDB token vĩnh viễn | Lưu token sai cách |
| E | OIDC tự xây | IAM Identity Center | Identity Center không hỗ trợ OIDC |

#### Quy tắc nhớ cho thi

- **"Custom auth + cấp AWS credentials cho mobile app"** → **Cognito Identity Pools** (cho OIDC) hoặc **IAM SAML identity provider** (cho SAML) — không phải IAM Identity Center.
- **AWS IAM Identity Center (SSO)** → chỉ hợp với ứng dụng **SAML 2.0** truy cập qua **web browser**, không hợp mobile app hoặc OIDC.
- **Authorization token** không nên lưu vĩnh viễn trong DynamoDB — chỉ lưu tạm theo session.
- Với multi-select "chọn 2 giải pháp độc lập", kiểm tra từng option có tự đứng vững một mình không, đừng cố ghép cặp.

### TD explanation

AWS supports identity federation with SAML 2.0 (Security Assertion Markup Language 2.0), an open standard that many identity providers (IdPs) use. This feature enables federated single sign-on (SSO), so users can log in to the AWS Management Console or call the AWS API operations without having to create an IAM user for everyone in your organization. By using SAML, you can simplify the process of configuring federation with AWS because you can use the IdP’s service instead of writing custom identity proxy code.
You can use a role to configure your SAML 2.0-compliant identity provider (IdP) and AWS to permit your federated users to access the AWS Management Console. The role grants the user permissions to carry out tasks in the console. The following diagram illustrates the flow for SAML-enabled single sign-on.

The diagram illustrates the following steps:

The user browses your organization’s portal and selects the option to go to the AWS Management Console. In your organization, the portal is typically a function of your IdP that handles the exchange of trust between your organization and AWS.
The portal verifies the user’s identity in your organization.
The portal generates a SAML authentication response that includes assertions that identify the user and include attributes about the user. The portal sends this response to the client’s browser.
The client browser is redirected to the AWS IAM Identity Center endpoint and posts the SAML assertion.
The endpoint requests temporary security credentials on behalf of the user and creates a console sign-in URL that uses those credentials.
AWS sends the sign-in URL back to the client as a redirect.
The client browser is redirected to the AWS Management Console. If the SAML authentication response includes attributes that map to multiple IAM roles, the user is first prompted to select the role for accessing the console.

Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. Your users can sign in directly with a username and password or through a third party such as Facebook, Amazon, Google, or Apple. The two main components of Amazon Cognito are user pools and identity pools. User pools are user directories that provide sign-up and sign-in options for your app users. Identity pools enable you to grant your users access to other AWS services. You can use identity pools and user pools separately or together.
Amazon Cognito identity pools provide temporary AWS credentials for users who are guests (unauthenticated) and for users who have been authenticated and have received a token.
OpenID Connect is an open standard for authentication that is supported by a number of login providers. Amazon Cognito supports the linking of identities with OpenID Connect providers that are configured through AWS Identity and Access Management. Once you’ve created an OpenID Connect provider in the IAM Console, you can associate it with an identity pool.
The option that says: Build a custom SAML-compatible solution to handle authentication and authorization. Configure the solution to use LDAP for user authentication and use SAML assertion to perform authorization to the IAM identity provider is correct. The requirement is to use a custom-built solution for user authentication, and this can use the company LDAP system for authentication. The SAML assertion is also needed to get authorization tokens from the IAM identity provider that will grant IAM roles to users who wish to access AWS resources.
The option that says: Build a custom OpenID Connect-compatible solution for the user authentication functionality. Use Amazon Cognito Identity Pools for authorizing access to AWS resources is correct. The custom OpenID Connect-compatible solution will allow users to log in from their mobile application much like a single sign-on functionality. Amazon Cognito Identity Pool will provide temporary tokens to federated users for accessing AWS resources.
The option that says: Build a custom SAML-compatible solution for user authentication. Leverage AWS IAM Identity Center for authorizing access to AWS resources is incorrect. The requirement is to grant federated access from the mobile application. AWS IAM Identity  Center supports single sign-on to business applications through web browsers only.
The option that says: Build a custom LDAP connector using Amazon API Gateway with AWS Lambda function for user authentication. Use Amazon DynamoDB to store user authorization tokens. Write another Lambda function that will validate user authorization requests based on the token stored on DynamoDB is incorrect. It is not recommended to store authorization tokens permanently on DynamoDB tables. These tokens should be generated upon user authentication and then temporarily saved on a DynamoDB for a fixed session length.
The option that says: Build a custom OpenID Connect-compatible solution in combination with AWS IAM Identity Center to create authentication and authorization functionality for the application is incorrect. AWS IAM Identity Center supports only SAML 2.0–based applications, so an OpenID Connect-compatible solution will not work for this scenario.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html
https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html
https://docs.aws.amazon.com/cognito/latest/developerguide/open-id.html
https://aws.amazon.com/iam/identity-center/faqs/

Check out these Amazon Cognito Cheat Sheets:
https://tutorialsdojo.com/amazon-cognito/

</details>

---

# Group G — Migration (4)

<a id="q6"></a>

## Q6

A company is hosting its production environment on its on-premises servers. Most of the applications are packed as Docker containers that are manually run on self-managed virtual machines. The web servers are using the latest commercial Oracle Java SE suite which costs the company thousands of dollars in licensing costs. The MySQL databases are installed on separate servers configured on a “source-replica” setup for high availability. The company wants to migrate the whole environment to AWS Cloud to take advantage of its flexibility and agility, as well as use OpenJDK to save licensing costs without major changes in its applications.
Which of the following application migration strategies meet the above requirement?

- **A.** Re-host the environment on the AWS Cloud platform by creating EC2 instances that mirror the current web servers and database servers. Host the Docker instances on Amazon EC2 and test the new OpenJDK Docker containers on these instances. Create a dump of the on-premises MySQL databases and upload it to an Amazon S3 bucket. Launch a new Amazon EC2 instance with a MySQL database and import the data from Amazon S3.
- **B.** Re-platform the environment on the AWS Cloud platform by running the Docker containers on Amazon ECS. Test the new OpenJDK Docker containers and upload them on Amazon Elastic Container Registry. Migrate the MySQL database to Amazon RDS using AWS Database Migration Service.
- **C.** Re-factor/re-architect the environment on AWS Cloud by converting the Docker containers to run on AWS Lambda Functions. Convert the MySQL database to Amazon DynamoDB using the AWS Schema Conversion Tool (AWS SCT) to save on costs.
- **D.** Re-platform the environment on the AWS Cloud platform by deploying the Docker containers on AWS App Runner to reduce operational overhead. Test the new OpenJDK Docker containers and upload them on Amazon Elastic Container Registry (ECR). Convert the MySQL database to Amazon DynamoDB using the AWS Schema Conversion Tool (AWS SCT) to save on costs.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B (you answered correctly)

🔑 **Key words:** move to OpenJDK; no major app changes

⚠️ **Watch:** Refactor/rearchitect = major changes

🧠 **Rule:** Swap runtime, keep app → replatform (containers on ECS + managed DB).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises: Docker containers (chạy tay trên VM) + Oracle Java SE (đắt licensing)
             MySQL source-replica setup
                        │
                        ▼  Muốn: OpenJDK (rẻ hơn) + AWS Cloud
                        │  Ràng buộc: KHÔNG thay đổi lớn ứng dụng
```

Yêu cầu chốt là "**use OpenJDK... without major changes in its applications**" — đây là chỉ báo rõ ràng cho chiến lược migration. Anh chọn đúng **B**: re-platform — Docker container chạy trên **Amazon ECS** + image lưu ở **ECR**, MySQL chuyển sang **Amazon RDS qua AWS DMS**.

#### Vì sao B đúng

Trong 6 chiến lược "6 Rs" migration, **Re-platforming (lift-tinker-and-shift)** đúng nghĩa là: đổi một phần runtime/hạ tầng bên dưới (đổi Oracle JDK → OpenJDK, tự quản lý DB → managed DB) **nhưng giữ nguyên kiến trúc cốt lõi của ứng dụng**:

- Container vẫn là container, chỉ đổi orchestration platform (self-managed VM → ECS).
- MySQL vẫn là MySQL, chỉ đổi từ self-managed sang **RDS for MySQL** (managed database), dùng **AWS DMS** để migrate data với downtime tối thiểu.
- Đổi JDK bên trong image Docker (Oracle → OpenJDK) không đòi hỏi sửa code ứng dụng.

#### Vì sao từng đáp án sai bị loại

- **A sai** vì đây là **re-hosting** ("lift-and-shift" thuần) — mirror y nguyên cấu trúc on-premises lên EC2, dùng dump/restore MySQL thủ công qua S3. Cách này **không tận dụng được elasticity/agility của cloud** như công ty mong muốn, và vẫn phải tự quản lý DB trên EC2 (không managed).
- **C sai** vì chuyển sang **AWS Lambda + DynamoDB** là **re-factor/re-architect** — đòi hỏi **thay đổi lớn kiến trúc ứng dụng** (từ container sang serverless, từ SQL sang NoSQL), trực tiếp vi phạm ràng buộc "without major changes". Đề cũng không có lý do gì để đổi MySQL sang DynamoDB.
- **D sai** vì dùng **AWS App Runner** thay ECS — về mặt kỹ thuật khả thi để giảm operational overhead, nhưng đề **không yêu cầu giảm ops overhead ở mức đó**, và vẫn kèm việc chuyển MySQL sang DynamoDB **vô căn cứ** (không có lý do nghiệp vụ nào được nêu trong đề).

#### So sánh nhanh 6 chiến lược liên quan

| Chiến lược | Đặc điểm | Áp dụng ở đây? |
|---|---|---|
| Re-host | Mirror y nguyên, chỉ đổi hạ tầng | Không tối ưu — bỏ lỡ managed service |
| **Re-platform** | Đổi một phần hạ tầng/runtime, giữ kiến trúc | ✅ Đúng — ECS + RDS, đổi JDK |
| Re-factor/re-architect | Thiết kế lại theo cloud-native | Sai — đòi hỏi thay đổi lớn |
| Repurchase | Chuyển sang SaaS khác | Không liên quan tình huống này |

#### Quy tắc nhớ cho thi

- **"Không thay đổi lớn ứng dụng" + "chuyển sang managed service"** → **Re-platform**, không phải Re-host (quá thô) hay Re-architect (quá nhiều thay đổi)
- **Container tự quản lý → container trên AWS** → nghĩ ngay đến **ECS/ECR**, không cần Lambda trừ khi đề yêu cầu serverless rõ ràng
- **Đổi database engine (MySQL → DynamoDB)** chỉ chọn khi đề **có lý do nghiệp vụ rõ ràng** (ví dụ cần scale khủng, schema-less...) — nếu không có, đó là dấu hiệu đáp án gài bẫy

### TD explanation

The six most common application migration strategies are:
Rehosting — Otherwise known as “lift-and-shift”. Many early cloud projects gravitate toward net new development using cloud-native capabilities, but in a large legacy migration scenario where the organization is looking to scale its migration quickly to meet a business case, applications can be rehosted.
Replatforming — Sometimes, this is called “lift-tinker-and-shift.” Here you might make a few cloud (or other) optimizations in order to achieve some tangible benefit, but you aren’t otherwise changing the core architecture of the application. You may be looking to reduce the amount of time you spend managing database instances by migrating to a database-as-a-service platform like Amazon Relational Database Service (Amazon RDS) or migrating your application to a fully managed platform like Amazon Elastic Beanstalk.

Repurchasing — Moving to a different product. Repurchasing is a move to a SaaS platform. Moving a CRM to Salesforce.com, an HR system to Workday, a CMS to Drupal, etc.
Refactoring / Re-architecting — Re-imagining how the application is architected and developed, typically using cloud-native features. This is typically driven by a strong business need to add features, scale, or performance that would otherwise be difficult to achieve in the application’s existing environment. For example, migrating from a monolithic architecture to a service-oriented (or server-less) architecture to boost agility.
Retire — This strategy basically means: “Get rid of.” Once you’ve discovered everything in your environment, you might ask each functional area who owns each application and see that some of the applications are no longer used. You can save costs by retiring these applications.
Retain — Usually this means “revisit” or do nothing (for now). Maybe you aren’t ready to prioritize an application that was recently upgraded or are otherwise not inclined to migrate some applications. You can retain these applications and revisit your migration strategy.
Therefore, the correct answer is: Re-platform the environment on the AWS Cloud platform by running the Docker containers on Amazon ECS. Test the new OpenJDK Docker containers and upload them on Amazon Elastic Container Registry. Migrate the MySQL database to Amazon RDS using AWS Database Migration Service.
The option that says: Re-host the environment on the AWS Cloud platform by creating EC2 instances that mirror the current web servers and database servers. Host the Docker instances on Amazon EC2 and test the new OpenJDK Docker images on these instances. Create a dump of the on-premises MySQL databases and upload it to an Amazon S3 bucket. Launch a new Amazon EC2 instance with a MySQL database and import the data from Amazon S3 is incorrect. Although this is possible, simply re-hosting your applications by mirroring your current on-premises setup does not take advantage of the cloud’s elasticity and agility. A better approach is to use Amazon ECS to run the Docker containers and migrate the MySQL database to Amazon RDS.
The option that says: Re-factor/re-architect the environment on AWS Cloud by converting the Docker containers to run on AWS Lambda Functions. Convert the MySQL database to Amazon DynamoDB using the AWS Schema Conversion Tool (AWS SCT) to save on costs is incorrect because this solution requires major changes on the current application to execute successfully. In addition, there is nothing mentioned in the scenario that warrants the conversion of the MySQL database to Amazon DynamoDB.
The option that says: Re-platform the environment on the AWS Cloud platform by deploying the Docker containers on AWS App Runner to reduce operational overhead. Test the new OpenJDK Docker containers and upload them on Amazon Elastic Container Registry (ECR). Convert the MySQL database to Amazon DynamoDB using the AWS Schema Conversion Tool (AWS SCT) to save on costs is incorrect. It is possible to use AWS App Runner to deploy highly available containerized workloads. However, there is nothing mentioned in the scenario that warrants the conversion of the MySQL database to Amazon DynamoDB.

References:
https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/
https://aws.amazon.com/blogs/enterprise-strategy/214-2/
https://aws.amazon.com/blogs/enterprise-strategy/considering-a-mass-migration-to-the-cloud/

AWS Migration Strategies Cheat Sheet:
https://tutorialsdojo.com/aws-migration-strategies-the-6-rs/

</details>

<a id="q8"></a>

## Q8

A company is hosting its production environment in AWS Fargate. To save costs, the Chief Information Officer (CIO) wants to deploy its new development environment workloads on its on-premises servers as this leverages existing capital investments. The company also uses AWS Artifact to access compliance reports and agreements for its hybrid environment. The CIO tasks the Solutions Architect to provide a solution that will:


have both on-premises and Fargate managed in the same cluster


easily migrate development environment workloads running on-premises to production environment running in AWS Fargate


ensure consistent tooling and API experience across container-based workloads


Which of the following is the MOST operationally efficient solution that meets these requirements?

- **A.** Use Amazon EKS Anywhere to simplify on-premises Kubernetes management with default component configurations and automated cluster management tools. This makes it easy to migrate the development workloads running on-premises to EKS in an AWS region on Fargate.
- **B.** Install and configure AWS Outposts in your on-premises data center. Run Amazon ECS on Outposts to launch the development environment workloads. Migrate development workloads to production that is running on AWS Fargate.
- **C.** Install and configure AWS Outposts in your on-premises data center. Run Amazon EKS Anywhere on Outposts to launch container-based workloads. Migrate development workloads to production that is running on AWS Fargate.
- **D.** Utilize Amazon ECS Anywhere to streamline software management on-premises and on AWS with a standardized container orchestrator. This makes it easy to migrate the development workloads running on-premises to ECS in an AWS region on Fargate.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** on-prem + Fargate same cluster; consistent tooling

⚠️ **Watch:** EKS Anywhere = different tooling

🧠 **Rule:** Hybrid ECS on-prem + AWS → ECS Anywhere.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises servers          AWS Fargate (production)
      │                              │
      │   Dev workloads              │
      └──────── cùng 1 CLUSTER ──────┘
                       │
       Yêu cầu: migrate dev → prod dễ dàng
                consistent tooling + API
```

Ba yêu cầu chốt: **on-prem và Fargate trong CÙNG một cluster**, **migrate dễ dàng**, **tooling/API nhất quán**. Anh chọn đúng **D**: **Amazon ECS Anywhere**.

#### Vì sao D đúng

ECS Anywhere cho phép **compute on-premises tham gia vào cùng một ECS cluster** như EC2/Fargate trong AWS:

- Cùng một control plane ECS quản lý cả instance on-prem và task Fargate → đúng "same cluster".
- Dùng chung API/CLI/console ECS cho cả hai môi trường → đúng "consistent tooling and API experience".
- Khi cần chuyển workload từ dev (on-prem) sang production (Fargate), chỉ cần thay đổi launch type/capacity provider của task definition, không cần học lại công cụ mới → "easily migrate".
- Không cần cài đặt/duy trì phần mềm orchestration riêng cho on-prem → giảm operational overhead, đáp ứng "MOST operationally efficient".

#### Vì sao từng đáp án sai bị loại

- **A sai** vì **Amazon EKS Anywhere** là bản Kubernetes chạy on-premises, nhưng **không tích hợp với Kubernetes Cluster API Provider for AWS** để dễ dàng kéo sang EKS trên AWS Region — nó là một hệ quản trị riêng, không cùng cluster với Fargate.
- **B sai** vì tuy dùng đúng ý tưởng "ECS on Outposts", nhưng **AWS Fargate không được hỗ trợ trên AWS Outposts** — Outposts chỉ chạy ECS trên EC2 instance, không có capacity provider Fargate. Vậy nên không thể nói "Fargate" trong lời giải này đúng nghĩa.
- **C sai** vì **EKS Anywhere không được thiết kế để chạy trên AWS Outposts** — nó chỉ nhắm tới hạ tầng tự quản lý (on-prem, VMware), không tích hợp với các dịch vụ Kubernetes/Fargate được quản lý bởi AWS.

#### So sánh nhanh

| Đáp án | Công nghệ | Chạy chung cluster với Fargate? | Cần hạ tầng thêm (Outposts)? |
|---|---|---|---|
| **D (đúng)** | ECS Anywhere | ✅ Có | Không |
| A | EKS Anywhere (không Outposts) | ❌ Không | Không |
| B | ECS trên Outposts | ❌ Outposts không hỗ trợ Fargate | Có |
| C | EKS Anywhere trên Outposts | ❌ Không tích hợp | Có |

#### Lưu ý thực tế

- AWS Outposts chủ yếu cần **EC2 instance** làm compute capacity — Fargate (serverless) không chạy được trên Outposts, đây là chi tiết dễ nhầm khi đề nhắc tới "hybrid + Fargate" cùng lúc.
- ECS Anywhere không cần Outposts — chỉ cần cài **SSM Agent + ECS Agent** trên máy on-premises rồi register vào cluster hiện có.

#### Quy tắc nhớ cho thi

- **"on-prem + Fargate cùng cluster, tooling nhất quán"** → **ECS Anywhere**
- **"Fargate + Outposts"** trong cùng một câu → gần như luôn là **bẫy sai** vì Fargate không chạy trên Outposts
- **EKS Anywhere** → chỉ dùng khi đề chỉ nói về **Kubernetes on-premises độc lập**, không cần tích hợp ngược về AWS-managed service

### TD explanation

Amazon Elastic Container Service (ECS) Anywhere is a feature of Amazon ECS that lets you run and manage container workloads on your infrastructure. This feature helps you meet compliance requirements and scale your business without sacrificing your on-premises investments.
It ensures consistency with the same on-premises Amazon ECS tools when you migrate to AWS.
ECS Anywhere extends the reach of Amazon ECS to provide you with a single management interface for all of your container-based applications, irrespective of the environment they’re running in. As a result, you have a simple, consistent experience when it comes to cluster management, workload scheduling, and monitoring for both the cloud and on-premises. With ECS Anywhere, you do not need to install and maintain any container orchestration software, thus removing the need for your team to learn specialized knowledge domains and skillsets for disparate tooling.
ECS Anywhere makes it easy for you to run your applications in on-premises environments as long as desired and then migrate to the cloud with a single click at any time.

Therefore, the correct answer is: Utilize Amazon ECS Anywhere to streamline software management on-premises and on AWS with a standardized container orchestrator. This makes it easy to migrate the development workloads running on-premises to ECS in an AWS region on Fargate as it can have on-premises compute, EC2 instances, and Fargate in the same ECS cluster, making it easy to migrate ECS workloads running on-premises to ECS in an AWS region on Fargate or EC2 in the future if necessary.

The option that says: Use Amazon EKS Anywhere to simplify on-premises Kubernetes management with default component configurations and automated cluster management tools. This makes it easy to migrate the development workloads running on-premises to EKS in an AWS region on Fargate is incorrect because Amazon EKS Anywhere is not designed to run in the AWS Cloud. It does not integrate with the Kubernetes Cluster API Provider for AWS.
The option that says: Install and configure AWS Outposts in your on-premises data center. Run Amazon ECS on Outposts to launch the development environment workloads. Migrate development workloads to production that is running on AWS Fargate is incorrect because AWS Fargate is not supported on AWS Outposts. Amazon ECS on AWS Outposts primarily requires Amazon EC2 instances as the compute capacity provider. Fargate tasks cannot be launched or managed from an Outposts environment.
The option that says: Install and configure AWS Outposts in your on-premises data center. Run Amazon EKS Anywhere on Outposts to launch container-based workloads. Migrate development workloads to production that is running on AWS Fargate is incorrect because Amazon EKS Anywhere is not designed to run on AWS Outposts. It is just intended for customer-managed infrastructure, such as on-premises servers or VMware environments, and does not integrate with AWS-managed Kubernetes services or Fargate for workload migration.

References:
https://aws.amazon.com/ecs/anywhere/
https://aws.amazon.com/ecs/anywhere/faqs/
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-on-outposts.html
https://docs.aws.amazon.com/eks/latest/userguide/eks-deployment-options.html

Check out this Amazon Elastic Container Service Cheat Sheet:
https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

</details>

<a id="q31"></a>

## Q31

A company is hosting its flagship product page on a three-tier web application in its on-premises data center. The popularity of the last product launch attracted a sudden surge of traffic to its site, which caused some downtime that resulted in a significant impact on the product’s sales volume. The management decided to move the application to AWS. The application uses a MySQL database and is written in the .NET Framework. The team used the AWS Application Discovery Service Agentless Collector to inventory the existing application and its database dependencies. The Solutions Architect must design a highly available and scalable infrastructure to handle the demand of 300,000 peak users.
Which of the following design options would satisfy the above requirements while being cost-effective?

- **A.** Create an AWS Elastic Beanstalk application with an Auto Scaling group of Amazon EC2 instances as web servers that spans two separate regions. Put the EC2 instances behind an Application Load Balancer in each region. Launch a Multi-AZ Amazon Aurora MySQL database with a cross-region read replica to the other region. Create zone entries in Amazon Route 53 with a geoproximity routing policy to direct the traffic between the two regions.
- **B.** Create an AWS Elastic Beanstalk application that contains a web server tier and an Amazon RDS MySQL Multi-AZ database tier. The web server tier should launch a fleet of Amazon EC2 Auto Scaling Groups spanning multiple Availability Zones and behind a Network Load Balancer. Create an Amazon Route 53 zone entry for the company’s domain name with an Alias record pointed to the NLB.
- **C.** Launch an AWS CloudFormation stack that contains an Amazon ECS cluster that spans multiple Availability Zones using Spot Instances. Create an Application Load Balancer in front of the ECS cluster. Use the stack to launch an Amazon RDS MySQL database in a Multi-AZ configuration with a “snapshot” deletion policy. Create an Amazon Route 53 zone entry for the company’s domain name with an Alias record pointed to the ALB.
- **D.** Launch an AWS CloudFormation stack that contains an Auto Scaling Group of Amazon EC2 instances spanning multiple Availability Zones that are behind an Application Load Balancer. Use the stack to launch an Amazon Aurora MySQL database cluster in a Multi-AZ configuration with a “retain” deletion policy. Create an Amazon Route 53 zone entry for the company’s domain name with an Alias record pointed to the ALB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** 300k peak users; HA + scalable; cost-effective

⚠️ **Watch:** Single-AZ or over-provisioned options

🧠 **Rule:** CloudFormation stack: multi-AZ ASG + ALB + Aurora MySQL.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises (3-tier, MySQL, .NET)  ──migrate──►  AWS
Yêu cầu: HA + scalable, chịu 300,000 peak users, COST-EFFECTIVE
```

Anh chọn đúng **D — CloudFormation stack: ASG (multi-AZ) + ALB + Aurora MySQL Multi-AZ, deletion policy "retain"**.

#### Vì sao D đúng

Bài chỉ cần chạy trong **một Region**, không có yêu cầu global users hay cross-region — nên phương án đơn giản, đủ HA trong một Region là tối ưu chi phí nhất:

- **ASG multi-AZ + Application Load Balancer**: ALB hoạt động ở tầng 7 (HTTP/HTTPS), hỗ trợ path-based routing — phù hợp web app 3-tier hơn Network Load Balancer (tầng 4, chỉ dùng cho TCP thô).
- **Amazon Aurora MySQL Multi-AZ**: tương thích MySQL sẵn có, tự động failover trong Multi-AZ, không cần tự quản lý replication.
- **Deletion Policy "Retain"** trên CloudFormation: khi xóa stack, DB vẫn được giữ lại — nếu cần dựng lại stack mới, có thể tái sử dụng ngay DB cũ, tránh phải khôi phục từ snapshot (tốn thời gian).

#### Vì sao các đáp án sai (distractor cần nhớ)

- **B (Elastic Beanstalk + RDS MySQL + Network Load Balancer):** NLB chỉ xử lý ở **Layer 4 (TCP)**, không hỗ trợ routing theo HTTP header/query/cookie — không phù hợp web app cần logic định tuyến ở tầng ứng dụng. Phải dùng ALB.
- **A (Elastic Beanstalk 2 regions + Aurora cross-region read replica + Route 53 geoproximity):** Chạy **2 region** với 2 Auto Scaling group là thừa và đắt hơn nhiều so với chỉ cần multi-AZ trong 1 region để xử lý 300k users. Read-replica ở region phụ chỉ đọc được, mọi write vẫn phải gửi về region chính — không giải quyết thêm gì về HA mà lại tăng chi phí đáng kể.
- **C (ECS trên Spot Instances + RDS MySQL "snapshot" deletion policy):** Spot Instances có thể bị AWS thu hồi bất cứ lúc nào theo cung/cầu — rủi ro giảm độ tin cậy cho ứng dụng cần chạy ổn định phục vụ 300k users. Deletion policy "**snapshot**" khi xóa stack sẽ cần thời gian **restore từ snapshot** rất lâu nếu cần dựng lại nhanh, kém hơn "retain".

#### So sánh nhanh

| Đáp án | Load Balancer | Số Region | Deletion Policy DB | Compute peak |
|---|---|---|---|---|
| **D. ASG + ALB + Aurora (đúng)** | ALB (L7) | 1 | Retain (nhanh) | On-Demand ổn định |
| B. Beanstalk + NLB | NLB (L4, sai) | 1 | — | On-Demand |
| A. 2 regions | ALB nhưng x2 region | 2 (thừa, đắt) | — | On-Demand x2 |
| C. ECS Spot | ALB | 1 | Snapshot (chậm restore) | Spot (rủi ro bị reclaim) |

#### Quy tắc nhớ cho thi

- **Web app HTTP/HTTPS cần routing thông minh** → **Application Load Balancer**, không phải Network Load Balancer (dành cho TCP thô, hiệu năng cực cao).
- **"Cost-effective" + chỉ cần chịu tải trong 1 Region** → đừng chọn giải pháp multi-region nếu đề không yêu cầu global users.
- **CloudFormation DeletionPolicy "Retain"** → giữ resource khi xóa stack, khôi phục nhanh; **"Snapshot"** → phải restore lại, chậm hơn.
- **Spot Instances** không phù hợp cho tầng cần độ tin cậy 24/7 liên tục dù rẻ hơn.

### TD explanation

AWS CloudFormation gives you an easy way to model a collection of related AWS resources, provision them quickly and consistently, and manage them throughout their lifecycles by treating infrastructure as code. A CloudFormation template describes your desired resources and their dependencies so you can launch and configure them together as a stack.
In CloudFormation, the AWS::AutoScaling::AutoScalingGroup resource defines an Amazon EC2 Auto Scaling group, which is a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.
Elastic Load Balancing is used to automatically distribute your incoming application traffic across all the EC2 instances that you are running. You can use Elastic Load Balancing to manage incoming requests by optimally routing traffic so that no one instance is overwhelmed.

To use Elastic Load Balancing with your Auto Scaling group, you attach the load balancer to your Auto Scaling group to register the group with the load balancer. Your load balancer acts as a single point of contact for all incoming web traffic to your Auto Scaling group. An Application Load Balancer is ideal for this scenario as it routes and load-balances at the application layer (HTTP/HTTPS) and supports path-based routing.
On CloudFormation, you can set the RDS DeletionPolicy as “Retain,” which keeps the resource without deleting it or its contents when its stack is deleted. This is helpful in the event that the stack is deleted and you need to quickly provision a new stack. You can quickly use the retained RDS instance from the old stack.
Hence, the correct answer is: Launch an AWS CloudFormation stack that contains an Auto Scaling Group of Amazon EC2 instances spanning multiple Availability Zones that are behind an Application Load Balancer. Use the stack to launch an Amazon Aurora MySQL database cluster in a Multi-AZ configuration with a “retain” deletion policy. Create an Amazon Route 53 zone entry for the company’s domain name with an Alias record pointed to the ALB.
The option that says: Create an AWS Elastic Beanstalk application that contains a web server tier and an Amazon RDS MySQL Multi-AZ database tier. The web server tier should launch a fleet of Amazon EC2 Auto Scaling Groups spanning multiple Availability Zones and behind a Network Load Balancer. Create an Amazon Route 53 zone entry for the company’s domain name with an Alias record pointed to the NLBis incorrect. Network Load Balancer (NLB) is typically used for TCP traffic (Layer 4) and is not suitable for handling web applications that work on HTTP/HTTPS (Layer 7) traffic. Moreover, when you’re working with web applications, it’s typical to implement routing decisions based on HTTP attributes like query parameters, headers, or cookies, a functionality that NLBs do not support due to their Layer 4 operational limitations.
The option that says: Create an AWS Elastic Beanstalk application with an Auto Scaling group of Amazon EC2 instances as web servers that spans two separate regions. Put the EC2 instances behind an Application Load Balancer in each region. Launch a Multi-AZ Amazon Aurora MySQL database with a cross-region read replica to the other region. Create zone entries in Amazon Route 53 with a geoproximity routing policy to direct the traffic between the two regions is incorrect. Creating two Auto Scaling groups in separate regions is unnecessary and expensive. Distributing the EC2 instance in multiple Availability Zones is enough to handle the traffic. In this setup, the database in the second region is a read-replica only, so any writes to the database will have to be sent to the main region’s RDS instance.
The option that says: Launch an AWS CloudFormation stack that contains an Amazon ECS cluster that spans multiple Availability Zones using Spot Instances. Create an Application Load Balancer in front of the ECS cluster. Use the stack to launch an Amazon RDS MySQL database in a Multi-AZ configuration with a “snapshot” deletion policy. Create an Amazon Route 53 zone entry for the company’s domain name with an Alias record pointed to the ALB is incorrect. Although the Spot instance provides good cost savings for the web tier, the reliability of the site will suffer as the Spot instances are usually reclaimed by AWS based on the supply and demand of its global computing capacity. The “snapshot” deletion policy on the database tier is also not ideal, as this will require a significant time to restore if you delete the CloudFormation stack.

References:
https://aws.amazon.com/cloudformation/
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html
https://aws.amazon.com/blogs/aws/parallel-stack-processing-and-nested-stack-updates-for-aws-cloudformation/

Check out these Cheat Sheets:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/
https://tutorialsdojo.com/aws-cloudformation/

</details>

<a id="q60"></a>

## Q60

A company recently adopted a hybrid cloud architecture, requiring the migration of databases from an on-premises data center to AWS. One of the applications requires a heterogeneous database migration, specifically transforming an on-premises Oracle database to PostgreSQL. To accomplish this, a schema and code transformation must be completed prior to migrating the data.
Which of the following options is the most suitable approach to migrate the database in AWS?

- **A.** Use the AWS Serverless Application Model (SAM) service to transform your database to PostgreSQL using AWS Lambda functions. Migrate the database to RDS using the AWS Database Migration Service (DMS).
- **B.** Use AWS Glue to convert the source schema and code to match that of the target PostgreSQL database in RDS. Use AWS Batch with Spot EC2 instances to cost-effectively migrate the data from the source database to the target database in a batch process.
- **C.** Use the AWS Schema Conversion Tool (SCT) to convert the source schema to match that of the target database. Migrate the data using the AWS Database Migration Service (DMS) from the source database to an Amazon RDS for PostgreSQL database.
- **D.** Migrate the database from your on-premises data center using the AWS Application Migration Service. Afterward, use the AWS Database Migration Service to convert and migrate your data to Amazon RDS for PostgreSQL database.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** Oracle → PostgreSQL; schema + code conversion first

⚠️ **Watch:** DMS alone doesn't convert schema/code

🧠 **Rule:** Heterogeneous → SCT (schema/code) + DMS (data).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises Oracle DB
        │
   Bước 1: Schema + code transformation
   (data types, stored procs, functions khác nhau
    giữa Oracle và PostgreSQL)
        │  ── AWS Schema Conversion Tool (SCT) ──
        ▼
   Schema PostgreSQL-compatible
        │
   Bước 2: Migrate data thực tế
        │  ── AWS Database Migration Service (DMS) ──
        ▼
Amazon RDS for PostgreSQL
```

Đây là **heterogeneous migration** (engine nguồn khác engine đích: Oracle → PostgreSQL) nên bắt buộc phải qua schema/code transformation **trước** khi migrate data. Đáp án đúng: **C**. Anh chọn đúng C.

#### Vì sao C đúng

**C đúng** vì đề bài nói rõ "a schema and code transformation must be completed prior to migrating the data" — đây chính xác là quy trình 2 bước chuẩn cho heterogeneous migration: **AWS SCT** chuyển đổi schema + code (data types, stored procedures...) từ Oracle sang tương thích PostgreSQL, sau đó **AWS DMS** thực hiện di chuyển data thật (và tự động convert data type trong lúc migrate).

#### Từng đáp án sai vì đâu

- **A sai:** AWS SAM là framework để xây dựng **serverless application** (Lambda, API Gateway...), hoàn toàn không phải công cụ transform schema database — dùng Lambda để "transform database" là sai use case.
- **B sai:** AWS Glue là dịch vụ **ETL** cho data preparation/analytics, không được thiết kế để convert schema/code Oracle→PostgreSQL; AWS Batch + Spot instances là compute rẻ cho batch job nhưng không giải quyết được phần chuyển đổi schema — thiếu công cụ cốt lõi (SCT).
- **D sai:** AWS Application Migration Service (MGN) dùng để **migrate toàn bộ application/server** (lift-and-shift hạ tầng), không chuyên biệt cho database; và quan trọng hơn — DMS **tự nó không convert schema/code**, nó chỉ migrate data (dù có tự động convert data type khi migrate, không thay được vai trò của SCT cho schema/stored procedure).

| Đáp án | Công cụ chuyển schema | Công cụ migrate data | Vấn đề |
|---|---|---|---|
| **C (đúng)** | AWS SCT | AWS DMS | Không |
| A | AWS SAM/Lambda | AWS DMS | Sai công cụ transform |
| B | AWS Glue | AWS Batch + Spot | Sai công cụ transform, sai công cụ migrate |
| D | (không có) | AWS MGN + DMS | Thiếu bước schema conversion; MGN sai use case |

#### Quy tắc nhớ cho thi

- **Heterogeneous migration** (engine khác engine, ví dụ Oracle → PostgreSQL/Aurora) → luôn 2 bước: **AWS SCT** (schema + code) rồi **AWS DMS** (data).
- **Homogeneous migration** (cùng engine, ví dụ Oracle → Oracle) → chỉ cần DMS, không cần SCT.
- **DMS không tự convert schema/stored procedure** — nó chỉ tự động convert data type trong lúc migrate data.
- AWS SAM = serverless app framework; AWS Glue = ETL; AWS MGN = lift-and-shift server/app — không cái nào thay được vai trò SCT.

### TD explanation

AWS Database Migration Service helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. The AWS Database Migration Service can migrate your data to and from the most widely used commercial and open-source databases.
AWS Database Migration Service can migrate your data to and from most of the widely used commercial and open-source databases. It supports homogeneous migrations, such as Oracle to Oracle, as well as heterogeneous migrations between different database platforms, such as Oracle to Amazon Aurora. Migrations can be from on-premises databases to Amazon RDS or Amazon EC2, databases running on EC2 to RDS, or vice versa, as well as from one RDS database to another RDS database. It can also move data between SQL, NoSQL, and text-based targets.

In heterogeneous database migrations, the source and target databases engines are different, like in the case of Oracle to Amazon Aurora, Oracle to PostgreSQL, or Microsoft SQL Server to MySQL migrations. In this case, the schema structure, data types, and database code of source and target databases can be quite different, requiring a schema and code transformation before the data migration starts. That makes heterogeneous migrations a two-step process.
Hence, the correct answer is: Use the AWS Schema Conversion Tool to convert the source schema and code to match that of the target database, and then use the AWS Database Migration Service to migrate data from the source database to the target database. All the required data type conversions will automatically be done by the AWS Database Migration Service during the migration. The source database can be located in your own premises outside of AWS, running on an Amazon EC2 instance, or it can be an Amazon RDS database. The target can be a database in Amazon EC2 or Amazon RDS.
The option that says: Migrate the database from your on-premises data center using the AWS Application Migration Service. Afterward, use the AWS Database Migration Service to convert and migrate your data to Amazon RDS for PostgreSQL database is incorrect because the AWS Application Migration Service is typically designed for migrating entire applications, which can include everything from the underlying infrastructure to the application itself. Although it is correct to use AWS Database Migration Service (DMS) to migrate the database, this option is still wrong because you should use the AWS Schema Conversion Tool to convert the source schema.
The option that says: Use AWS Glue to convert the source schema and code to match that of the target PostgreSQL database in RDS. Use AWS Batch with Spot EC2 instances to cost-effectively migrate the data from the source database to the target database in a batch process is incorrect because AWS Glue is primarily an ETL (extract, transform, load) service used for data preparation and analytics. It is not designed for schema conversion from Oracle to PostgreSQL. AWS Batch and EC2 Spot Instances, while cost-effective for batch processing, are not ideal for handling the specifics of a database migration involving schema conversion.
The option that says: Use the AWS Serverless Application Model (SAM) service to transform your database to PostgreSQL using AWS Lambda functions. Migrate the database to RDS using the AWS Database Migration Service (DMS) is incorrect. The Serverless Application Model (SAM) is an open-source framework that is primarily used to build serverless applications on AWS, and not for database migration.

References:
https://aws.amazon.com/dms/
https://aws.amazon.com/cloud-migration/

Check out these AWS Migration Cheat Sheets:
https://tutorialsdojo.com/aws-database-migration-service/
https://tutorialsdojo.com/aws-migration-strategies-the-6-rs/

</details>
