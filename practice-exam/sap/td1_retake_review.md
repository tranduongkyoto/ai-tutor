# TD Set 1 — Timed retake (2026-10-14) — Wrong Answer Review (9 questions)

Source: `td1_retake_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td1_retake_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q53](#q53) | ☐ | ☐ | ☐ |
| A | [Q70](#q70) | ☐ | ☐ | ☐ |
| A | [Q10](#q10) | ☐ | ☐ | ☐ |
| A | [Q39](#q39) | ☐ | ☐ | ☐ |
| B | [Q68](#q68) | ☐ | ☐ | ☐ |
| B | [Q59](#q59) | ☐ | ☐ | ☐ |
| C | [Q22](#q22) | ☐ | ☐ | ☐ |
| D | [Q21](#q21) | ☐ | ☐ | ☐ |
| D | [Q45](#q45) | ☐ | ☐ | ☐ |

---

# Group A — Read what the workload really needs (dynamic vs static, prod vs Spot, root cause) (4)

<a id="q53"></a>

## Q53

A company is migrating an interactive car registration web system hosted on its on-premises network to AWS Cloud. The current architecture of the system consists of a single NGINX web server and a MySQL database running on a Fedora server, which both reside in its on-premises data center. For the new cloud architecture, a load balancer must be used to evenly distribute the incoming traffic to the application servers. Amazon Route 53 must be used for both domain registration and domain management.

In this scenario, what would be the most efficient way to transfer the web application to AWS?

- **A.** 1. Use the AWS Transform MGN to create an EC2 AMI of the NGINX web server. 2. Configure auto-scaling to launch in two Availability Zones. 3. Launch a multi-AZ MySQL Amazon RDS instance in one availability zone only. 4. Import the data into Amazon RDS from the latest MySQL backup. 5. Create an ELB to front your web servers 6. Use Route 53 and create an A record pointing to the elastic load balancer.
- **B.** 1. Use AWS DataSync to transfer the web files from the on-premises NGINX server to an Amazon S3 bucket. 2. Run the website directly out of Amazon S3. 3. Migrate the database using the AWS Database Migration Service and AWS Schema Conversion Tool (AWS SCT). 4. Use Route 53 and create an alias record pointing to the ELB.
- **C.** 1. Launch two NGINX EC2 instances in two Availability Zones. 2. Copy the web files from the on-premises web server to each Amazon EC2 web server, using Amazon S3 as the repository. 3. Migrate the database using the AWS Database Migration Service. 4. Create an ELB to front your web servers. 5. Use Route 53 and create an alias A record pointing to the ELB.
- **D.** 1. Use AWS Transform to automatically migrate the existing NGINX web server from the on-premises Fedora server to AWS. 2. Configure Auto Scaling to launch two web servers in two Availability Zones. 3. Launch a Multi-AZ MySQL Amazon Relational Database Service (RDS) instance in one Availability Zone only. 4. Import the data into Amazon RDS from the latest MySQL backup. 5. Use Route 53 to create a private hosted zone and point a non-alias A record to the ELB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** INTERACTIVE web system, NGINX + MySQL, load balancer required, most efficient

🪤 **Your trap:** 🔁 Same question missed in the 10-14 marathon: S3 only serves static files (can't run NGINX logic), and the option points Route 53 at an ELB it never creates

🧠 **Rule:** Dynamic app + DB → EC2 in 2 AZs + DMS + ELB + Route 53 alias. Reject options with a step that contradicts another step.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises                          AWS (đích)
┌──────────────────────┐             ┌─────────────────────────────────┐
│ NGINX (1 server)     │  ───────►   │ ELB ► NGINX EC2 (AZ-a, AZ-b)    │
│ MySQL (Fedora)       │  ───────►   │ MySQL (qua DMS)                 │
└──────────────────────┘             │ Route 53: alias A ► ELB         │
   Hệ thống INTERACTIVE              └─────────────────────────────────┘
   Bắt buộc: load balancer + Route 53
```

Từ khóa quyết định: **interactive web system (NGINX + MySQL)**, **phải có load balancer**, **Route 53 quản lý domain**. Đáp án đúng: **C**. Anh chọn **B** (DataSync lên S3, chạy website trực tiếp từ S3).

⚠️ Lỗi lặp lại: câu này anh đã sai đúng kiểu này ở drill sớm hơn trong cùng ngày (chọn "DataSync → S3 static site" cho app NGINX + MySQL tương tác). Xem phần Quy tắc nhớ.

#### Đáp án C đúng vì sao

1. Launch **hai NGINX EC2 ở hai AZ** — giữ nguyên web server chạy được logic động, hai AZ cho HA.
2. Copy web files từ on-premises sang từng EC2, dùng **S3 làm repository** (S3 ở đây chỉ là chỗ trung chuyển file, không phải nơi chạy web).
3. Migrate DB bằng **AWS DMS** — nguồn vẫn hoạt động trong lúc migrate nên giảm downtime.
4. **ELB** đứng trước các web server (đúng yêu cầu đề).
5. Route 53 tạo **alias A record** trỏ tới ELB.

Mọi bước khớp nhau, không bước nào mâu thuẫn bước khác.

#### Vì sao B (anh chọn) sai

B trông "hiện đại, ít server" nhưng hỏng ở hai chỗ:

- **S3 không chạy được website động.** Hệ thống là interactive (NGINX + MySQL), TD nói rõ website non-static không host được trên S3. S3 chỉ phục vụ file tĩnh.
- **Tự mâu thuẫn:** bước 4 trỏ Route 53 alias tới "the ELB" nhưng B không hề tạo ELB nào. Với S3 website thì cũng không cần ELB, tức là bước 4 trái với bước 2.

Phụ: DataSync dùng để chuyển dữ liệu, không biến S3 thành web server; AWS SCT dùng khi đổi engine DB, còn MySQL sang MySQL thì đề không cần.

#### Các option còn lại

| Option | Lý do sai |
|---|---|
| **A** | Dùng **A record thường** (không alias) trỏ tới ELB; và "multi-AZ RDS **in one AZ only**" tự mâu thuẫn vì Multi-AZ phải dùng nhiều AZ. AWS Transform MGN chủ yếu để migrate VM. |
| **D** | Cũng "Multi-AZ ... one AZ only" mâu thuẫn; **private hosted zone + non-alias A record** trỏ tới ELB là sai cho web public. |
| **B** | S3 không host được site động; trỏ tới ELB không tồn tại. |

#### Lưu ý thực tế

- Quy ước TD cho Route 53: ELB, CloudFront, S3 → **A record + Alias**; EC2 → A record không alias; RDS → CNAME không alias.
- Alias record dùng được cho cả root domain (apex) lẫn subdomain; CNAME chỉ dùng cho subdomain.

#### Quy tắc nhớ cho thi

