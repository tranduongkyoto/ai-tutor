# TD Set 5 — Timed retake (2026-10-15) — Wrong Answer Review (9 questions)

Source: `td5_retake_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td5_retake_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q48](#q48) | ☐ | ☐ | ☐ |
| A | [Q17](#q17) | ☐ | ☐ | ☐ |
| A | [Q55](#q55) | ☐ | ☐ | ☐ |
| A | [Q38](#q38) | ☐ | ☐ | ☐ |
| B | [Q22](#q22) | ☐ | ☐ | ☐ |
| B | [Q39](#q39) | ☐ | ☐ | ☐ |
| B | [Q70](#q70) | ☐ | ☐ | ☐ |
| B | [Q44](#q44) | ☐ | ☐ | ☐ |
| C | [Q8](#q8) | ☐ | ☐ | ☐ |

---

# Group A — Hybrid networking & VPC routing (PrivateLink, Direct Connect gateway, prefixes, Lambda in VPC) (4)

<a id="q48"></a>

## Q48

An e-commerce company operates its core infrastructure within a private data center. This infrastructure is linked to AWS through a combination of AWS Direct Connect and a secure IPSec VPN, ensuring that sensitive customer data remains off the public internet. As part of its strategic growth, the company aims to extend its proprietary services to other e-commerce businesses hosted on AWS.

Which networking solution aligns with the company’s requirements?

- **A.** Establish a VPC Endpoint Service for the company’s applications and associate it with a Network Load Balancer that manages TCP traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect.
- **B.** Set up a VPC Endpoint Service for the company’s applications and link it with an Application Load Balancer that handles HTTP or HTTPS traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect.
- **C.** Set up a NAT Gateway in a VPC for the company’s applications and secure it with network access control and security group rules.
- **D.** Use AWS Direct Connect to link the company’s data center to a VPC in AWS. Within the VPC, set up security group rules to manage access to the company’s applications.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** expose services to other AWS customers privately, off the internet

🪤 **Your trap:** 🔁 5th miss — ALB cannot back a VPC endpoint service (twin options differ only NLB vs ALB)

🧠 **Rule:** PrivateLink endpoint service → Network Load Balancer (or GWLB), never ALB.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Data center công ty  ══ Direct Connect / VPN ══►  VPC của công ty
                                                    │
                                          Dịch vụ độc quyền (app)
                                                    │
                                   ??? ──► VPC Endpoint Service
                                                    │  (PrivateLink)
                                                    ▼
                                  VPC của các công ty e-commerce khác
                                  (Interface endpoint, KHÔNG qua internet)
```

Yêu cầu chốt: **chia sẻ dịch vụ cho khách hàng AWS khác**, dữ liệu **không đi qua public internet**. Đáp án đúng: **A (Endpoint Service + Network Load Balancer + Direct Connect)**. Anh chọn B (cùng cấu trúc nhưng dùng ALB).

⚠️ **Lỗi lặp lại (lần miss thứ 5):** hai đáp án A và B giống hệt nhau, chỉ khác **NLB vs ALB**. Đây là một "twin options" cổ điển. Chỉ cần nhớ một câu: **VPC Endpoint Service (PrivateLink) phải đứng sau NLB** (hoặc Gateway Load Balancer), không phải ALB.

#### Vì sao A đúng

- **VPC Endpoint Service** là cách để "xuất bản" dịch vụ của mình cho consumer ở VPC/account khác. Consumer tạo interface endpoint trỏ vào service, traffic đi trong mạng AWS, không ra internet.
- **Network Load Balancer** hoạt động ở layer 4, xử lý TCP, chịu được hàng triệu request/giây, HA và fault tolerance. Nó là front-end bắt buộc của endpoint service.
- **Direct Connect** giữ đường riêng từ data center tới AWS, nên dữ liệu nhạy cảm vẫn không đi qua internet.

#### Anh chọn B: vì sao trông đúng và vì sao sai

B trông đúng vì ALB là load balancer "quen thuộc" cho web app HTTP/HTTPS, và phần còn lại (Endpoint Service + Direct Connect) giống hệt A. Nhưng TD nói rõ: **ALB không thể dùng để tạo VPC Endpoint Service; endpoint service yêu cầu NLB.** Chỉ một từ khác nhau là đủ làm B sai.

#### Các đáp án sai còn lại

- **C (NAT Gateway):** NAT Gateway cho instance trong private subnet đi ra internet/AWS service, không cho ai khác truy cập vào dịch vụ. Còn đi ngược yêu cầu "không qua public internet". NACL/SG chỉ thêm kiểm soát, không tạo kết nối riêng.
- **D (Direct Connect + security group):** Direct Connect chỉ nối data center với VPC của chính công ty. Không có cơ chế để công ty khác trên AWS dùng dịch vụ.

| Đáp án | Cơ chế | Chia sẻ cho AWS customer khác? |
|---|---|---|
| **A. Endpoint Service + NLB** | PrivateLink | Có |
| B. Endpoint Service + ALB | Không hợp lệ (cần NLB) | Không |
| C. NAT Gateway | Outbound cho private subnet | Không |
| D. Direct Connect + SG | Chỉ on-prem tới VPC của mình | Không |

#### Lưu ý thực tế

- Nếu thật sự cần ALB (routing theo path/host) mà vẫn muốn PrivateLink: đặt **NLB phía trước ALB** (ALB làm target của NLB). Trong đề thi, nếu đáp án ghi thẳng "Endpoint Service + ALB" thì vẫn là sai.
- Consumer dùng **interface endpoint** (ENI trong subnet của họ); provider không cần peering hay route giữa hai VPC.

#### Quy tắc nhớ cho thi

- **Thấy "expose service cho AWS customer khác, private, không qua internet"** → **PrivateLink = VPC Endpoint Service**
- **Thấy "VPC Endpoint Service"** → **NLB** (hoặc GWLB cho appliance), **không bao giờ ALB**
- **Hai option giống hệt, chỉ khác NLB/ALB** → chọn **NLB** khi có chữ Endpoint Service
- Mnemonic: **PrivateLink = P**rivate **L**ayer-4 → **NLB** (L4/TCP)

### TD explanation

A VPC Endpoint Service allows the company’s applications to be accessed securely within the AWS network. This is a crucial component in the solution as it enables the company’s services to be exposed to other businesses on AWS without exposing the data to the public internet. This is particularly important given the sensitive nature of the data handled by the company.

The Network Load Balancer operates at the fourth layer of the Open Systems Interconnection (OSI) model and can handle millions of requests per second. By efficiently managing TCP traffic, the Network Load Balancer ensures high availability and fault tolerance of the applications. This is critical for maintaining a high-quality user experience, especially as the company expands its services to other businesses on AWS.

