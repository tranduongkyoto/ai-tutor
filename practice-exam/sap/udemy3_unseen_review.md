# Udemy Test #3 — unseen questions (Gate 1) — Wrong Answer Review (8 questions)

Source: `udemy3_unseen_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `udemy3_unseen_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q3](#q3) | ✅ 10-13 | ☐ | ☐ |
| A | [Q11](#q11) | ✅ 10-13 | ☐ | ☐ |
| A | [Q21](#q21) | ✅ 10-13 | ☐ | ☐ |
| A | [Q25](#q25) | ✅ 10-13 | ☐ | ☐ |
| A | [Q26](#q26) | ✅ 10-13 | ☐ | ☐ |
| B | [Q9](#q9) | ✅ 10-13 | ☐ | ☐ |
| B | [Q14](#q14) | ✅ 10-13 | ☐ | ☐ |
| C | [Q16](#q16) | ✅ 10-13 | ☐ | ☐ |

---

# Group A — Edge, routing & multi-Region delivery (5)

<a id="q3"></a>

## Q3

An e-commerce company manages its flagship applications on AWS. The Amazon EC2 instances running the applications are fronted by an Application Load Balancer (ALB). Amazon Route 53 provides public DNS services. Different URLs (mobile.ecomm.com, web.ecomm.com, api.ecomm.com) will serve the required content to the end-users.

As an AWS Certified Solutions Architect Professional, which combination of services would you use to serve the content to the end-users? (Select two)

- **A.** Use Path conditions in ALB listener to route *.ecomm.com to appropriate target groups
- **B.** Use Host conditions in ALB listener to route *.ecomm.com to appropriate target groups
- **C.** Use Host conditions in ALB listener to route $$$$.ecomm.com to appropriate target groups
- **D.** Use Host conditions in ALB listener to route ecomm.com to appropriate target groups
- **E.** Use Path component of Redirect actions in ALB listener configuration to route ecomm.com to appropriate target groups

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D · **You picked:** B, E

🔑 **Key words:** mobile./web./api.ecomm.com → different target groups

🪤 **Your trap:** Host *.ecomm.com (B) right; redirect action (E) doesn't forward to target groups

🧠 **Rule:** Route by hostname → ALB Host conditions (*.domain + apex); Path conditions only for /paths

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──► Route 53 (public DNS) ──► ALB (1 listener)
                                      │  rule theo Host header
          mobile.ecomm.com ──────────►├─► Target group: mobile
          web.ecomm.com ─────────────►├─► Target group: web
          api.ecomm.com ─────────────►└─► Target group: api
```

Yêu cầu then chốt: **phân biệt theo hostname** (mobile./web./api.) trên **một** ALB và đưa vào các target group khác nhau. Câu này chọn 2.

Đáp án đúng: **B (Host `*.ecomm.com`) + D (Host `ecomm.com`)**. Anh chọn B đúng, nhưng chọn thêm **E** (Redirect action) nên sai. E là lựa chọn làm hỏng đáp án.

#### Vì sao B + D tạo thành MỘT giải pháp

Host condition cho phép route theo hostname trong Host header (host-based routing). Ký tự hợp lệ: A-Z, a-z, 0-9, `-`, `.`, `*` (0 hoặc nhiều ký tự), `?` (đúng 1 ký tự).

Mấu chốt: **`*.ecomm.com` khớp `mobile.ecomm.com` nhưng KHÔNG khớp `ecomm.com`** (apex/root domain, không có phần subdomain). Vì vậy phải có thêm rule cho `ecomm.com`:

```
Rule 1: Host = *.ecomm.com  → bao phủ mobile / web / api (mọi subdomain)
Rule 2: Host = ecomm.com    → bao phủ apex domain
                              (B + D = bao phủ toàn bộ host)
```

#### Phần Anh chọn — E sai

**E (Path component của Redirect action):** Redirect action dùng để **chuyển hướng client sang URL khác** (trả HTTP 301/302), không **forward** request vào target group. Path component trong redirect chỉ là thành phần của URL đích. Đề cần "serve content từ target group theo hostname", nên redirect không giải quyết được.

Anh chọn B đúng vì nhận ra bài toán là host-based. Chỗ vấp là chọn nhầm "cặp" cho B: cặp đúng là D (apex), không phải E.

#### Các option còn lại

- **A (Path conditions `*.ecomm.com`):** Path condition so khớp phần **đường dẫn** bắt đầu bằng `/` (ví dụ `/img/*`), không phải hostname. Sai loại condition.
- **C (Host `$$$$.ecomm.com`):** `$` không nằm trong tập ký tự hợp lệ của hostname rule (chỉ có chữ, số, `-`, `.`, `*`, `?`).

| Condition / Action | So khớp trên | Dùng khi |
|---|---|---|
| **Host condition** | Host header (hostname) | Nhiều subdomain / domain, một ALB |
| Path condition | URL path (`/img/*`) | Tách theo đường dẫn |
| Redirect action | Không route, chỉ trả redirect | Đổi URL (HTTP sang HTTPS, đổi domain) |

#### Lưu ý thực tế

- Hostname rule phải có ít nhất một dấu `.`, và chỉ chữ cái sau dấu `.` cuối cùng. Rule không phân biệt hoa thường.
- Route 53 vẫn cần record (thường alias) cho từng hostname trỏ về ALB; ALB chỉ lo phần phân phối sau khi request đến.
- Muốn cả hai kiểu: kết hợp Host + Path trong cùng một rule (ví dụ `api.ecomm.com` và `/v2/*`).

#### Quy tắc nhớ cho thi

- **Thấy "mobile./web./api.domain" → khác target group** → **ALB Host conditions**
- **Thấy "`*.domain`"** → nhớ thêm rule cho **apex `domain`** (wildcard không khớp apex)
- **Thấy "/path"** → Path conditions; **Thấy "redirect"** → chỉ đổi URL, không forward
- Ký tự lạ như `$` trong hostname → option sai

### TD explanation

Correct options:

Use Host conditions in ALB listener to route *.ecomm.com to appropriate target groups

Use Host conditions in ALB listener to route ecomm.com to appropriate target groups

You can use host conditions to define rules that route requests based on the hostname in the host header (also known as host-based routing). This enables you to support multiple subdomains and different top-level domains using a single load balancer.

A hostname is not case-sensitive, can be up to 128 characters in length, and can contain any of the following characters:
1. A–Z, a–z, 0–9
2. - .
3. * (matches 0 or more characters)
4. ? (matches exactly 1 character)

You must include at least one "." character. You can include only alphabetical characters after the final "." character.

Example hostnames: example.com, test.example.com, *.example.com

The rule *.example.com matches test.example.com but doesn't match example.com. Hence, we also need to include ecomm.com along with *.ecomm.com to include all the hosts serving the requests.

Incorrect options:

Use Path component of Redirect actions in ALB listener configuration to route ecomm.com to appropriate target groups - You can use redirect actions to redirect client requests from one URL to another. The path component has an absolute path, starting with the leading "/". A path is case-sensitive, can be up to 128 characters in length, and consists of alphanumeric characters, wildcards (* and ?), & (using &), and the following special characters: _-.$/~"'@:+. This option is not useful for the given scenario.

Use Host conditions in ALB listener to route $$$$.ecomm.com to appropriate target groups - As discussed above, - ., * or ? can be used. '$' is not a valid character.

Use Path conditions in ALB listener to route *.ecomm.com to appropriate target groups - The path component has an absolute path, starting with the leading "/". Example HTTP path patterns /img/*, /img/*/pics, etc. It does not help while dealing with hostnames, as required for the given scenario.

Reference:

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html

</details>

<a id="q11"></a>

## Q11

A company is building an on-demand streaming application on AWS Cloud. The company has chosen Amazon S3 as its storage service and moved the existing videos to an Amazon S3 bucket. The application requires the video playback to start quickly, fast-forwarding should be more efficient and the overall user experience should be smoother without smothering the user's bandwidth.

Which AWS service(s) will help implement this solution effectively?

- **A.** Use AWS Elemental MediaConvert for file-based video processing, and Amazon CloudFront for delivery. Create a CloudFront distribution that points to the S3 bucket with videos uploaded. CloudFront will direct the request to the best edge location, based on the user’s location enhancing the overall user experience
- **B.** Use AWS Elemental MediaConvert for file-based video processing and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest
- **C.** Use Amazon S3 for storage and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest
- **D.** Deploy the application on Amazon EC2 instances with access to the S3 bucket. Configure these with a Network Load Balancer (NLB). Deploy the application stack in multiple AWS Regions around the world and configure Global Accelerator to serve content to the user

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** fast start, efficient fast-forward, don't saturate bandwidth

🪤 **Your trap:** S3+CloudFront+HLS skips transcoding into adaptive-bitrate renditions

🧠 **Rule:** VOD streaming → MediaConvert (transcode) + HLS manifest + CloudFront

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Video gốc ──► S3 bucket ──► ?? xử lý ──► ?? phân phối ──► Người xem
                                                          (mobile / TV / PC)
Yêu cầu: bắt đầu phát NHANH, tua nhanh hiệu quả,
         trải nghiệm mượt, KHÔNG phí băng thông người dùng
```

Đáp án đúng: **B** (MediaConvert + CloudFront + HLS + manifest). Anh chọn **C** (S3 + CloudFront + HLS + manifest, bỏ MediaConvert).

#### Vì sao B đúng

Giải pháp VOD đầy đủ gồm 3 mảnh:

```
S3 (lưu)  ──►  MediaConvert (transcode)  ──►  S3 (HLS segments + manifest .m3u8)
                                                      │
                                              CloudFront (cache ở edge)
                                                      │
                                         Player tải manifest URL
```

- **MediaConvert** chuyển video sang đúng kích thước, độ phân giải, định dạng cho từng thiết bị; với HLS thì **cắt video thành các segment ngắn** và tạo **manifest file**.
- **HLS** (cùng họ DASH, MSS, HDS): player lấy nội dung từng đoạn vài giây trước khi cần. Hệ quả: phát bắt đầu nhanh hơn, tua hiệu quả hơn, mượt hơn, chỉ trả tiền phần người xem thực sự xem.
- **CloudFront** trỏ vào manifest, cache segment ở edge, độ trễ thấp.

#### Phần Anh chọn — C sai ở đâu

C có đủ S3, CloudFront, HLS, manifest, nên trông rất hợp lý. Nhưng HLS **không tự có sẵn**: file video thô trong S3 chưa được cắt segment và chưa có manifest. Ai làm việc đó? Theo đề, C không có thành phần nào xử lý video, nên phải **tự xây** (custom-built) bước transcode/segment. Option B dùng MediaConvert (managed) cho đúng việc này.

Nói cách khác: "dùng HLS" là một giao thức, còn "tạo ra nội dung HLS" cần dịch vụ transcode.

#### Các option còn lại

- **A (MediaConvert + CloudFront trỏ thẳng vào S3, không HLS):** cách này dễ làm và chạy được trên hầu hết thiết bị, nhưng player tải cả file video. Nếu người xem bỏ giữa chừng, phần chưa xem vẫn bị tải và vẫn tốn tiền. Dùng băng thông kém hiệu quả, trái yêu cầu.
- **D (EC2 + NLB đa Region + Global Accelerator):** thiếu cả khả năng xử lý video của MediaConvert lẫn khả năng phân phối cache của CloudFront. Global Accelerator tối ưu đường đi mạng, không cache nội dung và không tạo streaming.

| Option | Transcode/segment | Giao thức streaming | Cache edge | Kết quả |
|---|---|---|---|---|
| A | MediaConvert | Không (tải cả file) | CloudFront | Phí băng thông |
| **B** | **MediaConvert** | **HLS + manifest** | **CloudFront** | **Đúng** |
| C | Không có | HLS (nhưng không có nội dung HLS) | CloudFront | Thiếu bước tạo HLS |
| D | Không có | Không | Không (Global Accelerator) | Sai công cụ |

#### Lưu ý thực tế

- Output MediaConvert ghi lại vào S3; CloudFront dùng S3 làm origin và player nhận URL dạng `https://<distribution>.cloudfront.net/<path>/playlist.m3u8`.
- Bộ ba S3 + MediaConvert + CloudFront là mô hình VOD chuẩn của AWS. Còn live streaming thì khác (MediaLive/MediaPackage), đừng nhầm.

#### Quy tắc nhớ cho thi

- **Thấy "VOD, video lưu trong S3, phát nhanh, tua mượt, tiết kiệm băng thông"** → **MediaConvert + HLS + CloudFront**
- **Thấy "chỉ đặt CloudFront trước S3 với file video"** → tải cả file, không tiết kiệm băng thông
- **Thấy "HLS/manifest" nhưng không có MediaConvert** → ai tạo segment? → option thiếu
- **Global Accelerator** không phải CDN: không cache, không transcode

### TD explanation

Correct option:

Use AWS Elemental MediaConvert for file-based video processing, and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest

A complete on-demand streaming solution typically makes use of Amazon S3 for storage, AWS Elemental MediaConvert for file-based video processing, and Amazon CloudFront for delivery.

Once videos are uploaded to the Amazon S3 bucket, you may need to convert your video into the size, resolution, or format needed by a particular television or connected device. AWS Elemental MediaConvert will take care of this for you. MediaConvert takes content from S3, transcodes it per your request, and stores the result back in S3. Transcoding processes video files, creating compressed versions of the original content to reduce its size, change its format, or increase playback device compatibility.

With your content safely stored and available in the formats required by your users, the next step is global delivery with Amazon CloudFront. The Amazon Content Delivery Network caches content at the edges for low latency and high throughput video delivery. Its scalability means that you can serve up as much or as little video as you want.

A family of video streaming protocols including Apple’s HTTP Live Streaming (HLS), Dynamic Adaptive Streaming over HTTP (DASH), Microsoft’s Smooth Streaming (MSS), and Adobe’s HTTP Dynamic Streaming (HDS) improves the user experience by delivering video as it is being watched, generally fetching content a few seconds ahead of when it will be needed. Playback starts more quickly, fast-forwarding is more efficient, and the overall user experience is smoother. With this option, you only pay for what the viewer watches, you don’t waste the user’s bandwidth, and users get to see the desired content more quickly.

You will need to do a little more work to implement the second option. First, you use MediaConvert to convert your video files to HLS format (the most widely supported streaming protocol). This will split the video into short segments and will also create a manifest file. Then, you point the CloudFront distribution at the manifest. Finally, to play the live stream, embed the manifest URL in the players that your users will play your live stream with. For example, to play a live stream for which the manifest file is myStream/playlist.m3u8 and the CloudFront distribution is d111111abcdef8.cloudfront.net, you embed the following URL in players: http://d111111abcdef8.cloudfront.net/myStream/playlist.m3u8

On-demand streaming of content stored in Amazon S3:

via - https://aws.amazon.com/cloudfront/streaming/

Incorrect options:

Use AWS Elemental MediaConvert for file-based video processing, and Amazon CloudFront for delivery. Create a CloudFront distribution that points to the S3 bucket with videos uploaded. CloudFront will direct the request to the best edge location, based on the user’s location enhancing the overall user experience - This option is very easy to implement and is supported by just about every mobile device and desktop. All you need to do is to put your content in an S3 bucket and create a CloudFront distribution that points to the bucket. Your user’s video player will use CloudFront URLs (accessible as part of the distribution) to request the video file. The request will be directed to the best edge location, based on the user’s location. The CDN will serve the video from its cache, fetching it from the S3 bucket if it is not already cached. This option has a couple of downsides. It makes inefficient use of your viewer’s bandwidth. If the user doesn’t bother to watch the entire video, content that would never be seen is still downloaded and you are paying for it.

Use Amazon S3 for storage and Amazon CloudFront for delivery. Use video streaming protocols like Apple’s HTTP Live Streaming (HLS) and create a manifest file. Point the CloudFront distribution at the manifest - For this case, AWS Elemental MediaConvert is required to convert your video into the size, resolution, or format needed by a particular television or connected device. Else this functionality will have to be custom-built.

Deploy the application on Amazon EC2 instances with access to the S3 bucket. Configure these with a Network Load Balancer (NLB). Deploy the application stack in multiple AWS Regions around the world and configure Global Accelerator to serve content to the user - AWS Elemental MediaConvert is required to convert your video into the size, resolution, or format needed by a particular television or connected device. Or this functionality will have to be custom-built. Video streaming protocols improve the user experience by delivering video as it is being watched, generally fetching content a few seconds ahead of when it will be needed. This will enhance the user experience by not hogging the network bandwidth of the user. The option lacks the video processing capabilities of AWS Elemental MediaConvert and the efficient delivery capabilities of CloudFront.

References:

https://aws.amazon.com/blogs/networking-and-content-delivery/how-flowplayer-improved-live-video-ingest-with-aws-global-accelerator/

https://aws.amazon.com/cloudfront/streaming/

</details>

<a id="q21"></a>

## Q21

A solutions architect at a retail company has configured a private hosted zone using Route 53. The architect needs to configure health checks for record sets within the private hosted zone that are associated with EC2 instances.

How can the architect build a solution to address the given use case?

- **A.** Configure a Route 53 health check that monitors an SNS topic which in turn notifies a CloudWatch alarm when the EC2 StatusCheckFailed metric fails
- **B.** Configure a Route 53 health check to a private IP associated with the instances inside the VPC to be checked
- **C.** Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric and then configure a health check that monitors the status of the metric
- **D.** Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric, add an alarm to the metric, and then configure a health check that monitors the state of the alarm

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** health check for records in a PRIVATE hosted zone

🪤 **Your trap:** Route 53 health checkers live on the internet — they can't reach private IPs

🧠 **Rule:** Private-zone health → CloudWatch metric → alarm → Route 53 health check on alarm state

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Private hosted zone (chỉ resolve trong VPC)
   app.internal.corp ──► EC2 (private IP 10.0.x.x)  trong VPC

Route 53 health checkers: nằm NGOÀI VPC, trên internet công cộng
        ✗ không với tới 10.0.x.x

Yêu cầu: health check cho record của PRIVATE hosted zone
```

Đáp án đúng: **D** (CloudWatch metric, thêm alarm, rồi health check theo trạng thái alarm). Anh chọn **B** (health check trỏ vào private IP).

#### Vì sao D đúng

Route 53 health check có thể giám sát một trong ba thứ: một endpoint (web server...), **trạng thái của các health check khác**, hoặc **trạng thái của một CloudWatch alarm**. Với private zone, cách khả thi là dùng loại thứ ba:

```
EC2 ──► metric StatusCheckFailed (CloudWatch)
              │
              ▼
        CloudWatch Alarm  (đặt trên metric)
              │  (Route 53 health check dựa trên dòng dữ liệu của alarm)
              ▼
   Route 53 health check "theo alarm"
              │
              ▼
   Gắn vào record trong private hosted zone (failover)
```

Dữ liệu metric nằm trong CloudWatch (bên trong AWS), nên không cần checker truy cập vào VPC. Lưu ý: để tăng độ bền và sẵn sàng, Route 53 không chờ alarm chuyển sang ALARM; trạng thái health check đổi từ healthy sang unhealthy dựa trên dòng dữ liệu và tiêu chí của alarm.

#### Phần Anh chọn — B sai ở đâu

B nghe rất tự nhiên: "health check tới IP của instance". Nhưng **health checker của Route 53 nằm ngoài VPC**, nên không gọi được private IP. Muốn health check endpoint trong VPC theo IP thì phải gán **public IP** cho instance, mà như vậy không còn là bài toán private.

⚠️ Chìa khóa là chữ **PRIVATE** hosted zone. Thấy từ này thì loại ngay mọi phương án "health check trực tiếp vào endpoint nội bộ".

#### Các option còn lại

- **A (health check giám sát SNS topic):** Route 53 health check **không giám sát được SNS topic**. Ngoài ra luồng "SNS thông báo cho alarm" cũng sai chiều: alarm mới là thứ bắn ra SNS, không phải ngược lại.
- **C (health check theo metric, không có alarm):** Route 53 health check giám sát được **alarm**, **không** đọc trực tiếp **metric**. Thiếu bước tạo alarm.

| Option | Health check nhắm vào | Hợp lệ? |
|---|---|---|
| A | SNS topic | Sai, không hỗ trợ |
| B | Private IP trong VPC | Sai, checker không vào được VPC |
| C | CloudWatch metric | Sai, chỉ hỗ trợ alarm |
| **D** | **CloudWatch alarm trên metric** | **Đúng** |

#### Lưu ý thực tế

- Pattern này áp dụng cho mọi nguồn trong VPC không có endpoint công khai: tạo metric (có thể là custom metric), alarm, health check theo alarm.
- Health check theo alarm có thể gắn vào failover/weighted record để Route 53 ngừng trả record unhealthy.
- Health check còn có thể giám sát health check khác (calculated health check) để gộp nhiều điều kiện.

#### Quy tắc nhớ cho thi

- **Thấy "private hosted zone + health check"** → **CloudWatch metric, alarm, health check theo alarm**
- **Thấy "health check vào private IP"** → sai, checker ở ngoài VPC
- **Route 53 health check giám sát được**: endpoint, health check khác, **CloudWatch alarm** (không phải metric, không phải SNS)
- Metric luôn đi qua **alarm** trước khi Route 53 dùng được

### TD explanation

Correct option:

Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric, add an alarm to the metric, and then configure a health check that monitors the state of the alarm

A private hosted zone is a container that holds information about how you want Amazon Route 53 to respond to DNS queries for a domain and its subdomains within one or more VPCs that you create with the Amazon VPC service.

via https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html

Amazon Route 53 health checks monitor the health and performance of your web applications, web servers, and other resources. Each health check that you create can monitor one of the following:

The health of a specified resource, such as a web server.

The status of other health checks.

The status of an Amazon CloudWatch alarm.

Additionally, with Amazon Route 53 Application Recovery Controller, you can set up routing control health checks with DNS failover records to manage traffic failover for your application.

For the given use case, you need to create a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric, add an alarm to the metric, and then create a health check that is based on the data stream for the alarm. To improve resiliency and availability, Route 53 doesn't wait for the CloudWatch alarm to go into the ALARM state. The status of a health check changes from healthy to unhealthy based on the data stream and the criteria in the CloudWatch alarm.

via https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html

Incorrect options:

Configure a Route 53 health check that monitors an SNS topic which in turn notifies a CloudWatch alarm when the EC2 StatusCheckFailed metric fails - As mentioned above, the Route 53 health checks cannot monitor an SNS topic, so this option is incorrect.

Configure a Route 53 health check to a private IP associated with the instances inside the VPC to be checked - Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC. Therefore, you cannot configure a Route 53 health check to a private IP associated with an instance.

Configure a CloudWatch metric that checks the status of the EC2 StatusCheckFailed metric and then configure a health check that monitors the status of the metric - Route 53 health checks can monitor CloudWatch alarms. The Route 53 health checks cannot directly monitor the CloudWatch metrics, so this option is incorrect.

References:

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html

</details>

<a id="q25"></a>

## Q25

A company has its web application hosted on Amazon EC2 instances that are deployed in a single AWS Region. The company has now expanded its operations into new geographies and the company wants to offer low-latency access for the application to its customers. To comply with different financial regulations of each geography, the application needs to operate in silos and the underlying instances in one region should not interact with instances running in other regions.

Which of the following represents the most optimal solution to automate the application deployment to different AWS regions?

- **A.** Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation stack set from an administrator account to launch stack instances that deploy the application to various other regions
- **B.** Create a shell script that uses the AWS CLI to query the current state in one region and output an AWS CloudFormation template. Create a CloudFormation stack from the template by using the AWS CLI, specifying the --region parameter to deploy the application to other regions
- **C.** Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation change set from an administrator account to launch stack instances that deploy the application to various other regions
- **D.** Create a CloudFormation template describing the application infrastructure in the Resources section. Create a CloudFormation stack from the template by using the AWS CLI, specify multiple regions using the --regions parameter to deploy the application

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** automate deployment to many Regions, isolated silos

🪤 **Your trap:** create-stack has no --regions; one stack = one Region

🧠 **Rule:** Multi-Region / multi-account deploy → CloudFormation StackSets

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại:  1 Region ──► web app (EC2)

Mục tiêu:  Region A    Region B    Region C   ...
           ┌──────┐    ┌──────┐    ┌──────┐
           │ app  │    │ app  │    │ app  │   triển khai CÙNG hạ tầng
           └──────┘    └──────┘    └──────┘   ở nhiều Region, tự động
           (mỗi Region là một silo, không tương tác chéo Region)
```

Yêu cầu: **tự động hóa deploy cùng một hạ tầng sang nhiều Region**. Lưu ý "silo" nghĩa là mỗi Region chạy độc lập, không phải cần replicate hay kết nối chéo.

Đáp án đúng: **A** (CloudFormation StackSets). Anh chọn **D** (create-stack với `--regions`).

#### Vì sao A đúng

Một template CloudFormation mô tả hạ tầng trong phần `Resources`. Từ một **administrator account**, tạo **stack set**, chỉ định danh sách Region (và account đích), CloudFormation tạo **stack instances** ở từng Region.

```
Template (Resources)
      │
  Stack set  (tạo ở admin account)
      │
      ├─► Stack instance @ Region A
      ├─► Stack instance @ Region B
      └─► Stack instance @ Region C
```

Stack set bảo đảm cùng resource, cùng cấu hình được triển khai nhất quán ở mọi Region đích. Khi tạo/cập nhật/xóa còn có thể đặt operation preferences: thứ tự Region, failure tolerance, số account chạy đồng thời.

#### Phần Anh chọn — D sai ở đâu

D trông gần giống A: cùng template, chỉ khác là dùng CLI. Sai ở chi tiết: lệnh `aws cloudformation create-stack` chỉ nhận **`--region` (một Region)**, **không có tham số `--regions`**. Một stack chỉ tồn tại trong **một Region**. Muốn nhiều Region phải dùng stack set (nhiều stack instances) hoặc chạy lệnh nhiều lần.

⚠️ Bẫy: option có vẻ "tiện" bằng một tham số không tồn tại. Nếu AWS cho phép nhiều Region trong một stack thì đã không cần StackSets.

#### Các option còn lại

- **B (script AWS CLI query hiện trạng rồi sinh template):** tự chế, không "optimal". AWS đã có sẵn tính năng này dưới dạng stack set; script dễ sai lệch và phải bảo trì.
- **C (change set):** change set chỉ để **xem trước tác động** khi cập nhật một stack hiện có, không dùng để triển khai ra nhiều Region.

| Công cụ | Phạm vi | Dùng để |
|---|---|---|
| Stack | 1 Region, 1 account | Quản lý nhóm resource |
| Change set | 1 stack | Xem trước thay đổi trước khi update |
| **Stack set** | **Nhiều Region / nhiều account** | **Triển khai cùng template hàng loạt** |
| Script CLI tự viết | Tùy script | Không tối ưu, tự bảo trì |

#### Lưu ý thực tế

- Stack set là **regional resource**: tạo ở Region nào thì chỉ thấy/sửa ở Region đó (nhưng vẫn triển khai stack instances sang các Region đích).
- Template nên tránh hard-code thứ chỉ có ở một Region (ví dụ AMI ID); dùng `Mappings`, hoặc SSM parameter để lấy AMI theo Region.
- Chọn đúng mục tiêu "silo": không cần peering hay replication giữa các Region, chỉ cần deploy lặp lại.

#### Quy tắc nhớ cho thi

- **Thấy "deploy cùng hạ tầng tới nhiều Region/account"** → **CloudFormation StackSets**
- **Thấy "`--regions` của create-stack"** → không tồn tại, bẫy
- **Thấy "change set"** → chỉ preview update của một stack
- **Thấy "script tự viết" cạnh managed feature** → gần như luôn sai ("most optimal")

### TD explanation

Correct option:

Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation stack set from an administrator account to launch stack instances that deploy the application to various other regions

via - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html

Here are the relevant CloudFormation concepts:

Template: A CloudFormation template is a JSON or YAML formatted text file. You can save these files with any extension, such as .json, .yaml, .template, or .txt. CloudFormation uses these templates as blueprints for building your AWS resources.

Stack: When you use CloudFormation, you manage related resources as a single unit called a stack. You create, update, and delete a collection of resources by creating, updating, and deleting stacks. All the resources in a stack are defined by the stack's CloudFormation template.

Change set: If you need to make changes to the running resources in a stack, you update the stack. Before making changes to your resources, you can generate a change set, which is a summary of your proposed changes. Change sets allow you to see how your changes might impact your running resources, especially for critical resources, before implementing them.

Stack set: A stack set lets you create stacks in AWS accounts across regions by using a single CloudFormation template. All the resources included in each stack are defined by the stack set's CloudFormation template. As you create the stack set, you specify the template to use, in addition to any parameters and capabilities that the template requires.

After you've defined a stack set, you can create, update, or delete stacks in the target accounts and AWS Regions you specify. When you create, update, or delete stacks, you can also specify operation preferences, such as the order of Regions in which you want the operation to be performed, the failure tolerance beyond which stack operations stop, and the number of accounts in which operations are performed on stacks concurrently. A stack set is a regional resource. If you create a stack set in one AWS Region, you can't see it or change it in other Regions.

via - https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html

For the given use case, you need to create a stack set that includes the CloudFormation template that you want to use to create stacks and then identify the AWS Regions in which you want to deploy stacks in your target accounts. A stack set ensures consistent deployment of the same stack resources, with the same settings, to all specified target accounts within the Regions you choose.

Incorrect options:

Create a CloudFormation template describing the application infrastructure in the Resources section. Create a CloudFormation stack from the template by using the AWS CLI, specify multiple regions using the --regions parameter to deploy the application - You can create a stack using the AWS Management Console or using AWS CloudFormation commands in the AWS CLI. The aws cloudformation create-stack command supports only a region parameter for a single region and not regions parameter for multiple regions.

via - https://aws.amazon.com/blogs/infrastructure-and-automation/multiple-account-multiple-region-aws-cloudformation/

Create a shell script that uses the AWS CLI to query the current state in one region and output an AWS CloudFormation template. Create a CloudFormation stack from the template by using the AWS CLI, specifying the --region parameter to deploy the application to other regions - Creating a script is not an elegant solution to provision same infrastructure in multiple AWS regions since this functionality is directly offered by AWS in the form of stack sets.

Create a CloudFormation template describing the application infrastructure in the Resources section. Use CloudFormation change set from an administrator account to launch stack instances that deploy the application to various other regions - When you need to update a stack, understanding how your changes will affect running resources before you implement them can help you update stacks with confidence. Change sets allow you to preview how proposed changes to a stack might impact your running resources, for example, whether your changes will delete or replace any critical resources, AWS CloudFormation makes the changes to your stack only when you decide to execute the change set, allowing you to decide whether to proceed with your proposed changes or explore other changes by creating another change set. You cannot use change sets to deploy an application to multiple AWS regions.

References:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html

</details>

<a id="q26"></a>

## Q26

A global multi-player gaming application runs on UDP protocol and it needs to add functionality where you can assign multiple players to a single session on a game server based on factors such as geographic location, player skill, and a few more configurable parameters. The application is accessed by players spread out across different regions of the world.

What is the BEST way to configure this requirement?

- **A.** Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance using VPC subnet endpoints
- **B.** Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance using VPC sharing
- **C.** Use custom routing accelerator of Global Accelerator in front of Network Load Balancer (NLB) to route traffic that can maintain session data
- **D.** Use Application Load Balancer (ALB) with sticky sessions enabled to maintain player session data. Configure Global Accelerator to front the ALB for cross-region elasticity

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** UDP game, assign players to a specific session/instance

🪤 **Your trap:** NLB load-balances — can't target a specific instance deterministically

🧠 **Rule:** Deterministic user→instance routing → Global Accelerator custom routing + VPC subnet endpoints

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Người chơi toàn cầu (UDP)
        │
        ▼
 Global Accelerator ──► ?? ──► EC2 game server (nhiều session / instance)

Yêu cầu: gán nhiều người chơi vào ĐÚNG MỘT session trên ĐÚNG MỘT game server
         (theo vị trí, kỹ năng, cấu hình...) — tức routing "xác định" (deterministic)
```

Đáp án đúng: **A** (custom routing accelerator + **VPC subnet endpoints**). Anh chọn **C** (custom routing accelerator đặt trước NLB).

#### Vì sao A đúng

**Custom routing accelerator** là loại accelerator cho phép dùng **logic ứng dụng của chính mình** để định tuyến một hoặc nhiều người dùng đến **một EC2 instance cụ thể** (trong một hoặc nhiều Region). Dùng cho game nhiều người chơi, VoIP, EdTech, social media gán người dùng vào một media server.

```
Matchmaking logic của app
      │  chọn: người chơi X, Y ──► session S1 @ 10.0.1.25:7777
      ▼
Custom routing accelerator
   mỗi (IP, port) của instance ↔ một port riêng trên accelerator
      │
      ▼
VPC subnet endpoint  (chứa các EC2 chạy game)
      │
      ▼
 Đúng EC2 + đúng port của session
```

Điểm cốt lõi: custom routing accelerator **chỉ hỗ trợ VPC subnet endpoints**. Mỗi subnet endpoint chứa các EC2 chạy ứng dụng; traffic chỉ được route đến EC2 trong subnet đó. App ánh xạ người dùng sang một port của accelerator, và traffic được đẩy đúng tới IP:port của session.

#### Phần Anh chọn — C sai ở đâu

C hợp lý vì NLB hỗ trợ UDP, và Global Accelerator cho hiệu năng toàn cầu. Hai lỗi:

1. Custom routing accelerator **không nhận NLB làm endpoint**, chỉ nhận **VPC subnet**.
2. NLB **cân bằng tải**: nó chọn target theo thuật toán của nó, nên **không thể chỉ định deterministic** người chơi nào đến instance nào. Đề cần chính xác điều ngược lại.

#### Các option còn lại

- **B (custom routing + VPC sharing):** VPC sharing là tính năng chia sẻ subnet giữa nhiều account trong Organization, không phải loại endpoint của Global Accelerator. Custom routing chỉ hỗ trợ **VPC subnet endpoints**.
- **D (ALB sticky sessions + Global Accelerator):** **ALB không xử lý UDP** (chỉ HTTP/HTTPS). Sticky session chỉ giữ "dính" lâu dài với một target, không cho phép app chọn target.

| Option | Endpoint | UDP | Chọn instance cụ thể | Kết quả |
|---|---|---|---|---|
| **A** | **VPC subnet** | Có | **Có (deterministic)** | **Đúng** |
| B | "VPC sharing" | Không phải endpoint hợp lệ | Không | Sai |
| C | NLB | Có | Không (load balance) | Sai |
| D | ALB | Không | Không | Sai |

📝 Ghi chú kỹ thuật: Global Accelerator thường (standard accelerator) phù hợp khi muốn load balancing qua ALB/NLB/EC2/EIP. Custom routing là kiểu khác, chỉ dùng khi **app tự quyết định** instance đích.

#### Lưu ý thực tế

- Custom routing chỉ route đến EC2 trong subnet endpoint; không dùng cho ALB/NLB.
- Cần thành phần matchmaking của ứng dụng để chọn session và tra cứu port tương ứng.
- Tách bạch: "route dựa trên health/vị trí tự động" thì standard accelerator; "route chỉ định đích" thì custom routing.

#### Quy tắc nhớ cho thi

- **Thấy "assign players/users to a specific session/instance"** → **Global Accelerator custom routing**
- **Thấy "custom routing"** → endpoint chỉ là **VPC subnet**, không phải NLB/ALB
- **Thấy "UDP"** → loại ALB; **Thấy "deterministic"** → loại NLB (load balancer không deterministic)
- **VPC sharing** là khái niệm nhiều account, không liên quan endpoint của Global Accelerator

### TD explanation

Correct option:

Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance - A custom routing accelerator is a new type of accelerator in Global Accelerator. It allows you to use your own application logic to deterministically route one or more users to a specific Amazon EC2 instance destination in a single or multiple AWS Regions. This is useful for use cases where you want to control which session on an EC2 instance your user traffic is sent to.

One example is a multi-player gaming application where you want to assign multiple players to a single session on a game server, based on factors such as geographic location, player skill, and gaming configuration. Other examples are VoIP, EdTech, and social media applications that assign multiple users to a specific media server to initiate voice, video, and messaging sessions. With a custom routing accelerator, you can direct multiple users to a unique port on your accelerator, and their traffic will be routed to a specific destination IP address and port that your application session is running on.

Custom routing accelerators support only VPC subnet endpoints, each containing one or more EC2 instances that are running your application. Each VPC subnet endpoint, which could be in a single or multiple Regions, contains the IP addresses of the EC2 instances that host your application. With a custom routing accelerator, you can put your accelerator in front of up to thousands of EC2 instances running in a single or multiple VPCs. Custom routing accelerators support VPC subnet endpoints with a maximum size of /17 and route traffic only to EC2 instances within each subnet.

Incorrect options:

Use Application Load Balancer (ALB) with sticky sessions enabled to maintain player session data. Configure Global Accelerator to front the ALB for cross-region elasticity - Application Load Balancer (ALB) cannot be used for UDP traffic. It works for HTTP and HTTPS traffic only.

Use custom routing accelerator of Global Accelerator to deterministically route one or more users to a specific instance using VPC sharing - VPC sharing allows multiple AWS accounts to create their application resources, such as Amazon EC2 instances, Amazon Relational Database Service (RDS) databases, Amazon Redshift clusters, and AWS Lambda functions, into shared, centrally-managed virtual private clouds (VPCs). Custom routing accelerator supports only VPC subnet endpoints.

Use custom routing accelerator of Global Accelerator in front of Network Load Balancer (NLB) to route traffic that can maintain session data - As discussed above, Custom routing accelerator supports only VPC subnet endpoints.

Reference:

https://aws.amazon.com/global-accelerator/features/

</details>

---

# Group B — Monitoring, logging & tamper-proofing (2)

<a id="q9"></a>

## Q9

A healthcare company has to maintain a log of all transactions for audit and compliance purposes. The company is planning stringent security measures for all of its CloudTrail log files.

Which of the following would you suggest as the LEAST effort options to secure the CloudTrail logs? (Select two)

- **A.** Integrate with Amazon CloudWatch alarms to generate an alarm whenever changes are made to CloudTrail log files
- **B.** To prevent access rights violation, use AWS root user account to manage CloudTrail logs
- **C.** Use Amazon S3 MFA Delete on the S3 bucket that holds CloudTrail logs and digest files
- **D.** Enable CloudTrail log file integrity validation
- **E.** Enable Amazon S3 encryption using AWS KMS keys on the S3 bucket that stores CloudTrail logs to prevent unauthorized modification of the log files

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D · **You picked:** D, E

🔑 **Key words:** LEAST effort to secure CloudTrail logs

🪤 **Your trap:** Integrity validation (D) right; KMS (E) gives confidentiality, not tamper/delete protection

🧠 **Rule:** Tamper-proof CloudTrail → log file integrity validation + S3 MFA Delete

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
API activity ──► CloudTrail ──► S3 bucket (log files + digest files)
                                    ▲
         Kẻ xấu / admin sai quyền ──┘  muốn SỬA hoặc XÓA log

Yêu cầu: bảo vệ log CloudTrail cho audit/compliance, ÍT CÔNG SỨC NHẤT
```

Đề hỏi về **tamper-proof** (chống sửa/xóa, và phát hiện bị sửa/xóa), không phải bảo mật nội dung. Đáp án đúng: **C (S3 MFA Delete)** + **D (log file integrity validation)**. Anh chọn đúng D, nhưng chọn thêm **E (KMS)** thay vì C, nên bộ đáp án sai.

#### Pick nào làm hỏng đáp án

Đáp án phải là một cặp "phát hiện + ngăn chặn":

```
D  = PHÁT HIỆN : log bị sửa / xóa / thiếu?  (hash + digest file có ký)
C  = NGĂN CHẶN : khó xóa vĩnh viễn object / đổi versioning (cần MFA)
```

Anh có D (phát hiện) nhưng thiếu phần ngăn chặn. **E là pick làm hỏng** vì nó không cung cấp thứ đề cần.

#### D đúng — Log file integrity validation

- Khi bật, CloudTrail tạo **hash cho mỗi log file** được deliver.
- Mỗi giờ CloudTrail tạo thêm **digest file** tham chiếu các log file của giờ đó, chứa hash của từng file.
- Digest file được **ký bằng private key** của một cặp key; sau đó dùng public key để validate. Mỗi Region dùng cặp key khác nhau.
- Kết quả: khẳng định được log chưa bị đổi, bị xóa, hoặc không có log nào được deliver trong một khoảng thời gian.
- Chỉ cần bật một setting trên trail, nên "ít công sức".

#### C đúng — S3 MFA Delete

- Digest file nằm **cùng bucket** với log file, nên bảo vệ bucket là bảo vệ cả hai.
- MFA Delete yêu cầu xác thực thêm khi **đổi versioning state** hoặc **xóa vĩnh viễn một object version**.
- Dù kẻ tấn công có password của IAM user đủ quyền xóa, vẫn bị chặn nếu không có MFA.

#### E sai — Anh chọn

**Vì sao trông đúng:** "encryption" thường gắn với bảo mật mạnh hơn, và đề có chữ "unauthorized modification".

**Vì sao sai:** SSE-KMS chỉ bảo vệ **confidentiality** (người không có quyền key không đọc được dữ liệu at rest). Nó **không** bảo vệ integrity hay chống xóa. Principal có đủ quyền vẫn có thể delete object, overwrite, hoặc đổi bucket policy. Vế "to prevent unauthorized modification" trong option là mồi nhử.

#### A và B sai

- **A (CloudWatch alarm khi log file thay đổi):** làm được vì CloudTrail và CloudWatch tích hợp chặt, nhưng cần thêm công sức (metric filter, alarm, cấu hình) so với C, D. Đề hỏi LEAST effort. Ngoài ra alarm chỉ báo, không chặn.
- **B (dùng root user quản lý log):** root user không nên dùng cho việc vận hành, đây là security best practice cơ bản. Sai ngay.

| Option | Loại bảo vệ | Chống sửa/xóa? | Công sức |
|---|---|---|---|
| **D. Integrity validation** | Phát hiện | Phát hiện sửa/xóa | Thấp (bật setting) |
| **C. MFA Delete** | Ngăn chặn | Chặn xóa vĩnh viễn | Thấp |
| E. SSE-KMS | Confidentiality | Không | Thấp nhưng sai mục tiêu |
| A. CloudWatch alarm | Cảnh báo | Không | Cao hơn |
| B. Root user | (anti-pattern) | Không | Không liên quan |

#### Lưu ý thực tế

- Digest file validate bằng AWS CLI (`aws cloudtrail validate-logs`) hoặc tự viết script theo tài liệu.
- Ngoài MFA Delete, thực tế còn dùng S3 Object Lock, nhưng nếu đề liệt kê MFA Delete thì chọn theo đáp án đề.

#### Quy tắc nhớ cho thi

- **Thấy "tamper-proof CloudTrail logs"** → **log file integrity validation + S3 MFA Delete**
- **Thấy KMS / encryption trong câu hỏi về tamper** → **chỉ là confidentiality**, thường là bẫy
- **Thấy "LEAST effort" + CloudWatch alarm** → alarm tốn công hơn bật setting có sẵn
- **Thấy "root user để vận hành"** → luôn sai
- Mnemonic: **Phát hiện (D) + Ngăn chặn (C)**, KMS là **che mắt** chứ không **khóa tay**

### TD explanation

Correct options:

Enable CloudTrail log file integrity validation - Validated log files are invaluable in security and forensic investigations. For example, a validated log file enables you to assert positively that the log file itself has not changed, or that particular user credentials performed specific API activity. The CloudTrail log file integrity validation process also lets you know if a log file has been deleted or changed, or assert positively that no log files were delivered to your account during a given time.

When you enable log file integrity validation, CloudTrail creates a hash for every log file that it delivers. Every hour, CloudTrail also creates and delivers a file that references the log files for the last hour and contains a hash of each. This file is called a digest file. CloudTrail signs each digest file using the private key of a public and private key pair. After delivery, you can use the public key to validate the digest file. CloudTrail uses different key pairs for each AWS region.

Use Amazon S3 MFA Delete on the S3 bucket that holds CloudTrail logs and digest files - The digest files are delivered to the same Amazon S3 bucket associated with your trail as your CloudTrail log files. If your log files are delivered from all regions or from multiple accounts into a single Amazon S3 bucket, CloudTrail will deliver the digest files from those regions and accounts into the same bucket.

Configuring multi-factor authentication (MFA) ensures that any attempt to change the versioning state of your bucket or permanently delete an object version requires additional authentication. This helps prevent any operation that could compromise the integrity of your log files, even if a user acquires the password of an IAM user that has permission to permanently delete Amazon S3 objects.

Incorrect options:

Enable Amazon S3 encryption using AWS KMS keys on the S3 bucket that stores CloudTrail logs to prevent unauthorized modification of the log files - This option sounds correct because encryption is commonly associated with stronger security controls. However, S3 default encryption with AWS KMS only protects the confidentiality of data at rest, not its integrity or deletion. Even when logs are encrypted, any IAM principal with sufficient permissions can still delete objects, overwrite them, or change access policies.

Integrate with Amazon CloudWatch alarms to generate an alarm whenever changes are made to CloudTrail log files - CloudTrail and CloudWatch are closely integrated and it is possible to implement something like this. However, this requires additional effort compared to the correct options.

To prevent access rights violation, use AWS root user account to manage CloudTrail logs - Root user account should not be used for any operational use cases as a security best practice, so this option is incorrect.

References:

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html

</details>

<a id="q14"></a>

## Q14

The development team at a company has noticed issues with the Quality of Service (QoS) in the traffic to the EC2 instances hosting a VOIP program. The team needs to inspect the network packets to determine if it is a programming error or a networking error.

As an AWS Certified Solutions Architect Professional, which of the following options would you suggest for the given use case?

- **A.** Configure traffic mirroring on the source EC2 instances hosting the VOIP program, set up a network monitoring program on a target EC2 instance and stream the logs to an S3 bucket for further analysis
- **B.** Use CloudWatch to inspect the network packets
- **C.** Provision another EC2 instance with an ENI added to act as a monitoring interface. Configure the port to promiscuous mode and sniff the traffic to analyze the packets. Direct the output of this single stream to an S3 bucket for further analysis
- **D.** Use VPC Flow Logs to inspect the network packets

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** inspect network PACKETS for VoIP QoS

🪤 **Your trap:** VPC Flow Logs = metadata only (IPs, ports, accept/reject)

🧠 **Rule:** Packet contents → VPC Traffic Mirroring to a monitoring instance

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──VoIP──► EC2 (VOIP program)     QoS kém: jitter? latency? loss?
                    │
                    ▼
        Cần xem NỘI DUNG PACKET để biết
        lỗi do code (application) hay do network
```

Từ khóa quyết định: **inspect the network PACKETS**. Đáp án đúng: **A (Traffic Mirroring + monitoring tool trên target EC2)**. Anh chọn **D (VPC Flow Logs)**.

⚠️ **Lỗi lặp lại:** Anh đã nhầm Traffic Mirroring với VPC Flow Logs ở TD3 Q45, và đã làm lab Traffic Mirroring ngày 10-09. Lần này vẫn chọn Flow Logs, nên cần chốt một quy tắc phân biệt rõ ràng bên dưới.

#### A đúng — Traffic Mirroring

```
Source EC2 (VOIP)
   │  ENI
   │  copy toàn bộ traffic (Traffic Mirroring session)
   ▼
Target EC2 (Wireshark / tool phân tích)
   │
   ▼
Stream log sang S3 để phân tích tiếp
```

- **Traffic Mirroring** copy traffic đi qua elastic network interface của source rồi gửi sang target để điều tra.
- Target chạy network monitoring program (ví dụ Wireshark) nên thấy được **packet thật**: payload, header, timing để suy ra jitter, latency, error rate.
- QoS của VoIP phụ thuộc bandwidth, latency, jitter, error rate. Đây là loại phân tích cần packet-level.

#### D sai — Anh chọn: VPC Flow Logs

**Vì sao trông đúng:** Flow Logs cũng "capture traffic của network interface", publish được sang CloudWatch Logs hoặc S3, nghe giống giám sát mạng.

**Vì sao sai:** Flow Logs chỉ ghi **metadata** của IP traffic (source/destination IP, port, protocol, bytes, accept/reject), tạo cho VPC, subnet hoặc network interface. Nó **không** chứa packet content nên không dùng để inspect packets.

#### B và C sai

- **B (CloudWatch):** thu thập metric, log, alarm. Không inspect được network packet.
- **C (EC2 thêm ENI, promiscuous mode, sniff):** trong VPC có cơ chế chống packet sniffing. Dù đặt NIC vào promiscuous mode, hypervisor **không giao** traffic không gửi đến instance đó. Hai instance của cùng một khách hàng trên cùng host vật lý cũng không nghe được traffic của nhau.

#### Bảng phân biệt (chốt cho lần sau)

| Công cụ | Thấy gì | Dùng khi |
|---|---|---|
| **VPC Flow Logs** | Metadata: IP, port, protocol, bytes, accept/reject | Ai nói chuyện với ai, bị SG/NACL chặn không |
| **VPC Traffic Mirroring** | Packet thật (copy traffic từ ENI) | Deep packet inspection, troubleshoot, security forensics |
| CloudWatch | Metric, log, alarm | Giám sát tài nguyên |
| Promiscuous mode | Không hoạt động trong VPC | Bẫy |

#### Lưu ý thực tế

- Traffic Mirroring gửi traffic copy tới target (ENI, NLB...), nên target cần đủ băng thông xử lý.
- Flow Logs vẫn hữu ích cho câu hỏi "traffic có bị REJECT không", nhưng không trả lời "payload/jitter ra sao".

#### Quy tắc nhớ cho thi

- **Thấy "inspect packets" / "packet capture" / "Wireshark" / "deep packet inspection"** → **VPC Traffic Mirroring**
- **Thấy "IP traffic info" / "accepted or rejected" / "who connected"** → **VPC Flow Logs**
- **Thấy "promiscuous mode / sniff" trên EC2** → **sai**, hypervisor không chuyển traffic của VM khác
- **Thấy "CloudWatch inspect packets"** → sai
- Mnemonic: **Flow Logs = "phong bì" (địa chỉ, kích thước)**, **Traffic Mirroring = "mở thư đọc nội dung"**

### TD explanation

Correct option:

Configure traffic mirroring on the source EC2 instances hosting the VOIP program, set up a network monitoring program on a target EC2 instance and stream the logs to an S3 bucket for further analysis

Quality of Service (QoS) is a set of technologies that enable a network to dependably run high-priority applications and traffic under limited network capacity. QoS technologies accomplish this by providing differentiated handling and capacity allocation to specific flows in network traffic. Bandwidth (throughput), latency (delay), jitter (variance in latency), and error rate are the metrics relevant to QoS. This implies that QoS is of particular importance to high-bandwidth, real-time traffic such as voice over IP (VoIP), video conferencing, and video-on-demand that have a high sensitivity to latency and jitter.

Generally, the promiscuous mode allows the user to bypass the normal operation mode by forwarding all traffic it receives to the CPU. However for AWS, even if you can turn your NIC to Promiscuous mode, the hypervisor will never pass traffic intended for another virtual machine to your EC2 instance. You need to use traffic mirroring as it allows you to copy traffic passing through an elastic network adaptor and send it toward another instance for further investigation. For the given use case, you need to set up traffic mirroring on the source EC2 instances hosting the VOIP program and then install a network monitoring program (such as Wireshark) on the traffic mirroring target EC2 instance. Finally, you can stream the logs from the target EC2 instance to an S3 bucket for further analysis.

Incorrect options:

Use CloudWatch to inspect the network packets - Amazon CloudWatch is a monitoring service for AWS cloud resources and the applications you run on AWS. You can use Amazon CloudWatch to collect and track metrics, collect and monitor log files, and set alarms. CloudWatch cannot be used to inspect the network packets.

Use VPC Flow Logs to inspect the network packets - VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon CloudWatch Logs or Amazon S3. You can create a flow log for a VPC, a subnet, or a network interface. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored. VPC Flow Logs cannot be used to inspect the network packets.

Provision another EC2 instance with an ENI added to act as a monitoring interface. Configure the port to promiscuous mode and sniff the traffic to analyze the packets. Direct the output of this single stream to an S3 bucket for further analysis - Amazon EC2 instances running with an Amazon VPC have built-in protection against packet sniffing. It is not possible for a virtual instance running in promiscuous mode to receive or “sniff” traffic that is intended for a different virtual instance. While customers can place their interfaces into promiscuous mode, the hypervisor will not deliver any traffic to them that is not addressed to them. Even two virtual instances that are owned by the same customer located on the same physical host cannot listen to each other’s traffic. So this option is incorrect.

References:

https://d1.awsstatic.com/whitepapers/Security/Networking_Security_Whitepaper.pdf

https://medium.com/@macsat101/packet-sniffing-using-wireshark-on-aws-183b7983685d

https://www.paloaltonetworks.com/cyberpedia/what-is-quality-of-service-qos

</details>

---

# Group C — Migration strategy fit (1)

<a id="q16"></a>

## Q16

A legacy web application runs 24/7 and it is currently hosted on an on-premises server with an outdated version of the Operating System (OS). The OS support will end soon and the team wants to expedite migration to an Amazon EC2 instance with an updated version of the OS. The application also references 90 TB of static data in the form of images that need to be moved to AWS.

How should this be accomplished most cost-effectively?

- **A.** Use AWS Application Migration Service to migrate the application and all its data to Amazon EC2 instance
- **B.** Replatform the server to Amazon EC2 while choosing an AMI of your choice to cater to the OS requirements. Use AWS Snowball to transfer the image data to Amazon S3
- **C.** Set up the application on AWS Fargate for a serverless solution and use AWS Snowball to transfer the image data to Amazon S3
- **D.** Use AWS Direct Connect to establish a dedicated connection between on-premises systems and AWS. Transfer data to Amazon S3 using this link. Migrate the application to Amazon EC2 instance

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** expedite, new OS version, 24/7 app, 90 TB images, cost-effective

🪤 **Your trap:** Fargate = re-architect to containers (slower, more change)

🧠 **Rule:** New OS fast → replatform to EC2 with a fresh AMI; bulk data → Snowball

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises                               AWS
┌──────────────────────┐                  ┌──────────────────────┐
│ Legacy web app 24/7  │   ───────────►   │ EC2 + AMI có OS mới  │
│ OS cũ sắp hết support│                  │                      │
│ 90 TB ảnh tĩnh       │   ───────────►   │ S3                   │
└──────────────────────┘                  └──────────────────────┘

Yêu cầu: expedite, OS mới, chạy 24/7, cost-effective
```

Đáp án đúng: **B (replatform lên EC2 với AMI OS mới + Snowball cho 90 TB sang S3)**. Anh chọn **C (Fargate + Snowball)**. Phần Snowball của Anh đúng, chỉ sai ở phần compute.

#### B đúng — Replatform lên EC2

- Đề nói "updated version of the OS", tức là chọn **AMI có OS phù hợp** rồi cài app lên. Đây là replatform: thay nền tảng nhưng giữ nguyên kiến trúc app.
- Amazon cung cấp sẵn AMI cho nhiều loại OS.
- Theo TD, EC2 là lựa chọn rẻ nhất trong các option.
- **Snowball** phù hợp chuyển 90 TB: chuyển bằng thiết bị vật lý, tránh chi phí mạng cao, thời gian truyền lâu và lo ngại bảo mật của truyền tải lớn qua mạng. Sau đó dữ liệu vào **S3**, nơi lưu trữ rẻ nhất trên AWS, kết hợp lifecycle policy để giảm thêm chi phí.

#### C sai — Anh chọn: Fargate

**Vì sao trông đúng:** "serverless" nghe hiện đại, không phải quản lý OS.

**Vì sao sai:**

```
Fargate = container hóa app
   → đổi kiến trúc (re-architect) → cần dev effort riêng + chi phí kèm theo
   → KHÔNG "expedite"
   → app chạy 24/7 → Fargate đắt hơn EC2
```

Đề muốn **nhanh** và **rẻ nhất**. Fargate vi phạm cả hai. Phần Snowball trong C không sai, lỗi nằm ở compute.

#### A và D sai

- **A (Application Migration Service, MGN):** là dịch vụ chính để **lift and shift**. Đề cần **thay OS** (replatform), không chỉ lift-and-shift y nguyên OS cũ. Vì vậy sai.
- **D (Direct Connect + chuyển qua link):** quá mức cho một lần migrate; cần thời gian provision và chi phí cao, không phù hợp use case.

#### Bảng so sánh

| Option | Chiến lược | Compute | Data 90 TB | Vấn đề |
|---|---|---|---|---|
| **B** | Replatform | EC2 + AMI mới | Snowball | Khớp mọi yêu cầu |
| C | Re-architect | Fargate | Snowball | Chậm, tốn dev effort, đắt hơn khi 24/7 |
| A | Rehost | MGN lift-and-shift | Qua MGN | Không đổi OS |
| D | Rehost/replatform | EC2 | Direct Connect | Provision lâu, tốn kém cho việc một lần |

#### Lưu ý thực tế

- Snowball mất thời gian vận chuyển thiết bị vật lý; nếu cần app chạy sớm, có thể dựng EC2 trước rồi nạp ảnh sau.
- Chỉ dùng Direct Connect khi có nhu cầu kết nối lâu dài, không phải di chuyển dữ liệu một lần.

#### Quy tắc nhớ cho thi

- **Thấy "expedite" + "cập nhật OS"** → **replatform lên EC2 với AMI mới**
- **Thấy "Fargate / serverless" cho legacy app** → thường là **re-architect**, chậm và tốn dev effort
- **Thấy "app chạy 24/7" + "cost-effective"** → EC2 rẻ hơn Fargate
- **Thấy "hàng chục TB, một lần"** → **Snowball**, không phải Direct Connect
- **Thấy "MGN"** → lift-and-shift, không thay OS

### TD explanation

Correct option:

Replatform the server to Amazon EC2 while choosing an AMI of your choice to cater to the OS requirements. Use AWS Snowball to transfer the image data to Amazon S3

Re-platforming the server to Amazon EC2 instances is the best choice here since the use case speaks about updating the existing operating system. Amazon provides pre-configured AMIs to choose different flavors of OS to cater to each requirement. Also, Amazon EC2 is the least expensive of all options.

Key differences between Rehosting and Replatforming:

via - https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/

AWS Snowball, a part of the AWS Snow Family, is an edge computing, data migration, and edge storage device that comes in two options. Snowball Edge Storage Optimized devices provide both block storage and Amazon S3-compatible object storage, and 40 vCPUs. They are well suited for local storage and large-scale data transfer.

Amazon Snowball is a data transport solution that accelerates moving terabytes to petabytes of data into and out of Amazon Web Services services using storage devices designed to be secure for physical transport. Using Snowball helps to eliminate challenges that can be encountered with large-scale data transfers including high network costs, long transfer times, and security concerns.

Snowball is the right data transfer choice if you need to securely and quickly transfer terabytes to many petabytes of data to Amazon Web Services services. Snowball can also be the right choice if you don’t want to make expensive upgrades to your network infrastructure.

Finally, transfer the image data from Snowball to Amazon S3, which is the most cost-effective storage solution offered on AWS, when combined with lifecycle policies to further accelerate cost savings.

Incorrect options:

Use AWS Direct Connect to establish a dedicated connection between on-premises systems and AWS. Transfer data to Amazon S3 using this link. Migrate the application to Amazon EC2 instance - AWS Direct Connect is an overkill for a one-time migration requirement. Also, Direct Connect takes time to provision and is cost-prohibitive for this use case.

Set up the application on AWS Fargate for a serverless solution and use AWS Snowball to transfer the image data to Amazon S3 - AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). AWS Fargate makes it easy to focus on building your applications. Using Fargate implies changing the architecture of the solution, so it would need separate development effort along with the associated cost. In addition, Fargate is costlier than hosting on Amazon EC2 instance when the application runs 24/7 - as mentioned in the given use case.

Use AWS Application Migration Service to migrate the application and all its data to Amazon EC2 instance - AWS Application Migration Service (AWS MGN) is the primary migration service recommended to lift and shift your applications to AWS. Customers considering CloudEndure Migration are encouraged to use AWS Application Migration Service for future migrations. For the current use case, we are not only looking for lift and shift but for replatforming too. Hence, this option is incorrect.

References:

https://aws.amazon.com/snowball/

https://aws.amazon.com/application-migration-service/

https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/

https://blogs.perficient.com/2021/06/17/aws-cost-analysis-comparing-lambda-ec2-fargate/

</details>