- **Thấy "interactive / dynamic app + DB"** → **EC2 (2 AZ) + DMS + ELB + Route 53 alias**; KHÔNG chọn "chạy từ S3".
- **Thấy S3 static website** → chỉ khi đề nói rõ nội dung tĩnh.
- **Thấy "Multi-AZ ... one AZ only"** → tự mâu thuẫn, loại ngay.
- **Thấy "đề yêu cầu ELB" mà option không tạo ELB** → loại.
- **Thấy ELB + Route 53** → **alias A record**.
- Mẹo nhớ lỗi lặp: "App có logic server-side thì S3 không chạy được".

### TD explanation

This is a trick question that contains a lot of information to confuse you, especially if you don’t know the fundamental concepts of AWS. All options seem to be correct except for their last steps in setting up Route 53. The options that have a step to launch a multi-AZ MySQL Amazon RDS instance in one availability zone only are wrong since a Multi-AZ deployment configuration uses multiple Availability Zones.

To route domain traffic to an ELB load balancer, use Amazon Route 53 to create an alias record that points to your load balancer. An alias record is a Route 53 extension to DNS. It’s similar to a CNAME record, but you can create an alias record both for the root domain, such as example.com, and for subdomains, such as www.example.com. (You can create CNAME records only for subdomains). For EC2 instances, always use a Type A Record without an Alias. For ELB, Cloudfront, and S3, always use a Type A Record with an Alias, and finally, for RDS, always use the CNAME Record with no Alias.

AWS Database Migration Service helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. The AWS Database Migration Service can migrate your data to and from the most widely used commercial and open-source databases.

Hence, the correct answer is:

1. Launch two NGINX EC2 instances in two Availability Zones.

2. Copy the web files from the on-premises web server to each Amazon EC2 web server, using Amazon S3 as the repository.

3. Migrate the database using the AWS Database Migration Service.

4. Create an ELB to front your web servers.

5. Use Route 53 and create an alias A record pointing to the ELB.

 

The following sets of options are incorrect because they are just using an A record without an Alias:

1. Use the AWS Transform MGN to create an EC2 AMI of the NGINX web server.

2. Configure auto-scaling to launch in two Availability Zones.

3. Launch a multi-AZ MySQL Amazon RDS instance in one availability zone only.

4. Import the data into Amazon RDS from the latest MySQL backup.

5. Create an ELB to front your web servers.

6. Use Route 53 and create an A record pointing to the elastic load balancer.

—

1. Use AWS Transform to automatically migrate the existing NGINX web server from the on-premises Fedora server to AWS.

2. Configure Auto Scaling to launch two web servers in two Availability Zones.

3. Launch a Multi-AZ MySQL Amazon Relational Database Service (RDS) instance in one Availability Zone only.

4. Import the data into Amazon RDS from the latest MySQL backup.

5. Use Route 53 to create a private hosted zone and point a non-alias A record to the ELB.

Take note as well that the AWS Transform MGN is primarily used to migrate virtual machines only, which can be from VMware vSphere and Windows Hyper-V to your AWS cloud.

The following option is incorrect because the web system that is being migrated is a non-static (dynamic) website, which cannot be hosted in S3:

1. Use AWS DataSync to transfer the web files from the on-premises NGINX server to an Amazon S3 bucket.

2. Run the website directly out of Amazon S3.

3. Migrate the database using the AWS Database Migration Service and AWS Schema Conversion Tool (AWS SCT).

4. Use Route 53 and create an alias record pointing to the ELB.

 

References:

https://aws.amazon.com/cloud-migration/

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.html

 

Check out these Amazon Route 53 and AWS Database Migration Service Cheat Sheets:

https://tutorialsdojo.com/amazon-route-53/

https://tutorialsdojo.com/aws-database-migration-service/

</details>

<a id="q70"></a>

## Q70

A tech company plans to host a website using an Amazon S3 bucket. The solutions architect created a new S3 bucket called “www.tutorialsdojo.com” in us-west-2 AWS region, enabled static website hosting, and uploaded the static web content files including the index.html file. The custom domain www.tutorialsdojo.com has been registered using Amazon Route 53 to be associated with the S3 bucket. The next day, a new Route 53 Alias record set was created which points to the S3 website endpoint: http://www.tutorialsdojo.com.s3-website-us-west-2.amazonaws.com. Upon testing, users cannot see any content on the bucket. Both the domains tutorialsdojo.com and www.tutorialsdojo.com do not work properly.

Which of the following is the MOST likely cause of this issue that the Architect should fix?

- **A.** The site will not work because the URL does not include a file name at the end. This means that you need to use this URL instead: www.tutorialsdojo.com/index.html
- **B.** The S3 bucket does not have public read access which blocks the website visitors from seeing the content.
- **C.** The site does not work because you have not set a value for the error.html file, which is a required step.
- **D.** Route 53 is still propagating the domain name changes. Wait for another 12 hours and then try again.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** S3 static website, alias record created, users see no content

🪤 **Your trap:** 'Wait 12 hours for propagation' — Route 53 propagates in ~60 s; waiting is never the fix

🧠 **Rule:** S3 website returns nothing → bucket policy must allow public s3:GetObject (and Block Public Access off). Fix the real cause, never 'just wait'.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
User ──► Route 53 (alias A) ──► S3 website endpoint
                                 bucket: www.tutorialsdojo.com (us-west-2)
                                 static website hosting: bật
                                 index.html: đã upload