![image](https://media.tutorialsdojo.com/public/secure-networking-solution-050524.png)

AWS Direct Connect provides a dedicated, private link from the company’s data center to AWS. This ensures secure and efficient data transfer, which is vital for the company given the sensitive nature of its data. By maintaining a secure connection between the company’s data center and AWS using Direct Connect, the company can ensure that its sensitive data remains secure while still being able to extend its services to other businesses on AWS.

Hence, the correct answer is: **Establish a VPC Endpoint Service for the company’s applications and associate it with a Network Load Balancer that manages TCP traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect.**

The option that says: **Set up a VPC Endpoint Service for the company’s applications and link it with an Application Load Balancer that handles HTTP or HTTPS traffic. Maintain a secure connection between the company’s data center and AWS using Direct Connect** is incorrect because the Application Load Balancer cannot be used to create a VPC Endpoint Service. VPC Endpoint Services require Network Load Balancers.

The option that says: **Use AWS Direct Connect to link the company’s data center to a VPC in AWS. Within the VPC, set up security group rules to manage access to the company’s applications** is incorrect because it does not provide a way for the company to extend its services to other businesses on AWS. While AWS Direct Connect and security group rules provide secure connectivity and access control, they do not enable the company to expose its applications as services that other AWS users can consume.

The option that says: **Set up a NAT Gateway in a VPC for the company’s applications and secure it with network access control and security group rules** is incorrect because a NAT Gateway is used to enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating a connection with those instances. However, the question specifies that the company’s data cannot traverse the public internet. While network access control and security group rules add a layer of security, they do not provide the necessary private connectivity for the company’s sensitive data.

**References:**

[https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.htm](https://docs.aws.amazon.com/vpc/latest/privatelink/configure-endpoint-service.html)[https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
 [https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

**Check out these AWS Cheat Sheets:**[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)
 [https://tutorialsdojo.com/aws-direct-connect/](https://tutorialsdojo.com/aws-direct-connect/)
 [https://tutorialsdojo.com/aws-elastic-load-balancing-elb/](https://tutorialsdojo.com/aws-elastic-load-balancing-elb/)

</details>

<a id="q17"></a>

## Q17

A company has an on-premises data center and uses a single 1 Gbps AWS Direct Connect connection to connect to its cloud resources in the us-east-1 region. The AWS Direct Connect connection uses a single private virtual interface to establish a connection to the VPC in us-east-1. The company has plans to expand and create a new VPC in the us-west-1 region. The solutions architect must design a solution that will add redundancy to the current AWS Direct Connect connection and use the same network to provide connectivity to the new VPC in the new region.

Which of the following should the solutions architect implement to meet the requirements?

- **A.** Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for each Direct Connect connection. Create a transit gateway for each region’s VPC. Connect both private VIFs to the transit gateways.
- **B.** Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new public virtual interface for the second connection. Connect the us-west-1 VPC to the new public virtual interface.
- **C.** Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for the second connection. Create virtual private gateways on each VPC and associate both of them to the two private VIFs.
- **D.** Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection. Create a Direct Connect gateway. Create a new private virtual interface for each connection and associate them both to the Direct Connect gateway. Create a virtual private gateway for each region’s VPC and connect them to the Direct Connect gateway.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** add DX redundancy + reach a NEW VPC in another Region over the same network

🪤 **Your trap:** 🔁 A transit gateway per Region adds parts; DX private VIFs reach other Regions only through a Direct Connect gateway

🧠 **Rule:** 2nd DX connection + one Direct Connect gateway; a private VIF per connection associated to the DX gateway; VGW per VPC (any Region).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises DC
     │  DX #1 (1 Gbps, hiện có)      DX #2 (mới, để dự phòng)
     └───── private VIF ─────┐   ┌───── private VIF ─────┘
                             ▼   ▼
                     Direct Connect gateway   (global)
                        │               │
                       VGW             VGW
                        │               │
                  VPC us-east-1    VPC us-west-1 (mới)
```

Yêu cầu: (1) thêm **redundancy** cho Direct Connect, (2) dùng **cùng mạng** để tới VPC mới ở **Region khác**. Đáp án đúng: **D**. Anh chọn A (transit gateway cho mỗi Region).

⚠️ **Lỗi lặp lại (đã miss ở lần làm TD5 đầu):** thêm Transit Gateway khi đề chỉ cần Direct Connect gateway. Câu hỏi này có **hai VPC, mỗi Region một cái** và chỉ cần tới được chúng; không có nhu cầu gom nhiều VPC cùng Region.

#### Vì sao D đúng

- **Direct Connect gateway** là resource **toàn cầu**: tạo ở Region nào cũng truy cập được từ các Region khác. Một private VIF tới DX gateway có thể tiếp cận nhiều VPC ở Region/account khác nhau, nên giảm công quản lý Direct Connect.
- Kết nối thứ hai cho redundancy: tạo **private VIF cho từng connection** và **associate cả hai vào cùng DX gateway**.
- Mỗi VPC có **virtual private gateway (VGW)**, nối vào DX gateway bằng virtual private gateway association.

#### Anh chọn A: vì sao trông đúng và vì sao sai

A nghe "hiện đại": transit gateway mỗi Region, nối cả hai private VIF vào. Sai theo TD vì để dùng Transit Gateway qua Direct Connect cần **Direct Connect gateway + transit virtual interface**, **không phải private VIF**. A thiếu DX gateway và dùng sai loại VIF, nên không chạy. Ngoài ra transit gateway chỉ hợp lý khi có nhiều VPC cùng Region (TD: "associate DX gateway với transit gateway when you have multiple VPCs in the same Region"), mà đề chỉ có một VPC mỗi Region.

#### Các đáp án sai còn lại

- **C (private VIF + VGW từng VPC):** không thể nối trực tiếp hai VGW ở hai Region khác nhau vào private VIF. Cần DX gateway.
- **B (public VIF):** public VIF không cần cho yêu cầu này; chỉ dùng private VIF hoặc transit VIF để tới VPC. Còn thiếu hẳn giải pháp cho multi-Region.

| Mô hình | VIF | Gateway ở giữa | Khi nào dùng |
|---|---|---|---|
| **D. DX gateway + VGW** | Private VIF | DX gateway, VGW mỗi VPC | Ít VPC, nhiều Region |
| A (sai). TGW không có DX gateway | Private VIF | Transit gateway | Sai loại VIF, thiếu DX gateway |
| DX gateway + TGW | Transit VIF | DX gateway, TGW | Nhiều VPC cùng Region |

#### Lưu ý thực tế

- Nếu đề đổi thành "nhiều VPC mỗi Region, quản lý tập trung" thì hướng đúng là **DX gateway + Transit Gateway + transit VIF**. Chỉ khi đó TGW mới được dùng.
- Bước "Remove the current private VIF" trong D là cách đề mô tả việc dựng lại các VIF để gắn vào DX gateway.

#### Quy tắc nhớ cho thi

- **Thấy "Direct Connect tới VPC ở Region khác"** → **Direct Connect gateway**
- **Private VIF** → VGW (qua DX gateway); **Transit VIF** → Transit Gateway (qua DX gateway)
- **Thấy "transit gateway" + "private VIF"** → hai thứ này không đi chung, loại ngay
- **"Redundancy"** → thêm connection thứ hai, một VIF mỗi connection, cùng gắn vào DX gateway
- Mnemonic: **Khác Region = DX gateway; nhiều VPC cùng Region = thêm TGW + transit VIF**

### TD explanation

**AWS Direct Connect** makes it easy to establish a dedicated connection from an on-premises network to one or more VPCs in the same region.

**A Direct Connect gateway** is a globally available resource to enable connections to multiple Amazon VPCs across different regions or AWS accounts. This feature also allows you to connect to any participating VPCs from one private VIF, reducing AWS Direct Connect management, as shown in the following figure.

![image](https://media.tutorialsdojo.com/sap_private_vif.png)

Use AWS Direct Connect gateway to connect your VPCs. You associate an AWS Direct Connect gateway with either of the following gateways:

-A transit gateway when you have multiple VPCs in the same Region

-A virtual private gateway

A Direct Connect gateway is a globally available resource. You can create the Direct Connect gateway in any Region and access it from all other Regions. In the diagram, each VPC has a virtual private gateway that connects to the Direct Connect gateway using a virtual private gateway association. The Direct Connect gateway uses a private virtual interface for the connection to the AWS Direct Connect location. There is an AWS Direct Connect connection from the location to the customer data center.

Therefore, the correct answer is: **Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection. Create a Direct Connect gateway. Create a new private virtual interface for each connection and associate them both to the Direct Connect gateway. Create a virtual private gateway for each region’s VPC and connect them to the Direct Connect gateway.**  A Direct Connect gateway is needed to connect VPCs from separate regions into a single (or redundant) Direct Connect connection using a private virtual interface.

The option that says: **Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for the second connection. Create virtual private gateways on each VPC and associate both of them to the two private VIFs** is incorrect. You can’t directly connect two virtual private gateways from two different regions to a private VIF. You will need to have a Direct Connect gateway for this.

The option that says: **Remove the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new private virtual interface for each Direct Connect connection. Create a transit gateway for each region’s VPC. Connect both private VIFs to the transit gateways** is incorrect. Transit gateway can be used to connect multiple VPCs from multiple regions, however, you will need a Direct Connect gateway and a transit virtual interface for this, not a private virtual interface.

The option that says: **Retain the current private virtual interface. Request to provision a second AWS Direct Connect connection for redundancy. Create a new public virtual interface for the second connection. Connect the us-west-1 VPC to the new public virtual interface** is incorrect. Depending on the configuration for the VPCs in each region, you will only use a private VIF or a transit VIF to meet the company requirements. You do not need a public VIF.

**References:**

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/virtualgateways.html)

[https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html)

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html)

[https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway.html](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-gateway.html)

**Check out this AWS Direct Connect Cheat Sheet:**

[https://tutorialsdojo.com/aws-direct-connect/](https://tutorialsdojo.com/aws-direct-connect/)

</details>

<a id="q55"></a>

## Q55

A digital marketing firm is planning to integrate its local servers with AWS for better scalability. The firm has chosen a 200 Mbps AWS Direct Connect connection for this integration. The proposed setup includes a transit gateway and a Direct Connect gateway to ensure smooth communication between several Amazon VPCs and the local servers.

The firm needs to make sure that its local servers can interact with the VPC resources through a transit virtual interface (VIF) using the Direct Connect connection.

Which two actions should the firm take to achieve these requirements? (Select TWO.)

*(Chọn nhiều đáp án)*

- **A.** Advertise the allowed prefixes to a range that is the same or wider than the VPC CIDR block on the Direct Connect gateway.
- **B.** Advertise the VPC prefixes list on the Direct Connect gateway for the transit gateway association.
- **C.** Configure the Direct Connect connection by setting the MACsec encryption mode parameter to `must_encrypt`.
- **D.** Upgrade the Direct Connect connection from 200 Mbps to 500 Mbps.
- **E.** Use the same Connection Key Name (CKN) and Connectivity Association Key (CAK) for all Direct Connect connections.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, B · **You picked:** C, D

🔑 **Key words:** transit VIF, DX gateway + transit gateway, local servers must reach VPCs

🪤 **Your trap:** MACsec / more bandwidth don't fix reachability — it's a routing (prefix) problem

🧠 **Rule:** DX gateway ↔ TGW association: allowed prefixes must cover (≥) the VPC CIDRs and the VPC prefixes must be advertised.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Local servers ══ DX 200 Mbps ══ Transit VIF ══► Direct Connect gateway
                                                     │  (association)
                                                     ▼
                                             Transit gateway ──► nhiều VPC
```

Yêu cầu: local servers **tới được tài nguyên VPC** qua transit VIF. Đáp án đúng: **A + B**. Anh chọn C + D (MACsec + nâng băng thông).

Đây là bài toán **routing/prefix**, không phải bảo mật hay hiệu năng.

#### Hai đáp án đúng ghép thành MỘT giải pháp

**A. Allowed prefixes ≥ VPC CIDR:** trên DX gateway, allowed prefixes là bộ lọc cho phép quảng bá các CIDR (IPv4 và IPv6) tới on-premises. Phải đặt **bằng hoặc rộng hơn** CIDR của VPC thì mọi IP trong VPC mới được tới từ local servers.

**B. Quảng bá danh sách VPC prefixes trên DX gateway cho transit gateway association:** allowed prefixes list dùng để route traffic on-premises tới/từ DX gateway và transit gateway, kể cả khi VPC gắn với transit gateway chưa gán CIDR.

```
association DX gateway <-> TGW
        │
        ├─ allowed prefixes bao phủ VPC CIDR   (A)
        └─ VPC prefixes được advertise         (B)
        =>  on-prem thấy route tới VPC
```

#### Anh chọn C + D: vì sao trông đúng và vì sao sai

- **D (nâng 200 Mbps lên 500 Mbps):** băng thông chỉ cải thiện hiệu năng. Đề không nói tốc độ hiện tại thiếu, và băng thông không tạo ra route.
- **C (MACsec `must_encrypt`):** mã hóa. Tham số này không ảnh hưởng chuyện server có tới được VPC hay không.

Cả hai "nghe có lý" (nhanh hơn, an toàn hơn) nhưng không giải quyết vấn đề **reachability**.

#### Đáp án sai còn lại

- **E (CKN/CAK giống nhau cho mọi connection):** CKN/CAK dùng cho MACsec. Dùng chung khóa cho mọi connection là thực hành bảo mật kém và không liên quan tới kết nối tới VPC.

| Option | Loại | Giúp reachability? |
|---|---|---|
| **A. Allowed prefixes ≥ VPC CIDR** | Routing | Có |
| **B. Advertise VPC prefixes** | Routing | Có |
| C. MACsec must_encrypt | Mã hóa | Không |
| D. Nâng băng thông | Hiệu năng | Không |
| E. Chung CKN/CAK | MACsec key | Không |

#### Lưu ý thực tế

📝 **Ghi chú kỹ thuật:** cách diễn đạt của B hơi lạ so với console thật; trên thực tế bước này nằm ở cấu hình allowed prefixes khi tạo association giữa DX gateway và transit gateway. Giữ nguyên đáp án đề.

- Allowed prefixes là thứ AWS quảng bá về on-premises; với Transit Gateway đây là bước cấu hình trên association.

#### Quy tắc nhớ cho thi

- **Thấy "transit VIF + DX gateway + TGW, on-prem không tới VPC"** → xem **allowed prefixes** (≥ VPC CIDR) và prefix advertisement
- **MACsec / bandwidth / CKN-CAK** → bảo mật hoặc hiệu năng, **không** sửa lỗi routing
- **"Reachability"** → luôn nghĩ route/prefix trước, nâng cấp sau

### TD explanation

The prefix list, which includes IPv4 and IPv6 addresses, is a filter that permits the same or a smaller range of CIDRs to be promoted to the Direct Connect gateway. When setting up a Direct Connect gateway, it’s important to set the allowed prefixes to a range that is the same or wider than the VPC CIDR block. This ensures that all IP addresses within the VPC can be reached from the local servers.

![Direct Connect gateway](https://media.tutorialsdojo.com/public/direct-connect-associate-gateway-042024.png)

If you want to connect your AWS Direct Connect connection to the VPCs or VPNs that are attached to your transit gateway, you can use an AWS Direct Connect gateway. To do this, you need to associate a Direct Connect gateway with the transit gateway and create a transit virtual interface for your AWS Direct Connect connection to the Direct Connect gateway.

![Allowed prefixes](https://media.tutorialsdojo.com/public/direct-connect-associate-direct-connect-gateway-042024.png)

Provisioning the allowed prefixes list on the Direct Connect gateway is a necessary step. This list is used to route on-premises traffic to or from a Direct Connect gateway to the transit gateway, even when the VPCs attached to the transit gateway do not have assigned CIDRs. This setup ensures that the local servers can interact with the AWS VPC resources through the transit VIF.

Hence, the correct answers are:

**– Advertise the allowed prefixes to a range that is the same or wider than the VPC CIDR block on the Direct Connect gateway.**

**– Advertise the VPC prefixes list on the Direct Connect gateway for the transit gateway association.**

The option that says: **Upgrade the Direct Connect connection from 200 Mbps to 500 Mbps** is incorrect because while upgrading the connection speed typically improves performance, it is not necessary for the local servers to interact with the AWS VPC resources. The question does not indicate that the current speed is insufficient.

The option that says: **Configure the Direct Connect connection by setting the MACsec encryption mode parameter to****`must_encrypt`** is incorrect because it is not necessary for the local servers to interact with the Amazon VPC resources through a transit virtual interface (VIF) using the Direct Connect connection. The encryption mode parameter does not affect the interaction between the servers and VPC resources.

The option that says: **Use the same Connection Key Name (CKN) and Connectivity Association Key (CAK) for all Direct Connect connections** is incorrect because the CKN and CAK are primarily used for MACsec encryption. Using the same keys for all connections would not be a good security practice, and it is not necessary for the local servers to interact with the AWS VPC resources.

**References:**

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/allowed-to-prefixes.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/allowed-to-prefixes.html)

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html)

**Check out this AWS Direct Connect Gateway Cheat Sheet:**

[https://tutorialsdojo.com/aws-direct-connect/](https://tutorialsdojo.com/aws-direct-connect/)

</details>

<a id="q38"></a>

## Q38

A company is developing a serverless application that is deployed on AWS Lambda. The application consists of several Lambda functions that resize, watermark, and process images. The metadata generated from the functions is written in an Amazon DynamoDB table. The company deployed an Amazon Neptune DB cluster in three private subnets inside a VPC. A new feature was developed that requires the Lambda functions to access the Neptune DB cluster.

Which of the following options are possible solutions to allow the Lambda functions to access both the DynamoDB table and Neptune DB cluster? (Select TWO.)

*(Chọn nhiều đáp án)*

- **A.** Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Create a DynamoDB VPC endpoint and update the route table for routing DynamoDB requests.
- **B.** Deploy the AWS Lambda functions into three new public subnets in the same VPC. Update the Amazon Neptune DB security group to allow connections from the Lambda security group. Route internet traffic to the Internet Gateway.
- **C.** Keep the Lambda functions outside the VPC. Configure the Neptune DB security group to allow inbound access from the AWS Lambda IP range.
- **D.** Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Route the internet traffic of the Lambda functions through a NAT gateway.
- **E.** Keep the AWS Lambda functions outside the VPC. Create a VPC endpoint for the Amazon Neptune service. Update the Lambda functions to use this endpoint to send requests to the Neptune DB cluster.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** A, B

🔑 **Key words:** Lambda must reach Neptune (private subnets) AND DynamoDB

🪤 **Your trap:** Lambda ENIs in a VPC never get public IPs — public subnet + IGW gives no internet/AWS-API access

🧠 **Rule:** VPC Lambda → private subnets + SG rule to the DB; reach DynamoDB via gateway VPC endpoint or NAT gateway.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Lambda (resize, watermark, process ảnh)
     │                    │
     ▼                    ▼
 Neptune (3 private     DynamoDB (public service
 subnet trong VPC)       endpoint qua HTTPS API)
```

Lambda mặc định chạy **ngoài VPC** nên không với tới Neptune ở private subnet. Phải đưa Lambda **vào VPC** rồi tìm đường tới **DynamoDB**. Đáp án đúng: **A + D**. Anh chọn A (đúng) + B (sai).

#### Hai đáp án đúng, hai cách khác nhau tới DynamoDB

Cả hai: Lambda vào **private subnet** cùng VPC, Neptune security group cho phép từ Lambda security group. Khi gắn Lambda vào VPC, Lambda tạo **Hyperplane ENI** cho mỗi subnet trong cấu hình VPC của function.

- **A:** tạo **DynamoDB VPC endpoint** và cập nhật route table. Lambda vào DynamoDB thẳng trong mạng AWS.
- **D:** route outbound qua **NAT gateway**. DynamoDB là HTTPS API, NAT cho private resource đi ra tới nó.

Hai cách này là hai lựa chọn tương đương (hai "đáp án khả thi"), nên đề chọn 2 nhưng thực chất mỗi cái là một giải pháp hoàn chỉnh.

#### Anh chọn B: vì sao sai

B đặt Lambda ở **public subnet** + route tới **Internet Gateway**. Anh nghĩ: public subnet + IGW = có internet. Với EC2 thì đúng, vì instance có public IP. Với Lambda thì **không**:

```
EC2 public subnet:   public IP + IGW      ──► internet OK
Lambda ENI trong VPC: chỉ private IP,
                      KHÔNG có public IP   ──► IGW không dịch được
                                              ──► KHÔNG ra internet
```

TD: *Lambda functions do not, and cannot, have public IP addresses.* IGW chỉ làm việc với resource có public IP. Vì vậy dù đặt vào public subnet, Lambda vẫn không gọi được DynamoDB qua internet. Muốn ra internet phải đi **NAT gateway đặt trong public subnet**, còn Lambda ở **private subnet**.

#### Các đáp án sai còn lại

- **C (Lambda ngoài VPC + cho phép Lambda IP range vào Neptune SG):** Lambda mặc định ngoài VPC và không truy cập được tài nguyên bên trong VPC; Neptune lại nằm ở private subnet.
- **E (Lambda ngoài VPC + VPC endpoint cho Neptune):** endpoint chỉ dùng được từ tài nguyên bên trong VPC, Lambda ngoài VPC không dùng được.

| Option | Lambda ở đâu | Tới Neptune | Tới DynamoDB |
|---|---|---|---|
| **A** | Private subnet | SG rule | VPC endpoint |
| **D** | Private subnet | SG rule | NAT gateway |
| B | Public subnet | SG rule | Không (không public IP) |
| C | Ngoài VPC | Không | Có (nhưng Neptune không tới được) |
| E | Ngoài VPC | Không | Có (nhưng Neptune không tới được) |

#### Lưu ý thực tế

- Lambda trong VPC mất đường ra internet và AWS API mặc định; luôn phải bổ sung **VPC endpoint** hoặc **NAT gateway**.
- NAT gateway phải nằm trong **public subnet**, còn Lambda ở private subnet.

#### Quy tắc nhớ cho thi

- **Thấy "Lambda cần vào DB trong VPC"** → Lambda vào **private subnet** + SG rule tới DB
- **Thấy "Lambda trong VPC cần gọi AWS service/internet"** → **VPC endpoint** hoặc **NAT gateway**
- **Thấy "Lambda ở public subnet + IGW"** → bẫy, Lambda không có public IP nên vô dụng
- Mnemonic: **Lambda trong VPC = luôn private subnet**

### TD explanation

**Amazon Neptune** is a fast, reliable, fully-managed graph database service that makes it easy to build and run applications that work with highly connected datasets. The core of Neptune is a purpose-built, high-performance graph database engine. This engine is optimized for storing billions of relationships and querying the graph with milliseconds latency.

You can configure a **Lambda function** to connect to private subnets in a virtual private cloud (VPC) in your AWS account. Use Amazon Virtual Private Cloud (Amazon VPC) to create a private network for resources such as databases, cache instances, or internal services. Connect your function to the VPC to access private resources while the function is running.

When you connect a function to a VPC, Lambda assigns your function to a Hyperplane ENI (elastic network interface) for each subnet in your function’s VPC configuration. Lambda creates a Hyperplane ENI the first time a unique subnet and security group combination is defined for a VPC-enabled function in an account.

![image](https://media.tutorialsdojo.com/public/td-lambda-neptune-ddb-diagram--28-08-2024.png)

Internet access from a private subnet requires **network address translation (NAT)**. To give internet access to an Amazon VPC-connected Lambda function, route its outbound traffic to a NAT gateway or NAT instance in a public subnet. Lambda functions do not, and cannot, have public IP addresses. You cannot send traffic to the internet, which happens via the VPC’s Internet Gateway, unless you have a public IP.

The option that says: **Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Create a DynamoDB VPC endpoint and update the route table for routing DynamoDB requests** is correct. In the private subnet, the Lambda functions can directly access the Neptune DB cluster, and the DynamoDB table via the DynamoDB VPC endpoint.

The option that says: **Deploy the AWS Lambda functions into three new private subnets in the same VPC. Update the Neptune DB security group to allow connections from the Lambda security group. Route the internet traffic of the Lambda functions through a NAT gateway** is correct. Since DynamoDB is accessed via HTTPS API calls on the internet, you can use a NAT gateway to allow private resources, such as the Lambda functions, to route their traffic to the internet.

The option that says: **Deploy the AWS Lambda functions into three new public subnets in the same VPC. Update the Amazon Neptune DB security group to allow connections from the Lambda security group. Route internet traffic to the Internet Gateway** is incorrect. You can deploy Lambda functions on a public subnet. However, since Lambda functions typically do not have a public IP, they can’t directly access the internet even if you associate an internet gateway to the VPC.

The option that says: **Keep the AWS Lambda functions outside the VPC. Create a VPC endpoint for the Amazon Neptune service. Update the Lambda functions to use this endpoint to send requests to the Neptune DB cluster**is incorrect. Since the Neptune DB cluster is in a private subnet, it is not exposed to the outside world. A VPC endpoint is exposed only to resources inside a VPC, so Lamdba functions can’t connect to it either.

The option that says: **Keep the Lambda functions outside the VPC. Configure the Neptune DB security group to allow inbound access from the AWS Lambda IP range** is incorrect. Lambda functions by default are created outside a VPC and they can’t access any resources that are inside a VPC.

**References:**

[https://docs.aws.amazon.com/neptune/latest/userguide/intro.html](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)

[https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)

[https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/](https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/)

**Check out these Amazon VPC and AWS Lambda Cheat Sheets:**

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

[https://tutorialsdojo.com/aws-lambda/](https://tutorialsdojo.com/aws-lambda/)

</details>

---

# Group B — Cheapest / least-overhead design fit (edge features, serverless, EKS for multi-cloud, PII off-chain) (4)

<a id="q22"></a>

## Q22

A company has developed an Optical Character Recognition (OCR) application that allows users to upload PDF files to an Amazon S3 bucket. The user-facing website is hosted on S3, and its content is distributed by Amazon CloudFront. When a user initiates an OCR job, the application makes a call to a REST API in Amazon API Gateway (Regional), which in turn invokes an AWS Lambda function asynchronously to start the OCR process. The OCR output’s S3 path is then stored in an Amazon DynamoDB table

Currently, the application stack is deployed in the `us-east-1` AWS region. The company wants to expand its user base to include users from Asia and the Middle East and aims to improve latency for these users.

Which combination of steps is the most cost-effective approach that would meet this requirement? (Select TWO.)

*(Chọn nhiều đáp án)*

- **A.** Enable S3 Transfer Acceleration on the S3 bucket and update the application code to use the Transfer Acceleration endpoint.
- **B.** Migrate the DynamoDB table to Amazon Aurora Serverless and use an Amazon RDS Proxy in front of the Lambda function.
- **C.** Upload the PDF files to an Amazon EBS-backed Amazon EC2 instance in the `us-east-1` region. Create an AWS Global Accelerator for the EC2 instance. Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint.
- **D.** Deploy additional Lambda functions and S3 buckets in Asia and Middle East regions. Set up cross-region S3 replication. Configure Route 53 Geolocation Routing to direct users to the closest regional resources.
- **E.** Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, E · **You picked:** A, D

🔑 **Key words:** users in Asia/Middle East, lower latency, MOST cost-effective

🪤 **Your trap:** Multi-Region copies + geolocation routing = overbuilt; a second stack costs far more

🧠 **Rule:** Global latency, cheapest → edge features: S3 Transfer Acceleration for uploads + edge-optimized API Gateway endpoint.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
User (Châu Á / Trung Đông)
   │
   ├─ tải website ──► CloudFront ──► S3 (website)        [ĐÃ nhanh sẵn]
   │
   ├─ upload PDF ───────────────────► S3 bucket (us-east-1)   ← chậm (xa)
   │
   └─ gọi REST API ─────────────────► API Gateway (Regional, us-east-1)
                                         └─► Lambda (async) ─► DynamoDB   ← chậm (xa)

Yêu cầu: giảm latency cho user Asia/Middle East, tiết kiệm chi phí NHẤT (chọn 2)
```

Đáp án đúng: **A + E**. Anh chọn đúng A, sai ở D (thay vì E).

Điểm mấu chốt: website tĩnh đã có CloudFront rồi. Chỉ còn **2 đường vào chậm**: upload PDF lên S3 và gọi API. Mỗi đường có một tính năng "edge" gắn sẵn, không cần dựng thêm stack.

#### A + E hợp thành MỘT giải pháp

```
Upload PDF:  User ─► edge location gần nhất ─(đường mạng tối ưu)─► S3 bucket     (A)
Gọi API:     User ─► edge location gần nhất ─(đường mạng tối ưu)─► API Gateway   (E)
```

- **A. S3 Transfer Acceleration:** user upload vào edge location của CloudFront, từ đó dữ liệu đi tới S3 qua đường mạng tối ưu. Hiệu quả với file lớn, khoảng cách xa. Phải **đổi code** sang dùng endpoint Transfer Acceleration.
- **E. Edge-Optimized API endpoint:** chỉ cần đổi endpoint type từ Regional sang Edge-Optimized, request được đưa vào qua edge location. Không dựng thêm gì, không đổi kiến trúc backend.

Cả hai đều là cấu hình bật lên, không thêm resource chạy 24/7 → rẻ nhất.

#### Lựa chọn của Anh: D sai ở đâu

D trông "chuẩn bài" vì nghĩ: user xa thì đặt resource gần user. Nhưng đề hỏi **cost-effective nhất**.

- Phải nhân bản **Lambda + S3 ở nhiều Region** → thêm chi phí và công vận hành.
- **Cross-region replication** thường dùng cho DR, archive, migration; giữ nhiều bản dữ liệu ở nhiều Region làm **tăng chi phí storage**.
- Route 53 **Geolocation** chỉ chọn Region theo vị trí user, bản thân nó không tăng tốc gì.
- Còn kéo theo bài toán DynamoDB nằm ở đâu, dữ liệu đồng bộ ra sao.

Nói ngắn gọn: D giải được bài toán nhưng là "dựng stack thứ hai", đắt hơn nhiều so với bật 2 tính năng edge.

#### Các đáp án sai còn lại

- **B (Aurora Serverless + RDS Proxy):** đổi database sang quan hệ không liên quan gì tới latency của user ở xa. Chỉ tốn công migrate.
- **C (EC2 + Global Accelerator):** thêm EC2 → tăng overhead vận hành và chi phí. Global Accelerator thừa vì CloudFront đã lo phân phối nội dung HTTP/HTTPS toàn cầu. (Phần Edge-Optimized trong C đúng, nhưng phần còn lại làm hỏng cả đáp án.)

| Cách | Thêm gì | Chi phí / vận hành |
|---|---|---|
| **A + E** | Bật Transfer Acceleration + đổi endpoint type | Thấp nhất |
| D | Lambda + S3 nhiều Region + replication + geo routing | Cao |
| C | EC2 + Global Accelerator | Cao, thêm server |
| B | Migrate DB | Không giải quyết latency |

#### Quy tắc nhớ cho thi

- **Thấy "upload từ user xa vào S3, giảm latency"** → **S3 Transfer Acceleration**
- **Thấy "API Gateway Regional, user toàn cầu"** → **Edge-Optimized endpoint**
- **Thấy "most cost-effective" + latency toàn cầu** → ưu tiên **tính năng edge bật sẵn**, tránh nhân bản cả stack nhiều Region
- **Thấy "multi-Region + replication + Geolocation"** cho bài chỉ cần giảm latency → thường là **overbuilt**
- **Đã có CloudFront** → **Global Accelerator** thường là thừa cho HTTP/HTTPS

### TD explanation

**Amazon S3 Transfer Acceleration** can speed up content transfers to and from Amazon S3 by as much as 50% – 500% for long-distance transfer of larger objects. Customers who have either web or mobile applications with widespread users or applications hosted far away from their S3 bucket can experience long and variable upload and download speeds over the Internet.

![S3 transfer acceleration](https://media.tutorialsdojo.com/Amazon-S3-TA.PNG)

S3 Transfer Acceleration enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration takes advantage of Amazon CloudFront’s globally distributed edge locations. As the data arrive at an edge location, they are routed to Amazon S3 over an optimized network path.

In the given scenario, since Amazon CloudFront is already in use for distributing content, the focus for reducing latency should be on the user’s interactions with the API and the S3 bucket where PDF files are uploaded. Enabling Amazon S3 Transfer Acceleration (S3TA) would speed up file uploads to the bucket, while switching the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint would enhance API call performance for users worldwide, including those in Asia and the Middle East

Hence, the correct answers are:

**– Enable S3 Transfer Acceleration on the S3 bucket and update the application code to use the Transfer Acceleration endpoint.**

**– Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint.**

The option that says: **Migrate the DynamoDB table to Amazon Aurora Serverless and use an Amazon RDS Proxy in front of the Lambda function**is incorrect. Simply switching to a relational database would not address the latency concerns for users in Asia and the Middle East.

The option that says: **Upload the PDF files to an Amazon EBS-backed Amazon EC2 instance in the `us-east-1` region. Create an AWS Global Accelerator for the EC2 instance. Switch the existing Amazon API Gateway from a Regional endpoint to an Edge-Optimized endpoint** is incorrect. The use of an EC2 instance would not only introduce additional operational overhead but also incur higher costs. AWS Global Accelerator is unnecessary since CloudFront is already handling global content distribution and latency reduction for HTTP/HTTPS content.

The option that says: **Deploy additional Lambda functions and S3 buckets in Asia and Middle East regions. Set up cross-region S3 replication. Configure Route 53 Geolocation Routing to direct users to the closest regional resources**is incorrect. Cross-region replication in Amazon S3 is typically used for disaster recovery, data archiving, or data migration purposes. Having multiple copies of data in different regions would increase storage costs.

**References:**

[https://aws.amazon.com/s3/transfer-acceleration/](https://aws.amazon.com/s3/transfer-acceleration/)

[https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html)

**Check out these Amazon S3 and Amazon API Gateway Cheat Sheets:**

[https://tutorialsdojo.com/amazon-s3/](https://tutorialsdojo.com/amazon-s3/)

[https://tutorialsdojo.com/amazon-api-gateway/](https://tutorialsdojo.com/amazon-api-gateway/)

</details>

<a id="q39"></a>

## Q39

A company hosts a .NET REST API in AWS. Currently, the business logic of the API is deployed on three EC2 instances distributed across different Availability Zones. The application is monolithic in nature, and some functions tend to consume more resources than others during operation. Clients interact with the API by calling its domain name. This domain is registered with Route 53, which uses a multi-value answer policy to route each request to one of the available EC2 instances.

The application experiences non-constant traffic throughout the day and becomes unresponsive during periods of peak demand. A solutions architect is tasked with redesigning the architecture to be more cost-effective and to have the least amount of operational overhead.

Which solution will meet these requirements?

- **A.** Split the API into multiple AWS Lambda functions to handle different components. Provision an Amazon API Gateway REST API to act as the interface for these Lambda functions. Configure a custom domain in API Gateway, then update the Route 53 record to map to this custom domain.
- **B.** Create a custom routing accelerator in AWS Global Accelerator, targeting the subnets housing the EC2 instances. Place the EC2 instances into an Auto Scaling group with a policy that scales based on average CPU utilization. Update the Route 53 records to resolve to the IP address provided by the Global Accelerator.
- **C.** Register the existing EC2 instances in an Auto Scaling group and use it as a target for an Application Load Balancer (ALB). Configure a dynamic scaling policy based on the ALB’s `RequestCountPerTarget` metric. Update Route 53 to direct traffic to the ALB’s endpoint.
- **D.** Move the API on an Amazon Elastic Kubernetes Service (EKS) cluster that uses EC2 Spot Instances. Configure a Kubernetes Ingress controller for request routing and create a corresponding ingress resource. Update Route 53 to point to the external IP provided by the Ingress controller.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** monolith REST API, spiky traffic, components use different resources, cost-effective, least operational overhead

🪤 **Your trap:** ASG + ALB still runs and patches EC2 for idle hours

🧠 **Rule:** Spiky API + least overhead → split into Lambda functions behind API Gateway (custom domain), scale per function.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại:
Client ─► Route 53 (multi-value answer) ─┬─► EC2 (AZ-a)
                                         ├─► EC2 (AZ-b)   .NET monolith
                                         └─► EC2 (AZ-c)

Vấn đề: traffic không đều, đỉnh điểm thì app "unresponsive"
        một số function ngốn tài nguyên hơn các function khác
Yêu cầu: cost-effective hơn + ÍT operational overhead NHẤT
```

Đáp án đúng: **A (Lambda + API Gateway)**. Anh chọn C (ASG + ALB).

#### A đúng vì sao

```
Client ─► Route 53 ─► API Gateway (custom domain) ─┬─► Lambda: function 1
                                                   ├─► Lambda: function 2
                                                   └─► Lambda: function 3 (nặng)
```

- **Serverless:** không còn server để cấp phát hay vá lỗi, trả tiền theo mức dùng. Traffic lên xuống thất thường → lúc vắng gần như không tốn gì.
- **Scale từng function độc lập:** đề cố ý nói "some functions consume more resources than others". Monolith buộc phải scale cả khối; tách thành Lambda thì function nặng scale riêng.
- **Custom domain** trên API Gateway, Route 53 trỏ vào đó: client vẫn gọi bằng domain cũ.

#### Lựa chọn của Anh: C sai ở đâu

C trông hợp lý vì ASG + ALB là mẫu quen thuộc để xử lý peak. Nhưng:

- Vẫn là **EC2 chạy monolith** → không scale riêng từng component được. Một function nặng làm quá tải instance thì phải thêm cả instance chứa toàn bộ app → kém cost-effective.
- Vẫn phải **quản lý và vá EC2** → overhead vận hành cao hơn A.
- Ngoài giờ cao điểm vẫn có instance chạy, trả tiền cả khi nhàn rỗi.

Bẫy của Anh: C thật sự giải quyết được "unresponsive lúc peak", nhưng đề hỏi **ít overhead nhất + cost-effective**, và gợi ý rõ ràng về việc tách component.

#### Các đáp án sai còn lại

- **B (Global Accelerator custom routing + ASG):** Global Accelerator dùng để cải thiện availability/performance cho user toàn cầu. Đề không nói user toàn cầu → thêm phức tạp và chi phí vô ích. Vẫn là EC2 monolith.
- **D (EKS + Spot):** Kubernetes có độ phức tạp và overhead vận hành cao, ngược mục tiêu "ít overhead nhất". Spot có thể bị thu hồi, không hợp workload không chịu được gián đoạn.

| Cách | Compute | Scale từng function | Overhead |
|---|---|---|---|
| **A. Lambda + API Gateway** | Serverless | Có | Thấp nhất |
| C. ASG + ALB | EC2 | Không (scale cả monolith) | Trung bình |
| B. Global Accelerator + ASG | EC2 | Không | Cao hơn, thêm thành phần thừa |
| D. EKS + Spot | Container trên EC2 | Có phần | Cao nhất |

#### Quy tắc nhớ cho thi

- **Thấy "traffic không đều/spiky" + "least operational overhead" + REST API** → **Lambda + API Gateway**
- **Thấy "một số function dùng nhiều tài nguyên hơn"** → gợi ý **tách ra, scale độc lập**
- **ASG + ALB** đúng khi phải giữ nguyên EC2, nhưng không phải đáp án "ít overhead nhất" nếu có lựa chọn serverless
- **Thấy EKS trong câu "least overhead"** → gần như luôn sai
- **Global Accelerator** chỉ khi đề nói user toàn cầu / IP tĩnh / failover nhanh

### TD explanation

AWS Lambda is a serverless compute service that lets you run your code without provisioning or managing servers. It executes your code only when needed and scales automatically, from a few requests per day to thousands per second. Amazon API Gateway is a fully managed service that makes it easy to create, publish, maintain, monitor, and secure APIs at any scale. It acts as a “front door” for applications to access data, business logic, or functionality from your backend services, such as Lambda functions, web applications, or real-time communication services. In combination, Lambda and API Gateway provide a powerful, scalable, and cost-effective solution to build and expose APIs without the need for server management.

![image](https://media.tutorialsdojo.com/public/aws-lambda-breaking-monolithic-into-microservices-sample-diagram.png)

In the scenario, by transitioning from monolithic to microservices using multiple AWS Lambda functions managed through Amazon API Gateway, the architecture becomes serverless. This significantly reduces operational overhead and costs for fluctuating traffic as you pay only for what you use. Additionally, breaking down the monolithic API into Lambda functions allows for fine-grained scalability. Unlike in a monolithic architecture where the entire application must scale as a unit, individual Lambda functions can scale independently based on the demand for that specific function.

Hence, the correct answer in this scenario is: **Split the API into multiple AWS Lambda functions to handle different components. Provision an Amazon API Gateway REST API to act as the interface for these Lambda functions. Configure a custom domain in API Gateway, then update the Route 53 record to map to this custom domain.**

The option that says: **Register the existing EC2 instances in an Auto Scaling group and use it as a target for an Application Load Balancer (ALB). Configure a dynamic scaling policy based on the ALB’s `RequestCountPerTarget` metric. Update Route 53 to direct traffic to the ALB’s endpoint**is incorrect. The use of EC2 instances to host a monolithic application presents a limitation in that you cannot scale individual components independently. If a function within the application overwhelms the resources of one of the EC2 instances, you’re forced to scale the entire application by adding more EC2 instances. Thus, this approach is less cost-effective.

The option that says: **Create a custom routing accelerator in AWS Global Accelerator, targeting the subnets housing the EC2 instances. Place the EC2 instances into an Auto Scaling group with a policy that scales based on average CPU utilization. Update the Route 53 records to resolve to the IP address provided by the Global Accelerator** is incorrect. AWS Global Accelerator is primarily used for improving the availability and performance of applications with global users by routing user traffic through AWS’s network infrastructure. However, unless the application has a global user base that would benefit from such optimized routing, incorporating Global Accelerator could add unnecessary complexity and cost.

The option that says: **Move the API on an Amazon Elastic Kubernetes Service (EKS) cluster that uses EC2 Spot Instances. Configure a Kubernetes Ingress controller for request routing and create a corresponding ingress resource. Update Route 53 to point to the external IP provided by the Ingress controller**is incorrect. Deploying the API on an Amazon EKS cluster would introduce considerable operational complexity. Kubernetes is powerful but has a steep learning curve and high operational overhead, making it less aligned with the goal of minimizing operational tasks. Moreover, although using Spot Instances can be cost-effective, they’re not suitable for all types of workloads, especially for applications that cannot tolerate disruptions.

**References:**

[https://aws.amazon.com/blogs/compute/migrating-a-monolithic-net-rest-api-to-aws-lambda/](https://aws.amazon.com/blogs/compute/migrating-a-monolithic-net-rest-api-to-aws-lambda/)

[https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html)

**Check out these AWS Lambda and Amazon API Gateway Cheat Sheets:**

[https://tutorialsdojo.com/aws-lambda/](https://tutorialsdojo.com/aws-lambda/)

[https://tutorialsdojo.com/amazon-api-gateway/](https://tutorialsdojo.com/amazon-api-gateway/)

</details>

<a id="q70"></a>

## Q70

An organization operates web and mobile platforms for online sales, inventory management, order processing, and shipping logistics. The platforms are running on Amazon EC2 instances across multiple regions. The organization’s databases include a MySQL database for the e-commerce site and a PostgreSQL database for analytics, both managed on EC2 instances.

A solutions architect requires a solution to transition the organization’s architecture to an event-driven, serverless architecture to improve efficiency and data processing speeds, enable real-time analytics, and streamline application data flows. The company also plans to launch a multi-cloud configuration that runs additional clusters on other cloud service providers to further improve the site’s performance.

Which of the following options would most efficiently meet these requirements?

- **A.** Create Auto Scaling groups for each platform component with specific EC2 instance numbers. Migrate e-commerce MySQL and analytics PostgreSQL databases to Amazon Aurora PostgreSQL. Use Amazon SNS to route incoming data to the right EC2 instances and databases.
- **B.** Use Amazon ECS with Fargate to repackage applications as microservices. Migrate e-commerce and analytics databases to Aurora Serverless MySQL and Redshift Serverless. Manage data flow between services using Amazon EventBridge.
- **C.** Migrate to microservices with Amazon EKS and Fargate. Use Aurora Serverless MySQL for e-commerce and Redshift Serverless for analytics. Use Amazon EventBridge to streamline and manage data flows.
- **D.** Migrate app components to microservices with Amazon EKS using AWS Fargate. Change e-commerce MySQL to Amazon Aurora MySQL and analytics DB to Amazon Redshift. Use Amazon Kinesis for real-time data streaming.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** event-driven serverless + additional clusters on OTHER cloud providers

🪤 **Your trap:** 🔁 ECS is AWS-only; 'multi-cloud clusters' points to Kubernetes

🧠 **Rule:** Containers that must also run on other clouds → EKS (Kubernetes) on Fargate; ECS only when AWS-only.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại: EC2 nhiều Region + MySQL (e-commerce) + PostgreSQL (analytics) tự quản trên EC2

Đích:  event-driven + serverless + real-time analytics
       + "chạy thêm cluster trên NHÀ CUNG CẤP CLOUD KHÁC" (multi-cloud)
```

Đáp án đúng: **C (EKS + Fargate, Aurora Serverless MySQL, Redshift Serverless, EventBridge)**. Anh chọn B (cùng bộ, nhưng ECS).

⚠️ **Lỗi lặp lại:** Anh cũng trượt đúng khái niệm này (ECS vs EKS) ở lần làm TD5 đầu tiên. B và C giống nhau gần như từng chữ, chỉ khác **ECS vs EKS**. Đây là điểm quyết định duy nhất.

#### Vì sao C đúng, B sai: chỉ một cụm từ

Cụm khóa: **"additional clusters on other cloud service providers"** → multi-cloud → cần **Kubernetes**.

- **ECS:** gắn chặt với tính năng riêng của AWS. TD nói ECS "typically does not support multi-cloud deployments".
- **EKS:** chạy Kubernetes, **portable**, dễ đưa workload ra vào AWS, tích hợp với cloud khác như Azure, GCP.
- **Fargate** chạy được với cả ECS và EKS → không phân biệt được hai đáp án này.

Các phần còn lại của B và C trùng nhau: Aurora Serverless MySQL, Redshift Serverless, EventBridge đều đúng yêu cầu serverless + event-driven.

#### Các đáp án sai còn lại

- **A:** vẫn chạy ASG với số EC2 cố định → **không serverless**. Gộp cả MySQL và PostgreSQL vào Aurora PostgreSQL, và SNS không phải cách điều phối dữ liệu hợp lý ở đây.
- **D:** có EKS + Fargate đúng, nhưng dùng Aurora MySQL và Redshift **bản provisioned** (không nêu serverless), và dùng **Kinesis** (streaming) thay vì EventBridge cho việc quản lý data flow giữa các service trong kiến trúc event-driven.

| Đáp án | Container | DB | Event | Vấn đề |
|---|---|---|---|---|
| **C** | **EKS + Fargate** | Aurora Serverless + Redshift Serverless | EventBridge | Đủ hết |
| B | ECS + Fargate | Aurora Serverless + Redshift Serverless | EventBridge | ECS không hợp multi-cloud |
| D | EKS + Fargate | Aurora + Redshift (không serverless) | Kinesis | Thiếu serverless DB, sai công cụ event |
| A | EC2 + ASG | Aurora PostgreSQL | SNS | Không serverless |

#### Quy tắc nhớ cho thi

- **Thấy "multi-cloud" / "other cloud providers" / "portable" / "on-premises + cloud"** → **EKS (Kubernetes)**, không phải ECS
- **Thấy "chỉ AWS, đơn giản"** → **ECS**
- **Mẹo nhớ:** "K" trong Kubernetes = "K"hông bị khóa vào AWS; **ECS = AWS-only**
- Hai đáp án giống hệt nhau trừ một service → **tìm cụm từ trong đề quyết định service đó** (ở đây: other cloud providers)
- **Event-driven giữa các service** → **EventBridge**; **Kinesis** là cho streaming dữ liệu

### TD explanation

**Amazon EKS** is a service that helps you run Kubernetes on AWS without having to set up or manage your own Kubernetes control plane. EKS allows you to concentrate on containers while AWS handles the underlying Kubernetes infrastructure. Amazon ECS on the other hand supports Docker containers, making it easier to run and scale containerized applications without worrying about managing virtual machine clusters.

ECS may be better if you want to use AWS-specific features. At the same time, EKS gives you more portability to move workloads on and off AWS if needed.

**AWS Fargate** is a serverless compute engine for containers. You can use containers without having to manage servers or clusters. AWS manages your containers, you only pay for the resources needed to run them. Fargate works with ECS and EKS.

**Aurora Serverless** is a serverless database that automatically scales capacity up or down to match your application’s needs. It is fully managed by AWS and provides high availability and auto-scaling for databases. **Amazon Redshift Serverless** is a fully managed serverless data warehousing service from AWS. With Redshift Serverless, you can run analytics and get insights from data without needing to provision and manage data warehouse infrastructure.

**Amazon EventBridge** is a serverless event bus service that allows you to connect applications together using data from various sources.

![image](https://media.tutorialsdojo.com/public/td-microservices-to-serverless-event-driven-21-APRL-24.png)

To improve the system, the applications can be migrated to a microservices architecture. By doing this, each microservice can be containerized and deployed to EKS on AWS Fargate, providing scalability and high availability without the need to manage servers. Additionally, the EKS is cloud-agnostic —meaning it is easier to integrate with other cloud service providers like Azure and GCP. For easy management, the transactional MySQL database can be migrated to Aurora Serverless. It provides the same capabilities as MySQL in a managed database that automatically scales based on usage. Similarly, the analytics data from transactions can be migrated to Redshift Serverless, which enables running ad-hoc queries and analytics on the data without having to worry about managing database capacity. To capture events from microservices and send relevant data to Aurora Serverless for transactions and Redshift Serverless for analytics, use EventBridge. This provides a central way to capture and route events and data between various services.

Hence, the correct answer is: **Migrate to microservices with Amazon EKS and Fargate. Use Aurora Serverless MySQL for e-commerce and Redshift Serverless for analytics. Use Amazon EventBridge to streamline and manage data flows.**

The option that says: **Use Amazon ECS with Fargate to repackage applications as microservices. Migrate e-commerce and analytics databases to Aurora Serverless MySQL and Redshift Serverless. Manage data flow between services using Amazon EventBridge** is incorrect. Although this option also suggests using Aurora Serverless, Amazon EventBridge, and Redshift Serverless, the container service being used is Amazon ECS, which typically does not support multi-cloud deployments, unlike EKS. While ECS with Fargate allows for container orchestration and management, it doesn’t fully address the requirement of explicit multi-cloud integration. In contrast, Amazon EKS (Elastic Kubernetes Service) with Fargate offers a more suitable platform for multi-cloud configuration with cost-effective serverless computing.

The option that says: **Create Auto Scaling groups for each platform component with specific EC2 instance numbers. Migrate e-commerce MySQL and analytics PostgreSQL databases to Amazon Aurora PostgreSQL. Use Amazon SNS to route incoming data to the right EC2 instances and databases** is incorrect. This solution fails to meet the serverless and event-driven architecture requirement as it still primarily relies on managing EC2 instances.

The option that says: **Migrate app components to microservices with Amazon EKS using AWS Fargate. Change e-commerce MySQL to Amazon Aurora MySQL and analytics DB to Amazon Redshift. Use Amazon Kinesis for real-time data streaming** is incorrect. Although the option suggests changing the e-commerce MySQL database to Amazon Aurora MySQL and the analytics database to Amazon Redshift, it doesn’t specifically mention utilizing the serverless variants of these databases. Leveraging Aurora Serverless MySQL and Redshift Serverless would provide better scalability and cost optimization, aligning more closely with the organization’s goal of streamlining data processing and achieving real-time analytics. Additionally, while Amazon Kinesis is suitable for real-time data streaming, it doesn’t address the requirement for efficient event-driven data flow management and integration between services in an event-driven architecture. Utilizing Amazon EventBridge would be more appropriate for managing data flows in such an architecture. Therefore, this option lacks full alignment with the requirements for transitioning to an event-driven, serverless architecture due to the omission of specific serverless database options and the choice of real-time data streaming service.

**References:**

[https://docs.aws.amazon.com/solutions/latest/constructs/aws-fargate-eventbridge.html](https://docs.aws.amazon.com/solutions/latest/constructs/aws-fargate-eventbridge.html)

[https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/event-driven-architectures.html](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/event-driven-architectures.html)

[https://aws.amazon.com/blogs/mt/moving-to-event-driven-architectures-with-serverless-event-aggregators/](https://aws.amazon.com/blogs/mt/moving-to-event-driven-architectures-with-serverless-event-aggregators/)

**Check out the following Cheat Sheets:**

[https://tutorialsdojo.com/amazon-aurora/](https://tutorialsdojo.com/amazon-aurora/)

[https://tutorialsdojo.com/amazon-redshift/](https://tutorialsdojo.com/amazon-redshift/)

[https://tutorialsdojo.com/amazon-elastic-kubernetes-service-eks/](https://tutorialsdojo.com/amazon-elastic-kubernetes-service-eks/)

[https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/](https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/)

[https://tutorialsdojo.com/aws-fargate/](https://tutorialsdojo.com/aws-fargate/)

</details>

<a id="q44"></a>

## Q44

A healthcare insurance company plans to implement a blockchain-based system to store patient records using Amazon Managed Blockchain. The system must allow patient records to be exchanged among various private entities while ensuring that the data is securely stored, transparent, and immutable.

What solution would meet these requirements?

- **A.** Store all patient data on an Amazon Managed Blockchain network. Use EC2 Arbitrum Nodes to encrypt and decrypt data before they are stored in the blockchain network. Use an Application Load Balancer (ALB) to access the EC2 nodes in an HTTPS endpoint.
- **B.** Store all patient data on an Amazon Managed Blockchain network.
- **C.** Store only the patient’s name and ID on an Amazon Managed Blockchain network. Store all other PII data off-chain in an Amazon DynamoDB table.
- **D.** Use AWS Lambda functions to store a hash of each PII data on an Amazon Managed Blockchain network. Store the PII data off-chain in an Amazon DynamoDB table.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** patient records on Managed Blockchain, secure, transparent, immutable

🪤 **Your trap:** Name and ID are still PII — any PII on an immutable chain can never be deleted

🧠 **Rule:** Blockchain + PII → store only a HASH on-chain; PII off-chain (DynamoDB).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Công ty bảo hiểm y tế ──► Amazon Managed Blockchain
        │                      (ledger phân tán, BẤT BIẾN, minh bạch với các thành viên)
        └─ dữ liệu bệnh nhân (PII) cần: an toàn + trao đổi giữa các private entity

Vấn đề: cái gì ghi lên chain thì KHÔNG xóa/sửa được
```

Đáp án đúng: **D (hash của PII lên chain, PII thật lưu off-chain trong DynamoDB)**. Anh chọn C.

#### D đúng vì sao

```
Lambda ─┬─► tạo HASH của PII ──────────► Managed Blockchain   (toàn vẹn + bất biến)
        └─► mã hóa PII (KMS) ──────────► DynamoDB (off-chain)  (lưu dữ liệu thật)

Đọc dữ liệu: lấy PII từ DynamoDB ─► băm lại ─► đối chiếu với hash on-chain
```

- **On-chain chỉ có hash:** mỗi hash là biểu diễn duy nhất của dữ liệu, không sửa được, nên vẫn chứng minh được tính toàn vẹn và bất biến mà không lộ PII.
- **Off-chain DynamoDB:** lưu PII thật, tận dụng khả năng scale và truy cập nhanh. Lambda mã hóa PII bằng KMS trước khi lưu.
- **Lambda** là lớp trung gian xử lý: băm, ghi chain, mã hóa, ghi DynamoDB.

#### Lựa chọn của Anh: C sai ở đâu

C nghe an toàn vì "chỉ để tên và ID trên chain, phần PII còn lại off-chain". Nhưng:

- **Tên và ID bệnh nhân vẫn là PII**, vẫn chịu quy định bảo vệ dữ liệu.
- Lưu ở dạng thường (plaintext) trên blockchain là không nên. Chain minh bạch với thành viên trong network và bất biến, nên PII đã ghi thì **không thể xóa**.
- Chia PII thành "nhẹ" và "nặng" không phải ranh giới đúng. Ranh giới đúng là **PII nào cũng không lên chain, chỉ hash**.

#### Các đáp án sai còn lại

- **B (lưu hết dữ liệu bệnh nhân lên chain):** blockchain minh bạch, mọi thành viên có thể truy cập, có thể không tuân thủ quy định như HIPAA yêu cầu kiểm soát riêng tư chặt chẽ.
- **A (lưu hết + EC2 Arbitrum node + ALB):** vẫn lưu toàn bộ dữ liệu lên chain. Arbitrum không phù hợp ngữ cảnh Managed Blockchain vì dịch vụ này đã lo hạ tầng. ALB phía trước EC2 node cũng không cung cấp authentication/authorization cho truy cập dữ liệu.

| Đáp án | On-chain chứa | Off-chain | Đánh giá |
|---|---|---|---|
| **D** | Hash của PII | PII trong DynamoDB | Đúng |
| C | Tên + ID (PII) | Phần PII còn lại | Vẫn lộ PII, không xóa được |
| B | Toàn bộ dữ liệu | Không có | Vi phạm riêng tư |
| A | Toàn bộ dữ liệu | Không có | Vi phạm riêng tư, kiến trúc sai |

#### Quy tắc nhớ cho thi

- **Thấy "blockchain + PII/patient data"** → **chỉ hash on-chain, PII off-chain (DynamoDB)**
- **Immutable = không xóa được** → bất kỳ PII nào lên chain đều là rủi ro
- **Tên, ID cũng là PII**, không có kiểu "PII ít nhạy cảm nên để lên chain"
- **Hash on-chain** dùng để **xác minh toàn vẹn** dữ liệu lấy từ off-chain

### TD explanation

Amazon Managed Blockchain is a fully managed service that helps build and manage Web3 applications with blockchain frameworks. With Amazon Managed Blockchain, you can securely transact and share data on a distributed and immutable ledger.

You can deploy a REST API to provide a simple interface to read and write to the blockchain network. One implementation of building REST APIs is with a serverless architecture using AWS Lambda and Amazon API Gateway. Lambda has built-in fault tolerance and provides high availability for the service itself and the functions it operates, allowing developers to focus on developing the business logic. An API Gateway provides a layer of security to AWS Lambda, allowing for features such as authentication and rate-limiting.

![image](https://media.tutorialsdojo.com/public/AmazonManagedBlockchainArchitecture.jpg)

In this scenario, sensitive patient data is processed in two main environments: on-chain and off-chain. The on-chain component involves storing a hashed version of the Personally Identifiable Information (PII), such as patient names, on Amazon Managed Blockchain. This ensures data integrity and immutability, as each hash is a unique representation of the data that cannot be altered.

For the off-chain component, the actual PII is stored in Amazon DynamoDB. This approach leverages DynamoDB’s scalability and fast access to secure and manage sensitive patient data. The reference to the on-chain hash ensures that any data retrieved can be verified against its immutable blockchain record.

AWS Lambda functions serve as the intermediary that processes the PII. First, they generate a hash of the data and store it on-chain in the blockchain. Second, Lambda functions encrypt the PII before storing it off-chain in DynamoDB. They manage the encryption process using secure algorithms and AWS Key Management Service (KMS) for key management, ensuring that the data is protected throughout its lifecycle.

Therefore, the correct answer is: **Use AWS Lambda functions to store a hash of each PII data on an Amazon Managed Blockchain network. Store the PII data off-chain in an Amazon DynamoDB table.**

The option that says: **Store all patient data on an Amazon Managed Blockchain network**is incorrect. This approach could lead to privacy concerns since blockchains are inherently transparent and could be accessible to all participants in the network. This approach may not comply with regulations such as HIPAA in the healthcare industry, which require strict privacy controls over patient information.

The option that says: **Store only the patient’s name and ID on an Amazon Managed Blockchain network. Store all other PII data off-chain in an Amazon DynamoDB table** is incorrect. Patient names and IDs are still considered personally identifiable information (PII) and are subject to data protection regulations. It is best practice not to store these in plaintext on blockchain.

The option that says: **Store all patient data on an Amazon Managed Blockchain network. Use EC2 Arbitrum Nodes to encrypt and decrypt data before they are stored in the blockchain network. Use an Application Load Balancer (ALB) to access the EC2 nodes in an HTTPS endpoint** is incorrect. Storing all patient data directly is not the best practice due to privacy and security regulations. Also, using Arbitrum is not appropriate in the context of Amazon Managed Blockchain, which already provides support for the underlying infrastructure that utilizes blockchain technology. Using an ALB with the EC2 nodes is also incorrect, as these do not provide any implementation of proper authentication and authorization for data access.

**References:**

[https://aws.amazon.com/managed-blockchain/faqs](https://aws.amazon.com/managed-blockchain/faqs)

[https://aws.amazon.com/blogs/database/building-a-serverless-blockchain-application-with-amazon-managed-blockchain/](https://aws.amazon.com/blogs/database/building-a-serverless-blockchain-application-with-amazon-managed-blockchain/)

</details>

---

# Group C — Least privilege in cross-account trust (1)

<a id="q8"></a>

## Q8

A Solutions Architect is configuring a multi-account AWS environment using AWS CloudFormation. The setup requires deploying an IAM role in the primary account (Account A), which should be assumed by an EC2 instance in a secondary account (Account B). The EC2 instance uses an instance profile that incorporates the necessary IAM role.

After deploying the CloudFormation template in Account A, the EC2 instance in Account B encounters permissions issues when attempting to assume the specified IAM role.

The Solutions Architect needs to ensure the EC2 instance in Account B can successfully assume the role created in Account A.

Which actions should the Solutions Architect take?

- **A.** In Account A, update the trust policy of the IAM role to include the ARN of the IAM role associated with the EC2 instance in Account B to allow the `AssumeRole` action.
- **B.** In the CloudFormation template, include both 'CAPABILITY_IAM' and 'CAPABILITY_NAMED_IAM' capabilities.
- **C.** In Account B, update the trust policy of the IAM role to include the primary Account A as a trusted entity and specify the EC2 instance as the principal.
- **D.** In Account A, modify the trust policy of the IAM role to allow the `AssumeRole` action from Account B’s root principal.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** EC2 in Account B must assume role in Account A; permission error

🪤 **Your trap:** Trusting Account B's root lets ANY identity in B assume the role — not least privilege (twin options: root vs role ARN)

🧠 **Rule:** Cross-account: edit the trust policy in the role's own account (A) and trust the specific role ARN of the caller.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Account A (role được tạo bằng CloudFormation)     Account B
┌──────────────────────────┐                  ┌──────────────────────────┐
│ IAM Role "target"        │ ◄── AssumeRole ──│ EC2 + instance profile   │
│  trust policy: ???       │                  │  (IAM role của EC2)      │
└──────────────────────────┘                  └──────────────────────────┘

Lỗi: EC2 ở B không assume được role ở A (thiếu permission)
```

Đáp án đúng: **A (sửa trust policy ở Account A, trust ARN role cụ thể của EC2 ở B)**. Anh chọn D (trust root của Account B). A và D là "twin options", khác nhau ở độ hẹp của principal.

#### Nguyên tắc cốt lõi

- **Trust policy** gắn với role, quy định ai (account, user, role, service) được assume. Role mới tạo mà chưa có statement thì **không ai assume được**.
- Role nằm ở **Account A** → trust policy sửa ở **Account A**, nơi role được tạo.
- Principal nên là **ARN của IAM role gắn với EC2 instance ở Account B** → đúng "least privilege".

#### Lựa chọn của Anh: D sai ở đâu

D đúng hướng: sửa ở Account A, cho phép `AssumeRole` từ B. Nhưng principal là **root của Account B** nghĩa là cho phép **mọi identity trong Account B** (có quyền sts:AssumeRole phía B) assume role ở A. Không theo least privilege. TD chốt: nên cấp cho IAM role hoặc user **cụ thể**.

```
D: Principal = arn:aws:iam::<B>:root           ─► mọi identity trong B (nếu được cấp quyền) → quá rộng
A: Principal = arn:aws:iam::<B>:role/<ec2-role> ─► chỉ role của EC2 đó → đúng least privilege
```

#### Các đáp án sai còn lại

- **C (sửa trust policy ở Account B):** trust policy của role được quản lý ở account **tạo ra role** (A), không phải account đi assume (B). Ngoài ra "EC2 instance làm principal" không phải cách khai báo đúng.
- **B (CAPABILITY_IAM + CAPABILITY_NAMED_IAM):** các capability này cần khi CloudFormation tạo/cập nhật IAM resource, giúp deployment thành công. Chúng **không xử lý** lỗi assume role cross-account (deployment ở A đã chạy xong).

| Đáp án | Sửa ở đâu | Principal | Kết quả |
|---|---|---|---|
| **A** | Account A | ARN role cụ thể của EC2 ở B | Đúng, least privilege |
| D | Account A | Root của Account B | Quá rộng |
| C | Account B | Sai account | Sai chỗ |
| B | Template | Không đổi trust | Không liên quan |

#### Lưu ý thực tế (đề không hỏi nhưng dễ vấp)

- Cross-account cần **hai phía**: trust policy ở role đích (A) cho phép principal, và phía B (identity-based policy của role EC2) phải cho phép hành động `sts:AssumeRole` trên role ở A. Đề đã chọn đáp án tập trung vào trust policy.

#### Quy tắc nhớ cho thi

- **Thấy "assume role cross-account"** → **sửa trust policy ở account chứa role** (account được truy cập)
- **Trust root của account vs ARN role cụ thể** → chọn **ARN cụ thể** khi đề nhấn mạnh least privilege
- **Root principal = cả account**, rộng hơn nhiều so với một role
- **CAPABILITY_IAM / NAMED_IAM** → chỉ để CloudFormation được phép tạo IAM resource, không sửa lỗi trust

### TD explanation

**IAM Roles and Cross-Account Access:** An IAM role is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumed by anyone who needs it. Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session.

You can use IAM Roles to delegate access to users, applications, or services that don’t normally have access to your AWS resources. For example, you might want to grant users in your AWS account access to resources they don’t usually have or grant users in one AWS account access to resources in another account.

An **instance profile** is a container that passes an AWS Identity and Access Management (IAM) role to an Amazon Elastic Compute Cloud (EC2) instance. It is used to securely provide temporary AWS credentials to the EC2 instance, allowing it to access other AWS services.

![image](https://media.tutorialsdojo.com/public/td-iam-trust-policy-assumerole-26-June-2024.png)

The issue in the given scenario is that the EC2 instance in Account B is unable to assume the IAM role in Account A due to insufficient permissions. This problem can be resolved by modifying the trust policy of the IAM role in Account A to grant the necessary permissions to Account B.

A **trust policy** is associated with an IAM role, which defines the principals (accounts, users, or services) that can assume the role. By default, a newly created role does not have any trust policy statements, which means that no principal can assume the role.

By adding the ARN of the IAM role associated with the EC2 instance in Account B as a trusted entity in the trust policy of the IAM role in Account A, the EC2 instance will be able to assume the role successfully.

Hence, the correct answer is: **In Account A, update the trust policy of the IAM role to include the ARN of the IAM role associated with the EC2 instance in Account B to allow the `AssumeRole` action.**

The option that says: **In Account B, update the trust policy of the IAM role to include the primary Account A as a trusted entity and specify the EC2 instance as the principal** is incorrect because the trust policy of an IAM role is managed in the account where the role is created, not in the account that assumes the role. In this case, the IAM role is created in Account A, so the trust policy should be updated in Account A, not in Account B.

The option that says: **In Account A, modify the trust policy of the IAM role to allow the `AssumeRole` action from Account B’s root principal** is incorrect because allowing the `AssumeRole` action from Account B’s root principal would allow any identities in Account B to assume the IAM role in Account A. Such strategy does not follow the principle of least privilege. It’s better to grant permissions to specific IAM roles or users.

The option that says: **In the CloudFormation template, include both ‘CAPABILITY_IAM’ and ‘CAPABILITY_NAMED_IAM’ capabilities** is incorrect. While these capabilities are required when creating or updating IAM resources using CloudFormation, they do not directly address the issue of cross-account role assumption. Including these capabilities ensures that the CloudFormation deployment succeeds, but it does not resolve the permissions issues encountered when the EC2 instance in Account B attempts to assume the role in Account A.

**References:**

[https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

**Check out this AWS IAM Cheat Sheet:**

[https://tutorialsdojo.com/aws-identity-and-access-management-iam/](https://tutorialsdojo.com/aws-identity-and-access-management-iam/)

</details>