Triệu chứng: người dùng KHÔNG thấy nội dung
```

Hỏi: nguyên nhân **MOST likely**. Đáp án đúng: **B** (bucket không có public read access). Anh chọn **D** (Route 53 còn đang propagate, chờ 12 giờ).

#### Đáp án B đúng vì sao

Mọi bước DNS/hosting trong đề đã làm đúng:

- Tên bucket **trùng khớp** tên record (`www.tutorialsdojo.com`) — yêu cầu của S3 website + Route 53 alias.
- Static website hosting đã bật, `index.html` đã upload, alias trỏ đúng S3 website endpoint.

Thứ duy nhất đề không nhắc là **quyền đọc công khai**. TD: bucket host website phải có **public read access**, và việc mọi người trên thế giới đọc được là chủ ý. Không có quyền này thì visitor bị chặn.

#### Vì sao D (anh chọn) sai

D nghe hợp lý vì record alias mới được tạo. Nhưng:

- Route 53 được thiết kế propagate thay đổi tới mạng authoritative DNS toàn cầu trong khoảng **60 giây** trong điều kiện bình thường. "Chờ 12 giờ" là sai về số liệu.
- Cấu hình DNS/alias/tên bucket đã đúng hết; phần còn thiếu là quyền đọc của bucket, nên chờ thêm không đổi được kết quả.

#### Các option còn lại

- **A (phải gõ /index.html):** sai. Không cần thêm tên file; index document tự được phục vụ.
- **C (phải set error.html):** sai. `error.html` không bắt buộc và không ảnh hưởng việc site có truy cập được hay không.

#### Lưu ý thực tế (đề không hỏi nhưng dễ vấp)

- Thực tế cần **tắt Block Public Access** ở mức bucket (và account nếu bị bật) thì bucket policy cho phép public `s3:GetObject` mới có hiệu lực.
- Thấy lỗi 403 từ S3 website endpoint → nghĩ tới permission trước DNS.

#### Quy tắc nhớ cho thi

- **Thấy "S3 website trả về không có nội dung / 403"** → **public read (bucket policy GetObject + Block Public Access tắt)**.
- **Thấy "chờ N giờ propagate"** → gần như luôn sai; Route 53 ~ **60 giây**. Sửa nguyên nhân thật, đừng "just wait".
- **Thấy "tên bucket = tên record"** → đã đúng, không phải lỗi.
- **error.html** → tùy chọn, không phải nguyên nhân.

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

<a id="q10"></a>

## Q10

A company is hosting its flagship product page on a three-tier web application in its on-premises data center. The popularity of the last product launch attracted a sudden surge of traffic to its site, which caused some downtime that resulted in a significant impact on the product’s sales volume. The management decided to move the application to AWS. The application uses a MySQL database and is written in the .NET Framework. The team used the AWS Application Discovery Service Agentless Collector to inventory the existing application and its database dependencies. The Solutions Architect must design a highly available and scalable infrastructure to handle the demand of 300,000 peak users.

Which of the following design options would satisfy the above requirements while being cost-effective?

- **A.** Create an AWS Elastic Beanstalk application with an Auto Scaling group of Amazon EC2 instances as web servers that spans two separate regions. Put the EC2 instances behind an Application Load Balancer in each region. Launch a Multi-AZ Amazon Aurora MySQL database with a cross-region read replica to the other region. Create zone entries in Amazon Route 53 with a geoproximity routing policy to direct the traffic between the two regions.
- **B.** Create an AWS Elastic Beanstalk application that contains a web server tier and an Amazon RDS MySQL Multi-AZ database tier. The web server tier should launch a fleet of Amazon EC2 Auto Scaling Groups spanning multiple Availability Zones and behind a Network Load Balancer. Create an Amazon Route 53 zone entry for the company’s domain name with an Alias record pointed to the NLB.
- **C.** Launch an AWS CloudFormation stack that contains an Amazon ECS cluster that spans multiple Availability Zones using Spot Instances. Create an Application Load Balancer in front of the ECS cluster. Use the stack to launch an Amazon RDS MySQL database in a Multi-AZ configuration with a “snapshot” deletion policy. Create an Amazon Route 53 zone entry for the company’s domain name with an Alias record pointed to the ALB.
- **D.** Launch an AWS CloudFormation stack that contains an Auto Scaling Group of Amazon EC2 instances spanning multiple Availability Zones that are behind an Application Load Balancer. Use the stack to launch an Amazon Aurora MySQL database cluster in a Multi-AZ configuration with a “retain” deletion policy. Create an Amazon Route 53 zone entry for the company’s domain name with an Alias record pointed to the ALB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** flagship product page, highly available, 300,000 peak users, cost-effective

🪤 **Your trap:** Spot Instances can be reclaimed — not for the always-on production web tier

🧠 **Rule:** Production HA web tier → ASG of On-Demand EC2 behind ALB + Aurora Multi-AZ (retain on delete). Spot only for interruptible work.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem 3-tier (.NET + MySQL)  ──►  AWS
  Sự cố: traffic tăng đột biến => downtime => mất doanh thu
  Yêu cầu: HA + scalable cho 300,000 peak users + COST-EFFECTIVE
```

Đáp án đúng: **D** (CloudFormation: ASG EC2 multi-AZ sau **ALB** + **Aurora MySQL Multi-AZ** với **Retain** + Route 53 alias tới ALB). Anh chọn **C** (ECS dùng **Spot Instances** + RDS MySQL Multi-AZ với "snapshot" deletion policy).

#### Đáp án D đúng vì sao

- **ASG nhiều AZ** sau **ALB**: scale theo tải, một AZ chết vẫn sống. ALB làm việc ở tầng ứng dụng (HTTP/HTTPS) và hỗ trợ path-based routing — hợp với web app.
- **Aurora Multi-AZ cluster**: lớp DB HA.
- **DeletionPolicy = Retain**: xóa stack thì DB vẫn còn, dựng lại stack mới có thể dùng luôn DB cũ, rất nhanh.
- **Route 53 alias** tới ALB.
- Không thừa: một Region, nhiều AZ là đủ -> hợp "cost-effective".

#### Vì sao C (anh chọn) sai

C có ALB, Multi-AZ, alias đều đúng, nhưng hỏng ở hai chỗ TD nêu:

- **Spot Instances cho web tier:** AWS có thể thu hồi Spot theo cung/cầu năng lực. Spot tiết kiệm tiền nhưng **độ tin cậy của site giảm** — không hợp trang flagship chịu 300,000 peak users vừa từng downtime.
- **"snapshot" deletion policy:** nếu xóa stack thì phải **restore từ snapshot, mất nhiều thời gian**, thua Retain.

#### Các option còn lại

- **A:** hai Region (ASG mỗi Region, ALB mỗi Region, Aurora cross-region read replica, geoproximity). **Không cần thiết và đắt**; multi-AZ trong một Region là đủ. Replica ở Region thứ hai chỉ đọc nên mọi ghi vẫn phải về Region chính.
- **B:** dùng **NLB** (Layer 4, TCP) cho web app HTTP/HTTPS; NLB không route theo HTTP attributes (query string, header, cookie) như ALB.

| Option | Điểm chết |
|---|---|
| A | Multi-region thừa, đắt, replica chỉ đọc |
| B | NLB (L4) thay vì ALB (L7) |
| C | Spot cho web tier + snapshot restore chậm |
| **D** | Không có |

#### Lưu ý thực tế

- "Cost-effective" không đồng nghĩa "rẻ nhất": với production tier luôn bật, On-Demand (hoặc giảm giá cam kết) hợp lý hơn Spot.
- Spot hợp với công việc **chịu gián đoạn** (batch, xử lý nền).

#### Quy tắc nhớ cho thi

- **Thấy "web tier production HA"** → **ASG On-Demand multi-AZ + ALB**; Spot là bẫy.
- **Thấy "HTTP/HTTPS, path-based routing"** → **ALB**, không phải NLB.
- **Thấy "CloudFormation + database"** → **DeletionPolicy Retain** để giữ DB khi xóa stack (snapshot chỉ là phương án restore chậm).
- **Thấy "multi-region" mà đề chỉ cần HA + cost-effective** → thừa, multi-AZ đủ.

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

<a id="q39"></a>

## Q39

A company needs a deployment solution for its application that is hosted on the AWS cloud. The company has the following requirements for the application: 

– The instances must have 500GB worth of static dataset that is accessible for the application upon boot up.

– The instances must be able to scale-out or scale-in depending on the traffic load of the application.

– The Development team must have a quick and automated way to deploy their code updates several times during the day.

– Security patches for the vulnerabilities on the operating system (OS) must be installed within 48 hours of release.

Which of the following solutions should the Solutions Architect implement to meet the company requirements while being cost-effective?

- **A.** Install OS patches and create a new AMI using AWS Systems Manager. Use this new AMI for the Auto Scaling group of EC2 instances and replace the existing instances. Deploy the new version of the application to the instances using AWS CodeDeploy. Mount an Amazon EFS volume containing the static dataset on the instances upon boot up.
- **B.** Install OS patches and create a new AMI using AWS Systems Manager. Use this new AMI for the Auto Scaling group of EC2 instances and replace the existing instances. Create a scheduled batch job that will run every night to deploy the new application version and install the OS patches. Mount an Amazon EFS volume containing the static dataset on the instances upon boot up.
- **C.** Create an Auto Scaling group of EC2 instances using the Amazon Linux AMI. Install the application on the EC2 instances. Replace the existing instances as soon as AWS releases a new Amazon Linux AMI version. Write a user data script that will download the 500 GB static dataset from an Amazon S3 bucket. Deploy the new version of the application to the instances using AWS CodeDeploy.
- **D.** Create an Auto Scaling group of EC2 instances using the Amazon Linux AMI. Install the application on the EC2 instances. Write a user data script that will download the 500 GB static dataset from an Amazon S3 bucket. Use AWS Systems Manager to install the OS patches as soon as they are released. Deploy the new version of the application to the instances using AWS CodeDeploy.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** 500 GB static dataset at boot, scale in/out, deploy code several times a day, patch within 48 h

🪤 **Your trap:** User data downloading 500 GB from S3 on every launch makes scale-out slow; patching live instances drifts from the AMI

🧠 **Rule:** Patch → bake new AMI (SSM) → replace instances; shared static data → mount EFS; app updates → CodeDeploy.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
┌───────────────────────── Yêu cầu ─────────────────────────┐
│ 1. 500 GB static dataset dùng được ngay lúc boot           │
│ 2. Scale-out / scale-in theo tải                           │
│ 3. Deploy code NHIỀU LẦN TRONG NGÀY, nhanh + tự động       │
│ 4. Vá lỗ hổng OS trong 48 giờ kể từ khi release            │
│ 5. Cost-effective                                          │
└────────────────────────────────────────────────────────────┘
```

Đáp án đúng: **A** = patched AMI (Systems Manager) + replace instances + **CodeDeploy** + mount **Amazon EFS** chứa dataset. Anh chọn **D** (user data tải 500 GB từ S3 + patch bằng Systems Manager trên instance đang chạy).

#### Đáp án A đúng: mỗi yêu cầu một công cụ

| Yêu cầu | Giải pháp trong A |
|---|---|
| Patch OS trong 48 h | **Systems Manager** cài patch và tạo **AMI mới**, dùng AMI này cho ASG rồi **thay instance cũ** |
| Deploy nhiều lần/ngày | **AWS CodeDeploy** |
| 500 GB dữ liệu tĩnh | **Amazon EFS** mount lúc boot; một file system dùng chung cho mọi instance |
| Scale in/out | **Auto Scaling group** |

EFS là NFS file system managed, mount được trên mọi EC2 Linux qua NFSv4.1, trả tiền theo dung lượng dùng, không phí tối thiểu.

#### Vì sao D (anh chọn) sai

D có CodeDeploy và Systems Manager nhưng phần dataset tính toán sai:

- User data tải 500 GB từ S3 khiến **mỗi instance mới đều phải tải** về **EBS cục bộ**.
- Gắn volume 500 GB cho từng instance **đắt hơn** việc dùng **một EFS** mount cho tất cả.
- Tải 500 GB mỗi lần launch làm scale-out chậm (instance chưa sẵn sàng khi traffic đang tăng).
- Patch trực tiếp trên instance đang chạy không đổi AMI gốc, nên instance mới launch từ AMI cũ lại thiếu patch (drift) trừ khi có thêm bước vá.

S3 rẻ hơn EFS khi chỉ tính lưu trữ, nhưng TD kết luận tổng chi phí của cách tải về từng instance cao hơn.

#### Các option còn lại

- **B:** đúng phần AMI + EFS, nhưng deploy app bằng **scheduled batch job mỗi đêm**. Dev cần deploy nhiều lần trong ngày nên batch hằng đêm không đáp ứng.
- **C:** thay instance khi AWS ra **Amazon Linux AMI mới**. Mỗi phiên bản mới thường mất **vài tuần đến vài tháng**, không bảo đảm vá trong 48 giờ. Cũng tải 500 GB từ S3 như D.

#### Lưu ý thực tế

- Patch Manager dùng **patch baseline** (rule tự duyệt patch sau N ngày) và có thể chạy bằng **maintenance window**; **Automation runbook** dùng để tạo AMI.
- EFS có hai storage class: Standard và Infrequent Access (IA, rẻ hơn cho file ít truy cập).

#### Quy tắc nhớ cho thi

- **Thấy "patch OS trong X giờ/ngày + ASG"** → **bake AMI mới (SSM Automation) rồi thay instance**.
- **Thấy "dữ liệu tĩnh lớn, mọi instance cần lúc boot"** → **EFS mount**, không tải từ S3 mỗi lần launch.
- **Thấy "deploy nhiều lần/ngày"** → **CodeDeploy**; batch job hằng đêm là sai.
- **Thấy "chờ AMI mới của AWS"** → không bảo đảm deadline.

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

---

# Group B — Edge & DNS (CloudFront geo-restriction, Global Accelerator + public alias) (2)

<a id="q68"></a>

## Q68

A global financial company is launching its new trading platform in AWS which allows people to buy and sell their bitcoin, ethereum, ripple, and other cryptocurrencies, as well as access to various financial reports. To meet the anti-money laundering and counter-terrorist financing (AML/CFT) measures compliance, all report files of the trading platform must not be accessible in certain countries which are listed in the Financial Action Task Force (FATF) list of non-cooperative countries or territories. You were given a task to ensure that the company complies with this requirement to avoid hefty monetary penalties.

In this scenario, what is the best way to satisfy this security requirement in AWS while still delivering content to users around the globe with lower latency?

- **A.** Create a CloudFront distribution with Geo-Restriction enabled to block all of the blacklisted countries from accessing the trading platform.
- **B.** Use Route 53 with a Geoproximity routing policy that blocks all traffic from the blacklisted countries.
- **C.** Deploy the trading platform using Elastic Beanstalk and deny all incoming traffic from the IP addresses of the blacklisted countries in the Network Access Control List (ACL) of the VPC.
- **D.** Use Route 53 with a Geolocation routing policy that blocks all traffic from the blacklisted countries.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** report files must NOT be accessible in listed countries, global low latency

🪤 **Your trap:** 🔁 Route 53 geolocation only ROUTES by location — it does not block (same miss as the 10-13 Pair drill)

🧠 **Rule:** Block countries → CloudFront geo restriction (or WAF geo match). Route 53 geolocation = routing, not access control.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
User (nước trong danh sách FATF) ─X─► report files
User (nước khác, toàn cầu)       ───► report files (latency thấp)

Yêu cầu: CHẶN truy cập theo quốc gia + giữ latency thấp toàn cầu
```

Đáp án đúng: **A** (CloudFront distribution + Geo-Restriction chặn các nước bị cấm). Anh chọn **D** (Route 53 Geolocation routing "block").

⚠️ Lỗi lặp lại: hôm trước ở pair drill anh đã sai đúng điểm này (Route 53 geolocation không chặn).

#### Đáp án A đúng vì sao

- CloudFront mặc định phục vụ nội dung bất kể vị trí user. **Geo restriction** cho phép: **whitelist** (chỉ nước được duyệt) hoặc **blacklist** (cấm nước trong danh sách). Đề cần blacklist.
- Chặn ở mức **cả distribution, theo quốc gia** — đúng nhu cầu "report files không truy cập được ở các nước FATF".
- CloudFront còn cho user khắp thế giới **truy cập file với latency thấp** — đáp ứng vế thứ hai của đề.
- Cần chặn mịn hơn mức quốc gia hoặc chỉ một phần file thì dùng dịch vụ geolocation bên thứ ba (TD nêu).

#### Vì sao D (anh chọn) sai

Route 53 chỉ là **DNS**: trả về bản ghi dựa trên cấu hình. Geolocation routing = **định tuyến** theo vị trí user (ví dụ user nước X trả về endpoint Y), chứ không phải "access control". Không có tùy chọn "block" thật sự trả về lỗi từ chối.

Hơn nữa Route 53 không cung cấp **low-latency delivery** như CloudFront, mà đề đòi cả hai.

Bẫy lặp lại: tên policy "geo..." gợi liên tưởng "chặn theo địa lý", nhưng thực chất chỉ là routing.

#### Các option còn lại

- **B (Route 53 Geoproximity "block"):** geoproximity định tuyến dựa trên vị trí **resource** và có thể dịch chuyển traffic giữa vị trí (bias); cũng không chặn. Không giúp latency.
- **C (Elastic Beanstalk + NACL chặn IP từng nước):** làm được nhưng **tốn công** và không được khuyến nghị; CloudFront geo restriction tốt hơn.

| Option | Cơ chế | Chặn theo nước? | Latency toàn cầu? |
|---|---|---|---|
| **A. CloudFront geo restriction** | Whitelist / blacklist theo nước | Có | Có |
| B. Route 53 geoproximity | Định tuyến theo vị trí resource | Không | Không |
| C. NACL chặn IP | Danh sách IP thủ công | Có nhưng cực nhọc | Không |
| D. Route 53 geolocation | Định tuyến theo vị trí user | Không | Không |

#### Lưu ý thực tế

- Cần luật linh hoạt hơn (kết hợp điều kiện khác) thì **AWS WAF geo match** là lựa chọn khác; trong đề này CloudFront geo restriction là đáp án.

#### Quy tắc nhớ cho thi

- **Thấy "block / không cho truy cập theo quốc gia"** → **CloudFront geo restriction** (hoặc WAF geo match).
- **Thấy Route 53 geolocation / geoproximity** → chỉ là **routing**, KHÔNG phải chặn.
- **Thấy "chặn + latency thấp toàn cầu"** → CloudFront giải quyết cả hai.
- Mẹo nhớ lỗi lặp: "Route 53 chỉ chỉ đường, không gác cổng".

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

<a id="q59"></a>

## Q59

A multinational financial firm plans to do a multi-regional deployment of its cryptocurrency trading application that’s being heavily used in the US and in Europe. The containerized application uses Kubernetes and has Amazon DynamoDB Global Tables as a centralized database to store and sync the data from two regions.

The architecture has distributed computing resources with several public-facing Application Load Balancers (ALBs). The Network team of the firm manages the public DNS internally and wishes to make the application available through an apex domain for easier access. S3 Multi-Region Access Points are also used for object storage workloads and hosting static assets.

Which is the MOST operationally efficient solution that the Solutions Architect should implement to meet the above requirements?

- **A.** Set up an AWS Global Accelerator, which has several endpoint groups that target specific endpoints and ALBs on the required AWS Regions. Create a public alias record in Amazon Route 53 that points your custom domain name to the DNS name assigned to your accelerator.
- **B.** Set up an AWS Transit Gateway with a multicast domain that targets specific ALBs on the required AWS Regions. Create a public record in Amazon Route 53 using the static IP address of the AWS Transit Gateway.
- **C.** Launch an AWS Global Accelerator with several endpoint groups that target the ALBs in all the relevant AWS Regions. Create an Amazon Route 53 Resolver Inbound Endpoint that points your custom domain name to the CNAME assigned to your accelerator.
- **D.** Launch an AWS Transit Gateway that targets specific ALBs on the required AWS Regions. Create a CNAME record in Amazon Route 53 that directly points your custom domain name to the DNS name assigned to the AWS Transit Gateway.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** multi-Region ALBs, apex domain, public DNS, most operationally efficient

🪤 **Your trap:** Twin options: Resolver INBOUND endpoint is for on-prem → AWS private DNS queries, not public records

🧠 **Rule:** Global Accelerator in front of regional ALBs + Route 53 public ALIAS record (apex OK) to the accelerator DNS name.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
        Client (US / EU)
              │
   example.com (APEX domain, public DNS)
              │  Route 53 public ALIAS ?
              ▼
     AWS Global Accelerator (standard)
      ┌───────┴────────┐
 endpoint group     endpoint group
   Region US          Region EU
   ALB(s)             ALB(s)
```

Yêu cầu: nhiều ALB public ở nhiều Region, dùng **apex domain**, DNS public, **MOST operationally efficient**. Đáp án đúng: **A**. Anh chọn **C**.

#### Đây là bẫy "twin options"

A và C giống nhau ở phần Global Accelerator (nhiều endpoint group tới ALB). Chỉ khác ở bước DNS:

| | A | C |
|---|---|---|
| Bước DNS | **Public alias record** trong Route 53 trỏ tới DNS name của accelerator | **Route 53 Resolver Inbound Endpoint** "trỏ" domain tới CNAME của accelerator |

Khi hai option giống hệt nhau trừ một thành phần, chỉ cần kiểm tra thành phần đó có đúng vai trò không.

#### Đáp án A đúng vì sao

- **Global Accelerator (standard)** hướng traffic qua mạng toàn cầu của AWS tới endpoint tối ưu theo health, vị trí client và policy. Endpoint có thể là NLB, ALB, EC2, Elastic IP ở một hoặc nhiều Region. Nhiều endpoint group tới nhiều ALB là đúng cách dùng.
- Với Route 53 làm DNS, tạo **alias record** trỏ domain tới **DNS name của accelerator**. Alias dùng được cho cả **root/apex domain** (ví dụ example.com) lẫn subdomain — khớp "apex domain".

#### Vì sao C (anh chọn) sai

Phần Global Accelerator của C hợp lệ. Hỏng ở **Resolver Inbound Endpoint**:

- Inbound endpoint chỉ cho phép **DNS query từ mạng on-premises (hoặc VPC khác) vào VPC**. Nó phục vụ giải quyết tên miền **private**, không dùng để publish bản ghi public cho Internet.
- Nó không "trỏ domain tới CNAME" nào cả; vai trò đó là của **record** trong hosted zone.
- Đề nói rõ "public DNS" và "apex": cần public alias record. CNAME cũng không dùng được ở apex.

#### Các option còn lại

- **B (Transit Gateway + multicast domain):** Transit Gateway không dùng để phân phối traffic tới nhiều ALB; multicast domain là để gửi một luồng dữ liệu tới nhiều máy nhận, và hoạt động giữa các subnet của VPC, không phải ALB. Cũng không có "static IP của TGW" để đặt public record.
- **D (Transit Gateway + CNAME):** TGW cũng không tích hợp được các ALB; thêm nữa **CNAME không dùng được cho apex domain** trong Route 53, phải dùng alias.

#### Lưu ý thực tế

- Custom routing accelerator chỉ hỗ trợ endpoint là subnet VPC (private IP), khác standard accelerator. Đề này cần standard.
- Có thể thay vì alias, tạo record dùng static IP của accelerator, nhưng alias tới DNS name là cách đề chọn.

#### Quy tắc nhớ cho thi

- **Thấy "nhiều ALB nhiều Region + một điểm vào"** → **Global Accelerator** với endpoint groups.
- **Thấy "apex domain"** → **alias record**, không dùng CNAME.
- **Thấy "Resolver Inbound Endpoint"** → on-prem/VPC khác hỏi DNS vào VPC, KHÔNG phải public DNS.
- **Thấy "Transit Gateway" trong câu hỏi cân bằng tải ALB** → loại.
- Mẹo twin options: so sánh hai option giống nhau, soi đúng phần khác biệt.

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

---

# Group C — Hybrid networking (dedicated private links = Direct Connect) (1)

<a id="q22"></a>

## Q22

A government agency has multiple VPCs in various AWS regions across the United States that need to be linked up to an on-premises central office network in Washington, D.C. The central office requires inter-region VPC access over a private network that is dedicated to each region for enhanced security and more predictable data transfer performance. Your team is tasked to quickly build this network mesh and to minimize the management overhead to maintain these connections.

Which of the following options is the most secure, highly available, and durable solution that you should use to set up this kind of interconnectivity?

- **A.** Create a link aggregation group (LAG) in the central office network to aggregate multiple connections at a single AWS Direct Connect endpoint in order to treat them as a single, managed connection. Use AWS Direct Connect Gateway to achieve inter-region VPC access to all of your AWS resources. Create a virtual private gateway in each VPC and then create a public virtual interface for each AWS Direct Connect connection to the Direct Connect Gateway.
- **B.** Implement a hub-and-spoke network topology in each region that routes all traffic through a network transit center using AWS Transit Gateway. Route traffic between VPCs and the on-premise network over AWS Site-to-Site VPN.
- **C.** Enable inter-region VPC peering which allows peering relationships to be established between VPCs across different AWS regions. This will ensure that the traffic will always stay on the global AWS backbone and will never traverse the public Internet.
- **D.** Utilize AWS Direct Connect Gateway for inter-region VPC access. Create a virtual private gateway in each VPC, then create a private virtual interface for each AWS Direct Connect connection to the Direct Connect gateway.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** many VPCs in many Regions ↔ on-prem, private DEDICATED network, predictable performance

🪤 **Your trap:** 🔁 Site-to-Site VPN runs over the internet — not dedicated (same miss as the 10-13 Pair drill)

🧠 **Rule:** Dedicated private connectivity to many VPCs/Regions → Direct Connect + DX Gateway + private VIF (VGW per VPC).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Washington D.C. (on-prem)                 AWS (nhiều Region US)
┌──────────────────┐   dedicated link   ┌─────────────────────┐
│ Central office   │ ═════════════════► │ VPC (Region 1) VGW  │
│ network          │ ═════════════════► │ VPC (Region 2) VGW  │
└──────────────────┘                    │ VPC (Region N) VGW  │
                                        └─────────────────────┘
 Yêu cầu: private network DEDICATED, hiệu năng dễ đoán,
          dựng nhanh, ÍT management overhead
```

Đáp án đúng: **D (Direct Connect Gateway + private VIF + VGW mỗi VPC)**. Anh chọn B (Transit Gateway + Site-to-Site VPN).

⚠️ Lỗi lặp lại: cùng nhầm "VPN vs Direct Connect Gateway" như ở pair drill 10-13. Đề nói "dedicated" + "predictable performance" thì VPN loại ngay.

#### D đúng — Direct Connect Gateway

```
On-prem ══ DX connection ══ private VIF ══► Direct Connect Gateway
                                                 │
                         ┌───────────────────────┼───────────────────────┐
                       VGW (VPC R1)           VGW (VPC R2)           VGW (VPC Rn)
```

- **Direct Connect** = kết nối vật lý dedicated từ on-prem tới AWS: privacy cao hơn, thêm bandwidth, hiệu năng dễ đoán hơn. Khớp đúng "private network dedicated" + "predictable data transfer performance".
- **Direct Connect Gateway** nối một DX connection (qua private VIF) tới nhiều VPC ở cùng hoặc khác Region. Mỗi VPC cần một **virtual private gateway (VGW)** associate với DX Gateway.
- Giảm overhead: không cần thiết lập nhiều BGP session cho từng VPC, giảm tải quản trị và tải lên thiết bị mạng.

#### Anh chọn B — vì sao sai

B trông hợp lý vì "hub-and-spoke + Transit Gateway" nghe giống mesh nhiều VPC, và có "private" ở on-prem. Nhưng **Site-to-Site VPN chạy trên Internet**, không phải đường dedicated. Đề yêu cầu dedicated network và hiệu năng dễ đoán, TD nói rõ chỉ dùng Transit Gateway không đáp ứng các điều kiện đó. B hợp với khách muốn tận dụng kết nối HA tự động do AWS cung cấp và tối ưu đầu tư license VPN của hãng thứ ba, không phải bài này.

#### Các option còn lại

- **A sai:** dùng **public** VIF. Chỉ cần **private** VIF vì chỉ kết nối tới tài nguyên bên trong VPC. LAG cũng không liên quan: nó chỉ gộp nhiều connection tại một DX endpoint thành một connection logic (LACP), không giải quyết bài toán multi-Region.
- **C sai:** inter-region VPC peering chạy trên AWS backbone nhưng phải setup và quản lý thủ công nhiều (overhead cao hơn DX Gateway), và kết nối không dedicated, không highly available. Peering cũng chỉ nối VPC với VPC, không phải đường on-prem.

| Option | Dedicated? | Private VIF/Overhead | Kết luận |
|---|---|---|---|
| **D. DX Gateway + private VIF** | Có | Thấp, ít BGP session | Đúng |
| A. DX Gateway + public VIF | Có | Sai loại VIF | Sai |
| B. TGW + Site-to-Site VPN | Không (qua Internet) | Không đáp ứng yêu cầu | Sai |
| C. Inter-region peering | Không | Setup thủ công nhiều | Sai |

#### Quy tắc nhớ cho thi

- **Thấy "dedicated private" + "predictable performance"** → **Direct Connect**, không phải VPN
- **Thấy "nhiều VPC / nhiều Region" + Direct Connect** → **DX Gateway + private VIF + VGW mỗi VPC**
- **Thấy "public VIF" khi chỉ truy cập tài nguyên trong VPC** → sai, dùng **private VIF**
- **Thấy "LAG"** → chỉ gộp link tại một endpoint, không liên quan multi-Region
- Mnemonic: **VPN = Internet; DX = dây riêng**

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

# Group D — Governance & app identity (Config vs GuardDuty, Cognito for mobile federation) (2)

<a id="q21"></a>

## Q21

A clinic runs its medical record system using a fleet of Windows-based Amazon EC2 instances with several EBS volumes attached to it. Since the records that they are storing are confidential health files of their patients, it is a requirement that the latest security patches are installed on the EC2 instances. In addition, there should be a system in the cloud architecture that checks all of the EC2 instances if they are using an approved Amazon Machine Image (AMI). The system that will be implemented should not impede developers from launching instances using an unapproved AMI, but you still have to be notified if there are non-compliant EC2 instances in your VPC.

Which of the following should the solutions architect implement to protect and monitor all of your instances as required above? (Select TWO.)

- **A.** Create an IAM policy that will restrict the developers from launching EC2 instances with an unapproved AMI.
- **B.** Set up a patch baseline that defines which patches are approved for installation on your instances using AWS Systems Manager Patch Manager.
- **C.** Set up Amazon GuardDuty that continuously monitors your instances if the latest security patches are installed and if there is an instance that is using an unapproved AMI. Use CloudWatch Alarms to notify you if there are any non-compliant instances running in your VPC.
- **D.** Use AWS Shield Advanced to automatically patch all of your EC2 instances and detect uncompliant EC2 instances which do not use approved AMIs.
- **E.** Use the AWS Config Managed Rule which automatically checks whether your running EC2 instances are using approved AMIs. Set up CloudWatch Alarms to notify you if there are any non-compliant instances running in your VPC.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** B, C

🔑 **Key words:** latest patches, check approved AMIs, must NOT impede developers, notify

🪤 **Your trap:** 🔁 GuardDuty detects threats (malicious activity), not patch level or AMI compliance

🧠 **Rule:** Patching → SSM Patch Manager baseline. Detect non-approved AMI without blocking → AWS Config managed rule approved-amis-by-id + alert.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Windows EC2 fleet (bệnh án bí mật)
   │
   ├── Yêu cầu 1: luôn có patch bảo mật mới nhất
   │
   └── Yêu cầu 2: kiểm tra instance có dùng AMI được duyệt không
                  - KHÔNG chặn developer launch AMI chưa duyệt
                  - nhưng PHẢI được thông báo khi có instance non-compliant
```

Đáp án đúng: **B + E**. Anh chọn B (đúng) và C (sai).

⚠️ Lỗi lặp lại: GuardDuty vs AWS Config đã sai cả ở lần TD1 đầu. GuardDuty là threat detection, không phải compliance.

#### Hai lựa chọn đúng tạo thành MỘT giải pháp

```
Yêu cầu 1 (patch)      → B: SSM Patch Manager + patch baseline
Yêu cầu 2 (AMI audit)  → E: AWS Config managed rule + CloudWatch Alarm
```

- **B:** Patch Manager tự động hóa việc vá cho managed instance (có Windows Server). **Patch baseline** chứa rule auto-approve patch sau N ngày kể từ khi phát hành, cùng danh sách approved/rejected patches. Có thể chạy theo lịch bằng Maintenance Window hoặc chọn nhóm instance qua tag.
- **E:** **AWS Config managed rule** là rule dựng sẵn, không cần viết Lambda (custom rule mới cần). Rule kiểm tra EC2 đang chạy có dùng AMI được duyệt không, chỉ **đánh giá và báo non-compliant**, không chặn launch. Kết hợp CloudWatch Alarm để nhận thông báo. Đúng yêu cầu "không cản developer nhưng phải được báo".

#### Anh chọn C — vì sao sai

C trông đúng vì "continuously monitors" + "notify bằng CloudWatch Alarms". Nhưng **GuardDuty là dịch vụ threat detection**: giám sát hành vi độc hại hoặc trái phép (API call bất thường, triển khai trái phép nghi ngờ account bị xâm nhập). Nó **không kiểm tra instance dùng AMI nào** (và đề nêu rõ nó không check approved AMI). Đây là câu hỏi compliance/config, không phải threat.

#### Các option còn lại

- **A sai:** IAM policy chặn launch AMI chưa duyệt thì có tác dụng ngăn, nhưng **cản developer**, vi phạm yêu cầu của đề.
- **D sai:** **Shield Advanced** để chống DDoS; không tự patch EC2 và không kiểm tra AMI.

| Dịch vụ | Làm gì | Hợp bài này? |
|---|---|---|
| **SSM Patch Manager** | Vá theo patch baseline | Có (B) |
| **AWS Config managed rule** | Đánh giá compliance, báo non-compliant | Có (E) |
| GuardDuty | Threat detection | Không |
| IAM policy | Chặn (preventive) | Không, vì không được cản dev |
| Shield Advanced | Chống DDoS | Không |

#### Quy tắc nhớ cho thi

- **Thấy "patch EC2"** → **SSM Patch Manager + patch baseline**
- **Thấy "approved AMI / compliance, không chặn, chỉ báo"** → **AWS Config managed rule (approved-amis-by-id)** + alarm
- **Thấy "chặn launch"** → IAM/SCP (preventive); **"không impede + notify"** → Config (detective)
- **GuardDuty** = threat (hành vi độc hại), **Config** = compliance (cấu hình), **Shield** = DDoS

### TD explanation

AWS Systems Manager Patch Manager automates the process of patching managed instances with security-related updates. For Linux-based instances, you can also install patches for non-security updates. You can patch fleets of Amazon EC2 instances or your on-premises servers and virtual machines (VMs) by operating system type. This includes supported versions of Windows Server, Ubuntu Server, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), CentOS, Amazon Linux, and Amazon Linux 2. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches. You can install patches on a regular basis by scheduling patching to run as a Systems Manager Maintenance Window task. You can also install patches individually or to large groups of instances by using Amazon EC2 tags. You can add tags to your patch baselines themselves when you create or update them.

AWS Config provides AWS managed rules, which are predefined, customizable rules that AWS Config uses to evaluate whether your AWS resources comply with common best practices. For example, you could use a managed rule to quickly start assessing whether your Amazon Elastic Block Store (Amazon EBS) volumes are encrypted or whether specific tags are applied to your resources. You can set up and activate these rules without writing the code to create an AWS Lambda function, which is required if you want to create custom rules. The AWS Config console guides you through the process of configuring and activating a managed rule. You can also use the AWS Command Line Interface or AWS Config API to pass the JSON code that defines your configuration of a managed rule.

In this scenario, you can use a combination of AWS Config Managed Rules and AWS Systems Manager Patch Manager to meet the requirements.

Therefore, the correct answers are:

– Set up a patch baseline that defines which patches are approved for installation on your instances using AWS Systems Manager Patch Manager.

– Use the AWS Config Managed Rule which automatically checks whether your running EC2 instances are using approved AMIs. Set up CloudWatch Alarms to notify you if there are any non-compliant instances running in your VPC.

The option that says: Creating an IAM policy that will restrict the developers from launching EC2 instances with an unapproved AMI is incorrect. Although you can use an IAM policy to prohibit your developers from launching unapproved AMIs, this will impede their work which violates what the scenario requires. Remember, as per the scenario, the system that you will implement should not impede developers from launching instances using an unapproved AMI.

The option that says: Set up Amazon GuardDuty that continuously monitors your instances if the latest security patches are installed and if there is an instance that is using an unapproved AMI. Use CloudWatch Alarms to notify you if there are any non-compliant instances running in your VPC is incorrect. Amazon GuardDuty is primarily used as a threat detection service that continuously monitors for malicious or unauthorized behavior to help you protect your AWS accounts and workloads. It monitors for activity such as unusual API calls or potentially unauthorized deployments that indicate a possible account compromise however, it does not check if your EC2 instances are using an approved AMI or not.

Using AWS Shield Advanced to automatically patch all of your EC2 instances and detecting uncompliant EC2 instances which do not use approved AMIs is incorrect. The AWS Shield Advanced service is most suitable to prevent DDoS attacks in your AWS resources. It cannot check the specific AMIs that your EC2 instances are using.

 

References:

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html

https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html

https://docs.aws.amazon.com/config/latest/developerguide/approved-amis-by-id.html

 

Check out these cheat sheets on AWS Config and AWS Systems Manager: 

https://tutorialsdojo.com/aws-config/

https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q45"></a>

## Q45

A company uses Lightweight Directory Access Protocol (LDAP) for its employee authentication and authorization. The company plans to release a mobile app that can be installed on employee’s smartphones. The mobile application will allow users to have federated access to AWS resources. Due to strict security and compliance requirements, the mobile application must use a custom-built solution for user authentication. It must also use IAM roles for granting user permissions to AWS resources. The Solutions Architect was tasked to create a solution that meets these requirements.

Which of the following options should the Solutions Architect implement to enable authentication and authorization for the application? (Select TWO.)

- **A.** Build a custom LDAP connector using Amazon API Gateway with AWS Lambda function for user authentication. Use Amazon DynamoDB to store user authorization tokens. Write another Lambda function that will validate user authorization requests based on the token stored on DynamoDB.
- **B.** Build a custom SAML-compatible solution to handle authentication and authorization. Configure the solution to use LDAP for user authentication and use SAML assertion to perform authorization to the IAM identity provider.
- **C.** Build a custom OpenID Connect-compatible solution in combination with AWS IAM Identity Center to create authentication and authorization functionality for the application.
- **D.** Build a custom SAML-compatible solution for user authentication. Leverage AWS IAM Identity Center for authorizing access to AWS resources.
- **E.** Build a custom OpenID Connect-compatible solution for the user authentication functionality. Use Amazon Cognito Identity Pools for authorizing access to AWS resources.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** B, D

🔑 **Key words:** mobile app, custom-built authentication, federated access, IAM roles for permissions

🪤 **Your trap:** IAM Identity Center is for workforce SSO to accounts/business apps, not mobile app federation

🧠 **Rule:** Custom auth for a mobile app → custom SAML IdP + IAM SAML provider, or custom OIDC + Cognito Identity Pools (temp creds via IAM roles).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Nhân viên (LDAP) ──► Mobile app ──► Xác thực CUSTOM ──► IAM roles ──► AWS resources
                                    (bắt buộc tự build)  (temp credentials)
```

Yêu cầu chốt: **mobile app**, xác thực **custom-built**, **federated access**, quyền cấp qua **IAM roles**. Đáp án đúng: **B (custom SAML + LDAP + IAM identity provider)** và **E (custom OIDC + Cognito Identity Pools)**. Anh chọn B (đúng) và D (sai).

Lưu ý: B và E là **hai hướng độc lập, mỗi hướng đủ dùng**. Đề cho chọn 2 nhưng mỗi cái tự đáp ứng được yêu cầu.

#### Hai đáp án đúng

- **B:** Dùng LDAP của công ty để xác thực trong solution custom hỗ trợ SAML. **SAML assertion** gửi tới **IAM identity provider** để lấy quyền; IAM role được cấp cho user truy cập AWS resource. SAML 2.0 là chuẩn mở cho federated SSO mà không cần tạo IAM user cho từng người.
- **E:** Solution custom hỗ trợ **OpenID Connect** lo phần xác thực. **Cognito Identity Pools** cấp **temporary AWS credentials** cho user đã xác thực (đã có token). OIDC provider được cấu hình trong IAM rồi associate với identity pool.

#### Anh chọn D — vì sao sai

D (custom SAML + **IAM Identity Center** để authorize) trông hợp vì có SAML như B. Nhưng đề cần federated access từ **mobile app**; TD nêu **IAM Identity Center chỉ hỗ trợ SSO tới business application qua web browser**. Nó là workforce SSO, không phải cơ chế cấp credential cho app mobile. Phần authorization phải qua **IAM identity provider** (B) hoặc **Cognito Identity Pools** (E).

#### Các option còn lại

- **A sai:** tự build LDAP connector bằng API Gateway + Lambda, lưu token vĩnh viễn trong DynamoDB. TD: không nên lưu authorization token lâu dài trên DynamoDB; token phải sinh khi xác thực và chỉ lưu tạm trong một session length cố định.
- **C sai:** custom OIDC + IAM Identity Center. TD: **IAM Identity Center chỉ hỗ trợ ứng dụng SAML 2.0**, nên giải pháp OIDC không chạy được.

| Option | Authentication | Authorization | Kết luận |
|---|---|---|---|
| **B** | Custom SAML + LDAP | IAM identity provider (SAML assertion) | Đúng |
| **E** | Custom OIDC | Cognito Identity Pools | Đúng |
| D | Custom SAML | IAM Identity Center (chỉ web SSO) | Sai |
| C | Custom OIDC | IAM Identity Center (chỉ SAML) | Sai |
| A | LDAP connector tự build | Token lưu vĩnh viễn ở DynamoDB | Sai |

#### Quy tắc nhớ cho thi

- **Thấy "mobile app" + "federated" + "IAM roles"** → **Cognito Identity Pools** (temp creds) hoặc **SAML + IAM identity provider**
- **Thấy "custom OIDC"** → **Cognito Identity Pools**
- **Thấy "custom SAML + LDAP"** → **IAM SAML identity provider**
- **IAM Identity Center** = workforce SSO (web browser, SAML app), không dùng cho mobile app federation

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
