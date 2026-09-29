# TD Set 1 — Wrong Answer Review (29 questions)

Source: `TD_SAP_Review_Set1_Full.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td_set_1_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q5](#q5) | ✅ 09-29 | ☐ | ☐ |
| A | [Q36](#q36) | ✅ 09-29 | ☐ | ☐ |
| A | [Q27](#q27) | ✅ 09-29 | ☐ | ☐ |
| A | [Q61](#q61) | ✅ 09-29 | ☐ | ☐ |
| B | [Q68](#q68) | ✅ 09-29 | ☐ | ☐ |
| B | [Q22](#q22) | ✅ 09-29 | ☐ | ☐ |
| B | [Q47](#q47) | ✅ 09-29 | ☐ | ☐ |
| B | [Q74](#q74) | ✅ 09-29 | ☐ | ☐ |
| C | [Q12](#q12) | ✅ 09-29 | ☐ | ☐ |
| C | [Q13](#q13) | ✅ 09-29 | ☐ | ☐ |
| C | [Q53](#q53) | ✅ 09-29 | ☐ | ☐ |
| C | [Q73](#q73) | ✅ 09-29 | ☐ | ☐ |
| D | [Q28](#q28) | ✅ 09-29 | ☐ | ☐ |
| D | [Q40](#q40) | ✅ 09-29 | ☐ | ☐ |
| D | [Q55](#q55) | ✅ 09-29 | ☐ | ☐ |
| E | [Q10](#q10) | ✅ 09-29 | ☐ | ☐ |
| E | [Q14](#q14) | ✅ 09-29 | ☐ | ☐ |
| E | [Q17](#q17) | ✅ 09-29 | ☐ | ☐ |
| E | [Q25](#q25) | ✅ 09-29 | ☐ | ☐ |
| F | [Q64](#q64) | ☐ | ☐ | ☐ |
| F | [Q21](#q21) | ☐ | ☐ | ☐ |
| F | [Q65](#q65) | ☐ | ☐ | ☐ |
| F | [Q72](#q72) | ☐ | ☐ | ☐ |
| F | [Q69](#q69) | ☐ | ☐ | ☐ |
| F | [Q62](#q62) | ☐ | ☐ | ☐ |
| G | [Q57](#q57) | ☐ | ☐ | ☐ |
| G | [Q26](#q26) | ☐ | ☐ | ☐ |
| G | [Q29](#q29) | ☐ | ☐ | ☐ |
| G | [Q42](#q42) | ☐ | ☐ | ☐ |

---

# Group A — Hybrid networking & DNS (4)

<a id="q5"></a>

## Q5

A multinational investment bank has a hybrid cloud architecture that uses a single 1 Gbps AWS Direct Connect connection to integrate its on-premises network to AWS Cloud. The bank has a total of 10 VPCs, which are all connected to its on-premises data center via the same Direct Connect connection that the engineer manages. Based on the recent IT audit, the existing network setup has a single point of failure, which needs to be addressed immediately. The engineer is also evaluating AWS VPN as a potential backup connectivity option for the hybrid network.
Which of the following is the MOST cost-effective solution that should be implemented in order to improve the connection redundancy of the hybrid network?

- **A.** Establish VPN tunnels from your on-premises data center to each of the 10 VPCs. Terminate each VPN tunnel connection at the virtual private gateway (VGW) of the respective VPC. Configure BGP for route management.
- **B.** Establish another 1 Gbps Direct Connect connection with corresponding private Virtual Interfaces (VIFs) to connect all of the 10 VPCs individually. Set up a Border Gateway Protocol (BGP) peering session for all of the VIFs.
- **C.** Establish another 1 Gbps Direct Connect connection using a public Virtual Interface (VIF). Prepare a VPN tunnel that will terminate on the virtual private gateway (VGW) of the respective VPC using the public VIF. Handle the failover to the VPN connection through the use of BGP.
- **D.** Establish a new point-to-point Multiprotocol Label Switching (MPLS) connection to all of your 10 VPCs. Configure BGP to use this new connection with an active/passive routing.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** 10 VPCs on one DX = single point of failure; evaluating VPN as backup; MOST cost-effective

🪤 **Your trap:** MPLS can't connect directly to VPCs — needs colocation at a DX location anyway; far pricier than VPN

🧠 **Rule:** Cheapest DX backup → Site-to-Site VPN to each VGW (BGP prefers DX, fails over to VPN). Second DX = max resilience, not cheapest.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises DC                         AWS (10 VPCs)
┌─────────────────┐   1x DX 1Gbps     ┌───────┬───────┬─── ... ──┐
│  Ngân hàng đa    │ ═══════════════► │ VPC1  │ VPC2  │   VPC10  │
│  quốc gia        │  (SINGLE POINT   └───────┴───────┴──────────┘
└─────────────────┘    OF FAILURE)
Yêu cầu: thêm redundancy, MOST COST-EFFECTIVE, đang xét VPN làm backup
```

Đáp án đúng: **A** — dựng VPN tunnel từ DC đến VGW của từng VPC, dùng BGP để quản lý route. Anh chọn **D** (MPLS).

#### Vì sao A đúng

DX là kết nối vật lý, dựng thêm một DX thứ hai để dự phòng thì rất tốn kém và vẫn mất thời gian lắp đặt. Theo whitepaper AWS, cách "cost-effective" chuẩn để backup cho DX chính là **Site-to-Site VPN** chạy qua Internet, terminate tại VGW, và dùng **BGP** để route ưu tiên qua DX, tự động failover sang VPN khi DX rớt. VPN là dịch vụ managed, trả theo giờ + data, không cần đầu tư hạ tầng mới — đúng nghĩa "MOST cost-effective".

#### Vì sao D (lựa chọn của anh) sai

MPLS nghe có vẻ là giải pháp mạng doanh nghiệp "chuyên nghiệp", nhưng **không thể kết nối trực tiếp vào VPC**. Muốn tích hợp MPLS với AWS, anh vẫn phải đặt Customer Gateway (CGW) tại **cùng địa điểm colocation với DX location** để tạo cross-connect vật lý — nghĩa là vẫn phải dùng Direct Connect làm cầu nối, tốn thêm phí colocation + thiết bị. Vì vậy MPLS vừa không tự thân kết nối được, vừa đắt hơn nhiều so với VPN.

#### Các lựa chọn sai khác

- **B — DX thứ hai (private VIF) cho cả 10 VPC:** Về mặt kỹ thuật khả thi và cho resilience cao nhất, nhưng chi phí một đường DX 1Gbps mới là rất lớn — không phải phương án "cost-effective" nhất. Đây là bẫy "đúng nhưng không rẻ nhất".
- **C — DX thứ hai qua public VIF + VPN:** Vẫn phải trả tiền cho một đường DX mới (chỉ khác là dùng public VIF thay vì private) → tốn kém tương đương B, không giải quyết được yêu cầu "cost-effective".

#### So sánh các phương án

| Phương án | Cơ chế | Chi phí | Redundancy |
|---|---|---|---|
| **A. VPN qua Internet + BGP** | Site-to-Site VPN đến VGW mỗi VPC | Thấp (managed, theo giờ) | Đủ dùng làm backup |
| B/C. DX thứ hai | Đường DX vật lý mới | Rất cao | Cao nhất nhưng không rẻ |
| D. MPLS | Cần colocation + DX location | Cao, phức tạp | Không tự kết nối VPC được |

#### Lưu ý thực tế

- VPN không đạt băng thông tương đương DX 1Gbps — chỉ chấp nhận được nếu ứng dụng chịu được bandwidth thấp hơn khi failover.
- BGP tự ưu tiên đường có metric/AS-path tốt hơn (thường DX) và tự chuyển sang VPN khi DX down, không cần cấu hình thủ công failover.

#### Quy tắc nhớ cho thi

- **"Backup rẻ nhất cho DX"** → **Site-to-Site VPN đến VGW + BGP**, không phải DX thứ hai.
- **"Second DX"** → resilience tối đa, nhưng KHÔNG phải đáp án khi đề hỏi "cost-effective".
- **"MPLS + AWS"** → luôn cần colocation tại DX location, không tự nối vào VPC được.

### TD explanation

With AWS Direct Connect plus VPN, you can combine one or more AWS Direct Connect dedicated network connections with the Amazon VPC VPN. This combination provides an IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, and provides a more consistent network experience than Internet-based VPN connections.
You can use AWS Direct Connect to establish a dedicated network connection between your network and create a logical connection to public AWS resources, such as an Amazon virtual private gateway IPsec endpoint. This solution combines the AWS managed benefits of the VPN solution with low latency, increased bandwidth, more consistent benefits of the AWS Direct Connect solution, and an end-to-end, secure IPsec connection.

It costs a lot of money to establish a Direct Connect connection which you rarely use. For a more cost-effective solution, you can configure a backup VPN connection for failover with your AWS Direct Connect connection.
If you want a short-term or lower-cost solution, you might consider configuring a hardware VPN as a failover option for a Direct Connect connection. VPN connections are not designed to provide the same level of bandwidth available to most Direct Connect connections. Ensure that your use case or application can tolerate a lower bandwidth if you are configuring a VPN as a backup to a Direct Connect connection.
Hence, the correct answer is: Establish VPN tunnels from your on-premises data center to each of the 10 VPCs. Terminate each VPN tunnel connection at the virtual private gateway (VGW) of the respective VPC. Configure BGP for route management.
The following options are incorrect:
– Establish another 1 Gbps Direct Connect connection using a public Virtual Interface (VIF). Prepare a VPN tunnel that will terminate on the virtual private gateway (VGW) of the respective VPC using the public VIF. Handle the failover to the VPN connection through the use of BGP.
– Establish another 1 Gbps Direct Connect connection with corresponding private Virtual Interfaces (VIFs) to connect all of the 10 VPCs individually. Set up a Border Gateway Protocol (BGP) peering session for all of the VIFs.
Establishing yet another 1 Gbps AWS Direct Connect connection is not a cost-effective solution. It is better to establish a VPN connection instead as a backup.
The option that says: Establishing a new point-to-point Multiprotocol Label Switching (MPLS) connection to all of your 10 VPCs and Configuring BGP to use this new connection with an active/passive routing is incorrect because you can’t directly connect to your Multiprotocol Label Switching (MPLS) to AWS. To integrate your MPLS infrastructure, you need to set up a colocation with Direct Connect by placing the CGW in the same physical facility as the Direct Connect location, which will facilitate a local cross-connect between the CGW and AWS devices.

References:
https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/vpn-connection-as-a-backup-to-aws-dx-connection-example.html
https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-plus-vpn-network-to-amazon.html
https://aws.amazon.com/answers/networking/aws-network-connectivity-over-mpls/

Check out this AWS Direct Connect Cheat Sheet:
https://tutorialsdojo.com/aws-direct-connect/

</details>

<a id="q36"></a>

## Q36

A stocks brokerage firm hosts its legacy application on Amazon EC2 in a private subnet of its Amazon VPC. The application is accessed by the employees from their corporate laptops through a proprietary desktop program. The company network is peered with the AWS Direct Connect (DX) connection to provide a fast and reliable connection to the private EC2 instances inside the VPC. To comply with the strict security requirements of financial institutions, the firm is required to encrypt its network traffic that flows from the employees’ laptops to the resources inside the VPC.
Which of the following solution will comply with this requirement while maintaining the consistent network performance of Direct Connect?

- **A.** Using the current Direct Connect connection, create a new private virtual interface and input the network prefixes that you want to advertise. Create a new site-to-site VPN connection to the VPC with the BGP protocol using the DX connection. Configure the company network to route employee traffic to this VPN.
- **B.** Using the current Direct Connect connection, create a new public virtual interface and input the network prefixes that you want to advertise. Create a new site-to-site VPN connection to the VPC over the Internet. Configure the employees’ laptops to connect to this VPN.
- **C.** Using the current Direct Connect connection, create a new public virtual interface and input the network prefixes that you want to advertise. Create a new site-to-site VPN connection to the VPC with the BGP protocol using the DX connection. Configure the company network to route employee traffic to this VPN.
- **D.** Using the current Direct Connect connection, create a new private virtual interface and input the network prefixes that you want to advertise. Create a new site-to-site VPN connection to the VPC over the Internet. Configure the employees’ laptops to connect to this VPN.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** encrypt laptop→VPC traffic; keep DX consistent performance

🪤 **Your trap:** Private VIF can't carry the VPN — VPN endpoints are AWS public IPs

🧠 **Rule:** IPsec VPN over Direct Connect → PUBLIC VIF + Site-to-Site VPN to the VGW (or Transit VIF + TGW private IP VPN).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Laptop nhân viên (Corporate network)          VPC (private subnet)
        │                                            │
        │   Direct Connect (private VIF hiện có)     │
        └──────────────► EC2 app ◄────────────────────┘
Yêu cầu: MÃ HÓA traffic laptop → VPC, vẫn giữ hiệu năng ổn định của DX
```

Đáp án đúng: **C** — tạo **public VIF** mới trên DX hiện có, dựng Site-to-Site VPN (BGP) qua DX đó, route traffic nhân viên qua VPN này. Anh chọn **A** (dùng private VIF).

#### Vì sao C đúng

Site-to-Site VPN endpoint (VGW) là một **địa chỉ IP public** của AWS. Muốn VPN "đi qua" đường Direct Connect (thay vì qua Internet công khai) để giữ độ trễ ổn định và không phải trả thêm băng thông Internet, DX buộc phải quảng bá được các prefix public đó — mà chỉ **public VIF** làm được việc này (nó cho phép truy cập tất cả AWS public IP addresses). Vì vậy: public VIF (để "mang" traffic VPN) + Site-to-Site VPN (để mã hóa) + BGP (route) = vừa an toàn vừa giữ hiệu năng DX.

#### Vì sao A (lựa chọn của anh) sai

**Private VIF chỉ dùng để nói chuyện với private IP bên trong VPC** (EC2, load balancer nội bộ...) — nó không mang được kết nối tới VGW public endpoint để dựng VPN. TD explanation nói rõ: "you must use a public virtual interface for your AWS Direct Connect (DX) connection... You won't be able to establish an encrypted VPN along with your DX connection if you create a private virtual interface." Tức là chọn private VIF thì về mặt kỹ thuật **không dựng được VPN qua DX** — không phải chỉ là "kém hơn", mà là không khả thi.

⚠️ **Lỗi lặp lại:** Đây là lần thứ 4 anh vấp phải khái niệm "public VIF cho VPN over Direct Connect" — cần khắc sâu quy tắc: hễ đề nói "mã hóa traffic qua DX" hoặc "VPN kết hợp DX" → luôn là **public VIF**, private VIF chỉ dùng khi kết nối trực tiếp thuần túy tới tài nguyên VPC không cần mã hóa thêm.

#### Các lựa chọn sai khác

- **B — public VIF + VPN qua Internet:** Public VIF đúng, nhưng VPN lại đi qua Internet chứ không qua DX → mất luôn lợi ích "hiệu năng ổn định của DX" mà đề yêu cầu giữ lại.
- **D — private VIF + VPN qua Internet:** Sai cả hai tiêu chí: VIF sai loại (không dựng VPN được) và VPN lại đi qua Internet, không giữ hiệu năng DX.

#### So sánh các phương án

| Phương án | Loại VIF | Đường đi VPN | Có đúng không |
|---|---|---|---|
| **C (đúng)** | Public VIF | Qua DX (BGP) | ✅ Mã hóa + giữ hiệu năng DX |
| A (anh chọn) | Private VIF | Qua DX | ❌ Private VIF không dựng được VPN |
| B | Public VIF | Qua Internet | ❌ Mất hiệu năng ổn định của DX |
| D | Private VIF | Qua Internet | ❌ Sai cả VIF và đường đi |

#### Lưu ý thực tế

- Ngoài public VIF, còn có cách khác dùng **Transit VIF + Transit Gateway + VPN với private IP** (AWS Direct Connect + Transit Gateway) để mã hóa qua DX mà route hoàn toàn bằng private IP — nhưng đây không phải lựa chọn có trong đề này.

#### Quy tắc nhớ cho thi

- **"Mã hóa traffic qua Direct Connect"** → phải dùng **public VIF** (hoặc transit VIF + TGW) để mang VPN, không phải private VIF.
- **"Private VIF"** → chỉ kết nối thẳng tới private IP trong VPC, không mang được VPN endpoint.
- **"VPN + DX cùng lúc, giữ hiệu năng DX"** → VPN phải chạy **qua DX**, không phải qua Internet.

### TD explanation

To connect to services such as EC2 using just Direct Connect you need to create a private virtual interface. However, if you want to encrypt the traffic flowing through Direct Connect, you will need to use the public virtual interface of DX to create a VPN connection that will allow access to AWS services such as S3, EC2, and other services.
To connect to AWS resources that are reachable by a public IP address (such as an Amazon Simple Storage Service bucket) or AWS public endpoints, use a public virtual interface. With a public virtual interface, you can:
– Connect to all AWS public IP addresses globally.
– Create public virtual interfaces in any DX location to receive Amazon’s global IP routes.
– Access publicly routable Amazon services in any AWS Region (except for the AWS China Region).

To connect to your resources hosted in an Amazon Virtual Private Cloud (Amazon VPC) using their private IP addresses, use a private virtual interface. With a private virtual interface, you can:
– Connect VPC resources (such as Amazon Elastic Compute Cloud (Amazon EC2) instances or load balancers) on your private IP address or endpoint.
– Connect a private virtual interface to a DX gateway. Then, associate the DX gateway with one or more virtual private gateways in any AWS Region (except the AWS China Region).
– Connect to multiple VPCs in any AWS Region (except the AWS China Region), because a virtual private gateway is associated with a single VPC.
If you want to establish a virtual private network (VPN) connection from your company network to an Amazon Virtual Private Cloud (Amazon VPC) over an AWS Direct Connect (DX) connection, you must use a public virtual interface for your DX connection.
Therefore, the correct answer is: Using the current Direct Connect connection, create a new public virtual interface, and input the network prefixes that you want to advertise. Create a new site-to-site VPN connection to the VPC with the BGP protocol using the DX connection. Configure the company network to route employee traffic to this VPN.
The option that says: Using the current Direct Connect connection, create a new private virtual interface, and input the network prefixes that you want to advertise. Create a new site-to-site VPN connection to the VPC with the BGP protocol using the DX connection. Configure the employees’ laptops to connect to this VPN is incorrect because you must use a public virtual interface for your AWS Direct Connect (DX) connection and not a private one. You won’t be able to establish an encrypted VPN along with your DX connection if you create a private virtual interface.
The following options are incorrect because you need to establish the VPN connection through the DX connection, and not over the Internet.
– Using the current Direct Connect connection, create a new public virtual interface, and input the network prefixes that you want to advertise. Create a new site-to-site VPN connection to the VPC over the internet. Configure the employees’ laptops to connect to this VPN.
– Using the current Direct Connect connection, create a new private virtual interface, and input the network prefixes that you want to advertise. Create a new site-to-site VPN connection to the VPC over the internet. Configure the company network to route employee traffic to this VPN.

References:
https://aws.amazon.com/premiumsupport/knowledge-center/public-private-interface-dx/
https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-vpn.html
https://aws.amazon.com/premiumsupport/knowledge-center/create-vpn-direct-connect/

Check out this AWS Direct Connect Cheat Sheet:
https://tutorialsdojo.com/aws-direct-connect/

</details>

<a id="q27"></a>

## Q27

A company wants to implement a multi-account strategy across several research facilities. Approximately 50 teams will each require a dedicated AWS account. The organization has a centralized Cloud Center of Excellence team that manages all domains and subdomains, so the company needs a streamlined DNS architecture that simplifies private DNS management across accounts. The solution must allow private DNS to be shared among virtual private clouds (VPCs) in different AWS accounts.
Which of the following solutions has the LEAST complex DNS architecture and allows all VPCs to resolve the needed domain names?

- **A.** On AWS Resource Access Manager (RAM), set up a shared services VPC on your central account. Create a peering from this VPC to each VPC on the other accounts. On Amazon Route 53, create a private hosted zone associated with the shared services VPC. Manage all domains and subdomains on this hosted zone. On each of the other AWS Accounts, create a Route 53 private hosted zone and configure the Name Server entry to use the DNS of the central account.
- **B.** Set up AWS Direct Connect connections among the VPCs of each account using private virtual interfaces. Ensure that each VPC has the attributes enableDnsHostnames and enableDnsSupport set to “FALSE”. On Amazon Route 53, create a private hosted zone associated with the central account’s VPC. Manage all domains and subdomains on this hosted zone. Programmatically associate the VPCs from other accounts with this hosted zone.
- **C.** On AWS Resource Access Manager (RAM), set up a shared services VPC on your central account. Set up VPC peering from this VPC to each VPC on the other accounts. On Amazon Route 53, create a private hosted zone associated with the shared services VPC. Manage all domains and subdomains on this zone. Programmatically associate the VPCs from other accounts with this hosted zone.
- **D.** Set up a VPC peering connection among the VPC of each account. Ensure that the each VPC has the attributes enableDnsHostnames and enableDnsSupport set to “TRUE”. On Amazon Route 53, create a private hosted zone associated with the central account’s VPC. Manage all domains and subdomains on this hosted zone. On each of the other AWS Accounts, create a Route 53 private hosted zone and configure the Name Server entry to use the DNS of the central account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** ~50 accounts; central team owns all domains; share private DNS across VPCs in different accounts; LEAST complex

🪤 **Your trap:** Private hosted zones can't be delegated via NS records to another account's zone — names won't resolve

🧠 **Rule:** Cross-account private DNS → one PHZ in the central account + programmatically associate other accounts' VPCs (create-vpc-association-authorization + associate-vpc-with-hosted-zone).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
                    Central account (Cloud CoE team)
                    ┌────────────────────────────┐
                    │  Shared services VPC       │
                    │  Route 53 Private Hosted   │
                    │  Zone (quản lý mọi domain) │
                    └───────────┬────────────────┘
                     VPC peering│  + programmatic
                                │    VPC association
        ┌───────────┬──────────┼──────────┬───────────┐
      VPC (team1)  VPC (team2)  ...     VPC (team~50, các account khác)
Yêu cầu: ~50 account, DNS LEAST complex, share private DNS xuyên account
```

Đáp án đúng: **C** — shared services VPC ở account trung tâm + VPC peering + một Private Hosted Zone (PHZ) duy nhất, rồi **programmatically associate** VPC của các account khác với PHZ đó. Anh chọn **D**.

#### Vì sao C đúng

Route 53 Private Hosted Zone chỉ trả lời DNS cho các VPC **được associate trực tiếp** với nó. Với nhiều account, cách chuẩn là dùng API `create-vpc-association-authorization` (từ account sở hữu PHZ) + `associate-vpc-with-hosted-zone` (từ account có VPC) để mỗi VPC ở account khác tự "join" vào đúng một PHZ trung tâm. Đây là kiến trúc DNS đơn giản nhất: **một PHZ, nhiều VPC association** — không cần tạo PHZ riêng ở từng account, không cần đồng bộ record giữa các zone.

#### Vì sao D (lựa chọn của anh) sai

D dùng NS record: mỗi account tự tạo PHZ riêng, rồi set NS record trỏ về DNS server của account trung tâm — đây là mô hình "delegation" kiểu DNS public thông thường (zone cha → zone con qua NS). Nhưng **Private Hosted Zone của Route 53 không hỗ trợ delegation qua NS record** giữa các zone như public zone làm được. Route 53 Resolver trong một VPC chỉ tự động trả lời cho các PHZ mà VPC đó **được associate**, nó không "đi theo" NS record để hỏi zone khác. Vì vậy dù NS record được set đúng, các VPC ở account khác vẫn **không resolve được** tên miền trong PHZ trung tâm — về bản chất đây là kiến trúc không hoạt động, chứ không chỉ là "phức tạp hơn".

#### Các lựa chọn sai khác

- **A** — Giống C nhưng dùng NS record thay vì programmatic association ở bước cuối → mắc lỗi tương tự D: chỉ set NS record là không đủ, PHZ không tự "nghe" domain qua NS delegation.
- **B** — Dùng AWS Direct Connect để nối các VPC (sai công cụ — DX là kết nối on-premises↔AWS, không phải cách nối VPC↔VPC) và set `enableDnsHostnames`/`enableDnsSupport` = **FALSE**, trong khi hai attribute này mặc định là TRUE và **cần TRUE** để VPC resolver truy vấn Route 53 — set FALSE sẽ làm hỏng luôn khả năng DNS resolve trong VPC.

#### So sánh các phương án

| Phương án | Kết nối VPC | Cách "share" DNS | Có hoạt động? |
|---|---|---|---|
| **C (đúng)** | VPC peering từ shared VPC | Programmatic VPC association vào 1 PHZ | ✅ Đơn giản nhất, hoạt động |
| A | VPC peering từ shared VPC | NS record trỏ về central DNS | ❌ PHZ không hỗ trợ NS delegation |
| D (anh chọn) | VPC peering trực tiếp giữa tất cả VPC | NS record | ❌ Tương tự A, và phải peering full-mesh ~50 VPC |
| B | AWS Direct Connect | Programmatic association | ❌ Sai công cụ kết nối, sai DNS attribute |

#### Lưu ý thực tế

- `enableDnsHostnames` và `enableDnsSupport` mặc định là **TRUE** khi tạo VPC — chỉ cần nhớ chúng phải TRUE để Resolver hoạt động, không phải là bước phải chủ động set.
- Với ~50 account, thực tế nên dùng **Route 53 Resolver rules chia sẻ qua AWS RAM** hoặc **AWS Organizations + Route 53 Profiles** để tránh peering full-mesh, nhưng trong các lựa chọn của đề, VPC peering + associate PHZ là mô hình đơn giản nhất được đưa ra.

#### Quy tắc nhớ cho thi

- **"Share private DNS xuyên nhiều account"** → **một PHZ trung tâm + programmatic VPC association**, không phải NS record.
- **"NS record cho Private Hosted Zone"** → luôn là bẫy, PHZ không delegate qua NS như public zone.
- **enableDnsHostnames/enableDnsSupport** → phải là **TRUE** (mặc định), không phải FALSE.

### TD explanation

When you create a VPC using Amazon VPC, Route 53 Resolver automatically answers DNS queries for local VPC domain names for EC2 instances (ec2-192-0-2-44.compute-1.amazonaws.com) and records in private hosted zones (acme.example.com). For all other domain names, Resolver performs recursive lookups against public name servers.
You also can integrate DNS resolution between Resolver and DNS resolvers on your network by configuring forwarding rules. Your network can include any network that is reachable from your VPC, such as the following:
– The VPC itself
– Another peered VPC
– An on-premises network that is connected to AWS with AWS Direct Connect, a VPN, or a network address translation (NAT) gateway

VPC sharing allows customers to share subnets with other AWS accounts within the same AWS Organization. This is a very powerful concept that allows for a number of benefits:
– Separation of duties: centrally controlled VPC structure, routing, IP address allocation.
– Application owners continue to own resources, accounts, and security groups.
– VPC sharing participants can reference each other’s security group IDs.
– Efficiencies: higher density in subnets, efficient use of VPNs and AWS Direct Connect.
– Hard limits can be avoided, for example, 50 VIFs per AWS Direct Connect connection through simplified network architecture.
– Costs can be optimized through reuse of NAT gateways, VPC interface endpoints, and intra-Availability Zone traffic.
Essentially, we can decouple accounts and networks. In this model, the account that owns the VPC (owner) shares one or more subnets with other accounts (participants) that belong to the same organization from AWS Organizations. After a subnet is shared, the participants can view, create, modify, and delete their application resources in the subnets shared with them. Participants cannot view, modify, or delete resources that belong to other participants or the VPC owner. You can simplify network topologies by interconnecting shared Amazon VPCs using connectivity features, such as AWS PrivateLink, AWS Transit Gateway, and Amazon VPC peering.
Therefore, the correct answer is: On AWS Resource Access Manager (RAM), set up a shared services VPC on your central account. Set up VPC peering from this VPC to each VPC on the other accounts. On Amazon Route 53, create a private hosted zone associated with the shared services VPC. Manage all domains and subdomains on this zone. Programmatically associate the VPCs from other accounts with this hosted zone.
The option that says: Set up AWS Direct Connect connections among the VPCs of each account using private virtual interfaces. Ensure that each VPC has the attributes <code>enableDnsHostnames</code> and <code>enableDnsSupport</code> set to “FALSE”. On Amazon Route 53, create a private hosted zone associated with the central account’s VPC. Manage all domains and subdomains on this hosted zone. Programmatically associate the VPCs from other accounts with this hosted zone is incorrect because simply using AWS Direct Connect is not a suitable service to connect the various VPCs. In addition, attributes enableDnsHostnames and enableDnsSupport are set to “TRUE” by default and are needed for VPC resources to query Route 53 zone entries.
The option that says: Set up a VPC peering connection among the VPC of each account. Ensure that each VPC has the attributes enableDnsHostnames and enableDnsSupport set to “TRUE”. On Amazon Route 53, create a private hosted zone associated with the central account’s VPC. Manage all domains and subdomains on this hosted zone. On each of the other AWS Accounts, create a Route 53 private hosted zone and configure the Name Server entry to use the DNS of the central account is incorrect. You won’t be able to resolve the hosted private zone entries even if you configure your Route 53 zone NS entry to use the central account’s DNS servers.
The option that says: On AWS Resource Access Manager (RAM), set up a shared services VPC on your central account. Create a peering from this VPC to each VPC on the other accounts. On Amazon Route 53, create a private hosted zone associated with the shared services VPC. Manage all domains and subdomains on this hosted zone. On each of the other AWS Accounts, create a Route 53 private hosted zone and configure the Name Server entry to use the DNS of the central account is incorrect. Although creating the shared services VPC is a good solution, configuring Route 53 Name Server (NS) records to point to the shared services VPC’s Route 53 is just not enough. You need to associate the VPCs from other accounts to the hosted zone on the central account.

References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html
https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple-accounts-and-vpc-management/
https://aws.amazon.com/blogs/security/simplify-dns-management-in-a-multiaccount-environment-with-route-53-resolver/

Check out these Amazon VPC and Route 53 Cheat Sheets:
https://tutorialsdojo.com/amazon-vpc/
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q61"></a>

## Q61

A company develops Docker containers to host web applications on its on-premises data center. The company wants to migrate its workload to the cloud and use AWS Fargate. The solutions architect has created the necessary task definition and service for the Fargate cluster. For security requirements, the cluster is placed on a private subnet in the VPC that has no direct connection outside of the VPC. The following error is received when trying to launch the Fargate task:
CannotPullContainerError: API error (500): Get https://111122223333.dkr.ecr.us-east-1.amazonaws.com/v2/: net/http: request canceled while waiting for connection
Which of the following options should be able to fix this issue?

- **A.** Update the AWS Fargate task definition and set the auto-assign public IP option to ENABLED. Create a gateway VPC endpoint for Amazon ECR. Update the route table to allow AWS Fargate to pull images on Amazon ECR via the endpoint.
- **B.** Update the AWS Fargate task definition and set the auto-assign public IP option to DISABLED. Launch a NAT gateway on the public subnet of the VPC and update the route table of the private subnet to route requests to the Internet.
- **C.** This is a limitation of the “awsvpc” network mode. Update the AWS Fargate definition to use the “bridge” network mode instead to allow connections to the Internet.
- **D.** Update the AWS Fargate task definition and set the auto-assign public IP option to DISABLED. Launch a NAT gateway on the private subnet of the VPC and update the route table of the private subnet to route requests to the Internet.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** Fargate in private subnet, no outside connection; CannotPullContainerError to ECR

🪤 **Your trap:** Public IP is useless without an IGW; ECR needs INTERFACE endpoints (ecr.api + ecr.dkr) + S3 gateway endpoint, not a single gateway endpoint

🧠 **Rule:** Private Fargate can't pull images → NAT gateway in the PUBLIC subnet + private route 0.0.0.0/0 → NAT (or ECR interface endpoints + S3 gateway endpoint).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
                 VPC
┌───────────────────────────────────────┐
│  Private subnet          Public subnet │
│  ┌─────────────┐         ┌──────────┐  │
│  │ Fargate task│  ??? ──►│ NAT GW?  │──┼──► Internet Gateway ──► Amazon ECR
│  └─────────────┘         └──────────┘  │
└───────────────────────────────────────┘
Lỗi: CannotPullContainerError khi task ở private subnet, không có route ra ngoài
```

Đáp án đúng: **B** — auto-assign public IP = DISABLED, đặt NAT gateway ở **public subnet**, sửa route table của private subnet trỏ 0.0.0.0/0 → NAT GW. Anh chọn **A**.

#### Vì sao B đúng

ENI của Fargate task cần một route ra Internet để pull image từ ECR (registry API + layer download đều qua endpoint public trừ khi dùng VPC endpoint). Với task ở private subnet, cách chuẩn: **không** gán public IP (vì subnet private thường không có route trực tiếp tới IGW nên public IP cũng vô dụng), mà đặt **NAT gateway trong public subnet** (NAT GW cần chính nó có public IP + route tới IGW), rồi route table của private subnet trỏ traffic ra Internet qua NAT GW đó. Đây là mô hình NAT gateway kinh điển: NAT luôn nằm ở subnet có đường ra IGW, phục vụ các subnet phía sau nó.

#### Vì sao A (lựa chọn của anh) sai

A bật public IP cho task **đang nằm ở private subnet** — nhưng private subnet không có route tới Internet Gateway, nên có gán public IP cũng **không dùng được** để ra Internet (ENI vẫn không resolve/route được ra ngoài). Thêm nữa, A dùng **gateway VPC endpoint cho ECR** — nhưng ECR chỉ có **interface endpoint** (`ecr.api` + `ecr.dkr`, dùng PrivateLink/ENI), gateway endpoint chỉ tồn tại cho S3 và DynamoDB. Vì vậy A sai ở cả hai điểm: public IP vô nghĩa trong private subnet, và loại endpoint không tồn tại cho ECR.

#### Các lựa chọn sai khác

- **C** — Đổ lỗi cho network mode "awsvpc" và đề xuất đổi sang "bridge": sai vì Fargate **chỉ hỗ trợ awsvpc**, không có network mode khác để chọn; đây không phải là hạn chế của awsvpc mà đơn giản là thiếu route Internet.
- **D** — Giống B nhưng đặt NAT gateway ở **private subnet**: NAT gateway cần có địa chỉ IP public và route trực tiếp đến IGW — nếu đặt trong private subnet thì nó cũng bị chính giới hạn routing như các resource khác trong subnet đó, tức là tự nó cũng không ra được Internet. NAT gateway bắt buộc phải ở public subnet.

#### So sánh các phương án

| Phương án | Public IP task | Vị trí NAT/endpoint | Đúng/Sai |
|---|---|---|---|
| **B (đúng)** | DISABLED | NAT GW ở public subnet | ✅ |
| A (anh chọn) | ENABLED | Gateway endpoint (sai loại) cho ECR | ❌ Cả 2 điểm |
| C | — | Đổi network mode (không tồn tại) | ❌ |
| D | DISABLED | NAT GW ở **private** subnet | ❌ Sai vị trí NAT |

#### Lưu ý thực tế

- Cách khác để giải quyết mà không cần NAT: tạo **interface VPC endpoint cho `ecr.api` và `ecr.dkr`** + **gateway VPC endpoint cho S3** (vì image layer thực chất lưu trên S3) — cách này bảo mật hơn (không cần Internet route) nhưng không nằm trong option đúng của đề này.
- `CannotPullContainerError` gần như luôn là dấu hiệu thiếu route ra ngoài (NAT hoặc VPC endpoint), không liên quan đến IAM permission trong đa số trường hợp.

#### Quy tắc nhớ cho thi

- **"Fargate/EC2 ở private subnet cần Internet"** → NAT gateway **luôn đặt ở public subnet**, không đặt ở private subnet.
- **"ECR + VPC endpoint"** → chỉ có **interface endpoint**, không có gateway endpoint cho ECR (gateway endpoint chỉ dành cho S3/DynamoDB).
- **"awsvpc là hạn chế"** → sai, Fargate chỉ hỗ trợ awsvpc, không phải bug cần đổi mode.

### TD explanation

AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.
Fargate allocates the right amount of compute resources, eliminating the need to choose instances and scale cluster capacity. You only pay for the resources required to run your containers, so there is no over-provisioning and paying for additional servers. Fargate runs each task or pod in its own kernel providing the tasks and pods their own isolated compute environment.

The CannotPullContainer error (500) is caused by the Connection timed out when connecting to Amazon ECR. This indicates that when creating a task, the container image specified could not be retrieved.
When a Fargate task is launched, its elastic network interface requires a route to the Internet to pull container images. If you receive an error similar to the following when launching a task, it is because a route to the Internet does not exist:
CannotPullContainerError: API error (500): Get https://111122223333.dkr.ecr.us-east-1.amazonaws.com/v2/: net/http: request canceled while waiting for connection"
To resolve this issue, you can:
– For tasks in public subnets, specify ENABLED for Auto-assign public IP when launching the task.
– For tasks in private subnets, specify DISABLED for Auto-assign public IP when launching the task, and configure a NAT gateway in your VPC to route requests to the Internet.
Therefore, the correct answer is: Update the AWS Fargate task definition and set the auto-assign public IP option to DISABLED. Launch a NAT gateway on the public subnet of the VPC and update the route table of the private subnet to route requests to the internet. The NAT gateway in the public subnet should have a public IP address and a route to the Intenet Gateway. The tasks in the private subnet will send Internet traffic to the NAT gateway to be able pull the images on Amazon Elastic Container Registry.
The option that says: Update the AWS Fargate task definition and set the auto-assign public IP option to ENABLED. Create a gateway VPC endpoint for Amazon ECR. Update the route table to allow AWS Fargate to pull images on Amazon ECR via the endpoint is incorrect. Since the Fargate tasks are on private subnet, you don’t need to enable the auto-assign public IP option. Additionally, you should interface VPC endpoint, not gateway VPC endpoint.
The option that says: Update the AWS Fargate task definition and set the auto-assign public IP option to DISABLED. Launch a NAT gateway on the private subnet of the VPC and update the route table of the private subnet to route requests to the Internet is incorrect. The NAT gateway should be placed in a public subnet because it needs a Public IP address and a direct route to the Internet Gateway (IGW). If it is placed on a private subnet, it will have the same routing limitation as those resources in the private subnet.
The option that says: This is a limitation of the “awsvpc” network mode. Update the AWS Fargate definition to use the “bridge” network mode instead to allow connections to the Internet is incorrect. AWS Fargate only supports the “awsvpc” network mode. Each task is allocated its own elastic network interface (ENI) that is used for communication inside the VPC.

References:
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_cannot_pull_image.html
https://aws.amazon.com/premiumsupport/knowledge-center/ecs-pull-container-api-error-ecr/
https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html

Check out this AWS Fargate Cheat Sheet:
https://tutorialsdojo.com/aws-fargate/

</details>

---

# Group B — Security controls (4)

<a id="q68"></a>

## Q68

A company wants to launch its online shopping website to give customers an easy way to purchase the products they need. The proposed setup is to host the application on an AWS Fargate cluster, utilize a Load Balancer to distribute traffic between the Fargate tasks, and use Amazon CloudFront for caching and content delivery. The company wants to ensure that the website complies with industry best practices and should be able to protect customers from common “man-in-the-middle” attacks for e-commerce websites such as DNS spoofing, HTTPS spoofing, or SSL hijacking.
Which of the following configurations will provide the MOST secure access to the website?

- **A.** Use Route 53 for domain registration. Use a third-party DNS service that supports DNSSEC for DNS requests that use the customer-managed keys. Use AWS Certificate Manager (ACM) to generate a valid 2048-bit TLS/SSL certificate for the domain name and configure the Application Load Balancer HTTPS listener to use this TLS/SSL certificate. Use Server Name Identification and HTTP to HTTPS redirection on CloudFront.
- **B.** Register the domain name on Route 53. Since Route 53 only supports DNSSEC for registration, host the company DNS root servers on Amazon EC2 instances running the BIND service. Enable DNSSEC for DNS requests to ensure the replies have not been tampered with. Generate a valid certificate for the website domain name on AWS ACM and configure the Application Load Balancers HTTPS listener to use this TLS/SSL certificate. Use Server Name Identification and HTTP to HTTPS redirection on CloudFront.
- **C.** Register the domain name on Route 53. Use a third-party DNS provider that supports the import of the customer-managed keys for DNSSEC. Import a 2048-bit TLS/SSL certificate from a third-party certificate service to AWS Certificate Manager (ACM). Configure the Application Load Balancer with an HTTPS listener to use the imported TLS/SSL certificate. Use Server Name Identification and HTTP to HTTPS redirection on CloudFront.
- **D.** Register the domain name on Route 53 and enable DNSSEC validation for all public hosted zones to ensure that all DNS requests have not been tampered with during transit. Use AWS Certificate Manager (ACM) to generate a valid TLS/SSL certificate for the domain name. Configure the Application Load Balancer with an HTTPS listener to use the ACM TLS/SSL certificate. Use Server Name Identification and HTTP to HTTPS redirection on CloudFront.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** e-commerce on Fargate + ALB + CloudFront; prevent DNS spoofing / SSL hijacking; MOST secure

🪤 **Your trap:** No need for a third-party DNS provider or bought certificate — Route 53 signs DNSSEC natively and ACM issues free certs

🧠 **Rule:** Anti-MITM → Route 53 DNSSEC signing on the public hosted zone + ACM cert on the ALB + CloudFront HTTP→HTTPS redirect.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Customer ──DNS──► Route 53 (public hosted zone) ──► CloudFront ──► ALB (HTTPS) ──► Fargate tasks
Yêu cầu: chống DNS spoofing, HTTPS spoofing, SSL hijacking — MOST secure, e-commerce
```

Đáp án đúng: **D** — Route 53 domain + **bật DNSSEC signing trên public hosted zone** + ACM cert cho ALB HTTPS listener + SNI/redirect trên CloudFront. Anh chọn **C**.

#### Vì sao D đúng

Ba lớp bảo vệ tương ứng ba loại tấn công:
- **DNSSEC signing trên Route 53 public hosted zone** → chống DNS spoofing (đảm bảo data origin authentication, response không bị giả mạo trong quá trình transit).
- **ACM cert gắn vào ALB HTTPS listener** → chống SSL hijacking (traffic mã hóa end-to-end, ACM cấp cert miễn phí và tự động renew).
- **SNI + HTTP→HTTPS redirect trên CloudFront** → đảm bảo client luôn đi qua bản HTTPS, chống HTTPS spoofing/downgrade.

Route 53 **đã hỗ trợ DNSSEC signing natively** từ cuối 2020 — TD explanation nói rõ: "Amazon now allows you to enable DNSSEC signing for all existing and new public hosted zones". Không cần dịch vụ DNS thứ ba nào cả.

#### Vì sao C (lựa chọn của anh) sai

C dùng "third-party DNS provider hỗ trợ import customer-managed key cho DNSSEC" và "import certificate từ third-party certificate service vào ACM". Đây từng là cách làm hợp lệ **trước khi** Route 53 hỗ trợ DNSSEC — nhưng bây giờ là dư thừa: Route 53 tự ký DNSSEC (Route 53 quản lý zone-signing key, anh chỉ quản key-signing key qua KMS nếu muốn), và ACM **tự phát hành certificate 2048-bit miễn phí** không cần mua từ bên thứ ba. C về mặt kỹ thuật vẫn "possible" (TD explanation nói "Although this is possible") nhưng không phải MOST secure/most straightforward — nó thêm phụ thuộc bên ngoài không cần thiết mà không tăng thêm bảo mật.

#### Các lựa chọn sai khác

- **A** — Tương tự C: dùng third-party DNS cho DNSSEC dù Route 53 đã hỗ trợ native, không cần thiết.
- **B** — Sai nghiêm trọng hơn: giả định "Route 53 chỉ hỗ trợ DNSSEC cho registration" rồi tự host root DNS servers trên EC2 chạy BIND — đây là **giải pháp workaround cũ** từ thời DNSSEC signing chưa có trên Route 53. Giờ đã lạc hậu và tự vận hành BIND làm tăng surface bị tấn công, không phải giải pháp "most secure".

#### So sánh các phương án

| Phương án | DNSSEC | Certificate | Vấn đề |
|---|---|---|---|
| **D (đúng)** | Route 53 native signing | ACM (miễn phí) | Không |
| C (anh chọn) | Third-party DNS + import key | Import cert từ bên thứ 3 vào ACM | Dư thừa, không cần thiết |
| A | Third-party DNS (customer-managed key) | ACM tự tạo | Vẫn dư thừa phần DNS |
| B | Tự host BIND trên EC2 | ACM | Giải pháp cũ, lạc hậu, rủi ro cao |

#### Lưu ý thực tế

- DNSSEC signing chống giả mạo **response** DNS trong transit; muốn phía **resolver** trong VPC cũng validate response đã ký, cần bật **DNSSEC validation trên Route 53 Resolver** — đây là khái niệm khác (validation) so với "signing" (áp dụng cho zone mình sở hữu).
- ACM certificate miễn phí chỉ dùng được với các service tích hợp ACM (ALB, CloudFront, API Gateway...) — không export ra được để dùng ngoài AWS.

#### Quy tắc nhớ cho thi

- **"Chống DNS spoofing"** → **DNSSEC signing** trên Route 53 public hosted zone (native, không cần bên thứ 3).
- **"Chống SSL hijacking / MITM"** → ACM cert trên ALB + HTTPS listener.
- **"Third-party DNS cho DNSSEC" hoặc "tự host BIND"** → luôn là bẫy lỗi thời, Route 53 đã làm được native.

### TD explanation

Amazon now allows you to enable Domain Name System Security Extensions (DNSSEC) signing for all existing and new public hosted zones, and enable DNSSEC validation for Amazon Route 53 Resolver. Amazon Route 53 DNSSEC provides data origin authentication and data integrity verification for DNS and can help customers meet compliance mandates, such as FedRAMP.
When you enable DNSSEC signing on a hosted zone, Route 53 cryptographically signs each record in that hosted zone. Route 53 manages the zone-signing key, and you can manage the key-signing key in AWS Key Management Service (AWS KMS). Amazon’s domain name registrar, Route 53 Domains, already supports DNSSEC, and customers can now register domains and host their DNS on Route 53 with DNSSEC signing enabled. When you enable DNSSEC validation on the Route 53 Resolver in your VPC, it ensures that DNS responses have not been tampered with in transit. This can prevent DNS Spoofing.

AWS Certificate Manager is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources. SSL/TLS certificates are used to secure network communications and establish the identity of websites over the Internet as well as resources on private networks. AWS Certificate Manager removes the time-consuming manual process of purchasing, uploading, and renewing SSL/TLS certificates. Using a valid SSL Certificate for your application load balancer ensures that all requests are encrypted on transit as well as protection against SSL hijacking.
CloudFront supports Server Name Indication (SNI) for custom SSL certificates, along with the ability to take incoming HTTP requests and redirect them to secure HTTPS requests to ensure that clients are always directed to the secure version of your website.
Therefore, the correct answer is: Register the domain name on Route 53 and enable DNSSEC validation for all public hosted zones to ensure that all DNS requests have not been tampered with during transit. Use AWS Certificate Manager (ACM) to generate a valid TLS/SSL certificate for the domain name. Configure the Application Load Balancer with an HTTPS listener to use the ACM TLS/SSL certificate. Use Server Name Identification and HTTP to HTTPS redirection on CloudFront.
The option that says: Register the domain name on Route 53. Use a third-party DNS provider that supports the import of the customer-managed keys for DNSSEC. Import a 2048-bit TLS/SSL certificate from a third-party certificate service to AWS Certificate Manager (ACM). Configure the Application Load Balancer with an HTTPS listener to use the imported TLS/SSL certificate. Use Server Name Identification and HTTP to HTTPS redirection on CloudFront is incorrect. Although this is possible, you don’t have to rely on a third-party DNS provider as Route 53 supports DNSSEC signing. Also, ACM can secure a 2048-bit TLS/SSL Certificate for free so you don’t have to buy certificates from other providers.
The option that says: Use Route 53 for domain registration. Use a third-party DNS service that supports DNSSEC for DNS requests that use the customer-managed keys. Use AWS Certificate Manager (ACM) to generate a valid 2048-bit TLS/SSL certificate for the domain name and configure the Application Load Balancer HTTPS listener to use this TLS/SSL certificate. Use Server Name Identification and HTTP to HTTPS redirection on CloudFront is incorrect. This is also possible, but you don’t have to rely on a third-party DNS provider as Amazon Route 53 already supports DNSSEC signing.
The option that says: Register the domain name on Route 53. Since Route 53 only supports DNSSEC for registration, host the company DNS root servers on Amazon EC2 instances running the BIND service. Enable DNSSEC for DNS requests to ensure the replies have not been tampered with. Generate a valid certificate for the website domain name on AWS ACM and configure the Application Load Balancers HTTPS listener to use this TLS/SSL certificate. Use Server Name Identification and HTTP to HTTPS redirection on CloudFront is incorrect as this solution is no longer recommended. This setup was previously used as a workaround when DNSSEC signing was not supported natively yet in Amazon Route 53.

References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-configure-dnssec.html
https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html
https://aws.amazon.com/about-aws/whats-new/2020/12/announcing-amazon-route-53-support-dnssec/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/amazon-route-53/
https://tutorialsdojo.com/amazon-cloudfront/
https://tutorialsdojo.com/aws-certificate-manager/

</details>

<a id="q22"></a>

## Q22

A company runs several clusters of Amazon EC2 instances in AWS. An unusual API activity and port scanning in the VPC have been identified by the security team. They noticed that there are multiple port scans being triggered to the EC2 instances from a specific IP address. To fix the issue immediately, the solutions architect has decided to simply block the offending IP address. The solutions architect is also instructed to fortify their existing cloud infrastructure security from the most frequently occurring network and transport layer DDoS attacks. 
Which of the following is the most suitable method to satisfy the above requirement in AWS?

- **A.** Deny access from the IP Address block in the Network ACL. Use AWS Shield Advanced to protect your cloud resources.
- **B.** Change the Windows Firewall settings to deny access from the IP address block. Use Amazon GuardDuty to detect potentially compromised instances or reconnaissance by attackers, and AWS Systems Manager Patch Manager to properly apply the latest security patches to all of your instances.
- **C.** Deny access from the IP Address block by adding a specific rule to all of the Security Groups. Use a combination of AWS WAF and AWS Config to protect your cloud resources against common web attacks.
- **D.** Block the offending IP address using Route 53. Use Amazon Macie to automatically discover, classify, and protect sensitive data in AWS, including DDoS attacks.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** port scans from one IP; block IP immediately; protect from network/transport-layer (L3/L4) DDoS

🪤 **Your trap:** Per-instance Windows Firewall doesn't scale; GuardDuty detects, doesn't block or stop DDoS

🧠 **Rule:** Block an IP → NACL deny (SGs have no deny). L3/L4 DDoS protection → AWS Shield (Advanced for extra protection + DRT).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
IP tấn công cụ thể ──port scan──► EC2 instances (nhiều cluster)
Yêu cầu 1: block ngay IP đó
Yêu cầu 2: chống DDoS L3/L4 (network/transport layer) "phổ biến nhất"
```

Đáp án đúng: **A** — Deny IP trong **Network ACL** + dùng **AWS Shield Advanced**. Anh chọn **B**.

#### Vì sao A đúng

Hai yêu cầu, hai công cụ riêng biệt:
- **Block một IP cụ thể** → chỉ NACL làm được vì NACL có rule **deny** rõ ràng theo dải IP; Security Group chỉ có allow (whitelist), không deny được một IP cụ thể.
- **Chống DDoS L3/L4 phổ biến nhất** → AWS Shield (Standard mặc định miễn phí cho mọi customer, chống hầu hết DDoS L3/L4; Advanced thêm mitigation nâng cao + DRT + cost protection). TD explanation: "AWS Shield Standard defends against most common, frequently occurring network and transport layer DDoS attacks."

#### Vì sao B (lựa chọn của anh) sai

B đề xuất đổi **Windows Firewall** trên từng instance để block IP — về lý thuyết có ngăn được traffic đó tới instance, nhưng: (1) phải làm thủ công **trên từng instance riêng lẻ**, không scale khi có "several clusters", trong khi NACL áp dụng ở mức subnet cho toàn bộ instance cùng lúc; (2) **GuardDuty chỉ phát hiện** hành vi bất thường (như port scan) và **Systems Manager Patch Manager chỉ vá lỗi** — cả hai đều **không chặn và không chống DDoS**. Đây đúng là bẫy: GuardDuty rất hợp lý để "phát hiện" port scan trong câu hỏi (đúng là nó detect được reconnaissance), nhưng đề hỏi giải pháp bảo vệ + chống DDoS, mà GuardDuty không làm được vai trò đó.

#### Các lựa chọn sai khác

- **C** — Deny IP bằng cách thêm rule vào **tất cả Security Group**: SG không hỗ trợ deny rule, chỉ allow — không thể chặn một IP cụ thể theo cách này. AWS WAF + AWS Config cũng không phải công cụ chống DDoS L3/L4 (WAF là L7, Config chỉ là compliance/audit).
- **D** — "Block IP bằng Route 53": Route 53 là DNS service, không có khái niệm block IP theo traffic thực tế. Amazon Macie là dịch vụ phát hiện/phân loại dữ liệu nhạy cảm (PII...), hoàn toàn không liên quan tới DDoS.

#### So sánh các phương án

| Phương án | Block IP bằng | Chống DDoS bằng | Đúng/Sai |
|---|---|---|---|
| **A (đúng)** | Network ACL (deny) | AWS Shield Advanced | ✅ |
| B (anh chọn) | Windows Firewall (per-instance) | GuardDuty + Patch Manager | ❌ Không scale, không chống DDoS |
| C | Security Group (không deny được) | WAF + Config | ❌ Sai cả 2 |
| D | Route 53 (không làm được) | Macie | ❌ Sai cả 2 |

#### Lưu ý thực tế

- Security Group **không có rule deny** — chỉ có thể "không cho phép" bằng cách không thêm allow rule, không thể chặn một IP cụ thể trong khi vẫn allow các IP khác trên cùng port.
- GuardDuty + WAF + Shield Advanced thường **kết hợp** trong kiến trúc thực tế (GuardDuty detect → Shield/WAF mitigate), nhưng câu hỏi này chỉ hỏi công cụ **block + chống DDoS**, không hỏi pipeline phát hiện.

#### Quy tắc nhớ cho thi

- **"Block/deny một IP cụ thể"** → **Network ACL**, không phải Security Group (SG chỉ allow).
- **"Chống DDoS L3/L4 phổ biến"** → **AWS Shield** (Standard/Advanced).
- **GuardDuty** → chỉ detect, không block, không chống DDoS.

### TD explanation

AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency, so there is no need to engage AWS Support to benefit from DDoS protection. There are two tiers of AWS Shield – Standard and Advanced.

All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional charge. AWS Shield Standard defends against most common, frequently occurring network and transport layer DDoS attacks that target your web site or applications. When you use AWS Shield Standard with Amazon CloudFront and Amazon Route 53, you receive comprehensive availability protection against all known infrastructure (Layer 3 and 4) attacks.
A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC. A network ACL has separate inbound and outbound rules, and each rule can either allow or deny traffic. Network ACLs are stateless; responses to allowed inbound traffic are subject to the rules for outbound traffic (and vice versa).
Therefore the correct answer is: Deny access from the IP Address block in the Network ACL. Use AWS Shield Advanced to protect your cloud resources.
The option that says: Block the offending IP address using Route 53. Use Amazon Macie to automatically discover, classify, and protect sensitive data in AWS, including DDoS attacks is incorrect because Amazon Macie is just a security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. It does not provide security against DDoS attacks. In addition, you cannot block the offending IP address using Route 53. You should use Network ACL for this scenario.
The option that says: Change the Windows Firewall settings to deny access from the IP address block. Use Amazon GuardDuty to detect potentially compromised instances or reconnaissance by attackers, and AWS Systems Manager Patch Manager to properly apply the latest security patches to all of your instances is incorrect. You have to use Network ACL to block the specific IP address to your network and not just change the firewall of your Windows server. Amazon GuardDuty and AWS Systems Manager Patch Manager are not suitable to fortify your AWS Cloud against DDoS attacks.
The option that says: Deny access from the IP Address block by adding a specific rule to all of the Security Groups. Use a combination of AWS WAF and AWS Config to protect your cloud resources against common web attacks is incorrect because it is still better to block the offending IP address on the Network ACL level as you cannot directly deny an IP address in your Security Group. AWS WAF and AWS Config are helpful to improve the security of your cloud infrastructure in AWS but these services are not enough to protect your infrastructure against DDoS attacks. You have to use AWS Shield Advanced in this scenario.

References:
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html
https://aws.amazon.com/shield/

Check out these AWS WAF and AWS Shield Cheat Sheets:
https://tutorialsdojo.com/aws-waf/
https://tutorialsdojo.com/aws-shield/

</details>

<a id="q47"></a>

## Q47

A private bank is hosting a secure web application that allows its agents to view highly sensitive information about the clients. The amount of traffic that the web app will receive is known and not expected to fluctuate. An SSL will be used as part of the application’s data security. The chief information security officer (CISO) is concerned about the security of the SSL private key. The CISO wants to ensure that the key cannot be accidentally or intentionally moved outside the corporate environment. The solutions architect is also concerned that the application logs might contain some sensitive information. The EBS volumes used to store the data are already encrypted. In this scenario, the application logs must be stored securely and durably so that they can only be decrypted by authorized employees. 
Which of the following is the most suitable and highly available architecture that can meet all of the requirements?

- **A.** Distribute traffic to a set of web servers using an Elastic Load Balancer. To secure the SSL private key, upload the key to the load balancer and configure the load balancer to offload the SSL traffic. Lastly, write your application logs to an instance store volume that has been encrypted using a randomly generated AES key.
- **B.** Distribute traffic to a set of web servers using an Elastic Load Balancer. Use TCP load balancing for the load balancer and configure your web servers to retrieve the SSL private key from a private Amazon S3 bucket on boot. Use another private Amazon S3 bucket to store your web server logs using Amazon S3 server-side encryption.
- **C.** Distribute traffic to a set of web servers using an Elastic Load Balancer that performs TCP load balancing. Use an AWS CloudHSM to perform the SSL transactions and deliver your application logs to a private Amazon S3 bucket using server-side encryption.
- **D.** Distribute traffic to a set of web servers using an Elastic Load Balancer that performs TCP load balancing. Use CloudHSM deployed to two Availability Zones to perform the SSL transactions and deliver your application logs to a private Amazon S3 bucket using server-side encryption.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** C

🔑 **Key words:** SSL private key must never leave; logs durable + only authorized decrypt; MOST highly available

🪤 **Your trap:** Picked CloudHSM without multi-AZ — one HSM = single point of failure

🧠 **Rule:** Keys never leave + HA → CloudHSM cluster across ≥2 AZs, TCP (L4) LB pass-through, logs to S3 with SSE.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Clients ──HTTPS──► ELB (TCP LB) ──► Web servers (fleet)
Yêu cầu 1: SSL private key KHÔNG được rời khỏi corporate environment (cố ý hoặc vô tình)
Yêu cầu 2: App logs mã hóa, chỉ authorized employee decrypt được, durable
Yêu cầu 3: MOST highly available
```

Đáp án đúng: **D** — TCP load balancing + **CloudHSM triển khai trên ≥2 AZ** để làm SSL transaction + log vào S3 với server-side encryption. Anh chọn **C** (CloudHSM nhưng không nói rõ multi-AZ).

#### Vì sao D đúng

**CloudHSM** là dịch vụ cho phép thực hiện SSL/TLS handshake mà **key không bao giờ xuất ra khỏi HSM** — đáp ứng chính xác yêu cầu "key không thể bị di chuyển ra ngoài môi trường, cố ý hoặc vô tình" (khác với việc lưu key trên ELB hay S3, vẫn còn khả năng key bị export). Vì đề hỏi "**MOST** highly available", một cụm CloudHSM chỉ có 1 node là **single point of failure** — phải triển khai **CloudHSM cluster trải trên ít nhất 2 Availability Zone** để đạt HA thực sự. TCP load balancing (Layer 4) là bắt buộc vì ELB chỉ pass-through traffic, không terminate SSL — SSL transaction diễn ra ở CloudHSM/web server, không phải ở ELB.

#### Vì sao C (lựa chọn của anh) sai

C gần như giống hệt D về CloudHSM + TCP LB + log vào S3 SSE — nhưng **không nói rõ CloudHSM được deploy ở nhiều AZ**. TD explanation nói thẳng: "the architecture did not explicitly say that the CloudHSM is deployed to multiple Availability Zones, which means that this architecture is not highly available compared with the correct option." Đây là bẫy tinh: hai lựa chọn giống nhau ~95%, chỉ khác một chi tiết "multi-AZ" — nhưng đề nhấn mạnh từ khóa "**most highly available**" nên chi tiết đó chính là điểm quyết định.

#### Các lựa chọn sai khác

- **A** — Upload private key lên ELB để offload SSL: chính là điều CISO **không muốn** — key rời khỏi kiểm soát và nằm trên hạ tầng managed của ELB. Log ghi vào **instance store** (ephemeral) — mất dữ liệu khi instance terminate → không durable.
- **B** — Lưu private key trên S3 bucket để web server tải về khi boot: key vẫn phải "di chuyển" ra khỏi vị trí gốc (tải xuống mỗi lần boot) — không đảm bảo "never leaves corporate environment" theo cách an toàn như CloudHSM.

#### So sánh các phương án

| Phương án | Quản lý SSL key | Log storage | HA? |
|---|---|---|---|
| **D (đúng)** | CloudHSM, ≥2 AZ | S3 + SSE | ✅ |
| C (anh chọn) | CloudHSM (không rõ AZ) | S3 + SSE | ❌ Có thể chỉ 1 AZ |
| A | Upload key lên ELB | Instance store (ephemeral) | ❌ Key rời khỏi kiểm soát, log mất khi terminate |
| B | Key trên S3, tải khi boot | S3 + SSE | ❌ Key vẫn di chuyển ra ngoài vị trí gốc |

#### Lưu ý thực tế

- 📝 **Ghi chú kỹ thuật:** TD explanation phân tích thêm rằng "server-side encryption" trong đáp án đúng cố tình mơ hồ giữa **SSE-S3** (AWS tự quản lý key AES-256) và **SSE-C** (khách hàng tự cung cấp và giữ key). Vì yêu cầu "chỉ authorized employee mới decrypt được", TD suy luận ngầm rằng đáp án đúng ám chỉ **SSE-C** — nhưng đề bài không nói rõ điều này, chỉ ghi "server-side encryption" chung. Đây là điểm hơi gượng ép của câu hỏi (ambiguous by design theo lời TD tự nhận), nên hiểu đây là dạng câu hỏi cố ý mập mờ để tăng độ khó, không phải một quy tắc AWS tổng quát.
- CloudHSM cluster tự động đồng bộ dữ liệu key giữa các HSM node trong cluster (không cần đồng bộ tay).

#### Quy tắc nhớ cho thi

- **"Key không được rời khỏi môi trường"** → **CloudHSM** (SSL transaction diễn ra trong HSM, key không export).
- **"MOST highly available" + CloudHSM** → phải là **cluster trải ≥2 AZ**, một HSM đơn = SPOF.
- **"SSL key trên ELB/S3"** → luôn là bẫy vì key vẫn có thể bị di chuyển/truy cập ngoài ý muốn.

### TD explanation

AWS CloudHSM is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud. With CloudHSM, you can manage your own encryption keys and automate time-consuming administrative tasks for you, such as hardware provisioning, software patching, high-availability, and backups.

The correct answer is the option that says: Distribute traffic to a set of web servers using an Elastic Load Balancer that performs TCP load balancing. Use CloudHSM deployed to two Availability Zones to perform the SSL transactions and deliver your application logs to a private Amazon S3 bucket using server-side encryption. It uses CloudHSM for performing the SSL transaction without requiring any additional way of storing or managing the SSL private key. This is the most secure way of ensuring that the key will not be moved outside of the AWS environment. Also, it uses the highly available and durable S3 service for storing the logs. Take note that this option says “server-side encryption” and not “Amazon S3-Managed Encryption Keys”, which are two different things.
The option that says: Distribute traffic to a set of web servers using an Elastic Load Balancer. Use TCP load balancing for the load balancer and configure your web servers to retrieve the SSL private key from a private Amazon S3 bucket on boot. Use another private Amazon S3 bucket to store your web server logs using Amazon S3 server-side encryption is incorrect because it does not use a secure way of managing the SSL private key for the SSL transaction.
The option that says: Distribute traffic to a set of web servers using an Elastic Load Balancer. To secure the SSL private key, upload the key to the load balancer and configure the load balancer to offload the SSL traffic. Lastly, write your application logs to an instance store volume that has been encrypted using a randomly generated AES key is incorrect. The application logs are written to an ephemeral volume, which means that the data will be lost when the EC2 instance is terminated. Hence, this solution is neither durable nor secure.
The option that says: Distribute traffic to a set of web servers using an Elastic Load Balancer that performs TCP load balancing. Use an AWS CloudHSM to perform the SSL transactions and deliver your application logs to a private Amazon S3 bucket using server-side encryption is incorrect. Although it is almost similar to the correct option, the architecture did not explicitly say that the CloudHSM is deployed to multiple Availability Zones, which means that this architecture is not highly available compared with the correct option.
We deliberately designed the question to have this sort of ambiguity to make it more challenging as we know how hard the actual AWS SA Professional exam is. So in this case, the correct option does not say if it is using SSE-S3 or SSE-C. This is one of the trick part of this question. If it is using SSE-S3, then the current correct answer would definitely be wrong because AWS will be managing the AES-256 key.
However, if it uses SSE-C, then the AES-256 key would be managed by the authorized government employees only. Therefore, it is implied that the correct option is using SSE-C, instead of SSE-S3.
Remember that in SSE-C, when you upload an object, Amazon S3 uses the encryption key you provide to apply AES-256 encryption to your data and removes the encryption key from memory. Amazon S3 does not store the encryption key you provide. Instead, they store a randomly salted HMAC value of the encryption key in order to validate future requests. The salted HMAC value cannot be used to derive the value of the encryption key or to decrypt the contents of the encrypted object. That means, if you lose the encryption key, you lose the object.

References:
https://aws.amazon.com/cloudhsm/
https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q74"></a>

## Q74

A telecommunications company is planning to host a WordPress website on an Amazon ECS Cluster which uses the Fargate launch type. For security purposes, the database credentials should be provided to the WordPress image by using environment variables. Your manager instructed you to ensure that the credentials are secure when passed to the image and that they cannot be viewed on the cluster itself. The credentials must be kept in a dedicated storage with lifecycle management and key rotation.
Which of the following is the most suitable solution in this scenario that you can implement with the least effort?

- **A.** In the ECS task definition file of the ECS Cluster, store the database credentials and encrypt with KMS. Store the task definition JSON file in a private S3 bucket and ensure that HTTPS is enabled on the bucket to encrypt the data in-flight. Create an IAM role to the ECS task definiton script that allows access to the specific S3 bucket and then pass the --cli-input-json parameter when calling the ECS register-task-definition. Reference the task definition JSON file in the S3 bucket which contains the database credentials.
- **B.** Store the database credentials using the AWS Systems Manager Parameter Store and then encrypt them using AWS KMS. Create an IAM Role for your Amazon ECS task execution role and reference it with your task definition, which allows access to both KMS and the Parameter Store. Within your container definition, specify secrets with the name of the environment variable to set in the container and the full ARN of the Systems Manager Parameter Store parameter containing the sensitive data to present to the container.
- **C.** Store the database credentials using the AWS Secrets Manager and then encrypt them using AWS KMS. Create an IAM Role for your Amazon ECS task execution role and reference it with your task definition which allows access to both KMS and AWS Secrets Manager. Within your container definition, specify secrets with the name of the environment variable to set in the container and the full ARN of the Secrets Manager secret which contains the sensitive data, to present to the container.
- **D.** Migrate the container cluster to Amazon Elastic Kubernetes Service (EKS). Create manifest files for deployment and use the Kubernetes Secrets objects to store the database credentials. Reference the secrets on the manifest file using the secretKeyRef to use them a environment variables. Configure EKS to rotate the secret values automatically.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** 🔁 ECS Fargate env vars; credentials not visible on cluster; lifecycle management + KEY ROTATION; least effort

🪤 **Your trap:** 🔁 Same pick as the chapter drill: Parameter Store has no built-in rotation or lifecycle

🧠 **Rule:** 'Rotation' or 'lifecycle' in the question → Secrets Manager; reference it in the task definition `secrets` + task execution role.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
WordPress trên ECS Fargate
    │
    │ env var DB_PASSWORD = ???
    ▼
Task definition ──secrets──► [Secrets Manager hoặc Parameter Store] ──KMS──► container
Yêu cầu: credential không thấy được trên cluster, cần LIFECYCLE MANAGEMENT + KEY ROTATION, least effort
```

Đáp án đúng: **C** — Lưu credential trong **AWS Secrets Manager**, mã hóa bằng KMS, reference qua `secrets` trong container definition + task execution role có quyền KMS + Secrets Manager. Anh chọn **B** (Parameter Store).

#### Vì sao C đúng

⚠️ **Lỗi lặp lại:** đây là **cùng lựa chọn sai (Parameter Store)** anh đã chọn ở bài drill của chapter này — nghĩa là quy tắc "rotation/lifecycle → Secrets Manager" vẫn chưa "dính". Cần ghi nhớ chắc lần này.

Cả Secrets Manager và Parameter Store đều hỗ trợ cơ chế `secrets` trong ECS container definition để inject credential thành biến môi trường mà **không hiện giá trị plaintext** trong task definition hay trên cluster — điểm này cả B và C đều đáp ứng. Điểm phân biệt chính là câu đề chốt: **"dedicated storage with lifecycle management and key rotation"**. TD explanation nói thẳng: "If you want a single store for configuration and secrets, you can use Parameter Store. If you want a dedicated secrets store with lifecycle management, use Secrets Manager." → chỉ Secrets Manager có **rotation tự động** (tích hợp Lambda rotation function) và quản lý lifecycle secret chuyên biệt.

#### Vì sao B (lựa chọn của anh) sai

Parameter Store **hoàn toàn hợp lệ về mặt kỹ thuật** để lưu và inject credential (mã hóa bằng KMS qua SecureString, reference bằng ARN trong `secrets`) — đây là lý do nó "trông đúng": cấu hình gần giống C, IAM role giống nhau, cùng cơ chế secrets injection. Nhưng Parameter Store **không có tính năng rotation/lifecycle built-in** như Secrets Manager (muốn rotate phải tự viết Lambda + EventBridge schedule, không có sẵn). Vì đề yêu cầu rõ "**must be kept in dedicated storage with lifecycle management and key rotation**" — đây là cụm từ khóa chỉ đích danh Secrets Manager.

#### Các lựa chọn sai khác

- **A** — Lưu credential trong task definition JSON, đặt trong S3 bucket riêng: về lý thuyết khả thi nhưng đòi hỏi **rất nhiều bước thủ công** (tự mã hóa, tự quản S3 bucket, tự pass `--cli-input-json`) — trái với yêu cầu "least effort", và không có lifecycle/rotation built-in.
- **D** — Migrate từ ECS sang EKS để dùng Kubernetes Secrets: tốn công **di chuyển toàn bộ cluster** (ngược hẳn "least effort"), và quan trọng hơn — **Kubernetes không hỗ trợ tự động rotate secret** sẵn có (Secrets object chỉ lưu, không tự rotate).

#### So sánh các phương án

| Phương án | Nơi lưu | Rotation/lifecycle | Effort |
|---|---|---|---|
| **C (đúng)** | Secrets Manager | Có (built-in) | Thấp |
| B (anh chọn) | Parameter Store | Không có built-in | Thấp nhưng thiếu rotation |
| A | S3 (task def JSON) | Không có | Cao (nhiều bước thủ công) |
| D | Kubernetes Secrets (EKS) | Không tự động | Rất cao (migrate cluster) |

#### Lưu ý thực tế

- Task **execution role** (không phải task role) là role cần quyền đọc Secrets Manager + KMS decrypt — dễ nhầm giữa hai role này khi cấu hình IAM.
- Secret parameter có thể ở Region khác container đang chạy, nhưng phải **cùng account**.

#### Quy tắc nhớ cho thi

- **"Rotation" hoặc "lifecycle management"** trong đề → luôn chỉ **Secrets Manager**, không phải Parameter Store.
- **"Chỉ cần lưu config/secret đơn giản, không cần rotation"** → Parameter Store là đủ và rẻ hơn.
- **"Migrate ECS→EKS để lấy feature nhỏ"** → hầu như luôn là đáp án sai vì effort quá cao so với yêu cầu.

### TD explanation

Amazon ECS enables you to inject sensitive data into your containers by storing your sensitive data in either AWS Secrets Manager secrets or AWS Systems Manager Parameter Store parameters and then referencing them in your container definition. This feature is supported by tasks using both the EC2 and Fargate launch types.
Within your container definition, specify secrets with the name of the environment variable to set in the container and the full ARN of either the Secrets Manager secret or Systems Manager Parameter Store parameter containing the sensitive data to present to the container. The parameter that you reference can be from a different Region than the container using it, but must be from within the same account.

AWS Secrets Manager is a secrets management service that helps you protect access to your applications, services, and IT resources. This service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Using Secrets Manager, you can secure and manage secrets used to access resources in the AWS Cloud, on third-party services, and on-premises.
If you want a single store for configuration and secrets, you can use Parameter Store. If you want a dedicated secrets store with lifecycle management, use Secrets Manager.
Hence, the correct answer is the option that says: Store the database credentials using the AWS Secrets Manager and then encrypt them using AWS KMS. Create an IAM Role for your Amazon ECS task execution role and reference it with your task definition which allows access to both KMS and AWS Secrets Manager. Within your container definition, specify secrets with the name of the environment variable to set in the container and the full ARN of the Secrets Manager secret which contains the sensitive data, to present to the container.
The option that says: Store the database credentials using the AWS Systems Manager Parameter Store and then encrypt them using AWS KMS. Create an IAM Role for your Amazon ECS task execution role and reference it with your task definition, which allows access to both KMS and the Parameter Store. Within your container definition, specify secrets with the name of the environment variable to set in the container and the full ARN of the Systems Manager Parameter Store parameter containing the sensitive data to present to the container is incorrect. Although the use of Systems Manager Parameter Store in securing sensitive data in ECS is valid, this service doesn’t provide dedicated storage with lifecycle management and key rotation, unlike Secrets Manager.
The option that says: In the ECS task definition file of the ECS Cluster, store the database credentials and encrypt with KMS. Store the task definition JSON file in a private S3 bucket and ensure that HTTPS is enabled on the bucket to encrypt the data in-flight. Create an IAM role to the ECS task definiton script that allows access to the specific S3 bucket and then pass the --cli-input-json parameter when calling the ECS register-task-definition. Reference the task definition JSON file in the S3 bucket which contains the database credentials is incorrect. Although the solution may work, it is not recommended to store sensitive credentials in S3. This entails a lot of overhead and manual configuration steps which can be simplified by using the Secrets Manager or Systems Manager Parameter Store.
The option that says: Migrate the container cluster to Amazon Elastic Kubernetes Service (EKS). Create manifest files for deployment and use the Kubernetes Secrets objects to store the database credentials. Reference the secrets on the manifest file using the secretKeyRef to use them a environment variables. Configure EKS to rotate the secret values automatically is incorrect. It is possible to use EKS to host the container clusters and use the Secrets object to store secret values. However, this approach will entail more effort for the migration from ECS to EKS. Additionally, Kubernetes doesn’t natively support the automatic rotation of secrets.

References:
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html
https://aws.amazon.com/blogs/mt/the-right-way-to-store-secrets-using-parameter-store/

Check out this Amazon ECS Cheat Sheet:
https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

Check out this AWS Secrets Manager Cheat Sheet:
https://tutorialsdojo.com/aws-secrets-manager/

</details>

---

# Group C — Ops: patching, compliance, troubleshooting (4)

<a id="q12"></a>

## Q12

A clinic runs its medical record system using a fleet of Windows-based Amazon EC2 instances with several EBS volumes attached to it. Since the records that they are storing are confidential health files of their patients, it is a requirement that the latest security patches are installed on the EC2 instances. In addition, there should be a system in the cloud architecture that checks all of the EC2 instances if they are using an approved Amazon Machine Image (AMI). The system that will be implemented should not impede developers from launching instances using an unapproved AMI, but you still have to be notified if there are non-compliant EC2 instances in your VPC. 
Which of the following should the solutions architect implement to protect and monitor all of your instances as required above? (Select TWO.)

- **A.** Use AWS Shield Advanced to automatically patch all of your EC2 instances and detect uncompliant EC2 instances which do not use approved AMIs.
- **B.** Set up a patch baseline that defines which patches are approved for installation on your instances using AWS Systems Manager Patch Manager.
- **C.** Set up Amazon GuardDuty that continuously monitors your instances if the latest security patches are installed and if there is an instance that is using an unapproved AMI. Use CloudWatch Alarms to notify you if there are any non-compliant instances running in your VPC.
- **D.** Use the AWS Config Managed Rule which automatically checks whether your running EC2 instances are using approved AMIs. Set up CloudWatch Alarms to notify you if there are any non-compliant instances running in your VPC.
- **E.** Create an IAM policy that will restrict the developers from launching EC2 instances with an unapproved AMI.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D · **You picked:** B, C

🔑 **Key words:** 🔁 latest patches; check approved AMIs; must NOT block devs, just notify (Select TWO)

🪤 **Your trap:** GuardDuty = threat detection; it checks neither patches nor AMIs. (Drill pick was C,D — this time D was dropped)

🧠 **Rule:** Patching → SSM Patch Manager baseline. 'Detect but don't block' → AWS Config managed rule `approved-amis-by-id` (not IAM or SCP deny).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Fleet EC2 Windows (hồ sơ y tế)
        │
        ├── Yêu cầu 1: cài patch bảo mật mới nhất
        └── Yêu cầu 2: phát hiện instance dùng AMI KHÔNG được approve
                        → KHÔNG chặn dev, chỉ CẢNH BÁO (notify)

(Select TWO)
```

Đáp án đúng: **B (SSM Patch Manager – patch baseline)** + **D (AWS Config Managed Rule `approved-amis-by-id` + CloudWatch Alarm)**. Anh chọn B, C — đúng nửa, sai ở C.

⚠️ **Lỗi lặp lại:** câu này anh cũng đã chọn sai trong chapter drill (không phải cùng option, nhưng cùng kiểu nhầm giữa GuardDuty/Config cho việc "check compliance"). Ghi nhớ: **GuardDuty = threat detection, không phải compliance-check**.

#### B đúng — patch bằng SSM Patch Manager

Yêu cầu "latest security patches" chỉ có một dịch vụ làm đúng chức năng: **Patch Manager**. Anh tạo một **patch baseline** (quy định patch nào được auto-approve, sau bao nhiêu ngày kể từ ngày release), gắn baseline đó vào các instance qua Patch Group, rồi chạy patching theo Maintenance Window.

#### D đúng — kiểm tra AMI mà không chặn dev

Đề nói rõ: hệ thống **không được impede** (chặn) dev launch AMI chưa approve, chỉ cần **notify** khi có instance không compliant. Đây chính xác là hành vi của **AWS Config managed rule `approved-amis-by-id`**: nó chỉ đánh giá compliance sau khi resource đã tồn tại (detective control), không ngăn hành động tạo resource (preventive control). Kết hợp với CloudWatch Alarm để bắn cảnh báo khi có non-compliant resource.

#### Vì sao C (lựa chọn của anh) sai

**C sai vì GuardDuty không kiểm tra patch cũng không kiểm tra AMI.** GuardDuty là dịch vụ threat detection — nó phân tích VPC Flow Logs, CloudTrail, DNS logs để tìm hành vi bất thường (API call lạ, traffic đến IP độc hại...). Nó không có khả năng đọc patch state của OS hay so sánh AMI ID với danh sách approved. Đây là bẫy kinh điển: nghe "continuously monitor" là liên tưởng ngay đến GuardDuty, nhưng GuardDuty giám sát **bảo mật hành vi**, không giám sát **compliance cấu hình**.

#### Vì sao các lựa chọn khác sai

- **A (Shield Advanced):** chỉ chống DDoS, không patch, không kiểm tra AMI — sai hoàn toàn về domain.
- **E (IAM policy chặn AMI chưa approve):** đây là preventive control — sẽ **chặn** dev launch instance, vi phạm trực tiếp yêu cầu "should not impede developers".

| Dịch vụ | Vai trò trong câu này | Chặn hay chỉ cảnh báo |
|---|---|---|
| **SSM Patch Manager (B)** | Patch OS | — |
| **AWS Config managed rule (D)** | Check AMI compliance | Chỉ cảnh báo (detective) |
| IAM policy (E) | Deny launch AMI lạ | Chặn (preventive) — sai theo đề |
| GuardDuty (C) | Threat detection | Không liên quan patch/AMI |
| Shield Advanced (A) | Chống DDoS | Không liên quan |

#### Quy tắc nhớ cho thi

- **"patch OS tự động, có baseline"** → **SSM Patch Manager**
- **"check compliance nhưng KHÔNG chặn, chỉ notify"** → **AWS Config managed rule** (+ CloudWatch Alarm)
- **"chặn hành động ngay từ đầu"** → IAM policy / SCP — chỉ chọn khi đề **cho phép** impede
- **"GuardDuty"** → luôn là threat/behavior detection, không phải patch hay AMI compliance

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

<a id="q13"></a>

## Q13

A company runs hundreds of Windows-based Amazon EC2 instances on AWS. The Solutions Architect has been assigned to develop a workflow to ensure that the required patches of all Windows EC2 instances are properly identified and applied automatically. To maintain their system uptime requirements, it is of utmost importance to ensure that the EC2 instance reboots do not occur at the same time on all of their Windows instances. This is to avoid any loss of revenue that could be caused by any unavailability issues of their systems. 
Which of the following will meet the above requirements?

- **A.** Create a Patch Group with unique tags that you will assign to all of your EC2 Windows Instances. Associate the predefined AWS-DefaultPatchBaseline baseline on your patch group. Set up a maintenance window and associate it with your patch group. Assign the AWS-RunPatchBaseline document as a task within your maintenance window.
- **B.** Create two Patch Groups with unique tags that you will assign to all of your EC2 Windows Instances. Associate the predefined AWS-DefaultPatchBaseline baseline on both patch groups. Set up two non-overlapping maintenance windows and associate each with a different patch group. Using Patch Group tags, register targets with specific maintenance windows and lastly, assign the AWS-RunPatchBaseline document as a task within each maintenance window which has a different processing start time.
- **C.** Create two Patch Groups with unique tags that you will assign to all of your EC2 Windows Instances. Associate the predefined AWS-DefaultPatchBaseline baseline on both patch groups. Create two CloudWatch Events rules which are configured to use a cron expression to automate the execution of patching for the two Patch Groups using the AWS Systems Manager Run command. Set up an AWS Systems Manager State Manager document to define custom commands which will be executed during patch execution.
- **D.** Create a Patch Group with unique tags that you will assign to all of your EC2 Windows Instances. Associate the predefined AWS-DefaultPatchBaseline baseline on both patch groups. Create a CloudWatch Events rule configured to use a cron expression to automate the execution of patching in a given schedule using the AWS Systems Manager Run command. Set up an AWS Systems Manager State Manager document to define custom commands which will be executed during patch execution.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** hundreds of Windows EC2; auto-patch; reboots must NOT happen at the same time

🪤 **Your trap:** One patch group plus a CloudWatch cron patches everything at once and bypasses Maintenance Windows

🧠 **Rule:** Staggered patch reboots → 2+ patch groups (tags) + non-overlapping Maintenance Windows running AWS-RunPatchBaseline.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hàng trăm Windows EC2
        │
        └── Auto-patch, nhưng KHÔNG được reboot đồng thời hết
            (mất doanh thu nếu toàn bộ fleet down cùng lúc)
```

Đáp án đúng: **B (2 Patch Group + 2 Maintenance Window KHÔNG chồng lịch + AWS-RunPatchBaseline)**. Anh chọn **D** — chỉ có 1 Patch Group và dùng CloudWatch Events cron thay vì Maintenance Windows.

#### B đúng — vì sao cần 2 nhóm + 2 khung giờ riêng

Muốn "reboot không đồng thời" thì phải chia fleet ra **ít nhất 2 nhóm độc lập** để lúc nhóm này đang patch/reboot thì nhóm khác vẫn chạy, đảm bảo uptime:

```
Patch Group 1 ──► Maintenance Window 1 (00:00–02:00) ──► AWS-RunPatchBaseline
Patch Group 2 ──► Maintenance Window 2 (03:00–05:00) ──► AWS-RunPatchBaseline
        (2 window KHÔNG overlap → chỉ 1 nhóm bị patch/reboot tại 1 thời điểm)
```

Cơ chế đúng chuẩn SSM: gắn tag `Patch Group` cho từng instance → đăng ký patch baseline (AWS-DefaultPatchBaseline) cho từng group → tạo Maintenance Window, đăng ký target theo tag Patch Group → gán task `AWS-RunPatchBaseline` chạy theo lịch của window đó.

#### Vì sao D (lựa chọn của anh) sai

D chỉ tạo **một Patch Group duy nhất** — nghĩa là toàn bộ fleet nằm trong cùng một nhóm patching. D còn dùng **CloudWatch Events cron + Run Command** để tự động patch theo lịch, hoàn toàn bỏ qua Maintenance Windows. Hai vấn đề này cộng lại: tất cả instance được patch (và reboot) **cùng một lịch, cùng một lúc** — chính là điều đề bài cấm. Run Command tuy chạy được patch, nhưng nó là công cụ ad-hoc cho tác vụ quản trị đơn lẻ, không có khái niệm "khung bảo trì có target theo nhóm" như Maintenance Windows.

#### Vì sao các lựa chọn khác sai

- **A:** có đúng 1 Patch Group + 1 Maintenance Window, nhưng vẫn chỉ có **một** nhóm/một lịch → mọi instance vẫn reboot cùng lúc.
- **C:** có 2 Patch Group đúng, nhưng lại dùng **CloudWatch Events cron + Run Command + State Manager** thay vì Maintenance Windows — sai công cụ, và State Manager là để duy trì configuration state liên tục, không phải để chạy patch theo lịch gián đoạn.

| Lựa chọn | Số Patch Group | Công cụ lên lịch | Đạt yêu cầu "reboot lệch nhau"? |
|---|---|---|---|
| **B** | 2 | 2 Maintenance Window không chồng lịch | Đúng |
| A | 1 | 1 Maintenance Window | Sai — 1 nhóm duy nhất |
| C | 2 | CloudWatch Events cron + Run Command | Sai — không dùng Maintenance Windows |
| D | 1 | CloudWatch Events cron + Run Command | Sai cả hai yếu tố |

#### Quy tắc nhớ cho thi

- **"reboot không đồng thời / staggered patching"** → **≥2 Patch Group + Maintenance Window lịch lệch nhau**, không phải 1 nhóm 1 lịch
- **"patch OS theo lịch bảo trì, có target theo tag"** → **Maintenance Windows**, không phải CloudWatch Events + Run Command
- **AWS-RunPatchBaseline** luôn là document chạy trong Maintenance Window task để patch theo baseline đã đăng ký

### TD explanation

AWS Systems Manager Patch Manager automates the process of patching managed instances with both security-related and other types of updates. You can use Patch Manager to apply patches for both operating systems and applications.
You can patch fleets of Amazon EC2 instances or your on-premises servers and virtual machines (VMs) by operating system type. This includes supported versions of Windows Server, Ubuntu Server, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), CentOS, Amazon Linux, and Amazon Linux 2. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches. You can install patches on a regular basis by scheduling patching to run as a Systems Manager maintenance window task. You can also install patches individually or to large groups of instances by using Amazon EC2 tags. You can add tags to your patch baselines themselves when you create or update them.
You can use a patch group to associate instances with a specific patch baseline. Patch groups help ensure that you are deploying the appropriate patches, based on the associated patch baseline rules, to the correct set of instances. Patch groups can also help you avoid deploying patches before they have been adequately tested. For example, you can create patch groups for different environments (such as Development, Test, and Production) and register each patch group to an appropriate patch baseline.

When you run AWS-RunPatchBaseline, you can target managed instances using their instance ID or tags. SSM Agent and Patch Manager will then evaluate which patch baseline to use based on the patch group value that you added to the instance.
You create a patch group by using Amazon EC2 tags. Unlike other tagging scenarios across Systems Manager, a patch group must be defined with the tag key: Patch Group. Note that the key is case-sensitive. You can specify any value, for example, “web servers,” but the key must be Patch Group.

The AWS-DefaultPatchBaseline baseline is primarily used to approve all Windows Server operating system patches that are classified as “CriticalUpdates” or “SecurityUpdates” and that have an MSRC severity of “Critical” or “Important”. Patches are auto-approved seven days after release.
Hence, the option that says: Create two Patch Groups with unique tags that you will assign to all of your EC2 Windows Instances. Associate the predefined AWS-DefaultPatchBaseline baseline on both patch groups. Set up two non-overlapping maintenance windows and associate each with a different patch group. Using Patch Group tags, register targets with specific maintenance windows and lastly, assign the AWS-RunPatchBaseline document as a task within each maintenance window which has a different processing start time is the correct answer as it properly uses two Patch Groups, non-overlapping maintenance windows and the AWS-DefaultPatchBaseline baseline to ensure that the EC2 instance reboots do not occur at the same time.
The option that says: Create a Patch Group with unique tags that you will assign to all of your EC2 Windows Instances. Associate the predefined AWS-DefaultPatchBaseline baseline on your patch group. Set up a maintenance window and associate it with your patch group. Assign the AWS-RunPatchBaseline document as a task within your maintenance window is incorrect. Although it is correct to use a Patch Group, you must create another Patch Group to avoid any unavailability issues. Having two non-overlapping maintenance windows will ensure that there will be another set of running Windows EC2 instances while the other set is being patched.
The option that says: Create two Patch Groups with unique tags that you will assign to all of your EC2 Windows Instances. Associate the predefined AWS-DefaultPatchBaseline baseline on both patch groups. Create two CloudWatch Events rules which are configured to use a cron expression to automate the execution of patching for the two Patch Groups using the AWS Systems Manager Run command. Set up an AWS Systems Manager State Manager document to define custom commands which will be executed during patch execution is incorrect. The AWS Systems Manager Run Command is primarily used to remotely manage the configuration of your managed instances while AWS Systems Manager State Manager is just a configuration management service that automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define. These two services, including CloudWatch Events, are not suitable to be used in this scenario. The better solution would be to use AWS Systems Manager Maintenance Windows which lets you define a schedule for when to perform potentially disruptive actions on your instances such as patching an operating system, updating drivers, or installing software or patches.
The option that says: Create a Patch Group with unique tags that you will assign to all of your EC2 Windows Instances. Associate the predefined AWS-DefaultPatchBaseline baseline on both patch groups. Create a CloudWatch Events rule configured to use a cron expression to automate the execution of patching in a given schedule using the AWS Systems Manager Run command. Set up an AWS Systems Manager State Manager document to define custom commands which will be executed during patch execution is incorrect. Just as what is mentioned in the above, you have to use Maintenance Windows for scheduling the patches and you also need to set up two Patch Groups in this scenario instead of one.

References:
https://aws.amazon.com/blogs/mt/patching-your-windows-ec2-instances-using-aws-systems-manager-patch-manager/
https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-ssm-documents.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-scheduletasks.html

Check out this AWS Systems Manager Cheat Sheet:
https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q53"></a>

## Q53

A company has production, development, and test environments in its software development department, and each environment contains tens to hundreds of EC2 instances, along with other AWS services. Recently, Ubuntu released a series of security patches for a critical flaw that was detected in their OS. Although this is an urgent matter, there is no guarantee yet that these patches will be bug-free and production-ready hence, the company must immediately patch all of its affected Amazon EC2 instances in all the environments, except for the production environment. The EC2 instances in the production environment will only be patched after it has been verified that the patches work effectively. Each environment also has different baseline patch requirements that needed to be satisfied.
Using the AWS Systems Manager service, how should you perform this task with the least amount of effort?

- **A.** Tag each instance based on its environment and OS. Create various shell scripts for each environment that specifies which patch will serve as its baseline. Using AWS Systems Manager Run Command, place the EC2 instances into Target Groups and execute the script corresponding to each Target Group.
- **B.** Tag each instance based on its environment and OS. Create a patch baseline in AWS Systems Manager Patch Manager for each environment. Categorize EC2 instances based on their tags using Patch Groups and apply the patches specified in the corresponding patch baseline to each Patch Group.
- **C.** Schedule a maintenance period in AWS Systems Manager Maintenance Windows for each environment, where the period is after business hours so as not to affect daily operations. During the maintenance period, Systems Manager will execute a cron job that will install the required patches for each EC2 instance in each environment. After that, verify in Systems Manager Managed Instances that your environments are fully patched and compliant.
- **D.** Tag each instance based on its OS. Create a patch baseline in AWS Systems Manager Patch Manager for each environment. Categorize EC2 instances based on their tags using Patch Groups and then apply the patches specified in the corresponding patch baseline to each Patch Group. Afterward, verify that the patches have been installed correctly using Patch Compliance. Record the changes to patch and association compliance statuses using AWS Config.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** patch all envs EXCEPT prod; each env different baseline; least effort

🪤 **Your trap:** Tagging by OS only → can't tell environments apart, so prod can't be excluded

🧠 **Rule:** Per-environment patching → tag by environment + OS, one patch baseline per env, Patch Groups, Maintenance Windows.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Production OU   Development OU   Test OU
    │                │               │
    └── KHÔNG patch  └── Patch ngay  └── Patch ngay
        (chờ verify)     (baseline riêng)  (baseline riêng)

Yêu cầu: patch tất cả TRỪ production, mỗi env có baseline riêng, ÍT effort nhất
```

Đáp án đúng: **B (tag theo environment + OS, patch baseline riêng cho mỗi env, Patch Group)**. Anh chọn **D** — thiếu tag environment, chỉ tag theo OS.

#### B đúng — vì sao phải tag theo cả environment VÀ OS

Mấu chốt của câu này là **loại trừ được production** mà vẫn giữ effort thấp nhất. Muốn loại trừ theo environment thì tag phải chứa thông tin environment:

```
Tag: Patch Group = "dev-ubuntu", "test-ubuntu", "prod-ubuntu"
        │                │                │
   baseline riêng    baseline riêng    (không đăng ký patch execution)
```

Mỗi Patch Group ứng với một patch baseline riêng (đáp ứng "mỗi env có baseline khác nhau"), và vì có tag environment, admin có thể patch dev + test mà **không đụng đến** patch group của production — không cần script, không cần cron riêng, dùng đúng cơ chế native của Patch Manager.

#### Vì sao D (lựa chọn của anh) sai

D giống B ở gần hết các bước, nhưng chỉ **"tag each instance based on its OS"** — bỏ mất yếu tố environment. Nếu tag chỉ có OS (ví dụ tất cả instance Ubuntu đều mang tag `ubuntu` bất kể là prod/dev/test), thì khi anh apply patch cho Patch Group "ubuntu", **cả production cũng bị patch theo** — vi phạm trực tiếp yêu cầu "except for the production environment". Đây là bẫy tinh vi: D dùng đúng toàn bộ công cụ (Patch Manager, Patch Group, Patch Compliance, AWS Config) nhưng sai ở nguồn dữ liệu phân loại đầu vào (tag).

#### Vì sao các lựa chọn khác sai

- **A:** dùng shell script tự viết + Run Command đặt instance vào Target Group để chạy script — đây là cách làm thủ công, tốn nhiều effort hơn hẳn so với dùng sẵn Patch Manager/patch baseline có sẵn cơ chế auto-approve theo thời gian.
- **C:** dùng Maintenance Windows + cron job tự chạy patch cho từng environment — về mặt kỹ thuật khả thi nhưng đòi hỏi cấu hình nhiều (schedule, cron riêng cho mỗi env) hơn so với chỉ cần Patch Group + baseline như B.

| Lựa chọn | Tag theo | Loại trừ được prod? | Effort |
|---|---|---|---|
| **B** | Environment + OS | Có | Thấp nhất |
| D | Chỉ OS | **Không** — prod cũng bị patch | Thấp nhưng sai yêu cầu |
| A | Environment + OS | Có | Cao (script + Run Command thủ công) |
| C | — | Có | Cao (Maintenance Window + cron riêng từng env) |

#### Quy tắc nhớ cho thi

- **"mỗi environment có baseline riêng, cần loại trừ 1 env"** → tag phải bao gồm **environment**, không chỉ OS
- **"ít effort nhất, dùng Systems Manager"** → luôn ưu tiên **Patch Manager + Patch Group + baseline có sẵn**, tránh Run Command/script tự viết
- Nhìn kỹ câu trả lời gần giống nhau chỉ khác 1-2 chữ (ví dụ "OS" vs "environment and OS") — đây là bẫy phổ biến của TD

### TD explanation

AWS Systems Manager Patch Manager automates the process of patching managed instances with security-related updates. For Linux-based instances, you can also install patches for non-security updates. You can patch fleets of Amazon EC2 instances or your on-premises servers and virtual machines (VMs) by operating system type.
Patch Manager uses patch baselines, which include rules for auto-approving patches within days of their release, as well as a list of approved and rejected patches. You can install patches on a regular basis by scheduling patching to run as a Systems Manager Maintenance Window task. You can also install patches individually or to large groups of instances by using Amazon EC2 tags. For each auto-approval rule that you create, you can specify an auto-approval delay. This delay is the number of days of wait after the patch was released, before the patch is automatically approved for patching.

A patch group is an optional means of organizing instances for patching. For example, you can create patch groups for different operating systems (Linux or Windows), different environments (Development, Test, and Production), or different server functions (web servers, file servers, databases). Patch groups can help you avoid deploying patches to the wrong set of instances. They can also help you avoid deploying patches before they have been adequately tested. You create a patch group by using Amazon EC2 tags. Unlike other tagging scenarios across Systems Manager, a patch group must be defined with the tag key: Patch Group. After you create a patch group and tag instances, you can register the patch group with a patch baseline. By registering the patch group with a patch baseline, you ensure that the correct patches are installed during the patching execution.
Hence, the correct answer is: Tag each instance based on its environment and OS. Create a patch baseline in AWS Systems Manager Patch Manager for each environment. Categorize EC2 instances based on their tags using Patch Groups and apply the patches specified in the corresponding patch baseline to each Patch Group.
The option that says: Tag each instance based on its environment and OS. Create various shell scripts for each environment that specifies which patch will serve as its baseline. Using AWS Systems Manager Run Command, place the EC2 instances into Target Groups and execute the script corresponding to each Target Group is incorrect as this option takes more effort to perform because you are using Systems Manager Run Command instead of Patch Manager. The Run Command service enables you to automate common administrative tasks and perform ad hoc configuration changes at scale, however, it takes a lot of effort to implement this solution. You can use Patch Manager instead to perform the task required by the scenario since you need to perform this task with the least amount of effort.
The option that says: Tag each instance based on its OS. Create a patch baseline in AWS Systems Manager Patch Manager for each environment. Categorize EC2 instances based on their tags using Patch Groups and then apply the patches specified in the corresponding patch baseline to each Patch Group. Afterward, verify that the patches have been installed correctly using Patch Compliance. Record the changes to patch and association compliance statuses using AWS Config is incorrect. You should be tagging instances based on the environment and its OS type in which they belong and not just its OS type. This is because the type of patches that will be applied varies between the different environments. With this option, the Ubuntu EC2 instances in all of your environments, including in production, will automatically be patched.
The option that says: Schedule a maintenance period in AWS Systems Manager Maintenance Windows for each environment, where the period is after business hours so as not to affect daily operations. During the maintenance period, Systems Manager will execute a cron job that will install the required patches for each EC2 instance in each environment. After that, verify in Systems Manager Managed Instances that your environments are fully patched and compliant is incorrect because this is not the simplest way to address the issue using AWS Systems Manager. The AWS Systems Manager Maintenance Windows feature lets you define a schedule for when to perform potentially disruptive actions on your instances such as patching an operating system, updating drivers, or installing software or patches. Each Maintenance Window has a schedule, a maximum duration, a set of registered targets (the instances that are acted upon), and a set of registered tasks. Although this solution may work, it entails a lot of configuration and effort to implement.
References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html
https://aws.amazon.com/blogs/mt/patching-your-windows-ec2-instances-using-aws-systems-manager-patch-manager/

Check out this AWS Systems Manager Cheat Sheet:
https://tutorialsdojo.com/aws-systems-manager/

</details>

<a id="q73"></a>

## Q73

An enterprise runs its CMS application on an Auto Scaling group of Amazon EC2 instances behind an Application Load Balancer. The instances are placed on private subnets while the ALB is placed on public subnets. As part of best practices, the AWS Systems Manager Agent is installed on the instances and the AWS Systems Manager Session Manager is used to login into the instances. The EC2 instances send application logs to Amazon CloudWatch Logs.
Upon the deployment of the new application version, the new instances are being marked as unhealthy by the ALB and are being replaced by the Auto Scaling group. For troubleshooting, the solutions architect tries to log in on the unhealthy instances but the instances are getting terminated. The collected logs on CloudWatch Logs do not show definitive errors in the application.
Which of the following options is the quickest way for the solutions architect to troubleshoot the problem?

- **A.** Go to the Auto Scaling Groups section in the AWS console and suspend the “Terminate” process for the ASG. Log in to one of the unhealthy instances using AWS Systems Manager Session Manager.
- **B.** Create a temporary Amazon EC2 instance and deploy the new application version. Login to the EC2 instance using the SSH key. Add the instance to the Application Load Balancer to inspect application logs in real-time.
- **C.** Update the application log setting to have more verbose logging to capture more application logs. Ensure that the Amazon CloudWatch agent is installed and running on the instances.
- **D.** Select one of the new Amazon EC2 instances and enable EC2 instance termination protection. Gain access to the unhealthy instance using the AWS Systems Manager Session Manager.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** 🔁 new version marked unhealthy; ASG terminates before you can log in; quickest troubleshoot

🪤 **Your trap:** 🔁 Same pick as the chapter drill: verbose logging doesn't stop the ASG from terminating the instance

🧠 **Rule:** Keep unhealthy instances alive to debug → suspend the ASG 'Terminate' process (or lifecycle hook / standby), then Session Manager.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ALB (public subnet)
   │  health check
   ▼
ASG (private subnet) ── deploy version mới ── health check FAIL
   │                                              │
   └── instance bị mark unhealthy ──► ASG TERMINATE ngay
                                              │
                        Anh cố login qua Session Manager → instance đã bị xóa
                        CloudWatch Logs không có lỗi rõ ràng
```

Đáp án đúng: **A (suspend process "Terminate" của ASG, rồi login bằng Session Manager)**. Anh chọn **C** (tăng verbose logging).

⚠️ **Lỗi lặp lại:** đây đúng là lựa chọn anh đã chọn sai trong chapter drill (cùng pick C — verbose logging). Ghi nhớ: khi instance **bị xóa trước khi log kịp gửi**, tăng log verbosity vô nghĩa — vấn đề là **thời gian sống** của instance, không phải **độ chi tiết** của log.

#### A đúng — vì sao suspend "Terminate" là cách nhanh nhất

Root cause của việc không troubleshoot được là ASG **xóa instance ngay khi unhealthy**, nên bất kể log có chi tiết đến đâu, SSH/Session Manager có sẵn sàng đến đâu, anh cũng không kịp vào trước khi instance biến mất. Amazon EC2 Auto Scaling cho phép **suspend từng process riêng lẻ** (Launch, Terminate, HealthCheck, ReplaceUnhealthy...). Suspend đúng process **"Terminate"** giữ nguyên instance unhealthy còn sống, group vẫn hoạt động bình thường ở các process khác:

```
Suspend "Terminate" process
        │
        ▼
Instance unhealthy KHÔNG bị xóa
        │
        ▼
Login bằng Session Manager (không cần SSH key,
không cần mở port, không cần bastion) → xem log, process, config trực tiếp
```

Đây là cách nhanh nhất vì không cần dựng lại môi trường, không cần đợi log pipeline, không cần thêm resource.

#### Vì sao C (lựa chọn của anh) sai

C đề xuất tăng verbose logging và đảm bảo CloudWatch Agent đang chạy. Vấn đề là: **instance bị terminate trước khi anh có thể chỉnh log hoặc chờ log mới gửi lên**. Ngay cả log có verbose tối đa, nếu app crash/health check fail ngay ở early stage (trước khi CloudWatch Agent kịp flush log ra), thông tin vẫn không tới được CloudWatch Logs. C không giải quyết được nguyên nhân gốc — thời gian sống của instance quá ngắn để thu thập bất cứ thứ gì thêm.

#### Vì sao các lựa chọn khác sai

- **B (tạo instance tạm, SSH, gắn vào ALB):** khả thi về lý thuyết nhưng tốn nhiều bước — tạo instance mới, deploy lại version mới, cấu hình SSH key, đăng ký vào target group của ALB — chậm hơn nhiều so với chỉ suspend 1 process.
- **D (EC2 instance termination protection):** **termination protection chỉ chặn được việc terminate instance thủ công/qua API `TerminateInstances` trực tiếp**, không chặn được ASG tự xóa instance mà nó quản lý khi coi instance đó unhealthy — ASG vẫn có quyền thay thế instance của nó.

| Lựa chọn | Ngăn được ASG terminate? | Số bước triển khai | Tốc độ |
|---|---|---|---|
| **A. Suspend Terminate process** | Có | Ít | Nhanh nhất |
| D. Instance termination protection | **Không** (ASG vẫn xóa được) | Ít | — |
| C. Verbose logging | Không liên quan | Ít | Không giải quyết vấn đề |
| B. Instance tạm + SSH + ALB | Có (né vấn đề) | Nhiều | Chậm |

#### Quy tắc nhớ cho thi

- **"muốn giữ instance unhealthy sống để debug"** → **suspend ASG process "Terminate"** (hoặc lifecycle hook / đưa vào Standby), không phải EC2 termination protection
- **"EC2 termination protection"** → chỉ chặn xóa qua API/console thủ công, **không** chặn ASG replace instance của chính nó
- **"log không đủ thông tin vì instance chết quá nhanh"** → tăng verbose log không giúp gì, phải **kéo dài thời gian sống** của instance trước

### TD explanation

An Auto Scaling group contains a collection of EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. An Auto Scaling group also lets you use Amazon EC2 Auto Scaling features such as health check replacements and scaling policies. Both maintaining the number of instances in an Auto Scaling group and automatic scaling are the core functionality of the Amazon EC2 Auto Scaling service.
An Auto Scaling group starts by launching enough instances to meet its desired capacity. It maintains this number of instances by performing periodic health checks on the instances in the group. The Auto Scaling group continues to maintain a fixed number of instances even if an instance becomes unhealthy.
You can suspend and then resume one or more of the processes for your Auto Scaling group. You might want to do this, for example, so that you can investigate a configuration issue that is causing the process to fail or to prevent Amazon EC2 Auto Scaling from marking instances unhealthy and replacing them while you are making changes to your Auto Scaling group.

Session Manager is a fully managed AWS Systems Manager capability. With Session Manager, you can manage your Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, and on-premises servers and virtual machines (VMs). You can use either an interactive one-click browser-based shell or the AWS Command Line Interface (AWS CLI). Session Manager provides secure and auditable node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.
Therefore, the correct answer is: Go to the Auto Scaling Groups section in the AWS console and suspend the “Terminate” process for the ASG. Log in to one of the unhealthy instances using AWS Systems Manager Session Manager. This will stop the Auto Scaling group from terminating the EC2 instances, thus, giving you enough time to log in and troubleshoot the issue.
The option that says: Update the application log setting to have more verbose logging to capture more application logs. Ensure that the Amazon CloudWatch agent is installed and running on the instances is incorrect. This is possible however, this will not solve the problem of terminating EC2 instances. It is possible that the EC2 instances are terminated even before they start sending logs to CloudWatch logs.
The option that says: Select one of the new Amazon EC2 instances and enable EC2 instance termination protection. Gain access to the unhealthy instance using the AWS Systems Manager Session Manager is incorrect. Even if the EC2 instance protection is enabled, the ASG has the ability to terminate an EC2 instance that it has created. You should suspend the “Terminate” process of the ASG instead.
The option that says: Create a temporary Amazon EC2 instance and deploy the new application version. Login to the EC2 instance using the SSH key. Add the instance to the Application Load Balancer to inspect application logs in real-time is incorrect. This is possible, but it takes a log of steps and is not the quickest solution.

References:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html
https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html
https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html

Check out these AWS Systems Manager and AWS Auto Scaling Cheat Sheets:
https://tutorialsdojo.com/aws-systems-manager/
https://tutorialsdojo.com/aws-auto-scaling/

</details>

---

# Group D — Multi-account governance & cost (3)

<a id="q28"></a>

## Q28

A company is using AWS Organizations to manage their multi-account and multi-region AWS infrastructure. They are currently doing large-scale automation for their key daily processes to save costs. One of these key processes is sharing specified AWS resources, which an organizational account owns, with other AWS accounts of the company using AWS RAM. There is already an existing service which was previously managed by a separate organization account moderator, who also maintained the specific configuration details.
In this scenario, what could be a simple and effective solution that would allow the service to perform its tasks on the organization accounts on the moderator’s behalf?

- **A.** Attach an IAM role on the service detailing all the allowed actions that it will be able to perform. Install an SSM agent in each of the worker VMs. Use AWS Systems Manager to build automation workflows that involve the daily key processes.
- **B.** Configure a service-linked role for AWS RAM and modify the permissions policy to specify what the role can and cannot do. Lastly, modify the trust policy of the role so that other processes can utilize AWS RAM.
- **C.** Use trusted access by running the enable-sharing-with-aws-organization command in the AWS RAM CLI. Mirror the configuration changes that was performed by the account that previously managed this service.
- **D.** Enable cross-account access with AWS Organizations in the Resource Access Manager Console. Mirror the configuration changes that was performed by the account that previously managed this service.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** share resources via RAM with org accounts; service acts on moderator's behalf; simple

🪤 **Your trap:** 'Cross-account access' isn't a RAM feature — the actual mechanism is trusted access

🧠 **Rule:** RAM + Organizations → enable trusted access (`aws ram enable-sharing-with-aws-organization`).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations
   │
   ├── Org account (owner của resource, share qua AWS RAM)
   ├── Member accounts (nhận resource được share)
   │
   └── Moderator account cũ đã cấu hình 1 "service" chạy hộ (tự động hoá daily process)
              │
              └── Cần: service này tiếp tục thao tác trên TẤT CẢ account của org,
                       thay mặt moderator, càng đơn giản càng tốt
```

Đáp án đúng: **C (enable trusted access qua `enable-sharing-with-aws-organization` trong RAM CLI, rồi mirror lại config cũ)**. Anh chọn **D** ("Enable cross-account access... trong RAM Console") — nghe rất giống nhưng không phải tên tính năng thật.

#### C đúng — vì sao "trusted access" là cơ chế chuẩn

**Trusted access** là cơ chế của AWS Organizations cho phép một **AWS service** (ví dụ AWS RAM) tự động thực hiện tác vụ trên **toàn bộ account trong org**, thay mặt người dùng, mà không cần cấp quyền IAM thủ công cho từng account:

```
aws ram enable-sharing-with-aws-organization
        │
        ▼
AWS RAM tạo service-linked role (AWSResourceAccessManagerServiceRolePolicy)
        trong MỌI account của Organization
        │
        ▼
Service tự động share resource theo cấu hình đã định, không cần thiết lập
IAM role/permission riêng cho từng account
```

Đây chính xác là "simple and effective" theo yêu cầu đề: một lệnh CLI kích hoạt, AWS tự tạo role cần thiết, sau đó chỉ cần mirror lại config cũ mà moderator từng thiết lập.

#### Vì sao D (lựa chọn của anh) sai

D dùng chữ **"cross-account access"** — đây **không phải tên một tính năng thực sự tồn tại** trong RAM Console dưới hình thức được mô tả. Tính năng đúng cần kích hoạt là **trusted access**, không phải "cross-account access". Đây là bẫy dùng từ ngữ generic nghe hợp lý (cross-account nghe rất đúng ngữ cảnh chia sẻ resource giữa các account) nhưng sai thuật ngữ AWS chính xác — TD cố ý đặt option gần giống để kiểm tra người học có nhớ đúng tên cơ chế hay không.

#### Vì sao các lựa chọn khác sai

- **A (IAM role + SSM agent + Systems Manager automation):** Systems Manager là để tự động hoá tác vụ trên EC2/on-premises server, không phải cơ chế chia sẻ resource qua RAM giữa các account của Organization — sai domain, phức tạp hơn cần thiết.
- **B (service-linked role tự tạo, tự sửa trust policy):** sai vì hai lý do — (1) khi bật trusted access, AWS Organizations **tự tạo** service-linked role, không cần tự cấu hình tay; (2) **trust policy của service-linked role không thể sửa** — chỉ service được liên kết (AWS RAM) mới được assume role đó.

| Lựa chọn | Cơ chế | Đúng thuật ngữ AWS? | Effort |
|---|---|---|---|
| **C. Trusted access (CLI)** | `enable-sharing-with-aws-organization` | Đúng | Thấp |
| D. "Cross-account access" (Console) | Không phải tên tính năng thật | Sai | — |
| B. Tự tạo service-linked role | Trust policy không sửa được | Sai kỹ thuật | Cao |
| A. SSM + IAM role tự viết | Sai domain (SSM cho EC2, không cho RAM) | Sai | Cao |

#### Quy tắc nhớ cho thi

- **"1 AWS service làm việc thay mặt trên toàn Organization"** → **trusted access**, không phải "cross-account access"
- **"service-linked role"** → luôn được **tạo tự động** khi bật trusted access; **trust policy không sửa được**, chỉ service liên kết mới assume được
- Cẩn thận các option dùng từ nghe hợp lý (cross-account access, cross-account role) nhưng không khớp tên chính thức của tính năng AWS

### TD explanation

AWS Resource Access Manager (AWS RAM) enables you to share specified AWS resources that you own with other AWS accounts. To enable trusted access with AWS Organizations:

From the AWS RAM CLI, use the enable-sharing-with-aws-organizations command.
Name of the IAM service-linked role that can be created in accounts when trusted access is enabled: AWSResourceAccessManagerServiceRolePolicy.

You can use trusted access to enable an AWS service that you specify, called the trusted service, to perform tasks in your organization and its accounts on your behalf. This involves granting permissions to the trusted service but does not otherwise affect the permissions for IAM users or roles. When you enable access, the trusted service can create an IAM role called a service-linked role in every account in your organization. That role has a permissions policy that allows the trusted service to do the tasks that are described in that service’s documentation. This enables you to specify settings and configuration details that you would like the trusted service to maintain in your organization’s accounts on your behalf.

Therefore the correct answer is: Use trusted access by running the enable-sharing-with-aws-organization command in the AWS RAM CLI. Mirror the configuration changes that was performed by the account that previously managed this service.
The option that says: Attach an IAM role on the service detailing all the allowed actions that it will be able to perform. Install an SSM agent in each of the worker VMs. Use AWS Systems Manager to build automation workflows that involve the daily key processes is incorrect because this is not the simplest way to automate the interaction of AWS RAM with AWS Organizations. AWS Systems Manager is a tool that helps with the automation of EC2 instances, on-premises servers, and other virtual machines. It might not support all the services being used by the key processes.
The option that says: Configure a service-linked role for AWS RAM and modify the permissions policy to specify what the role can and cannot do. Lastly, modify the trust policy of the role so that other processes can utilize AWS RAM is incorrect. This is not the simplest solution for integrating AWS RAM and AWS Organizations since using AWS Organization’s trusted access will create the service-linked role for you. Also, the trust policy of a service-linked role cannot be modified. Only the linked AWS service can assume a service-linked role, which is why you cannot modify the trust policy of a service-linked role.
The option that says: Enable cross-account access with AWS Organizations in the Resources Access Manager Console. Mirror the configuration changes that was performed by the account that previously managed this service is incorrect because you should enable trusted access to AWS RAM, not cross-account access.

References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html
https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ram.html
https://aws.amazon.com/blogs/security/introducing-an-easier-way-to-delegate-permissions-to-aws-services-service-linked-roles/

Check out this AWS Resource Access Manager Cheat Sheet:
https://tutorialsdojo.com/aws-resource-access-manager/

</details>

<a id="q40"></a>

## Q40

A company has several AWS accounts that are managed using AWS Organizations. The company created only one organizational unit (OU), so all child accounts are members of the Production OU. The Solutions Architects control access to certain AWS services using SCPs that define the restricted services. The SCPs are attached at the root of the organization, which means the restrictions apply to all AWS accounts within the organization. The company recently acquired a small business firm, and its existing AWS account was invited to join the organization using the InviteAccountToOrganization operation in the Organizations API. Upon onboarding, the administrators of the small business firm cannot apply the required AWS Config rules to meet the parent company’s security policies.
Which of the following options will allow the administrators to update the Config rules on the AWS account without introducing long-term management overhead?

- **A.** Add the new account to a temporary Onboarding organization unit (OU) that has an attached SCP allowing changes to Config. Perform the needed changes while on this temporary OU before moving the new account to the Production OU.
- **B.** Instead of using a “deny list” to AWS services on the organization’s root SCPs, use an “allow list” to allow only the required AWS services. Temporarily add the Config service to the “allow list” for the principals of the new account and make the required changes.
- **C.** Remove the SCPs on the organization’s root and apply them to the Production OU instead. Create a temporary Onboarding OU that has an attached SCP allowing changes to Config. Add the new account to this temporary OU and make the required changes before moving it to the Production OU.
- **D.** Update the SCPs applied in the root of the AWS organization and remove the rule that restricts changes to the Config service. Deploy a new AWS Service Catalog to the whole organization, containing the company’s Config policies.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** root SCP blocks Config changes; acquired account can't apply Config rules; no long-term overhead

🪤 **Your trap:** Removing the root restriction lets EVERY account change Config; an onboarding OU alone still inherits the root deny

🧠 **Rule:** Deny at root blocks all OUs → move SCPs from root to the Production OU + temporary Onboarding OU for new accounts.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Organization Root
   │
   └── SCP (deny list các service, gồm "deny thay đổi Config") ── gắn ở ROOT
           │
           └── Production OU (duy nhất, chứa mọi account)
                   │
                   └── Account mới acquire, invite vào Org
                           │
                           └── Cần đổi Config rule NGAY, nhưng bị SCP ở root chặn
                               → cần giải pháp KHÔNG tăng long-term overhead
```

Đáp án đúng: **C (dời SCP từ root xuống Production OU + tạo Onboarding OU tạm có SCP riêng cho phép sửa Config)**. Anh chọn **D** (xoá rule chặn Config khỏi SCP ở root).

#### C đúng — vì sao phải dời SCP ra khỏi root

Cơ chế SCP: **một account chỉ có permission nếu được TẤT CẢ policy từ root xuống đến account đó allow.** Nếu SCP deny nằm ở **root**, deny này áp dụng cho **mọi OU dưới nó, không có ngoại lệ** — không OU con nào override được deny ở cấp cha bằng một allow riêng.

```
Root (SCP deny Config)  ← nếu để ở đây, KHÔNG OU nào thoát được deny này
   │
   ├── Production OU        (không có SCP riêng)
   └── Onboarding OU (tạm)  (SCP allow Config) ← vẫn bị deny từ root đè lên!
```

Giải pháp đúng: **dời SCP xuống Production OU**, để root không còn deny nào cả. Khi đó Onboarding OU (tạo mới, SCP riêng cho phép sửa Config) hoàn toàn độc lập với Production OU:

```
Root (không SCP)
   │
   ├── Production OU (SCP deny Config)     ← các account cũ vẫn bị hạn chế như trước
   └── Onboarding OU (SCP allow Config)     ← account mới sửa Config tự do ở đây
              │
              └── sau khi xong, move account này sang Production OU
```

Đây là giải pháp không tăng long-term overhead: Onboarding OU chỉ dùng tạm cho account mới gia nhập, không cần duy trì exception vĩnh viễn.

#### Vì sao D (lựa chọn của anh) sai

D xoá hẳn rule chặn Config **ở root** — nghĩa là **mọi account trong toàn Organization**, kể cả các account production hiện tại, đều có quyền sửa Config rules tuỳ ý. Điều này phá vỡ chính sách bảo mật ban đầu (chỉ định các Solutions Architect kiểm soát Config qua SCP), không phải một giải pháp "không tăng overhead" — ngược lại nó loại bỏ toàn bộ control mà công ty đã thiết lập.

#### Vì sao các lựa chọn khác sai

- **A (chỉ thêm Onboarding OU, giữ SCP ở root):** vô nghĩa vì deny ở root vẫn áp dụng cho Onboarding OU — Config vẫn bị chặn dù có SCP allow riêng ở OU con, vì deny luôn thắng allow khi ở cấp cao hơn.
- **B (chuyển deny-list sang allow-list, tạm thêm Config vào allow-list):** giải quyết được ngay lúc này nhưng **tăng long-term overhead** — mỗi khi có service mới cần dùng trong tương lai, admin phải liên tục cập nhật allow-list, phức tạp hơn nhiều so với quản lý theo OU.

| Lựa chọn | SCP đặt ở đâu | Account mới sửa Config được? | Overhead dài hạn |
|---|---|---|---|
| **C** | Production OU (dời từ root) + Onboarding OU riêng | Được, trong Onboarding OU | Thấp |
| A | Vẫn ở root | **Không** — deny root vẫn áp | — |
| B | Root, đổi deny-list → allow-list | Được (tạm allow) | Cao — phải maintain allow-list liên tục |
| D | Root, xoá rule Config | Được, nhưng **mọi** account đều được | Rủi ro bảo mật cao |

#### Quy tắc nhớ cho thi

- **SCP ở root luôn áp dụng cho mọi OU con** — không OU nào override được deny từ cấp cha bằng allow riêng
- **AWS khuyến nghị không gắn SCP trực tiếp vào root** — nên gắn vào OU cụ thể để dễ test và có OU riêng cho trường hợp ngoại lệ (onboarding)
- **"account mới cần ngoại lệ tạm thời, không tăng overhead dài hạn"** → tạo **Onboarding OU riêng**, không sửa SCP ở root, không dùng allow-list toàn Organization

### TD explanation

AWS Organizations helps you centrally manage and govern your environment as you grow and scale your AWS resources. Using AWS Organizations, you can programmatically create new AWS accounts and allocate resources, group accounts to organize your workflows, apply policies to accounts or groups for governance, and simplify billing by using a single payment method for all of your accounts.
With AWS Organizations, you can consolidate multiple AWS accounts into an organization that you create and centrally manage. You can create member accounts and invite existing accounts to join your organization. You can organize those accounts into groups and attach policy-based controls.

Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. SCPs help you to ensure your accounts stay within your organization’s access control guidelines. SCPs are available only in an organization that has all features enabled.
An SCP restricts permissions for IAM users and roles in member accounts, including the member account’s root user. Any account has only those permissions allowed by every parent above it. If a permission is blocked at any level above the account, either implicitly (by not being included in an Allow policy statement) or explicitly (by being included in a Deny policy statement), a user or role in the affected account can’t use that permission, even if the account administrator attaches the AdministratorAccess IAM policy with */* permissions to the user.
AWS strongly recommends that you don’t attach SCPs to the root of your organization without thoroughly testing the impact that the policy has on accounts. Instead, create an OU that you can move your accounts into one at a time, or at least in small numbers, to ensure that you don’t inadvertently lock users out of key services.
Hence, the correct answer is: Remove the SCPs on the organization’s root and apply them to the Production OU instead. Create a temporary Onboarding OU that has an attached SCP allowing changes to Config. Add the new account to this temporary OU and make the required changes before moving it to the Production OU. It is not recommended to attach the SCPs to the root of the organization, so it is better to move all the SCPs to the Production OU. This way, the temporary Onboarding OU can have an independent SCP to allow the required changes on AWS Config. Then, you can move the new AWS account to the Production OU.
The option that says: Update the SCPs applied in the root of the AWS organization and remove the rule that restricts changes to the Config service. Deploy a new AWS Service Catalog to the whole organization, containing the company’s Config policies is incorrect. Although AWS Service Catalog primarily allows organizations to create and manage catalogs of IT services that are approved for use on AWS, this will cause possible problems in the future for the administrators. Removing the AWS Config restriction on the root of the AWS organization’s SCP will allow all Admins on all AWS accounts to manage/change/update their own AWS Config rules.
The option that says: Add the new account to a temporary Onboarding organization unit (OU) that has an attached SCP allowing changes to Config. Perform the needed changes while on this temporary OU before moving the new account to the Production OU is incorrect. If the SCP applied to the organization’s root has a “deny” permission, all OUs under the organization will inherit that rule. You cannot override an explicit “deny” permission with an explicit “allow” applied to the temporary Onboarding OU.
The option that says: Instead of using a “deny list” to AWS services on the organization’s root SCPs, use an “allow list” to allow only the required AWS services. Temporarily add the Config service to the “allow list” for the principals of the new account and make the required changes is incorrect. This is possible; however, it will typically cause more management problems in the future, as you will have to update the “allow list” for any service that users may require in the future.

References:
https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html
https://aws.amazon.com/organizations/
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html

Check out these AWS Organizations and SCP Comparison Cheat Sheets:
https://tutorialsdojo.com/aws-organizations/
https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/

</details>

<a id="q55"></a>

## Q55

A graphics design startup is using multiple Amazon S3 buckets to store high-resolution media files for their various digital artworks. After securing a partnership deal with a leading media company, the two parties shall be sharing digital resources with one another as part of the contract. The media company frequently performs multiple object retrievals from the S3 buckets every day, which increased the startup’s data transfer costs. 
As the Solutions Architect, what should you do to help the startup lower their operational costs?

- **A.** Advise the media company to create their own S3 bucket. Then run the aws s3 sync s3://sourcebucket s3://destinationbucket command to copy the objects from their S3 bucket to the other party’s S3 bucket. In this way, future retrievals can be made on the media company’s S3 bucket instead.
- **B.** Enable the Requester Pays feature in all of the startup's S3 buckets to make the media company pay the cost of the data transfer from the buckets.
- **C.** Create a new billing account for the social media company by using AWS Organizations. Apply SCPs on the organization to ensure that each account has access only to its own resources and each other's S3 buckets.
- **D.** Provide cross-account access for the media company, which has permissions to access contents in the S3 bucket. Cross-account retrieval of S3 objects is charged to the account that made the request.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** partner frequently downloads from startup's S3; lower startup's data transfer cost

🪤 **Your trap:** s3 sync still charges transfer out + extra storage; cross-account GET is billed to the bucket owner

🧠 **Rule:** Make downloaders pay → S3 Requester Pays.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Startup's S3 buckets (chứa media chất lượng cao)
        │
        │  Media company GET nhiều lần/ngày
        ▼
Data transfer cost tăng cao cho STARTUP (bucket owner)

Yêu cầu: giảm chi phí vận hành cho STARTUP
```

Đáp án đúng: **B (bật Requester Pays trên các bucket của startup)**. Anh chọn **A** (đề nghị đối tác tự tạo bucket riêng và `aws s3 sync` sang).

#### B đúng — vì sao Requester Pays giải quyết đúng vấn đề

Theo default, **bucket owner luôn trả phí storage và data transfer** của request tới bucket đó — bất kể ai là người gửi request. Khi bật **Requester Pays**:

```
Request GET tới bucket (có Requester Pays)
        │
        ├── Phải có header/param x-amz-request-payer trong request
        │   (xác nhận requester đồng ý trả phí)
        ▼
   Chi phí REQUEST + DATA TRANSFER  → tính cho REQUESTER (media company)
   Chi phí STORAGE                  → vẫn luôn do BUCKET OWNER (startup) trả
```

Đây đúng là cơ chế được thiết kế riêng cho tình huống "bên ngoài truy vấn nhiều, chủ bucket không muốn ôm hết transfer cost" — không cần đổi kiến trúc, không cần tạo account/bucket mới, chỉ là một cấu hình trên bucket hiện có.

#### Vì sao A (lựa chọn của anh) sai

A đề xuất **đồng bộ toàn bộ object sang bucket của đối tác** bằng `aws s3 sync`. Vấn đề: **chính hành động sync này đã tạo ra data transfer cost** (out-bound từ bucket của startup) — startup vẫn phải trả chi phí này ngay từ lúc thực hiện đồng bộ, ngoài ra còn tốn thêm **chi phí storage nhân đôi** vì dữ liệu tồn tại ở cả hai bucket. Đây không giảm chi phí, mà chỉ dịch chuyển vấn đề, thậm chí tạo thêm chi phí mới lúc sync. Đây là bẫy: nghe "để media company tự lưu bên họ" tưởng như giải quyết gốc, nhưng chi phí chuyển giao ban đầu vẫn đổ lên startup.

#### Vì sao các lựa chọn khác sai

- **C (tạo billing account riêng qua Organizations + SCP giới hạn truy cập bucket của nhau):** sai vì AWS Organizations **không tạo billing account riêng cho từng member** — nó dùng **consolidated billing**, nghĩa là account chủ (management account) vẫn trả hộ toàn bộ chi phí của các account con. C hiểu sai bản chất billing của Organizations.
- **D (cross-account access, cho rằng request cross-account được charge cho account gọi):** sai vì **cross-account access mặc định KHÔNG đổi chủ thể chịu phí** — bucket owner vẫn là người trả chi phí request/data transfer trừ khi Requester Pays được bật rõ ràng. Đây là hiểu nhầm phổ biến về IAM cross-account: quyền truy cập (permission) và chi phí (billing) là hai khái niệm tách biệt.

| Lựa chọn | Ai chịu data transfer cost? | Tốn thêm chi phí phụ? |
|---|---|---|
| **B. Requester Pays** | Media company (requester) | Không |
| A. Sync sang bucket riêng | Startup (lúc sync) | Có — storage đôi + transfer lúc sync |
| D. Cross-account access | Startup (bucket owner, mặc định) | — |
| C. Organizations + SCP | Startup (do consolidated billing) | — |

#### Lưu ý thực tế

Muốn Requester Pays hoạt động, **mọi request** (GET/HEAD/POST) tới bucket phải kèm `x-amz-request-payer: requester` — nếu thiếu, request bị từ chối (bucket owner sẽ không tự động gánh chi phí thay). Anonymous request (không authenticated) **không thể** truy cập bucket có Requester Pays — vì AWS cần xác thực để biết charge cho ai.

#### Quy tắc nhớ cho thi

- **"muốn bên tải xuống chịu chi phí data transfer"** → **S3 Requester Pays**, không phải sync hay cross-account access
- **"AWS Organizations billing"** → luôn là **consolidated billing** (1 management account trả hộ), không có khái niệm "billing account riêng cho member account"
- **Cross-account IAM permission ≠ ai chịu billing** — permission chỉ quyết định được truy cập hay không, billing vẫn theo bucket owner trừ khi có Requester Pays

### TD explanation

In general, bucket owners pay for all Amazon S3 storage and data transfer costs associated with their bucket. A bucket owner, however, can configure a bucket to be a Requester Pays bucket. With Requester Pays buckets, the requester instead of the bucket owner pays the cost of the request and the data download from the bucket. The bucket owner always pays the cost of storing data.

You must authenticate all requests involving Requester Pays buckets. The request authentication enables Amazon S3 to identify and charge the requester for their use of the Requester Pays bucket. After you configure a bucket to be a Requester Pays bucket, requesters must include x-amz-request-payer in their requests either in the header, for POST, GET and HEAD requests, or as a parameter in a REST request to show that they understand that they will be charged for the request and the data download.
Hence, the correct answer is to enable the Requester Pays feature in all of the startup’s S3 buckets to make the media company pay the cost of the data transfer from the buckets.
The option that says: Advise the media company to create their own S3 bucket. Then run the aws s3 sync s3://sourcebucket s3://destinationbucket command to copy the objects from their S3 bucket to the other party’s S3 bucket. In this way, future retrievals can be made on the media company’s S3 bucket instead is incorrect because sharing all the assets of the startup to the media entails a lot of costs considering that you will be charged for the data transfer charges made during the sync process.
Creating a new billing account for the social media company by using AWS Organizations, then applying SCPs on the organization to ensure that each account has access only to its own resources and each other’s S3 buckets is incorrect because AWS Organizations does not create a separate billing account for every account under it. Instead, what AWS Organizations has is consolidated billing. You can use the consolidated billing feature in AWS Organizations to consolidate billing and payment for multiple AWS accounts. Every organization in AWS Organizations has a master account that pays the charges of all the member accounts.
The option that says: Provide cross-account access for the media company, which has permissions to access contents in the S3 bucket. Cross-account retrieval of S3 objects is charged to the account that made the request is incorrect because cross-account access does not shoulder the charges that are made during S3 object requests. Unless Requester Pays is enabled on the bucket, the bucket owner is still the one that is charged.

Reference:
https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

---

# Group E — Resilience / DR / performance (4)

<a id="q10"></a>

## Q10

A company hosts its online delivery system on a fleet of Amazon EC2 instances deployed in multiple Availability Zones in the ap-southeast-1 region. The instances are behind an Application Load Balancer that evenly distributes the load. The system is using a MySQL RDS instance to store the deliveries and transactions of the system. To ensure business continuity, the architect is instructed to set up a disaster recovery system in which the RTO must be less than 3 hours, and the RPO is 15 minutes when a system outage occurs. A pilot light environment was considered but would exceed the cost target, so a more economical approach is required. A system should also be implemented to automatically discover, classify, and protect any personally identifiable information (PII) or data store that contains one’s intellectual property. 




As the Solutions Architect, which disaster recovery strategy should be used to achieve the required RTO and RPO targets in the most cost-effective manner?

- **A.** Schedule a database backup to an Amazon S3 bucket every hour and store transaction logs to a separate S3 bucket every 5 minutes. Use Amazon Macie to automatically discover, classify, and protect your sensitive data.
- **B.** Schedule 15-minute DB backups to Amazon Glacier. Store the transaction logs to an Amazon S3 bucket every 5 minutes. Use Amazon Macie to automatically discover, classify, and protect your sensitive data.
- **C.** Schedule a database backup to AWS Storage Gateway every hour and store transaction logs to a separate Amazon S3 bucket every 5 minutes. Use AWS Shield to automatically discover, classify, and protect any personally identifiable information (PII) or intellectual property on your Storage Gateway.
- **D.** Set up asynchronous replication in the database using a Multi-AZ deployments configuration. Use AWS Shield to automatically discover, classify, and protect any personally identifiable information (PII) or intellectual property from your Amazon RDS database.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** RTO < 3h, RPO 15 min; cheaper than pilot light; discover PII

🪤 **Your trap:** 15-min backups to Glacier: retrieval time + restore risks RTO, and frequent Glacier writes aren't cheap

🧠 **Rule:** Backup & restore DR → hourly DB backups to S3 + transaction logs every 5 min (meets RPO). PII discovery → Macie (Shield = DDoS).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
EC2 (multi-AZ, sau ALB) ──► RDS MySQL (nguồn duy nhất)
Yêu cầu DR:
  RTO < 3h, RPO = 15 phút
  Pilot light: VƯỢT ngân sách → cần rẻ hơn
  + Tự động phát hiện/phân loại PII, IP (intellectual property)
```

Đây là bài toán **Backup and Restore** — chiến lược DR rẻ nhất trong 4 chiến lược (Backup & Restore → Pilot Light → Warm Standby → Multi-site Active/Active), vì scenario đã loại Pilot Light do chi phí. Đáp án đúng: **A** (backup DB lên S3 mỗi giờ + transaction log mỗi 5 phút + Macie). Anh chọn **B** (backup 15 phút lên Glacier).

#### Vì sao A đúng

- **Transaction log ghi vào S3 mỗi 5 phút** → khi restore, log gần nhất chỉ có thể mất tối đa ~15 phút dữ liệu → **đạt RPO 15 phút**.
- **Backup DB mỗi giờ lên S3** (không phải Glacier) → S3 cho phép tải xuống và restore ngay, không phải chờ retrieval → nằm trong **RTO < 3 giờ**.
- **Amazon Macie** là dịch vụ dùng machine learning để tự động discover/classify/protect **PII và intellectual property** trong dữ liệu — đúng chức năng scenario cần.

#### Vì sao B (Anh chọn) trông hợp lý nhưng sai

B trông hấp dẫn vì backup 15 phút khớp đúng số RPO ghi trong đề, và cũng dùng Macie đúng. Nhưng cái bẫy nằm ở **nơi lưu backup — Amazon Glacier**:

- Glacier **Standard Retrieval** mất khoảng **3–5 giờ** để lấy lại archive → riêng bước retrieval đã có thể vượt **RTO < 3 giờ**, chưa kể thời gian restore DB sau đó.
- Có thể dùng **Expedited Retrieval** (1–5 phút) để né vấn đề tốc độ, nhưng chi phí expedited retrieval cao hơn nhiều → không còn là **giải pháp cost-effective nhất** như đề yêu cầu.
- Ngoài ra, backup DB "mỗi 15 phút" lên Glacier tạo ra rất nhiều archive nhỏ, ghi Glacier thường xuyên cũng không rẻ như tưởng.

Nói cách khác: B tối ưu sai chỉ số — cố gắng khớp RPO bằng tần suất backup, nhưng lại phá RTO và chi phí vì chọn sai storage class.

#### Các lựa chọn sai khác

- **C — Storage Gateway + AWS Shield:** Storage Gateway là dịch vụ hybrid cloud storage (kết nối on-premises với AWS) — scenario không nói kiến trúc là hybrid. Đồng thời **AWS Shield chỉ chống DDoS**, không có khả năng discover/classify PII — sai chức năng hoàn toàn.
- **D — Multi-AZ async replication + AWS Shield:** Multi-AZ RDS dùng **đồng bộ (synchronous)** replication, không phải asynchronous (async là của Read Replica). Multi-AZ cũng chỉ bảo vệ khỏi lỗi AZ, không giúp gì khi mất cả Region — không đạt RTO/RPO cho DR thật sự. Và cũng dùng nhầm Shield thay vì Macie.

#### So sánh nhanh

| Lựa chọn | Nơi lưu backup | Retrieval | Dịch vụ PII |
|---|---|---|---|
| **A (đúng)** | S3, mỗi giờ + log 5 phút | Nhanh, tức thời | Macie ✓ |
| B (Anh chọn) | Glacier, mỗi 15 phút | 3–5h (standard) hoặc đắt (expedited) | Macie ✓ |
| C | Storage Gateway | Tùy hybrid setup | Shield ✗ |
| D | Multi-AZ (không phải backup) | Không giúp DR liên Region | Shield ✗ |

#### Quy tắc nhớ cho thi

- **"RPO ngắn nhưng RTO không cần cực nhanh, ngân sách hạn chế"** → chiến lược **Backup and Restore**: backup định kỳ lên **S3** (không phải Glacier) + transaction log tần suất cao để bù RPO.
- **"Glacier + cần restore nhanh"** → luôn kiểm tra retrieval time (Standard 3–5h, Expedited 1–5 phút nhưng đắt) trước khi chọn.
- **"Tự động discover/classify PII hoặc intellectual property"** → luôn là **Amazon Macie**, không phải Shield (Shield = DDoS) hay GuardDuty (threat detection).
- **Multi-AZ RDS = đồng bộ**, chỉ chống lỗi AZ; **Read Replica = bất đồng bộ**, có thể ở Region khác nhưng không tự động failover.

### TD explanation

Recovery time objective (RTO) is the time it takes after a disruption to restore a business process to its service level, as defined by the operational level agreement (OLA). For example, if a disaster occurs at 12:00 PM (noon) and the RTO is eight hours, the DR process should restore the business process to the acceptable service level by 8:00 PM.
Recovery point objective (RPO) is the acceptable amount of data loss measured in time. For example, if a disaster occurs at 12:00 PM (noon) and the RPO is one hour, the system should recover all data that was in the system before 11:00 AM. Data loss will span only one hour, between 11:00 AM and 12:00 PM (noon).
Amazon S3 is an ideal destination for backup data that might be needed quickly to perform a restore. Transferring data to and from Amazon S3 is typically done through the network and is therefore accessible from any location.

Amazon Macie is a security service that uses machine learning to automatically discover, classify, and protect sensitive data in AWS. Amazon Macie recognizes sensitive data such as personally identifiable information (PII) or intellectual property, and provides you with dashboards and alerts that give visibility into how this data is being accessed or moved. The fully managed service continuously monitors data access activity for anomalies and generates detailed alerts when it detects risk of unauthorized access or inadvertent data leaks.
Hence, the correct answer is: Schedule a database backup to an Amazon S3 bucket every hour and store transaction logs to a separate S3 bucket every 5 minutes. Use Amazon Macie to automatically discover, classify, and protect your sensitive data.
Using an S3 bucket makes data retrieval of the backups quicker. Since the transaction logs are stored in S3 every 5 minutes, this will help to restore the application to a state that is within the required RPO of 15 minutes.
The option that says: Schedule 15-minute DB backups to Amazon Glacier. Store the transaction logs to an Amazon S3 bucket every 5 minutes. Use Amazon Macie to automatically discover, classify, and protect your sensitive data is incorrect because retrieving the database backups from Amazon Glacier archives will normally take around 3 – 5 hours using the Standard Retrievals, and hence, this will not meet the RTO and RPO. Although you can use expedited retrievals, which can typically retrieve your archive within 1 – 5 minutes, this will entail additional cost and hence is not a cost-effective solution.
The option that says: Set up asynchronous replication in the database using a Multi-AZ deployments configuration. Use AWS Shield to automatically discover, classify, and protect any personally identifiable information (PII) or intellectual property from your Amazon RDS database is incorrect because asynchronous replication is only applicable for Read Replicas and not for a Multi-AZ deployment configuration. Although this will improve the availability of the RDS database, it won’t provide a better RTO or RPO, especially in the event of a regional outage since you can’t export a standby instance to another region. In addition, you have to use AWS Macie to protect your sensitive data in Amazon S3 and not AWS Shield.
The option that says: Schedule a database backup to AWS Storage Gateway every hour and store transaction logs to a separate Amazon S3 bucket every 5 minutes. Use AWS Shield to automatically discover, classify, and protect any personally identifiable information (PII) or intellectual property on your Storage Gateway is incorrect. AWS Storage Gateway is primarily used as a hybrid cloud storage service that connects your existing on-premises environments with the AWS Cloud. Although this can be a valid option, the scenario did not say that their architecture is hybrid or that they are using an on-premises data center. AWS Shield is primarily used to protect your resources from DDoS attacks, and not to automatically discover, classify, and protect any personally identifiable information (PII) or intellectual property.

References:
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html
https://docs.aws.amazon.com/macie/latest/user/data-classification.html

Check out this Amazon Macie Cheat Sheet:
https://tutorialsdojo.com/amazon-macie/

</details>

<a id="q14"></a>

## Q14

A company has a fitness tracking app that accompanies its smartwatch. The primary customers are North American and Asian users. The application is read-heavy as it pings the servers at regular intervals for user-authorization. The company wants the infrastructure to have the following capabilities:
– The application must be fault-tolerant to problems in any Region.
– The database writes must be highly-available in a single Region.
– The application tier must be able to read the database on multiple Regions.
– The application tier must be resilient in each Region.
– Relational database semantics must be reflected in the application.
Which of the following options must the Solutions Architect implement to meet the company requirements? (Select TWO.)

- **A.** Deploy the application tier on an Auto Scaling group of EC2 instances for each Region in an active-active configuration. Create a cluster of Amazon Aurora global database in both Regions. Configure the application to use the in-Region Aurora database endpoint for the read/write operations. Create snapshots of the application servers regularly. Store the snapshots in Amazon S3 buckets in both regions.
- **B.** Create a geoproximity routing policy on Amazon Route 53 to control traffic and direct users to their closest regional endpoint. Combine this with a multivalue answer routing policy with health checks to direct users to a healthy region at any given time.
- **C.** Deploy the application tier on an Auto Scaling group of EC2 instances for each Region. Create an RDS for MySQL database on each region. Configure the application to perform read/write operations on the local RDS. Enable cross-Region replication for the database servers. Create snapshots of the application and database servers regularly. Store the snapshots in Amazon S3 buckets in both regions.
- **D.** Deploy the application tier on an Auto Scaling group of EC2 instances for each Region. Create an RDS for MySQL database on each region. Configure the application to perform read/write operations on the local RDS. Enable Multi-AZ failover support for the EC2 Auto Scaling group and the RDS database. Enable cross-Region replication for the database servers.
- **E.** Create a geolocation routing policy on Amazon Route 53 to point the global users to their designated regions. Combine this with a failover answer routing policy with health checks to direct users to a healthy region at any given time.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, E · **You picked:** D, E

🔑 **Key words:** fault tolerant to Region failure; writes HA in one Region; reads multi-Region; relational (Select TWO)

🪤 **Your trap:** Cross-Region replication can't sync two RDS MySQL writers; Multi-AZ doesn't survive a Region failure

🧠 **Rule:** Multi-Region relational reads + single-Region writes → Aurora Global Database + Route 53 geolocation + failover records.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
North America users            Asia users
      │                             │
      ▼                             ▼
  Route 53 (?)  ──────────────────► chọn Region gần nhất, failover khi Region hỏng
      │
      ▼
Region A (App tier + DB)        Region B (App tier + DB)
Yêu cầu:
  - Fault-tolerant khi mất cả Region
  - Write HA nhưng CHỈ trong 1 Region
  - Read được ở NHIỀU Region
  - App tier resilient ở từng Region
  - Vẫn phải là relational DB (Select TWO)
```

Đây là bài multi-select: phải chọn **một đáp án cho tầng Route 53/routing** và **một đáp án cho tầng app + database**, hai đáp án đó ghép lại mới thành **một** giải pháp hoàn chỉnh. Đáp án đúng: **A** (app active-active + Aurora Global Database) + **E** (Route 53 geolocation + failover). Anh chọn đúng **E**, sai phần database (chọn **D** — RDS MySQL + cross-Region replication).

#### Vì sao A + E ghép thành một giải pháp

**A — tầng app & database:**
- **Aurora Global Database**: một cluster **primary** ở 1 Region nhận toàn bộ **write** (đạt "writes HA trong một Region duy nhất" vì Multi-AZ storage của Aurora tự nhân bản 6 bản trên 3 AZ), và tối đa 5 **secondary Region** đọc-chỉ (read-only) với replication lag dưới 1 giây — đạt "app tier đọc DB ở nhiều Region". Vẫn là **relational** (Aurora MySQL/PostgreSQL-compatible) — đúng yêu cầu "relational semantics".
- App tier chạy **Auto Scaling group ở mỗi Region, active-active** → mỗi Region tự phục vụ traffic của mình, "resilient in each Region".

**E — tầng routing:**
- **Geolocation routing policy**: đưa user Bắc Mỹ vào Region NA, user châu Á vào Region Asia — đúng theo vị trí user (khác **geoproximity**, cái đó định tuyến theo vị trí **resource**, không phải user).
- **Kết hợp Failover routing policy + health check**: nếu Region chính của user bị lỗi, Route 53 tự chuyển traffic sang Region còn lại — đạt "fault-tolerant to Region failure".

→ Ghép lại: user luôn được route đúng Region gần nhất (E), và nếu Region đó sập, cả app (A, active-active) và DB (A, Aurora Global có thể promote secondary lên primary dưới 1 phút) đều có phương án dự phòng.

#### Vì sao D (Anh chọn) trông hợp lý nhưng sai

D dùng **RDS for MySQL riêng ở mỗi Region + cross-Region replication + Multi-AZ**, nghe có vẻ "HA" và "cross-Region" đủ tiêu chuẩn. Nhưng:

- Yêu cầu "**app tier phải đọc được DB ở nhiều Region**" ngầm định là **mỗi Region cũng có DB riêng để ghi local** ("writes phải HA trong một Region" — số ít, chỉ 1 Region ghi). Nhưng D lại cho **mỗi Region tự ghi vào RDS MySQL riêng của mình** ("perform read/write operations on the local RDS") → tạo ra **hai database RDS MySQL độc lập cùng nhận write** ở hai Region → **không thể đồng bộ hai MySQL master cùng ghi** với nhau bằng cross-Region replication thông thường (không có conflict resolution).
- **Multi-AZ chỉ chống lỗi AZ**, hoàn toàn không giúp gì khi cả **Region** bị sập — không đạt "fault-tolerant to problems in any Region".

#### Các lựa chọn sai khác

- **B (Route 53 geoproximity + multivalue answer):** Geoproximity định tuyến theo vị trí **resource**, còn multivalue answer trả về ngẫu nhiên tối đa 8 record khỏe mạnh — có thể đưa user ở Asia sang Region NA dù NA còn khỏe → không tối ưu latency, cũng chưa chắc phù hợp UX người dùng.
- **C (2 RDS MySQL riêng, mỗi Region tự ghi/đọc local, cross-Region replication, không Multi-AZ):** cùng lỗi nền tảng như D — **không đồng bộ được hai MySQL master cùng ghi**, chỉ khác D ở việc không có Multi-AZ.

#### So sánh nhanh

| Lựa chọn | Database | Ghi ở? | Đồng bộ liên Region | Đúng? |
|---|---|---|---|---|
| **A** | Aurora Global Database | 1 Region primary | Có (built-in, <1s lag) | ✓ |
| C, D | RDS MySQL riêng mỗi Region | Mỗi Region tự ghi local | Cross-Region replication thường **không sync 2 master** | ✗ |

#### Quy tắc nhớ cho thi

- **"Write ở 1 Region, read nhiều Region, relational, fault-tolerant liên Region"** → luôn nghĩ đến **Aurora Global Database**, không phải RDS MySQL tự dựng cross-Region replication.
- **"2 RDS/MySQL riêng, mỗi bên tự ghi, rồi cross-Region replicate cho nhau"** → gần như luôn **sai** vì không sync được 2 master.
- **Multi-AZ ≠ Multi-Region**: Multi-AZ chỉ chống lỗi AZ, không chống lỗi Region.
- **Geolocation** = theo vị trí **user**; **Geoproximity** = theo vị trí **resource** (có thể lệch bias để dịch traffic).
- **Multivalue answer** = trả ngẫu nhiên nhiều IP khỏe, không kiểm soát được user đi Region nào → không hợp khi cần độ trễ thấp theo vùng địa lý cụ thể.

### TD explanation

Amazon Aurora Global Database is designed for globally distributed applications, allowing a single Amazon Aurora database to span multiple AWS regions. It replicates your data with no impact on database performance, enables fast local reads with low latency in each region, and provides disaster recovery from region-wide outages.
By using an Amazon Aurora global database, you can have a single Aurora database that spans multiple AWS Regions to support your globally distributed applications.
An Aurora global database consists of one primary AWS Region where your data is mastered, and up to five read-only secondary AWS Regions. You issue write operations directly to the primary DB cluster in the primary AWS Region. Aurora replicates data to the secondary AWS Regions using dedicated infrastructure, with latency typically under a second.
You can also change the configuration of your Aurora global database while it’s running to support various use cases. For example, you might want the read/write capabilities to move from one Region to another, say, in different time zones, to ‘follow the sun.’ Or, you might need to respond to an outage in one Region. With Aurora global database, you can promote one of the secondary Regions to the primary role to take full read/write workloads in under a minute.

On Amazon Route 53, after you create a hosted zone for your domain, such as tutorialsdojo.com, you can create records to tell the Domain Name System (DNS) how you want traffic to be routed for that domain. You can create a record that points to the DNS name of your Application Load Balancer on AWS.
When you create a record, you choose a routing policy, which determines how Amazon Route 53 responds to queries:
Simple routing policy – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.
Failover routing policy – Use when you want to configure active-passive failover.
Geolocation routing policy – Use when you want to route traffic based on the location of your users.
Geoproximity routing policy – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.
Latency routing policy – Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency.
Multivalue answer routing policy – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.
Weighted routing policy – Use to route traffic to multiple resources in proportions that you specify.
You can use Route 53 health checks to configure active-active and active-passive failover configurations. You configure active-active failover using any routing policy (or combination of routing policies) other than failover, and you configure active-passive failover using the failover routing policy.
The option that says: Create a geolocation routing policy on Amazon Route 53 to point the global users to their designated regions. Combine this with a failover answer routing policy with health checks to direct users to a healthy region at any given time is correct. You can use geolocation routing policy to direct the North American users to your servers on the North America region and configure failover routing to the Asia region in case the North America region fails. You can configure the same for the Asian users pointed to the Asia region servers and have the North America region as its backup.
The option that says: Deploy the application tier on an Auto Scaling group of EC2 instances for each Region in an active-active configuration. Create a cluster of Amazon Aurora global database in both Regions. Configure the application to use the in-Region Aurora database endpoint for the read/write operations. Create snapshots of the application servers regularly. Store the snapshots in Amazon S3 buckets in both regions is correct. The Amazon Aurora global database solves the problem on read/write as well as syncing the data across all the regions. With both regions in an active-active configuration, each region can accept the traffic from users around the world.
The option that says: Create a geoproximity routing policy on Amazon Route 53 to control traffic and direct users to their closest regional endpoint. Combine this with a multivalue answer routing policy with health checks to direct users to a healthy region at any given time is incorrect. Geoproximity routing policy is good to control the user traffic to specific regions. However, a multivalue answer routing policy may cause the users to be randomly sent to other healthy regions that may be far away from the user’s location.
The option that says: Deploy the application tier on an Auto Scaling group of EC2 instances for each Region. Create an RDS for MySQL database on each region. Configure the application to perform read/write operations on the local RDS. Enable cross-Region replication for the database servers. Create snapshots of the application and database servers regularly. Store the snapshots in Amazon S3 buckets in both regions is incorrect. You can’t sync two MySQL master databases that both accept writes on their respective regions.
The option that says: Deploy the application tier on an Auto Scaling group of EC2 instances for each Region. Create an RDS for MySQL database on each region. Configure the application to perform read/write operations on the local RDS. Enable Multi-AZ failover support for the EC2 Auto Scaling group and the RDS database. Enable cross-Region replication for the database servers is incorrect. You can’t sync two MySQL master databases that both accept writes on their respective regions. Enabling Multi-AZ on the RDS MySQL server does not protect you from AWS Regional failures.

References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html#aurora-global-database-overview
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-connecting.html

Check out these Amazon Aurora and Route 53 Cheat Sheets:
https://tutorialsdojo.com/amazon-aurora/
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q17"></a>

## Q17

An international foreign exchange company has a serverless forex trading application that was built using AWS SAM and is hosted on AWS Serverless Application Repository. They have millions of users worldwide who use their online portal 24/7 to trade currencies. However, they are receiving a lot of complaints that it takes a few minutes for their users to log in to their portal lately, including occasional HTTP 504 errors. As the Solutions Architect, you are tasked to optimize the system and to significantly reduce the time to log in to improve the customers’ satisfaction. 
Which of the following should you implement in order to improve the performance of the application with minimal cost? (Select TWO.)

- **A.** Set up multiple and geographically disperse VPCs to various AWS regions then create a transit VPC to connect all of your resources. Deploy the Lambda function in each region using AWS SAM, in order to handle the requests faster.
- **B.** Set up an origin failover by creating an origin group with two origins. Specify one as the primary origin and the other as the second origin which CloudFront automatically switches to when the primary origin returns specific HTTP status code failure responses.
- **C.** Increase the cache hit ratio of your CloudFront distribution by configuring your origin to add a Cache-Control max-age directive to your objects, and specify the longest practical value for max-age.
- **D.** Use Lambda@Edge to allow your Lambda functions to customize content that CloudFront delivers and to execute the authentication process in AWS locations closer to the users.
- **E.** Deploy your application to multiple AWS regions to accommodate your users around the world. Set up a Route 53 record with latency routing policy to route incoming traffic to the region that provides the best latency to the user.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D · **You picked:** D, E

🔑 **Key words:** SAM serverless app; slow logins + occasional 504; minimal cost (Select TWO)

🪤 **Your trap:** Deploying the app to multiple Regions is costly; max-age caching doesn't help dynamic login requests

🧠 **Rule:** Slow auth + 504 at CloudFront → Lambda@Edge for auth near users + origin failover (origin group).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users (toàn cầu) ──► CloudFront ──► Origin (serverless app trên AWS SAM)
                                       │
                                       ▼
                              đăng nhập chậm + HTTP 504 đôi lúc

Yêu cầu: cải thiện tốc độ login, MINIMAL COST (Select TWO)
```

Đáp án đúng: **B** (origin failover — origin group 2 origin) + **D** (Lambda@Edge chạy auth gần user). Anh chọn đúng **D**, sai ở phần còn lại (chọn **E** — deploy multi-Region + Route 53 latency routing).

#### Vì sao B + D ghép thành một giải pháp

**D — xử lý phần "chậm":**
- **Lambda@Edge** cho phép chạy Lambda tại các edge location của CloudFront (gần user hơn origin gốc), thực thi ngay ở 1 trong 4 điểm: viewer request, origin request, origin response, viewer response.
- Scenario nói **login chậm** → đưa **logic authentication chạy tại edge, gần user** giúp giảm round-trip time đáng kể mà **không cần deploy hạ tầng mới ở nhiều Region** (chi phí thấp hơn).

**B — xử lý phần "504 lỗi thoáng qua":**
- **Origin failover (origin group)**: CloudFront có 1 primary origin + 1 second origin; khi primary trả về mã lỗi cụ thể (như 5xx), CloudFront tự động chuyển sang origin thứ hai. Điều này trực tiếp giải quyết **"occasional HTTP 504 errors"** mà đề bài mô tả.

→ Ghép lại: Lambda@Edge giải quyết chậm khi login bình thường; origin failover giải quyết khi origin gốc gặp sự cố gây 504 — cả hai đều tận dụng hạ tầng CloudFront có sẵn, **không cần multi-Region deployment** → chi phí thấp.

#### Vì sao E (Anh chọn) trông hợp lý nhưng sai

E — deploy app ra nhiều Region + Route 53 latency routing — về mặt kỹ thuật **có thể** cải thiện hiệu năng (đưa app gần user hơn, route theo latency thấp nhất). Nhưng đề yêu cầu rõ **"minimal cost"**:

- Deploy toàn bộ ứng dụng serverless (SAM stack, Lambda, API Gateway, mọi resource liên quan) ra **nhiều AWS Region** kéo theo chi phí vận hành, đồng bộ dữ liệu, và quản lý nhân đôi ở mỗi Region — **chi phí cao hơn nhiều** so với chỉ thêm Lambda@Edge + origin failover trên CloudFront hiện có.
- Đây đúng là giải pháp "làm được" nhưng **không tối ưu chi phí** như đề bài đòi hỏi — TD luôn nhấn từ khóa cost khi loại phương án multi-Region.

#### Các lựa chọn sai khác

- **A (Transit VPC + Lambda multi-Region):** Cũng là một dạng multi-Region phức tạp — thêm chi phí hạ tầng VPC, Transit Gateway, và vẫn không giải quyết trực tiếp gốc rễ 504 lỗi origin.
- **C (Cache-Control max-age dài hơn):** Tăng cache hit ratio chỉ có ý nghĩa với **nội dung tĩnh (static)**. Vấn đề ở đây là **authentication — nội dung động, cá nhân hóa theo từng user** → không thể cache theo max-age. Không giải quyết đúng nguyên nhân (login chậm), không liên quan đến 504.

#### So sánh nhanh

| Lựa chọn | Giải quyết gì | Chi phí |
|---|---|---|
| **B (đúng)** | 504 lỗi từ origin | Thấp (chỉ config CloudFront) |
| **D (đúng)** | Login chậm (auth ở edge) | Thấp (Lambda@Edge) |
| E (Anh chọn) | Cả hai, gián tiếp | Cao (multi-Region toàn bộ app) |
| C | Không liên quan (cache tĩnh) | Thấp nhưng vô nghĩa ở đây |
| A | Cả hai, gián tiếp | Cao (Transit VPC + multi-Region) |

#### Quy tắc nhớ cho thi

- **"Login/auth chậm qua CloudFront"** → **Lambda@Edge**, không phải cache hay multi-Region.
- **"HTTP 5xx thoáng qua từ origin"** → **CloudFront origin failover (origin group)**.
- **"Minimal cost" xuất hiện trong đề** → luôn loại các phương án **deploy multi-Region toàn bộ ứng dụng**, dù về mặt kỹ thuật chúng có thể đúng.
- **Cache-Control / max-age** → chỉ hữu ích cho nội dung **tĩnh**, vô dụng với request đăng nhập động, cá nhân hóa từng user.

### TD explanation

Lambda@Edge lets you run Lambda functions to customize the content that CloudFront delivers, executing the functions in AWS locations closer to the viewer. The functions run in response to CloudFront events, without provisioning or managing servers. You can use Lambda functions to change CloudFront requests and responses at the following points:
– After CloudFront receives a request from a viewer (viewer request)
– Before CloudFront forwards the request to the origin (origin request)
– After CloudFront receives the response from the origin (origin response)
– Before CloudFront forwards the response to the viewer (viewer response)

In the given scenario, you can use Lambda@Edge to allow your Lambda functions to customize the content that CloudFront delivers and to execute the authentication process in AWS locations closer to the users. In addition, you can set up an origin failover by creating an origin group with two origins with one as the primary origin and the other as the second origin which CloudFront automatically switches to when the primary origin fails. This will alleviate the occasional HTTP 504 errors that users are experiencing.
The option that says: Deploy your application to multiple AWS regions to accommodate your users around the world. Set up a Route 53 record with latency routing policy to route incoming traffic to the region that provides the best latency to the user is incorrect. Although this may resolve the performance issue, this solution entails a significant implementation cost since you have to deploy your application to multiple AWS regions. Remember that the scenario asks for a solution that will improve the performance of the application with minimal cost.
The option that says: Increase the cache hit ratio of your CloudFront distribution by configuring your origin to add a Cache-Control max-age directive to your objects, and specify the longest practical value for max-age is incorrect because improving the cache hit ratio for the CloudFront distribution is irrelevant in this scenario. You can improve your cache performance by increasing the proportion of your viewer requests that are served from CloudFront edge caches instead of going to your origin servers for content. However, take note that the problem in the scenario is the sluggish authentication process of your global users and not just the caching of the static objects.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html
https://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html

Check out these Amazon CloudFront and AWS Lambda Cheat Sheets:
https://tutorialsdojo.com/amazon-cloudfront/
https://tutorialsdojo.com/aws-lambda/

</details>

<a id="q25"></a>

## Q25

A retail company hosts its web application on an Auto Scaling group of Amazon EC2 instances deployed across multiple Availability Zones. The Auto Scaling group is configured to maintain a minimum EC2 cluster size and automatically replace unhealthy instances. The EC2 instances are behind an Application Load Balancer so that the load can be spread evenly on all instances. The application target group health check is configured with a fixed HTTP page that queries a dummy item on the database. The web application connects to a Multi-AZ Amazon RDS MySQL instance. A recent outage caused a major loss to the company’s revenue. Upon investigation, it was found that the web server metrics are within the normal range but the database CPU usage is very high, causing the EC2 health checks to timeout. Failing the health checks, the Auto Scaling group continuously replaced the unhealthy instances thus causing the downtime.
Which of the following options should the Solution Architect implement to prevent this from happening again and allow the application to handle more traffic in the future? (Select TWO.)

- **A.** Reduce the load on the database tier by creating multiple read replicas for the Amazon RDS MySQL Multi-AZ cluster. Configure the web application to use the single reader endpoint of RDS for all read operations.
- **B.** Change the target group health check to use a TCP check on the EC2 instances instead of a page that queries the database. Create an Amazon Route 53 health check for the database dummy item web page to ensure that the application works as expected. Set up an Amazon CloudWatch alarm to send a notification to Admins when the health check fails.
- **C.** Change the target group health check to a simple HTML page instead of a page that queries the database. Create an Amazon Route 53 health check for the database dummy item web page to ensure that the application works as expected. Set up an Amazon CloudWatch alarm to send a notification to Admins when the health check fails.
- **D.** Reduce the load on the database tier by creating an Amazon ElastiCache cluster to cache frequently requested database queries. Configure the application to use this cache when querying the RDS MySQL instance.
- **E.** Create an Amazon CloudWatch alarm to monitor the Amazon RDS MySQL instance if it has a high-load or in impaired status. Set the alarm action to recover the RDS instance. This will automatically reboot the database to reset the queries.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C, D · **You picked:** A, B

🔑 **Key words:** DB CPU high → health check page queries DB → ASG replaces healthy instances (Select TWO)

🪤 **Your trap:** RDS MySQL has no single reader endpoint (that's Aurora); a TCP check doesn't validate the web app at all

🧠 **Rule:** Decouple ALB health check from DB (simple HTML page) + reduce DB load with ElastiCache.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
ALB ──► Target Group health check = trang HTML query dummy item trong DB
   │
   ▼
ASG (multi-AZ EC2) ──► RDS MySQL Multi-AZ
                          │
                    CPU RDS tăng cao (do traffic thật, không phải lỗi web server)
                          ▼
              health check timeout (do DB chậm trả lời)
                          ▼
         ASG hiểu lầm instance "unhealthy" → replace liên tục → outage

Yêu cầu: ngăn lặp lại + xử lý traffic lớn hơn trong tương lai (Select TWO)
```

Đáp án đúng: **C** (đổi health check target group sang trang HTML đơn giản + thêm Route 53 health check riêng cho trang query DB) + **D** (thêm ElastiCache để giảm tải DB). Anh chọn **A** và **B** — cả hai đều sai.

#### Vì sao C + D ghép thành một giải pháp

**C — tách health check khỏi DB:**
- Vấn đề gốc: health check của **target group ALB** đang gọi trang query DB → khi DB quá tải, health check timeout → ALB coi EC2 "unhealthy" dù **web server (EC2) hoàn toàn bình thường** (đề đã nói rõ "web server metrics are within the normal range"). ASG replace instance khỏe mạnh là sai lầm gốc gây outage.
- Sửa: đổi target group health check thành **trang HTML tĩnh đơn giản, không đụng DB** → EC2 chỉ bị coi unhealthy khi web server tự nó có vấn đề thật.
- Vẫn cần theo dõi tình trạng ứng dụng thật (kể cả tầng DB) → dùng **Route 53 health check riêng** trỏ vào trang có query DB, kết hợp **CloudWatch alarm** báo cho admin khi endpoint đó fail — tách biệt "giám sát" và "quyết định sống/chết của EC2 trong ASG".

**D — giảm tải DB để chịu traffic lớn hơn:**
- Đây là app **retail, đọc nhiều (read-heavy)** — thêm **ElastiCache** để cache các query lặp lại giúp giảm số lượng truy vấn thật xuống RDS, vừa giảm CPU DB hiện tại, vừa giúp hệ thống chịu được traffic tăng trong tương lai.

→ Ghép lại: C ngăn ASG "tự bắn vào chân mình" khi DB chậm; D giảm khả năng DB bị quá tải từ đầu — hai lớp bảo vệ bổ trợ nhau.

#### Vì sao A & B (Anh chọn) trông hợp lý nhưng sai

**A — read replica + reader endpoint:** Tạo read replica cho RDS MySQL là hướng đúng để tăng khả năng đọc, nhưng đây là **RDS MySQL** (không phải Aurora) — **RDS MySQL không có "single reader endpoint"** dùng chung cho nhiều read replica; đó là tính năng độc quyền của **Aurora**. Với RDS MySQL, mỗi read replica có endpoint riêng, ứng dụng phải tự chọn/định tuyến. Quan trọng hơn: A **không giải quyết nguyên nhân gốc** — health check vẫn gọi trực tiếp vào DB, ASG vẫn có thể replace nhầm instance khi CPU cao.

**B — TCP health check + Route 53 health check:** Trông giống C (cũng thêm Route 53 health check) nhưng khác ở health check target group — B đề xuất **TCP check**. Tuy nhiên: **Application Load Balancer chỉ hỗ trợ HTTP/HTTPS health check, không hỗ trợ TCP check** (TCP health check là của Network Load Balancer). Đây là sai kỹ thuật nền tảng khiến B bị loại ngay.

#### Các lựa chọn sai khác

- **E (CloudWatch alarm → RDS auto-recover/reboot):** Reboot RDS gây **downtime chủ động**. Nếu Multi-AZ, standby cũng sẽ nhận toàn bộ tải ngay khi failover và có thể sập theo — không giải quyết vấn đề tải cao, chỉ là "tắt rồi mở lại" tạm bợ.

#### So sánh nhanh

| Lựa chọn | Health check target group | Vấn đề |
|---|---|---|
| **C (đúng)** | HTML tĩnh, không đụng DB | ✓ |
| B (Anh chọn) | TCP check | ALB không hỗ trợ TCP health check ✗ |
| A (Anh chọn) | (không đổi health check) | RDS MySQL không có reader endpoint chung; không sửa gốc rễ ✗ |

#### Lưu ý thực tế

- **ALB health check chỉ support HTTP/HTTPS**; TCP/UDP health check thuộc về **Network Load Balancer (NLB)**. Đây là chi tiết dễ nhầm khi đề trộn ALB với NLB.
- Reader endpoint dùng chung nhiều read replica **chỉ có ở Aurora**, không có ở RDS MySQL/PostgreSQL thường.

#### Quy tắc nhớ cho thi

- **"Health check của ALB gọi vào DB → ASG replace nhầm instance khỏe"** → tách health check: **trang tĩnh cho target group**, **Route 53 health check riêng** để theo dõi thật + CloudWatch alarm báo admin.
- **"TCP health check trên ALB"** → luôn sai, ALB chỉ hỗ trợ HTTP/HTTPS.
- **"Giảm tải DB đọc-nhiều (read-heavy)"** → nghĩ ngay đến **ElastiCache** (cache tần suất cao) trước khi nghĩ đến việc chỉ thêm read replica.
- **"Single reader endpoint" chỉ có ở Aurora**, không có ở RDS MySQL/PostgreSQL classic.

### TD explanation

Amazon Route 53 health checks monitor the health and performance of your web applications, web servers, and other resources. Each health check that you create can monitor one of the following:
The health of a specified resource, such as a web server – You can configure a health check that monitors an endpoint that you specify either by IP address or by the domain name. At regular intervals that you specify, Route 53 submits automated requests over the Internet to your application. You can configure the health check to make requests similar to those that your users make, such as requesting a web page from a specific URL.
The status of other health checks – You can create a health check that monitors whether Route 53 considers other health checks healthy or unhealthy. One situation where this might be useful is when you have multiple resources that perform the same function, such as multiple web servers, and your chief concern is whether some minimum number of your resources are healthy.
The status of an Amazon CloudWatch alarm – You can create CloudWatch alarms that monitor the status of CloudWatch metrics, such as the number of throttled read events for an Amazon DynamoDB database or the number of Elastic Load Balancing hosts that are considered healthy.
After you create a health check, you can get the status of the health check, get notifications when the status changes, and configure DNS failover. To improve resiliency and availability, Route 53 doesn’t wait for the CloudWatch alarm to go into the ALARM state. The status of a health check changes from healthy to unhealthy based on the data stream and on the criteria in the CloudWatch alarm.

Your Application Load Balancer periodically sends requests to its registered targets to test their status. These tests are called health checks. Each load balancer node routes requests only to the healthy targets in the enabled Availability Zones for the load balancer. Each load balancer node checks the health of each target, using the health check settings for the target groups with which the target is registered. After your target is registered, it must pass one health check to be considered healthy. After each health check is completed, the load balancer node closes the connection that was established for the health check. If a target group contains only unhealthy registered targets, the load balancer nodes route requests across its unhealthy targets.
Each health check will be executed at configured intervals to all the EC2 instances so if the health check query page involves a database query, there will be several simultaneous queries to the database. This can increase the load of your database tier if there are many EC2 instances and the health check interval period is very quick.
Amazon ElastiCache is a web service that makes it easy to set up, manage, and scale a distributed in-memory data store or cache environment in the cloud. It provides a high-performance, scalable, and cost-effective caching solution. At the same time, it helps remove the complexity associated with deploying and managing a distributed cache environment.
ElastiCache for Memcached has multiple features to enhance reliability for critical production deployments:
– Automatic detection and recovery from cache node failures.
– Automatic discovery of nodes within a cluster enabled for automatic discovery so that no changes need to be made to your application when you add or remove nodes.
– Flexible Availability Zone placement of nodes and clusters.
– Integration with other AWS services such as Amazon EC2, Amazon CloudWatch, AWS CloudTrail, and Amazon SNS to provide a secure, high-performance, managed in-memory caching solution.
The option that says: Change the target group health check to a simple HTML page instead of a page that queries the database. Create an Amazon Route 53 health check for the database dummy item web page to ensure that the application works as expected. Set up an Amazon CloudWatch alarm to send a notification to Admins when the health check fails is correct. Changing the target group health check to a simple HTML page will reduce the queries to the database tier. The Route 53 health check can act as the “external” check on a specific page that queries the database to ensure that the application is working as expected. The Route 53 health check has an overall lower request count compared to using the target group health check.
The option that says: Reduce the load on the database tier by creating an Amazon ElastiCache cluster to cache frequently requested database queries. Configure the application to use this cache when querying the RDS MySQL instance is correct. Since this is a retail web application, most of the queries will be read-intensive as customers are searching for products. ElastiCache is effective at caching frequent requests, which overall improves the application response time and reduces database queries.
The option that says: Reduce the load on the database tier by creating multiple read replicas for the Amazon RDS MySQL Multi-AZ cluster. Configure the web application to use the single reader endpoint of RDS for all read operations is incorrect. This may be possible because creating read replicas is recommended to increase the read performance of an RDS cluster. However, this option does not resolve the original intention to reduce the number of repetitive queries hitting the database.
The option that says: Change the target group health check to use a TCP check on the EC2 instances instead of a page that queries the database. Create an Amazon Route 53 health check for the database dummy item web page to ensure that the application works as expected. Set up an Amazon CloudWatch alarm to send a notification to Admins when the health check fails is incorrect. An Application Load Balancer does not support a TCP health check. ALB only supports HTTP and HTTPS target health checks.
The option that says: Create an Amazon CloudWatch alarm to monitor the Amazon RDS MySQL instance if it has a high-load or in impaired status. Set the alarm action to recover the RDS instance. This will automatically reboot the database to reset the queries is incorrect. Recovering the database instance results in downtime. If you have the Multi-AZ enabled, the standby database will shoulder all the load causing it to crash too. It is better to scale the database by creating read replicas or adding an ElastiCache cluster in front of it.

References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html
https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/WhatIs.html

Check out these Amazon ElastiCache and Amazon RDS Cheat Sheets:
https://tutorialsdojo.com/amazon-elasticache/
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

---

# Group F — Serverless & app architecture (6)

<a id="q64"></a>

## Q64

A company has a hybrid setup for its mobile application. The on-premises data center hosts a 3TB MySQL database server that handles the write-intensive requests from the application. The on-premises network is connected to the AWS VPC with a VPN. On AWS, the serverless application runs on AWS Lambda and API Gateway with an Amazon DynamoDB table used for saving user preferences. The application scales well as more users use the mobile app. The user traffic is unpredictable, but there is an average increase of about 20% each month. A few months into operation, the company noticed the exponential increase in costs for Lambda. The Solutions Architect noticed that the Lambda execution time averages 4.5 minutes, and most of that is wait time due to latency when calling the on-premises data MySQL server.
Which of the following solutions should the Solutions Architect implement to reduce the overall cost?

- **A.** 1. Migrate the on-premises MySQL database server to Amazon RDS for MySQL. Enable Multi-AZ to ensure high availability.  2. Configure API caching on Amazon API Gateway to reduce the overall number of invocations to the Lambda functions.  3. Gradually lower the timeout and memory properties of the Lambda functions without increasing the execution time.  4. Configure AWS Application Auto Scaling on DynamoDB to automatically adjust the capacity based on user traffic
- **B.** 1. Provision an AWS Direct Connect connection from the on-premises data center to Amazon VPC instead of a VPN to significantly reduce the network latency to the MySQL server.  2. Create an Amazon CloudFront distribution with the API Gateway as the origin to cache the API responses and reduce the Lambda invocations.  3. Convert the Lambda functions to run them on Amazon EC2 Reserved Instances. Use Auto Scaling on peak time with a combination of Spot instances to further reduce costs.  4. Configure AWS Application Auto Scaling on DynamoDB to automatically adjust the capacity with user traffic.
- **C.** 1. Migrate the on-premises MySQL database server to Amazon RDS for MySQL. Enable Multi-AZ to ensure high availability.  2. Create an Amazon CloudFront distribution with the API Gateway as the origin to cache the API responses and reduce the Lambda invocations.  3. Gradually lower the timeout and memory properties of the Lambda functions without increasing the execution time.  4. Configure AWS Application Auto Scaling on DynamoDB to automatically adjust the capacity with user traffic and enable DynamoDB Accelerator to cache frequently accessed records.
- **D.** 1. Provision an AWS Direct Connect connection from the on-premises data center to Amazon VPC instead of a VPN to significantly reduce the network latency to the MySQL server.  2. Configure caching on the mobile application to reduce the overall Lambda function calls.  3. Gradually lower the timeout and memory properties of the Lambda functions without increasing the execution time.  4. Add an Amazon Elasticache cluster in front of DynamoDB to cache the frequently accessed records.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** 🔁 Lambda 4.5 min mostly waiting on on-prem MySQL; costs exploding; reduce overall cost

🪤 **Your trap:** 🔁 Same pick as the chapter drill: CloudFront in front of API Gateway + DAX add new paid services; API Gateway has built-in caching

🧠 **Rule:** Reduce Lambda invocations cheaply → API Gateway caching. Cut wait time → move DB to RDS, then right-size Lambda timeout/memory.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises DC ──VPN──► AWS VPC
┌──────────────┐            ┌──────────────────────────┐
│ MySQL 3TB     │◄──chờ 4.5 phút──│ Lambda (API Gateway)     │
│ write-intensive│           │ DynamoDB (user preferences)│
└──────────────┘            └──────────────────────────┘
Traffic tăng ~20%/tháng, không đều
Chi phí Lambda tăng vọt vì thời gian chờ MySQL chiếm hầu hết execution time
Yêu cầu: giảm CHI PHÍ TỔNG THỂ
```

Đáp án đúng: **A**. Anh chọn **C** — rất gần với A, chỉ khác đúng 1 điểm nhưng đó là điểm quyết định.

#### Vì sao A đúng

A xử lý đúng cả 3 nguồn chi phí trong đề:

1. **Di chuyển MySQL sang RDS for MySQL, Multi-AZ** → loại bỏ độ trễ VPN on-prem, đây là nguồn gốc của 4.5 phút execution time. Lambda tính tiền theo **duration × memory**, nên giảm wait time là giảm tiền trực tiếp và lớn nhất.
2. **API caching trên API Gateway** → giảm số lượt invoke Lambda cho các request lặp lại, mà không phải mua thêm dịch vụ nào — caching là tính năng có sẵn của API Gateway (TTL mặc định 300s, tối đa 3600s).
3. **Giảm dần timeout/memory của Lambda** (không tăng execution time) → tối ưu thêm chi phí theo GB-s mà không ảnh hưởng chức năng.
4. **Application Auto Scaling cho DynamoDB** → tự điều chỉnh capacity theo traffic thật, không trả tiền dư khi traffic thấp.

#### Vì sao C — lựa chọn của Anh — sai

C giống A ở 3/4 điểm, chỉ khác bước 2: **CloudFront đặt trước API Gateway để cache**, và bước 4 cộng thêm **DAX**.

**⚠️ Lỗi lặp lại:** đây đúng là cái trap Anh đã dính ở chapter drill — cứ thấy "cache" là phản xạ CloudFront, nhưng caching cho **API responses của API Gateway thì nên làm ngay trên API Gateway**, không cần thêm một dịch vụ CDN riêng. CloudFront là lớp cache/CDN đứng trước, phù hợp cho **static content phân phối toàn cầu**, không phải cách rẻ nhất để giảm invoke Lambda ở một API nội bộ. Thêm CloudFront = thêm một dịch vụ trả phí không cần thiết trong khi API Gateway đã có caching built-in.

Còn **DAX** (DynamoDB Accelerator) là cache in-memory cho độ trễ **microsecond**, dùng khi cần tốc độ đọc cực cao — rất đắt so với việc DynamoDB chỉ cần lưu user preferences đơn giản. Đề chỉ cần "giảm chi phí", không cần latency microsecond, nên DAX là over-engineering tốn tiền.

#### Các phương án sai khác

- **B — Direct Connect + CloudFront + EC2 Reserved/Spot:** Direct Connect cho một ứng dụng duy nhất không kinh tế (thường dùng khi có nhu cầu kết nối lớn, ổn định, nhiều ứng dụng). Chuyển Lambda sang EC2 Reserved Instances cũng ngược yêu cầu — traffic không đều, EC2 phải chạy 24/7 nên có thể đắt hơn Lambda khi traffic thấp.
- **D — Direct Connect + cache trên mobile app + ElastiCache trước DynamoDB:** cache ở phía client (mobile app) không kiểm soát được và không giảm tải cho backend một cách nhất quán; nên cache tại API Gateway. Thêm ElastiCache là thêm cluster phải trả tiền vận hành liên tục.

#### So sánh nhanh

| Việc cần làm | Cách đúng (A) | Cách sai hay bị chọn |
|---|---|---|
| Giảm wait time do MySQL | Migrate sang RDS | Direct Connect (đắt, không cần cho 1 app) |
| Giảm số lần invoke Lambda | API Gateway caching | CloudFront / cache ở mobile app |
| Giảm chi phí đọc DynamoDB | Application Auto Scaling | DAX / ElastiCache (đắt hơn nhiều) |

#### Quy tắc nhớ cho thi

- **"Cache response của API Gateway"** → dùng **caching built-in của API Gateway**, không phải CloudFront.
- **"DAX / ElastiCache"** → chỉ chọn khi đề cần **latency microsecond** hoặc đọc cực nhiều lần trên cùng dữ liệu; nếu đề chỉ nói "giảm cost" thì đây thường là bẫy tốn tiền.
- **"Direct Connect cho một ứng dụng"** → hầu như luôn sai vì không kinh tế; Direct Connect hợp lý khi có nhu cầu băng thông lớn, nhiều ứng dụng, lâu dài.
- **"Lambda tốn tiền do wait time gọi DB on-prem"** → giải pháp gốc là đưa DB vào AWS (RDS), không phải đổi kết nối mạng.

### TD explanation

Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale. API developers can create APIs that access AWS or other web services, as well as data stored in the AWS Cloud. As an API Gateway API developer, you can create APIs for use in your own client applications.
You can enable API caching in Amazon API Gateway to cache your endpoint’s responses. With caching, you can reduce the number of calls made to your endpoint and also improve the latency of requests to your API.
When you enable caching for a stage, API Gateway caches responses from your endpoint for a specified time-to-live (TTL) period, in seconds. API Gateway then responds to the request by looking up the endpoint response from the cache instead of making a request to your endpoint. The default TTL value for API caching is 300 seconds. The maximum TTL value is 3600 seconds. TTL=0 means caching is disabled.
With AWS Lambda, you pay only for what you use. You are charged based on the number of requests for your functions and the duration, the time it takes for your code to execute. Lambda counts a request each time it starts executing in response to an event notification or invoke call, including test invokes from the console.
Duration is calculated from the time your code begins executing until it returns or otherwise terminates, rounded up to the nearest 1ms*. The price depends on the amount of memory you allocate to your function.
Auto Scaling for DynamoDB helps automate capacity management for your tables and global secondary indexes. You simply specify the desired target utilization and provide upper and lower bounds for read and write capacity. DynamoDB will then monitor throughput consumption using Amazon CloudWatch alarms and then will adjust provisioned capacity up or down as needed.
Amazon DynamoDB auto scaling uses the AWS Application Auto Scaling service to dynamically adjust provisioned throughput capacity on your behalf, in response to actual traffic patterns. This enables a table or a global secondary index to increase its provisioned read and write capacity to handle sudden increases in traffic, without throttling. When the workload decreases, Application Auto Scaling decreases the throughput so that you don’t pay for unused provisioned capacity.

Migrating the on-premises MySQL server to Amazon RDS provides the best latency for the Lambda functions which will significantly reduce the cost for execution time. API Gateway can cache the API request to reduce the Lambda invocation which can reduce the cost further. Auto Scaling for DynamoDB also reduces the cost by provisioning capacity depending on the current user traffic.

Hence, the correct answer is:
– Migrate the on-premises MySQL database server to Amazon RDS for MySQL. Enable Multi-AZ to ensure high availability.
– Configure API caching on Amazon API Gateway to reduce the overall number of invocations to the Lambda functions.
– Gradually lower the timeout and memory properties of the Lambda functions without increasing the execution time.
– Configure AWS Application Auto Scaling on DynamoDB to automatically adjust the capacity based on user traffic.
The following option is incorrect:
– Provision an AWS Direct Connect connection from the on-premises data center to Amazon VPC instead of a VPN to significantly reduce the network latency to the MySQL server.
– Configure caching on the mobile application to reduce the overall Lambda function calls.
– Gradually lower the timeout and memory properties of the Lambda functions without increasing the execution time.
– Add an Amazon Elasticache cluster in front of DynamoDB to cache the frequently accessed records.
Although the Direct Connect connection can reduce the network latency compared to a VPN connection, provisioning a Direct Connection just for a single application is not economical. Having the MySQL server hosted in AWS offers even better network latency. Provisioning an Elasticache cluster also increases the cost. Caching the API requests should be done on the API Gateway, not on the mobile app itself.
The following option is incorrect:
– Provision an AWS Direct Connect connection from the on-premises data center to Amazon VPC instead of a VPN to significantly reduce the network latency to the MySQL server.
– Create an Amazon CloudFront distribution with the API Gateway as the origin to cache the API responses and reduce the Lambda invocations.
– Convert the Lambda functions to run them on Amazon EC2 Reserved Instances. Use Auto Scaling on peak time with a combination of Spot instances to further reduce costs.
– Configure AWS Application Auto Scaling on DynamoDB to automatically adjust the capacity with user traffic.
Provisioning a Direct Connection just for the application is not economical even if it offers better latency than a VPN connection. Caching the API requests should be done on the API Gateway, and not on CloudFront. EC2 Reserve instances could be more expensive than Lambda functions when application traffic is low.
The following option is incorrect:
– Migrate the on-premises MySQL database server to Amazon RDS for MySQL. Enable Multi-AZ to ensure high availability.
– Create an Amazon CloudFront distribution with the API Gateway as the origin to cache the API responses and reduce the Lambda invocations.
– Gradually lower the timeout and memory properties of the Lambda functions without increasing the execution time.
– Configure AWS Application Auto Scaling on DynamoDB to automatically adjust the capacity with user traffic and enable DynamoDB Accelerator to cache frequently accessed records.
Caching the API requests should be done on the API Gateway, and not on CloudFront. DynamoDB Accelerator is typically used for caching requests if you need response times in microseconds. This is very expensive.

References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html
https://aws.amazon.com/api-gateway/faqs/
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html
https://aws.amazon.com/lambda/pricing/

Check out these Amazon API Gateway, Amazon DynamoDB, and AWS Lambda Cheat Sheets:
https://tutorialsdojo.com/amazon-api-gateway/
https://tutorialsdojo.com/amazon-dynamodb/
https://tutorialsdojo.com/aws-lambda/

</details>

<a id="q21"></a>

## Q21

A startup in the fashion industry is building a mobile app that showcases its latest fashion accessories and gadgets. The marketing manager hired a famous model with millions of Instagram followers to promote their new products and hence, it is expected that the app will be a huge hit once it is launched in the market. It must have the ability to automatically scale to handle millions of views of its static contents and to allow users to store their own photos of themselves wearing fashionable accessories with a maximum of 100 characters for captions. 
In this scenario, which of the following solutions would fulfill this requirement?

- **A.** 1. Set up a SAML 2.0-based Federation that lets the users sign into the app using a third-party identity provider such as Amazon, Google, or Facebook. 2. Set up an RDS database and an S3 bucket to store the photos. 3. Use the AssumeRoleWithWebIdentity API call to assume the IAM role containing the proper permissions to communicate with the RDS database. 4. Distribute the static contents using S3 to improve scalability.
- **B.** 1. Use Cognito to handle user authentication and management. 2. Use an RDS database to store user data. 3. Create an S3 bucket to store all of the user photos and other static files. 4. Distribute the static contents using CloudFront to improve scalability.
- **C.** 1. Use Cognito to handle user authentication and management. 2. Launch a DynamoDB table to store user data. 3. Create an S3 bucket to store all of the user photos and other static files. 4. Distribute the static contents using CloudFront to improve scalability.
- **D.** 1. Configure an on-premises Active Directory (AD) server utilizing SAML 2.0 to manage the application users inside of the on-premises AD server. 2. Develop a custom code that authenticates against the LDAP server. 3. Use DynamoDB as the main database of the app and S3 as the scalable object storage. 4. Grant an IAM role assigned to the STS token to allow the end-user to access the required data in the DynamoDB table. 5. Distribute the static contents using CloudFront to improve scalability.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** millions of views of static content; users store photos + 100-char captions; auto scale

🪤 **Your trap:** SAML 2.0 is not how social IdPs (Google/Facebook) sign in; RDS scales worse than DynamoDB for simple items

🧠 **Rule:** Mobile app + social login + massive scale → Cognito + DynamoDB + S3 + CloudFront.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Mobile app fashion, dự kiến viral (KOL triệu follower)
┌─────────────────────────────────────────────┐
│ Static content (ảnh sản phẩm)  → auto-scale, triệu views │
│ User đăng ảnh + caption ≤100 ký tự           │
└─────────────────────────────────────────────┘
Yêu cầu: tự scale khối lượng lớn, đơn giản, rẻ
```

Đáp án đúng: **C** (Cognito + DynamoDB + S3 + CloudFront). Anh chọn **A** (SAML 2.0 Federation + RDS + S3 + S3-distribute).

#### Vì sao C đúng

- **Cognito** xử lý authentication/management, hỗ trợ sẵn **social identity provider** (Facebook, Google, Amazon) — đúng kiểu app tiêu dùng đại chúng.
- **DynamoDB** lưu user data (chỉ là caption ngắn ≤100 ký tự, không cần quan hệ bảng) → NoSQL scale ngang tốt hơn, không cần thiết kế schema quan hệ.
- **S3** lưu ảnh người dùng và static file.
- **CloudFront** phân phối static content tới lượng người dùng khổng lồ trên toàn cầu, giảm tải và tăng tốc so với việc client gọi trực tiếp S3.

Cả 4 dịch vụ đều scale gần như vô hạn, đúng yêu cầu "auto scale hàng triệu views" và "ứng dụng sẽ hit lớn".

#### Vì sao A — lựa chọn của Anh — sai

A dùng **SAML 2.0-based Federation** để "users sign into the app using a third-party identity provider such as Amazon, Google, or Facebook" — đây là điểm sai gốc: **SAML 2.0 không phải là cách các social IdP (Google, Facebook, Amazon) đăng nhập.** SAML 2.0 dùng cho **enterprise identity federation** (ví dụ liên kết với Active Directory/ADFS của doanh nghiệp). Các social IdP dùng chuẩn **OAuth 2.0 / OIDC**, được implement qua **Web Identity Federation** (`AssumeRoleWithWebIdentity`) hoặc đơn giản hơn — Cognito (Cognito tự động lo việc này ở phía sau).

A còn dùng **RDS** để lưu user data — với dữ liệu đơn giản kiểu caption/profile, RDS (quan hệ) không scale tốt bằng DynamoDB khi traffic tăng đột biến, và cần quản lý nhiều hơn (Multi-AZ, read replica, connection pool...).

A cũng "distribute static contents using **S3**" thay vì CloudFront — S3 phục vụ trực tiếp không có CDN cache biên (edge cache) toàn cầu, sẽ chậm hơn và tốn băng thông hơn khi có triệu người dùng cùng lúc so với CloudFront.

#### Các phương án sai khác

- **B:** Đúng Cognito + S3 + CloudFront nhưng vẫn dùng **RDS** cho user data — sai vì lý do tương tự A: dữ liệu đơn giản, cần scale lớn thì DynamoDB phù hợp hơn RDS.
- **D:** Dùng **on-premises AD server + SAML 2.0 + custom LDAP code** — hoàn toàn không hợp lý cho một **public mobile app** dành cho người dùng đại chúng (không phải nhân viên doanh nghiệp). Đây là kiến trúc dành cho enterprise SSO, không dành cho app tiêu dùng cần đăng nhập bằng Facebook/Google.

#### So sánh nhanh

| Thành phần | C (đúng) | A (Anh chọn) | Vấn đề của A |
|---|---|---|---|
| Auth | Cognito (hỗ trợ social IdP built-in) | SAML 2.0 Federation | SAML không dùng cho social login |
| Database | DynamoDB | RDS | RDS scale kém hơn với dữ liệu đơn giản |
| Phân phối static | CloudFront | S3 trực tiếp | Thiếu edge caching toàn cầu |

#### Quy tắc nhớ cho thi

- **"Đăng nhập bằng Google/Facebook/Amazon"** → đó là **Web Identity Federation / OIDC**, KHÔNG phải SAML 2.0.
- **"SAML 2.0"** → chỉ dùng khi đề nói **enterprise IdP** (Active Directory, ADFS, Okta liên kết doanh nghiệp).
- **"Mobile/web app quy mô lớn + social login"** → phản xạ **Cognito + DynamoDB + S3 + CloudFront**.
- **"Dữ liệu đơn giản, không cần join bảng, cần scale lớn"** → chọn DynamoDB thay RDS.

### TD explanation

Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0. Amazon S3 provides a scalable object storage solution. Amazon CloudFront is a Content  Delivery Network that helps your system to handle the millions of user views and finally, DynamoDB is a scalable database that can handle millions of records.

In this scenario, the top priority is scalability to meet the upcoming surge of users of your mobile app. Since all of these services can provide the scalability that your mobile app needs, the best option that you can choose is the following:
1. Use Cognito to handle user authentication and management.
2. Launch a DynamoDB table to store user data.
3. Create an S3 bucket to store all of the user photos and other static files.
4. Distribute the static contents using CloudFront to improve scalability.
The following option is incorrect because a SAML 2.0-based federation doesn’t use social media logins and it is better to use CloudFront to distribute static contents compared to an S3 bucket:
1. Set up a SAML 2.0-based Federation that lets the users sign into the app using a third party identity provider such as Amazon, Google or Facebook.
2. Set up an RDS database and an S3 bucket to store the photos.
3. Use the AssumeRoleWithWebIdentity API call to assume the IAM role containing the proper permissions to communicate with the RDS database.
4. Distribute the static contents using S3 to improve scalability.
The following option is incorrect because using an on-premise Active Directory server is not a suitable solution for this scenario:
1. Configure an on-premises Active Directory (AD) server utilizing SAML 2.0 to manage the application users inside of the on-premises AD server.
2. Develop a custom code that authenticates against the LDAP server.
3. Use DynamoDB as the main database of the app and S3 as the scalable object storage.
4. Grant an IAM role assigned to the STS token to allow the end-user to access the required data in the DynamoDB table.
5. Distribute the static contents using CloudFront to improve scalability.
Remember that this is a public mobile app and hence, it is better to set up a Web Identity Federation instead
The following option is incorrect because RDS is not as scalable as DynamoDB:
1. Use Cognito to handle user authentication and management.
2. Use an RDS database to store user data.
3. Create an S3 bucket to store all of the user photos and other static files.
4. Distribute the static contents using CloudFront to improve scalability.
Based on the type of data you will be storing, a relational database like RDS is not suitable to store simple data sets such as a 100-character caption which does not need multiple tables or relational data models.

References:
https://aws.amazon.com/cognito/
https://aws.amazon.com/blogs/security/protect-public-clients-for-amazon-cognito-by-using-an-amazon-cloudfront-proxy/
https://aws.amazon.com/blogs/mobile/building-fine-grained-authorization-using-amazon-cognito-user-pools-groups/

Check out these Amazon Cognito and Amazon S3 Cheat Sheets:
https://tutorialsdojo.com/amazon-cognito/
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q65"></a>

## Q65

A startup is building a web app that lets users post photos of good deeds in their neighborhood with a 143-character caption/article. The developers decided to write the application in ReactJS, a popular javascript framework so that it would run on the broadest range of browsers, mobile phones, and tablets. The app should provide access to Amazon DynamoDB to store the caption. The initial prototype shows that there aren’t large spikes in usage. 
Which option provides the most cost-effective and scalable architecture for this application?

- **A.** Configure the ReactJS client with temporary credentials from the Security Token Service using a Token Vending Machine (TVM) to provide signed credentials to an IAM user. This will allow GET and PUT operations to DynamoDB. Serve your web application from an NGINX server hosted in a fleet of EC2 instances that are load-balanced and auto-scaled. Your EC2 instances are configured with an IAM role that allows GET and PUT operations in DynamoDB.
- **B.** Register the web application with a Web Identity Provider such as Google, Facebook, Amazon, or any other popular social site. Create an IAM role for that web provider and set up permissions for the IAM role to allow GET and PUT operations in DynamoDB. Serve your web application from an NGINX server hosted on a fleet of EC2 instances, with a load balancer and auto-scaling. Add an IAM role to the EC2 instance to allow GET and PUT operations to DynamoDB tables.
- **C.** Configure the ReactJS client with temporary credentials from the Security Token Service using a Token Vending Machine (TVM) on an EC2 instance. This will provide signed credentials to an IAM user allowing GET and PUT operations in the DynamoDB table and the S3 bucket. You serve your mobile application out of an S3 bucket enabled as a website.
- **D.** Register the web application with a Web Identity Provider such as Google, Facebook, Amazon, or from any other popular social sites and use the AssumeRoleWithWebIdentity API of STS to generate temporary credentials. Create an IAM role for that web provider and set up permissions for the IAM role to allow GET and PUT operations in Amazon S3 and DynamoDB. Serve your web app out of an S3 bucket enabled as a website.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** B

🔑 **Key words:** ReactJS SPA; store caption in DynamoDB; no big spikes; most cost-effective + scalable

🪤 **Your trap:** NGINX on EC2 + ALB + ASG costs more than static hosting; no STS temporary creds

🧠 **Rule:** SPA + DynamoDB → S3 static website + web identity federation (AssumeRoleWithWebIdentity) → IAM role scoped to DynamoDB/S3.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Web app ReactJS (SPA) — chỉ là static files, browser render dynamic
┌──────────────────────────────────┐
│ User post ảnh + caption 143 ký tự │
│ Lưu caption vào DynamoDB           │
│ Traffic KHÔNG có spike lớn         │
└──────────────────────────────────┘
Yêu cầu: kiến trúc RẺ NHẤT + vẫn scalable
```

Đáp án đúng: **D** (Web Identity Provider + AssumeRoleWithWebIdentity + S3 static website). Anh chọn **B** (Web IdP + NGINX trên EC2 fleet + ALB + ASG).

#### Vì sao D đúng

Điểm mấu chốt: **ReactJS chỉ là một tập file static** (HTML/CSS/JS) — trình duyệt tự render "dynamic" ở client-side, còn phía server thực chất chỉ cần **phục vụ file tĩnh**. Vì vậy:

- **S3 static website hosting** là đủ để serve toàn bộ app — không cần server nào chạy 24/7, không cần load balancer, không cần auto-scaling group. Đây chính là lựa chọn rẻ nhất khi traffic không có spike lớn.
- **Web Identity Provider (Google/Facebook/Amazon) + `AssumeRoleWithWebIdentity`** để client lấy **temporary credentials từ STS** trực tiếp, rồi IAM role được cấp quyền GET/PUT vào S3 và DynamoDB — không cần máy chủ trung gian nào để phát hành credentials.

#### Vì sao B — lựa chọn của Anh — sai

B cũng dùng đúng Web Identity Provider để auth, nhưng lại **serve web app từ NGINX trên một fleet EC2 có load balancer + auto-scaling**. Đây là kiến trúc **highly available và scalable thật**, nhưng:

- Vì ReactJS app chỉ là file static, việc chạy nguyên một fleet EC2 (dù có ASG) để chỉ phục vụ file HTML/JS/CSS là **tốn kém không cần thiết** — phải trả tiền EC2 instance liên tục, ALB, và công vận hành (patch OS, quản lý AMI...).
- Đề nói rõ **"most cost-effective"**, và traffic **không có spike lớn** → không cần độ đàn hồi của EC2 ASG, S3 static hosting đã đủ scale và rẻ hơn nhiều.

#### Các phương án sai khác

- **A:** Dùng **Token Vending Machine (TVM) trên EC2 fleet + NGINX + ALB + ASG** để cấp credentials cho IAM **user** (không phải role). Vừa đắt (EC2 fleet) vừa dùng mô hình cũ (long-lived IAM user credentials thay vì role tạm thời qua STS).
- **C:** TVM chạy trên **một EC2 instance duy nhất** → **single point of failure**, không HA, không scale — nếu instance đó chết hoặc quá tải là sập toàn hệ thống. Ngoài ra vẫn cấp credentials cho IAM user, kém an toàn hơn AssumeRoleWithWebIdentity.

#### So sánh nhanh

| Phương án | Cách phát credentials | Nơi host app | Vấn đề |
|---|---|---|---|
| **D (đúng)** | AssumeRoleWithWebIdentity (STS, role) | S3 static website | Không có — rẻ nhất, scale tốt |
| B (Anh chọn) | Web IdP + IAM role cho EC2 | NGINX trên EC2 ASG + ALB | Tốn kém khi không cần scale lớn |
| A | TVM trên EC2 fleet, IAM user | NGINX trên EC2 ASG + ALB | Đắt, dùng IAM user (không nên) |
| C | TVM trên 1 EC2 | S3 static website | TVM là SPOF, không scale |

#### Lưu ý thực tế

- **Token Vending Machine (TVM)** là một pattern cũ trước khi Cognito/Web Identity Federation phổ biến — tự dựng server để cấp temporary credentials. Nếu chạy trên EC2, cần ít nhất phải HA (nhiều instance + LB); chạy trên 1 instance luôn là điểm yếu trong đề thi.
- IAM **role** (qua STS) luôn được ưu tiên hơn IAM **user** với access key vì credentials chỉ tồn tại tạm thời, tự động xoay.

#### Quy tắc nhớ cho thi

- **"ReactJS / Angular / Vue app + không cần server backend riêng"** → **S3 static website hosting** là lựa chọn rẻ nhất.
- **"Social login (Google/Facebook/Amazon) cho web/mobile"** → **Web Identity Federation + AssumeRoleWithWebIdentity**, cấp **IAM role**, không phải IAM user.
- **"Chạy trên 1 EC2 instance"** trong bất kỳ đáp án nào → luôn là dấu hiệu SPOF, gần như chắc chắn sai khi đề hỏi về scalable/durable.
- **"Most cost-effective + traffic không spike"** → tránh đáp án có EC2 fleet + ALB + ASG nếu có lựa chọn serverless/static rẻ hơn.

### TD explanation

ReactJS is a modern framework for creating front-ends for your web applications. From the users perspective, this website is dynamic since it asks for users to login and users can upload images to it. But since it is written on ReactJS framework, it is basically just a bunch of static files and the web browser renders the page dynamically.
We can have full-blown web pages like this and be hosted on Amazon S3 (with enabling static website hosting) with no problems. From Amazon S3’s perspective, it is hosting a static website, since all files that are on the bucket are static files only. But ReactJS allows the client’s web browser to interpret these static files and render the webpage dynamically for the user.
Amazon Cognito follows the OIDC specification to authenticate users of web and mobile apps. Users can sign in directly through the Amazon Cognito hosted UI or through a federated identity provider, such as Amazon, Facebook, Apple, or Google. The hosted UI workflows include sign-in and sign-up, password reset, and MFA. Since not all customer workflows are the same, you can customize Amazon Cognito workflows at key points with AWS Lambda functions, allowing you to run code without provisioning or managing servers. After a user authenticates, Amazon Cognito returns standard OIDC tokens. You can use the user profile information in the ID token to grant your users access to your own resources or you can use the tokens to grant access to APIs hosted by Amazon API Gateway. You can also exchange the tokens for temporary AWS credentials to access other AWS services.

If you don’t use Amazon Cognito, then you choose to write a custom code or app that interacts with a web IdP (Login with Amazon, Facebook, Google, or any other OIDC-compatible IdP) and then call the AssumeRoleWithWebIdentity API to trade the authentication token you get from those IdPs for AWS temporary security credentials. If you have already used this approach for existing apps, you can continue to use it. You can also deploy your app in the S3 bucket.
The option that says: Register the web application with a Web Identity Provider such as Google, Facebook, Amazon, or any other popular social sites and use the AssumeRoleWithWebIdentity API of STS to generate temporary credentials. Create an IAM role for that web provider and set up permissions for the IAM role to allow GET and PUT operations in Amazon S3 and DynamoDB. Serve your web app out of an S3 bucket enabled as a website is correct because it authenticates the application via a federated identity provider such as Google, Facebook, Amazon, or other social sites. It sets up proper permission for DynamoDB access and hosts the website in S3. Plus, it also uses STS and AssumeRoleWithWebIdentity API which provides a better authentication.
The option that says: Configure the ReactJS client with temporary credentials from the Security Token Service using a Token Vending Machine (TVM) on an EC2 instance. This will provide signed credentials to an IAM user allowing GET and PUT operations in the DynamoDB table and the S3 bucket. You serve your mobile application out of an S3 bucket enabled as a website is incorrect. The Token Vending Machine (STS Service) is implemented on just a single EC2 instance. This poses a single point of failure which means that the architecture is not highly available and not fault-tolerant. This is not a scalable solution either as the instance can become the performance bottleneck.
The option that says: Configure the ReactJS client with temporary credentials from the Security Token Service using a Token Vending Machine (TVM) to provide signed credentials to an IAM user. This will allow GET and PUT operations to DynamoDB. Serve your web application from an NGINX server hosted in a fleet of EC2 instances that are load-balanced and auto-scaled. Your EC2 instances are configured with an IAM role that allows GET and PUT operations in DynamoDB is incorrect. Although this solution is highly-available and scalable, deploying EC2 instances in an auto-scaled environment is not as a cost-effective solution as the S3 website.
The option that says: Register the web application with a Web Identity Provider such as Google, Facebook, Amazon, or from any other popular social site. Create an IAM role for that web provider and set up permissions for the IAM role to allow GET and PUT operations in DynamoDB. Serve your web application from an NGINX server hosted on a fleet of EC2 instances, with a load balancer and auto-scaling. Add an IAM role to the EC2 instance to allow GET and PUT operations to DynamoDB tables is incorrect because it does not mention any security token service that generates temporary credentials. Furthermore, deploying EC2 instances in an auto-scaled environment, albeit scalable, is not as cost-effective as the S3 website.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html
https://aws.amazon.com/blogs/security/how-to-add-authentication-single-page-web-application-with-amazon-cognito-oauth2-implementation/
https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-integrate-apps.html
https://aws.amazon.com/blogs/mobile/deploy-a-react-app-to-s3-and-cloudfront-with-aws-mobile-hub/

Check out these Amazon S3 and Amazon Cognito Cheat Sheets:
https://tutorialsdojo.com/amazon-s3/
https://tutorialsdojo.com/amazon-cognito/

</details>

<a id="q72"></a>

## Q72

A data analytics startup has been chosen to develop a data analytics system that will track all statistics in the Fédération Internationale de Football Association (FIFA) World Cup, which will also be used by other 3rd-party analytics sites. The system will record, store and provide statistical data reports about the top scorers, goal scores for each team, average goals, average passes, average yellow/red cards per match, and many other details. FIFA fans all over the world will frequently access the statistics reports every day and thus, it should be durably stored, highly available, and highly scalable. In addition, the data analytics system will allow the users to vote for the best male and female FIFA player as well as the best male and female coach. Due to the popularity of the FIFA World Cup event, it is projected that there will be over 10 million queries on game day and could spike to 30 million queries over the course of time. 
Which of the following is the most cost-effective solution that will meet these requirements?

- **A.** 1. Launch a MySQL database in Multi-AZ RDS deployments configuration with Read Replicas. 2. Generate the FIFA reports by querying the Read Replica. 3. Configure a daily job that performs a daily table cleanup.
- **B.** 1. Launch a MySQL database in Multi-AZ RDS deployments configuration. 2. Configure the application to generate reports from ElastiCache to improve the read performance of the system. 3. Utilize the default expire parameter for items in ElastiCache.
- **C.** 1. Generate the FIFA reports from MySQL database in Multi-AZ RDS deployments configuration with Read Replicas. 2. Set up a batch job that puts reports in an S3 bucket. 3. Launch a CloudFront distribution to cache the content with a TTL set to expire objects daily.
- **D.** 1. Launch a Multi-AZ MySQL RDS instance. 2. Query the RDS instance and store the results in a DynamoDB table. 3. Generate reports from DynamoDB table. 4. Delete the old DynamoDB tables every day.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** stats reports read by millions daily; durable, HA, scalable; most cost-effective

🪤 **Your trap:** ElastiCache with default expiry = extra cluster cost; still hits DB for every miss

🧠 **Rule:** Read-heavy, daily-changing reports → batch-generate to S3 + CloudFront with daily TTL (read replicas feed the batch).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
FIFA World Cup analytics — reports (top scorer, goals, thẻ vàng/đỏ...)
┌───────────────────────────────────────────┐
│ 10–30 triệu queries/ngày, đọc RẤT nhiều    │
│ Yêu cầu: durable + highly available +      │
│          highly scalable + RẺ NHẤT         │
└───────────────────────────────────────────┘
```

Đáp án đúng: **C** (RDS Multi-AZ + Read Replica → batch job đẩy report vào S3 → CloudFront cache TTL theo ngày). Anh chọn **B** (RDS Multi-AZ + ElastiCache đọc report, expire mặc định).

#### Vì sao C đúng

Đề yêu cầu đủ 3 thứ: **durable storage**, **database HA + scale**, và **CDN phân phối tới người dùng toàn cầu**. C đáp ứng đúng cả 3 với chi phí thấp nhất:

- **RDS Multi-AZ + Read Replica**: sinh report bằng cách query Read Replica (không ảnh hưởng ghi trên primary), Multi-AZ đảm bảo HA.
- **Batch job đẩy report ra S3**: S3 là nơi lưu **durable** — đây là mảnh còn thiếu ở phần lớn phương án khác.
- **CloudFront với TTL expire theo ngày**: vì report chỉ cần update 1 lần/ngày (dữ liệu trận đấu theo ngày), CloudFront cache ở edge sẽ hứng gần hết 10-30 triệu query/ngày mà **không cần chạm tới RDS lần nào cho các lượt đọc lặp lại** — đây là điểm rẻ nhất vì mỗi request được edge location trả lời thẳng, gần như miễn phí so với việc query DB liên tục.

#### Vì sao B — lựa chọn của Anh — sai

B thay CloudFront bằng **ElastiCache với default expire parameter**. Vấn đề:

- **Thiếu durable storage**: ElastiCache là in-memory cache, dữ liệu không durable — nếu cache miss hoặc cluster restart, vẫn phải quay lại RDS. Đề yêu cầu rõ "durably stored".
- **Thiếu CDN toàn cầu**: FIFA fans "all over the world" đọc report — ElastiCache nằm trong 1 region/VPC, không có edge location phân phối gần người dùng như CloudFront.
- **Default expire = generic TTL không tối ưu** cho pattern "dữ liệu chỉ đổi 1 lần/ngày" — không tận dụng được đặc điểm report ổn định trong ngày để giảm tải DB tối đa như thiết kế TTL-daily của C.
- Về chi phí: vẫn phải duy trì **ElastiCache cluster chạy 24/7** để hứng hàng chục triệu query — so với việc chỉ cần **S3 + CloudFront** (trả tiền theo request/băng thông, không cần cluster canh giữ), C rẻ hơn ở quy mô này.

#### Các phương án sai khác

- **A:** Chỉ có RDS Multi-AZ + Read Replica + "daily table cleanup" — không có bất kỳ durable storage riêng nào cho report, và không có CDN.
- **D:** Query RDS rồi lưu kết quả vào **DynamoDB**, sinh report từ DynamoDB, xóa table cũ mỗi ngày — vừa phải duy trì **cả RDS và DynamoDB** song song (2 loại DB = 2 lần chi phí vận hành), vừa không có CDN.

#### So sánh nhanh

| Phương án | Durable storage | CDN toàn cầu | Chi phí vận hành thêm |
|---|---|---|---|
| **C (đúng)** | S3 | CloudFront (TTL ngày) | Thấp — trả theo request |
| B (Anh chọn) | Không | Không | ElastiCache cluster 24/7 |
| A | Không | Không | — |
| D | DynamoDB (nhưng dư thừa) | Không | RDS + DynamoDB song song |

#### Lưu ý thực tế

- Pattern "**batch-generate report tĩnh → S3 → CloudFront cache theo TTL cố định**" là cách kinh điển để giảm tải DB cho các báo cáo/nội dung đọc nhiều nhưng **ít thay đổi trong khung thời gian xác định** (ví dụ 1 lần/ngày) — ưu tiên hơn cache in-memory (ElastiCache/DAX) khi không cần độ trễ ở mức milli/microsecond.

#### Quy tắc nhớ cho thi

- **"Report đọc rất nhiều, đổi ít lần trong ngày, cần rẻ + durable + CDN toàn cầu"** → **batch → S3 → CloudFront TTL theo ngày**.
- **"ElastiCache/DAX"** → tốt cho giảm latency real-time, nhưng **không durable** và không thay được CDN khi cần phân phối toàn cầu.
- **"Cần duy trì 2 loại DB (RDS + DynamoDB) chỉ để tạo report"** → thường là dấu hiệu thừa chi phí, không phải "most cost-effective".

### TD explanation

In this scenario, you are required to have the following:

A durable storage for the generated reports.
A database that is highly available and can scale to handle millions of queries.
A Content Delivery Network that can distribute the report files to users all over the world.

Amazon S3 is object storage built to store and retrieve any amount of data from anywhere. It’s a simple storage service that offers industry leading durability, availability, performance, security, and virtually unlimited scalability at very low costs.
Amazon RDS provides high availability and failover support for DB instances using Multi-AZ deployments. In a Multi-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. The primary DB instance is synchronously replicated across Availability Zones to a standby replica to provide data redundancy, eliminate I/O freezes, and minimize latency spikes during system backups.
Amazon RDS uses the MariaDB, Microsoft SQL Server, MySQL, Oracle, and PostgreSQL DB engines’ built-in replication functionality to create a special type of DB instance called a read replica from a source DB instance. The source DB instance becomes the primary DB instance. Updates made to the primary DB instance are asynchronously copied to the read replica.

Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you’re serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.
Hence, the following option is the best solution that satisfies all of these requirements:
1. Generate the FIFA reports from MySQL database in Multi-AZ RDS deployments configuration with Read Replicas.
2. Set up a batch job that puts reports in an S3 bucket.
3. Launch a CloudFront distribution to cache the content with a TTL set to expire objects daily.
In the above, S3 provides durable storage; Multi-AZ RDS with Read Replicas provide a scalable and highly available database and CloudFront provides the CDN.
The following option is incorrect:
1. Launch a MySQL database in Multi-AZ RDS deployments configuration with Read Replicas.
2. Generate the FIFA reports by querying the Read Replica.
3. Configure a daily job that performs a daily table cleanup.
Although the database is scalable and highly available, it neither has any durable data storage nor a CDN.
The following option is incorrect:
1. Launch a MySQL database in Multi-AZ RDS deployments configuration.
2. Configure the application to generate reports from ElastiCache to improve the read performance of the system.
3. Utilize the default expire parameter for items in ElastiCache.
Although this option handles and provides a better read capability for the system, it is still lacking a durable storage and a CDN.
The following option is incorrect:
1. Launch a Multi-AZ MySQL RDS instance.
2. Query the RDS instance and store the results in a DynamoDB table.
3. Generate reports from DynamoDB table.
4. Delete the old DynamoDB tables every day.
The above is not a cost-effective solution to maintain both RDS and a DynamoDB instance.

References:
https://aws.amazon.com/rds/details/multi-az/
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html

Check out this Amazon RDS Cheat Sheet:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q69"></a>

## Q69

A company processes several petabytes of images submitted by users on their photo hosting site every month. Each month, the images are processed in its on-premises data center by a High-Performance Computing (HPC) cluster with a capacity of 5,000 cores and 10 petabytes of data. Processing a month’s worth of images by thousands of jobs running in parallel takes about a week and the processed images are stored on a network file server, which also backups the data to a disaster recovery site.
The current data center is nearing its capacity so the users are forced to spread the jobs within the course of the month. This is not ideal for the requirement of the jobs, so the Solutions Architect was tasked to design a scalable solution that can exceed the current capacity with the least amount of management overhead while maintaining the current level of durability.
Which of the following solutions will meet the company’s requirements while being cost-effective?

- **A.** Create an Amazon SQS queue and submit the list of jobs to be processed. Create an Auto Scaling Group of Amazon EC2 Spot Instances that will process the jobs from the SQS queue. Share the raw data across all the instances using Amazon EFS. Store the processed images in an Amazon S3 bucket for long term storage.
- **B.** Using a combination of On-demand and Reserved Instances as Task Nodes, create an EMR cluster that will use Spark to pull the raw data from an Amazon S3 bucket. List the jobs that need to be processed by the EMR cluster on a DynamoDB table. Store the processed images on a separate Amazon S3 bucket.
- **C.** Package the executable file for the job in a Docker image stored on Amazon Elastic Container Registry (Amazon ECR). Run the Docker images on Amazon Elastic Kubernetes Service (Amazon EKS). Auto Scaling can be handled automatically by EKS. Store the raw data temporarily on Amazon EBS SC1 volumes and then send the images to an Amazon S3 bucket after processing.
- **D.** Utilize AWS Batch with Managed Compute Environments to create a fleet using Spot Instances. Store the raw data on an Amazon S3 bucket. Create jobs on AWS Batch Job Queues that will pull objects from the Amazon S3 bucket and temporarily store them to the EC2 EBS volumes for processing. Send the processed images back to another Amazon S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** batch image jobs; exceed capacity; least management overhead; keep durability; cost-effective

🪤 **Your trap:** SQS + Spot ASG = DIY scheduler; EFS costs more than S3; Spot interruptions can cause double processing

🧠 **Rule:** Batch jobs + least overhead → AWS Batch managed compute env with Spot + S3 for raw/processed data.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem HPC: 5,000 cores, 10PB data
┌─────────────────────────────────────────┐
│ Xử lý ảnh hàng tháng, hàng nghìn job song song │
│ Mất ~1 tuần/tháng, DC đang gần hết capacity     │
└─────────────────────────────────────────┘
Yêu cầu: scale VƯỢT capacity hiện tại
         + ÍT quản lý nhất (least management overhead)
         + vẫn giữ độ durable hiện tại
         + cost-effective
```

Đáp án đúng: **D** (AWS Batch + Managed Compute Environment + Spot + S3). Anh chọn **A** (SQS + Auto Scaling Group Spot + EFS + S3).

#### Vì sao D đúng

**AWS Batch** được sinh ra chính xác cho use case "hàng trăm nghìn batch job chạy song song": nó **tự động** provision loại và số lượng compute resource tối ưu theo khối lượng job, không cần cài đặt hay quản lý software/cluster lập lịch — đúng yêu cầu "least management overhead". Cụ thể:

- **Managed Compute Environment với Spot Instances**: AWS Batch tự lo việc chọn instance type, scale số lượng, và quản lý Spot interruption theo cơ chế nội bộ của Batch — Anh không phải tự viết logic retry/resume.
- **Raw data lưu trên S3** (không phải EFS) — S3 rẻ hơn và là dịch vụ lưu trữ chuẩn cho dữ liệu lớn, không cần mount file system chia sẻ.
- **Batch Job Queue** kéo object từ S3, lưu tạm trên **EBS** để xử lý, rồi đẩy kết quả sang S3 khác — giữ nguyên mức durable (S3 có độ durable rất cao) như DC hiện tại đang backup.

#### Vì sao A — lựa chọn của Anh — sai

A dùng **SQS + Auto Scaling Group của Spot Instances tự dựng** để xử lý job, và **EFS** để chia sẻ raw data giữa các instance. Hai điểm sai:

1. **Tự dựng scheduler bằng SQS + ASG = "DIY orchestration"** — Anh phải tự viết logic: đọc message từ queue, xử lý, xóa message, xử lý retry khi Spot bị reclaim... Đây là **nhiều management overhead hơn** so với AWS Batch đã đóng gói sẵn toàn bộ vòng đời job. Đề nhấn mạnh "least amount of management overhead" — đây là từ khóa quyết định loại A.
2. **EFS đắt hơn S3** cho việc lưu raw data quy mô petabyte, và **SQS + Spot không có cơ chế idempotency/checkpoint built-in** → một job có thể bị xử lý **2 lần** khi Spot instance bị thu hồi giữa lúc đang chạy (message quay lại queue nhưng phần việc đã làm dở không được theo dõi).

**Lỗi tư duy chung**: SQS + ASG là pattern hợp lệ để tự xây hệ thống xử lý job phân tán, nhưng khi đề đã có sẵn dịch vụ managed chuyên biệt (AWS Batch) làm đúng việc này với ít thao tác hơn, đó luôn là lựa chọn ưu tiên hơn giải pháp tự ráp.

#### Các phương án sai khác

- **B (EMR + Spark + DynamoDB job list):** phải tự vận hành **EMR cluster + Spark**, có instance On-demand/Reserved chạy liên tục dù job ít — tốn chi phí và management overhead cho một hệ thống lẽ ra chỉ cần chạy theo lô ảnh xử lý độc lập (không cần framework Big Data phân tán như Spark).
- **C (ECR + EKS + EBS SC1):** chuyển toàn bộ ứng dụng thành container trên EKS đòi hỏi **thay đổi lớn** cho ứng dụng hiện có; và **EBS SC1** (cold HDD, throughput-optimized) không co giãn nhanh — tạo volume lớn để chứa petabyte dữ liệu tạm thời là không kinh tế.

#### So sánh nhanh

| Phương án | Compute orchestration | Raw data storage | Management overhead |
|---|---|---|---|
| **D (đúng)** | AWS Batch (managed) | S3 | Thấp nhất |
| A (Anh chọn) | Tự dựng: SQS + ASG | EFS (đắt hơn) | Cao — tự viết logic |
| B | EMR + Spark (tự vận hành cluster) | S3 | Cao |
| C | EKS (Auto Scaling do EKS) | EBS SC1 (tạm) | Cao — phải container hóa lại |

#### Quy tắc nhớ cho thi

- **"Hàng trăm nghìn batch job, ít quản lý nhất"** → **AWS Batch với Managed Compute Environment**, không phải tự dựng SQS + ASG.
- **"SQS + ASG tự viết logic xử lý"** → chỉ chọn khi đề KHÔNG có lựa chọn AWS Batch/Step Functions managed tương đương.
- **"EFS vs S3 cho raw data lớn"** → S3 rẻ hơn cho lưu trữ khối lớn không cần POSIX file system chia sẻ.
- **"Spot Instance + xử lý job"** → cẩn thận nguy cơ **double processing**; AWS Batch xử lý việc này tốt hơn tự dựng queue.

### TD explanation

AWS Batch enables developers, scientists, and engineers to easily and efficiently run hundreds of thousands of batch computing jobs on AWS. AWS Batch dynamically provisions the optimal quantity and type of compute resources (e.g., CPU or memory optimized instances) based on the volume and specific resource requirements of the batch jobs submitted. With AWS Batch, there is no need to install and manage batch computing software or server clusters that you use to run your jobs, allowing you to focus on analyzing results and solving problems.
There is no additional charge for AWS Batch. You only pay for the AWS resources (e.g. EC2 instances or Fargate jobs) you create to store and run your batch jobs. From the AWS Batch use cases page, we can see an example similar to this scenario wherein Digital Media and Entertainment companies require highly scalable batch computing resources to enable accelerated and automated processing of data as well as the compilation and processing of files, graphics, and visual effects for high-resolution video content. Use AWS Batch to accelerate content creation, dynamically scale media packaging, and automate asynchronous media supply chain workflows.

In AWS Batch, job queues are mapped to one or more compute environments. Compute environments contain the Amazon ECS container instances that are used to run containerized batch jobs. A specific compute environment can also be mapped to one or many job queues. Within a job queue, the associated compute environments each have an order that’s used by the scheduler to determine where jobs that are ready to be run should run.
Therefore, the correct answer is: Utilize AWS Batch with Managed Compute Environments to create a fleet using Spot Instances. Store the raw data on an Amazon S3 bucket. Create jobs on AWS Batch Job Queues that will pull objects from the Amazon S3 bucket and temporarily store them to the EC2 EBS volumes for processing. Send the processed images back to another Amazon S3 bucket.
The option that says: Package the executable file for the job in a Docker image stored on Amazon Elastic Container Registry (Amazon ECR). Run the Docker images on Amazon Elastic Kubernetes Service (Amazon EKS). Auto Scaling can be handled automatically by EKS. Store the raw data temporarily on Amazon EBS SC1 volumes and then send the images to an Amazon S3 bucket after processing is incorrect. Although this is possible, converting the application to a container and deploying it to an EKS cluster will entail a lot of changes for the application. Additionally, since you can’t quickly increase/decrease SC1 EBS volumes, creating a large volume to handle petabytes of data is not cost-effective.
The option that says: Using a combination of On-demand and Reserved Instances as Task Nodes, create an EMR cluster that will use Apache Spark to pull the raw data from an Amazon S3 bucket. List the jobs that need to be processed by the EMR cluster on a DynamoDB table. Store the processed images on a separate Amazon S3 bucket is incorrect as managing the EMR cluster and Apache Spark adds significant management overhead for this solution. There is also an additional cost for the EC2 instances that are constantly running even if there are only a few jobs that need to be run.
The option that says: Create an Amazon SQS queue and submit the list of jobs to be processed. Create an Auto Scaling Group of Amazon EC2 Spot Instances that will process the jobs from the SQS queue. Share the raw data across all the instances using Amazon EFS. Store the processed images in an Amazon S3 bucket for long term storage is incorrect as Amazon EFS is more expensive than storing the raw data on S3 buckets. This is also not efficient as listing the jobs on SQS Queue can cause some to be processed twice, depending on the state of your Spot instances.

References:
https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html
https://aws.amazon.com/batch/use-cases/
https://aws.amazon.com/blogs/compute/building-high-throughput-genomic-batch-workflows-on-aws-batch-layer-part-3-of-4/

Check out this AWS Batch Cheat Sheet:
https://tutorialsdojo.com/aws-batch/

</details>

<a id="q62"></a>

## Q62

An innovative Business Process Outsourcing (BPO) startup is planning to launch a scalable and cost-effective call center system using AWS. The system should be able to receive inbound calls from thousands of customers and generate user contact flows. Callers must have the capability to perform basic tasks such as changing their password or checking their balance without them having to speak to a call center agent. It should also have advanced deep learning functionalities such as automatic speech recognition (ASR) to achieve highly engaging user experiences and lifelike conversational interactions. A feature that allows the solution to query other business applications and send relevant data back to callers must also be implemented.
Which of the following is the MOST suitable solution that the Solutions Architect should implement?

- **A.** Set up a cloud-based contact center using the AWS Ground Station service. Create a conversational chatbot using Amazon Alexa for Business with automatic speech recognition and natural language understanding to recognize the intent of the caller then integrate it with AWS Ground Station. Connect the solution to various business applications and other internal systems using AWS Lambda functions.
- **B.** Set up a cloud-based contact center using the Amazon Connect service. Create a conversational chatbot using Amazon Comprehend with automatic speech recognition and natural language understanding to recognize the intent of the caller then integrate it with Amazon Connect. Connect the solution to various business applications and other internal systems using AWS Lambda functions.
- **C.** Set up a cloud-based contact center using the Amazon Connect service. Create a conversational chatbot using Amazon Lex with automatic speech recognition and natural language understanding to recognize the intent of the caller then integrate it with Amazon Connect. Connect the solution to various business applications and other internal systems using AWS Lambda functions.
- **D.** Set up a cloud-based contact center using the AWS Elemental MediaConnect service. Create a conversational chatbot using Amazon Polly with automatic speech recognition and natural language understanding to recognize the intent of the caller then integrate it with AWS Elemental MediaConnect. Connect the solution to various business applications and other internal systems using AWS Lambda functions.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** call center self-service; ASR + natural language; query business apps

🪤 **Your trap:** MediaConnect = live video transport; Polly = text-to-speech, not speech recognition

🧠 **Rule:** Contact center → Amazon Connect; conversational bot with ASR/NLU → Amazon Lex (+ Lambda to query backends).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
BPO call center: inbound calls, hàng nghìn khách hàng
┌───────────────────────────────────────────┐
│ Tự đổi password / check balance — KHÔNG cần agent │
│ Cần: ASR (nhận diện giọng nói) + NLU (hiểu ý định)  │
│ Cần: query business apps trả data lại cho caller   │
└───────────────────────────────────────────┘
```

Đáp án đúng: **C** (Amazon Connect + Amazon Lex + Lambda). Anh chọn **D** (AWS Elemental MediaConnect + Amazon Polly + Lambda).

#### Vì sao C đúng

- **Amazon Connect** là dịch vụ **contact center** đúng nghĩa: cung cấp contact flow (giống IVR), quản lý gọi vào, hàng đợi, định tuyến — chính là "cloud-based contact center" mà đề yêu cầu.
- **Amazon Lex** là dịch vụ có **cả ASR (automatic speech recognition) và NLU (natural language understanding)** — dùng chung công nghệ deep learning với Alexa, cho phép nhận diện giọng nói ở tần số telephony (8kHz) và hiểu ý định người gọi mà không cần họ nói đúng cụm từ cố định.
- **Lambda** được Lex gọi để **query business applications** và trả dữ liệu lại cho caller (ví dụ tra số dư) — đúng yêu cầu "query other business applications and send relevant data back to callers".

Kết hợp Connect (hạ tầng contact center) + Lex (bot ASR/NLU) + Lambda (tích hợp backend) khớp với đúng toàn bộ yêu cầu đề.

#### Vì sao D — lựa chọn của Anh — sai

D có hai điểm sai gốc:

1. **AWS Elemental MediaConnect** không phải contact center — đây là dịch vụ **truyền tải video trực tiếp chất lượng cao (live video transport)**, dùng cho broadcast/streaming, hoàn toàn không liên quan đến call center hay contact flow.
2. **Amazon Polly** là dịch vụ **text-to-speech** (biến văn bản thành giọng nói) — chỉ làm một chiều "nói ra", **không có khả năng nhận diện giọng nói (ASR) hay hiểu ý định (NLU)**. Đề yêu cầu rõ "automatic speech recognition" và "recognize the intent of the caller" — đây là việc của Lex, không phải Polly.

**Trap dễ nhầm:** Polly (text→speech) và Lex (speech→text + hiểu ý định, hội thoại hai chiều) là hai dịch vụ khác chức năng hoàn toàn — Polly không thể thay Lex trong vai trò chatbot hội thoại.

#### Các phương án sai khác

- **A:** Dùng **AWS Ground Station** (dịch vụ điều khiển liên lạc vệ tinh) làm contact center — không liên quan gì đến call center. **Alexa for Business** dùng để biến thiết bị Alexa thành trợ lý năng suất trong phòng họp/văn phòng, không phải nền tảng xây dựng chatbot cho contact center.
- **B:** Đúng Amazon Connect, nhưng dùng **Amazon Comprehend** để làm chatbot — Comprehend là dịch vụ **NLP phân tích văn bản** (trích xuất insight, entity, sentiment từ text có sẵn), **không có ASR** (không xử lý giọng nói) và không phải công cụ xây dựng conversational bot.

#### So sánh nhanh

| Dịch vụ | Vai trò thật | Có ASR? | Có NLU/hội thoại? | Dùng cho contact center? |
|---|---|---|---|---|
| **Amazon Lex** | Conversational bot | Có | Có | Có (tích hợp Connect) |
| Amazon Polly | Text-to-speech | Không | Không | Không |
| Amazon Comprehend | Phân tích văn bản (NLP) | Không | Không (không phải hội thoại) | Không |
| Amazon Connect | Nền tảng contact center | — | — | Có |
| AWS Elemental MediaConnect | Truyền video trực tiếp | — | — | Không |
| AWS Ground Station | Điều khiển vệ tinh | — | — | Không |

#### Quy tắc nhớ cho thi

- **"Contact center / call center trên AWS"** → **Amazon Connect**.
- **"ASR + NLU, chatbot hội thoại, hiểu ý định người dùng"** → **Amazon Lex**.
- **"Text → Speech" (đọc chữ thành giọng nói)** → **Amazon Polly** (không phải chatbot).
- **"Phân tích văn bản có sẵn, trích insight"** → **Amazon Comprehend** (không phải ASR/chatbot).
- Thấy tên dịch vụ lạ như **MediaConnect, Ground Station, Alexa for Business** xuất hiện ở câu về contact center → hầu như luôn là bẫy do tên nghe "liên quan" nhưng sai chức năng.

### TD explanation

Amazon Connect provides a seamless omnichannel experience through a single unified contact center for voice and chat. Contact center agents and managers don’t have to learn multiple tools because Amazon Connect has the same contact routing, queuing, analytics, and management tools in a single UI across voice, web chat, and mobile chat.
Amazon Lex is a service for building conversational interfaces into any application using voice and text. Amazon Lex provides the advanced deep learning functionalities of automatic speech recognition (ASR) for converting speech to text and natural language understanding (NLU) to recognize the intent of the text, enabling you to build applications with highly engaging user experiences and lifelike conversational interactions. With Amazon Lex, the same deep learning technologies that power Amazon Alexa are now available to any developer, enabling you to quickly and easily build sophisticated, natural language conversational bots (“chatbots”).

Contact flows define the experience your customers have when they interact with your contact center. These are similar in concept to Interactive Voice Response (IVR). Contact flows are comprised of blocks, with each block defining a step or interaction in your contact center. For example, there are blocks to play a prompt, get input from a customer, branch based on customer input, or invoke an AWS Lambda function or an Amazon Lex bot.
By using an Amazon Lex chatbot in your Amazon Connect call center, callers can perform tasks such as changing a password, requesting a balance on an account, or scheduling an appointment without needing to speak to an agent. These chatbots use automatic speech recognition and natural language understanding to recognize the intent of the caller. They are able to recognize human speech at an optimal (8 kHz) telephony audio sampling rate and understand the caller’s intent without requiring the caller to speak in specific phrases. Amazon Lex uses AWS Lambda functions to query your business applications, provide information back to callers, and make updates as requested. Amazon Lex chatbots also maintain context and manage the dialogue, dynamically adjusting responses based on the conversation.
Hence, the correct answer is: Set up a cloud-based contact center using the Amazon Connect service. Create a conversational chatbot using Amazon Lex with automatic speech recognition and natural language understanding to recognize the intent of the caller then integrate it with Amazon Connect. Connect the solution to various business applications and other internal systems using AWS Lambda functions.
The option that says: Set up a cloud-based contact center using the AWS Ground Station service. Create a conversational chatbot using Amazon Alexa for Business with automatic speech recognition and natural language understanding to recognize the intent of the caller then integrate it with AWS Ground Station. Connect the solution to various business applications and other internal systems using AWS Lambda functions is incorrect. AWS Ground Station is a fully managed service that lets you control satellite communications, process data, and scale your operations without having to worry about building or managing your own ground station infrastructure. This service is not suitable as a cloud-based contact center. Moreover, Alexa for Business simply empowers companies to use Alexa devices as their intelligent assistant to be more productive in meeting rooms, at their desks, and even with the Alexa devices they already use at home or on the go. You should use a different machine learning service, such as Amazon Lex, to create a conversational chatbot.
The option that says: Set up a cloud-based contact center using the AWS Elemental MediaConnect service. Create a conversational chatbot using Amazon Polly with automatic speech recognition and natural language understanding to recognize the intent of the caller then integrate it with AWS Elemental MediaConnect. Connect the solution to various business applications and other internal systems using AWS Lambda functions is incorrect because AWS Elemental MediaConnect is just a high-quality transport service for live video. You have to use Amazon Connect instead to set up your cloud-based contact center. And although Amazon Polly is a machine learning service, it is quite limited as it just turns text into lifelike speech that allows you to create applications that talk and build entirely new categories of speech-enabled products. A more suitable service to use here is Amazon Lex.
The option that says: Set up a cloud-based contact center using the Amazon Connect service. Create a conversational chatbot using Amazon Comprehend with automatic speech recognition and natural language understanding to recognize the intent of the caller then integrate it with Amazon Connect. Connect the solution to various business applications and other internal systems using AWS Lambda functions is incorrect because Amazon Comprehend is used to derive and understand valuable insights from text within documents. It doesn’t have automatic speech recognition (ASR) for converting speech to text nor natural language understanding (NLU). You have to use Amazon Lex for this scenario

References:
https://aws.amazon.com/connect/
https://aws.amazon.com/lex/
https://aws.amazon.com/blogs/contact-center/easily-set-up-interactive-messages-for-your-amazon-connect-chatbot/

Check out this Amazon Lex Cheat Sheet:
https://tutorialsdojo.com/amazon-lex/

</details>

---

# Group G — Migration (4)

<a id="q57"></a>

## Q57

A major entertainment studio operates a hybrid cloud infrastructure with its on-premises data center connected to AWS through an AWS Direct Connect connection. The studio maintains an extensive archive of over 50 TB of raw footage, documentaries, and feature films stored on an on-premises tape library, which is actively managed by its existing Media Asset Management (MAM) system.
To modernize its content discovery workflow, the studio wants to implement an automated tagging system that leverages facial recognition technology to identify and catalog the actors and personalities appearing across its entire video archive, storing a still image of each recognized individual. The studio also has a long-term goal of fully migrating these media assets, along with the MAM video contents, to AWS while ensuring minimal interruption to its day-to-day production operations.
Which of the following options provides a solution that uses the LEAST amount of ongoing management overhead while causing MINIMAL disruption to the existing system?

- **A.** Use AWS DataSync to migrate all of the media files from the on-premises library into Amazon S3. Provision a large Amazon EC2 instance and allow it to access the S3 bucket. Install an open-source facial recognition tool on the instance, like OpenFace or OpenCV. Process the media files to retrieve the metadata and push this information into the MAM solution. Lastly, copy the media files to another S3 bucket.
- **B.** Set up a tape gateway appliance on-premises and connect it to your AWS Storage Gateway. Configure the MAM solution to fetch the media files from the current archive and push them into the tape gateway to be stored in Amazon Glacier. Using Amazon Rekognition, build a collection from the catalog of faces. Utilize an AWS Lambda function that invokes the Rekognition JavaScript SDK to have Rekognition process the video directly from the tape gateway in real time, retrieve the required metadata, and push the metadata into the MAM solution.
- **C.** Integrate the file system of your local data center to AWS Storage Gateway by setting up a file gateway appliance on-premises. Utilize the MAM solution to extract the media files from the current data store and send them into the file gateway. Build a collection using Amazon Rekognition by populating a catalog of faces from the processed media files. Use an AWS Lambda function to invoke the Rekognition JavaScript SDK to fetch the media file from the Amazon S3 bucket that backs the file gateway, retrieve the needed metadata, and finally, persist the information into the MAM solution.
- **D.** Use Amazon Kinesis Video Streams to set up a video ingestion stream and with Amazon Rekognition, build a collection of faces. Stream the media files from the MAM solution into Kinesis Video Streams and configure Rekognition to process the streamed files. Launch a stream consumer to retrieve the required metadata, and push the metadata into the MAM solution. Finally, configure the stream to store the files in an Amazon S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** facial recognition over video archive; later full migration; minimal disruption + least ops

🪤 **Your trap:** Tape gateway → Glacier: Rekognition can't read video from virtual tapes

🧠 **Rule:** Hybrid media + ML → File Gateway (NFS/SMB → S3) + Rekognition face collection via Lambda.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises tape library (50+ TB) ──DX──► AWS
        │
   MAM system quản lý archive
        │
Yêu cầu: nhận diện khuôn mặt (facial recognition) trên toàn bộ video
         + về sau migrate hết sang AWS
         + LEAST ops overhead, MINIMAL disruption
```

Đáp án đúng: **C** (File Gateway + Amazon Rekognition collection + Lambda). Anh chọn **B** (Tape Gateway + Rekognition qua Lambda "real time").

#### Vì sao C đúng

- **AWS Storage Gateway – File Gateway**: expose một file share (NFS/SMB) trên on-premises, MAM chỉ cần "copy file" vào file gateway như một ổ đĩa mạng bình thường — **không cần thay đổi lớn trong MAM** → đúng "minimal disruption".
- File gateway lưu file thật dưới dạng object trong một **S3 bucket** phía sau nó → dữ liệu **có thể đọc trực tiếp từ S3** ngay lập tức.
- **Amazon Rekognition**: dùng `IndexFaces` để tạo **collection** (catalog khuôn mặt) từ ảnh/video đã có trong S3, rồi Lambda gọi Rekognition SDK để lấy metadata (ai xuất hiện trong clip) và đẩy vào MAM.
- Toàn bộ chuỗi này dùng dịch vụ **fully managed** (Storage Gateway, S3, Rekognition, Lambda) → không cần EC2 tự quản lý → **least ops overhead**.
- Về lâu dài, dữ liệu đã nằm sẵn trong S3 (qua file gateway) nên **thuận lợi cho việc migrate toàn bộ MAM sang AWS sau này**.

#### Vì sao B (Anh chọn) trông hợp lý nhưng sai

B cũng dùng đúng combo "Storage Gateway + Rekognition", nên rất dễ nhầm là đáp án đúng. Nhưng B chọn nhầm loại gateway:

- **Tape Gateway lưu dữ liệu dưới dạng virtual tape, được archive vào Glacier/Glacier Deep Archive.** Đây là kho lưu trữ **lạnh, không được thiết kế để đọc file "trực tiếp" hay real-time** — Rekognition (hay bất kỳ dịch vụ nào) **không thể fetch video trực tiếp từ tape gateway** để xử lý ngay, vì dữ liệu đã được archive.
- Ý tưởng "Lambda gọi Rekognition xử lý video trực tiếp từ tape gateway theo thời gian thực" về bản chất **không khả thi** — muốn xử lý được, vẫn phải retrieve dữ liệu ra khỏi Glacier trước (mất thời gian, không phải real time).
- Tape Gateway đúng là lựa chọn tốt cho **archive lâu dài** (thay thế physical tape) chứ không phải cho workflow cần **đọc/xử lý dữ liệu ngay** như facial recognition.

#### Các lựa chọn sai khác

- **A (DataSync migrate hết vào S3 + EC2 tự cài OpenFace/OpenCV):** Yêu cầu tự provision và duy trì một **EC2 instance lớn** với công cụ facial recognition mã nguồn mở → tăng **ops overhead** đáng kể (patch, scale, maintain) so với dùng Rekognition managed. Ngoài ra "migrate hết" ngay từ đầu cũng gây disruption lớn hơn cần thiết cho một yêu cầu ban đầu chỉ là tagging.
- **D (Kinesis Video Streams):** Kinesis Video Streams được thiết kế cho **video streaming thời gian thực** (camera, live feed), không tối ưu cho việc xử lý **video đã có sẵn** (pre-existing archive). Phải thay đổi MAM để "stream" toàn bộ media file vào KVS — thay đổi luồng làm việc hiện tại nhiều hơn, tăng độ phức tạp và ops overhead so với chỉ "copy file" vào file gateway.

#### So sánh nhanh

| Lựa chọn | Loại gateway/service | Đọc video ngay được? | Ops overhead |
|---|---|---|---|
| **C (đúng)** | File Gateway (NFS/SMB → S3) | ✓ (S3 trực tiếp) | Thấp |
| B (Anh chọn) | Tape Gateway (→ Glacier) | ✗ (archive lạnh) | Trung bình, nhưng bất khả thi |
| A | DataSync + EC2 tự quản | ✓ nhưng phải tự vận hành EC2 | Cao |
| D | Kinesis Video Streams | Chỉ hợp streaming realtime | Cao (đổi cả MAM workflow) |

#### Quy tắc nhớ cho thi

- **"Tape Gateway" → luôn gắn với Glacier/Deep Archive, dữ liệu lạnh, không xử lý ngay được.**
- **"File Gateway" → S3 phía sau, đọc/ghi tức thời như file share bình thường → hợp cho các workload cần xử lý dữ liệu ngay (như Rekognition).**
- **"Facial recognition trên archive video có sẵn"** → **Amazon Rekognition (collection + IndexFaces) + Lambda**, không phải tự dựng OpenCV trên EC2.
- **"Minimal disruption to existing MAM"** → ưu tiên giải pháp chỉ cần MAM "copy file" vào gateway, tránh phương án buộc phải đổi kiến trúc luồng dữ liệu của MAM (như stream vào KVS).

### TD explanation

Amazon Rekognition can store information about detected faces in server-side containers known as collections. You can use the facial information that’s stored in a collection to search for known faces in images, stored videos, and streaming videos. Amazon Rekognition supports the IndexFaces operation. You can use this operation to detect faces in an image and persist information about facial features that are detected in a collection. This is an example of a storage-based API operation because the service persists information on the server.
To store facial information, you must first create (CreateCollection) a face collection in one of the AWS Regions in your account. You specify this face collection when you call the IndexFaces operation. After you create a face collection and store facial feature information for all faces, you can search the collection for face matches. To search for faces in an image, call SearchFacesByImage. To search for faces in a stored video, call StartFaceSearch. To search for faces in a streaming video, call CreateStreamProcessor.

AWS Storage Gateway offers file-based, volume-based, and tape-based storage solutions. With a tape gateway, you can cost-effectively and durably archive backup data in GLACIER or DEEP_ARCHIVE. A tape gateway provides a virtual tape infrastructure that scales seamlessly with your business needs and eliminates the operational burden of provisioning, scaling, and maintaining a physical tape infrastructure.
You can run AWS Storage Gateway either on-premises as a VM appliance, as a hardware appliance, or in AWS as an Amazon Elastic Compute Cloud (Amazon EC2) instance. You deploy your gateway on an EC2 instance to provision iSCSI storage volumes in AWS. You can use gateways hosted on EC2 instances for disaster recovery, data mirroring, and providing storage for applications hosted on Amazon EC2.
Hence, the correct answer is: Integrate the file system of your local data center to AWS Storage Gateway by setting up a file gateway appliance on-premises. Utilize the MAM solution to extract the media files from the current data store and send them into the file gateway. Build a collection using Amazon Rekognition by populating a catalog of faces from the processed media files. Use an AWS Lambda function to invoke the Rekognition JavaScript SDK to fetch the media file from the Amazon S3 bucket that backs the file gateway, retrieve the needed metadata, and finally, persist the information into the MAM solution.
The option that says: Use Amazon Kinesis Video Streams to set up a video ingestion stream and with Amazon Rekognition, build a collection of faces. Stream the media files from the MAM solution into Kinesis Video Streams and configure Rekognition to process the streamed files. Launch a stream consumer to retrieve the required metadata, and push the metadata into the MAM solution. Finally, configure the stream to store the files in an Amazon S3 bucket is incorrect. This approach requires significant changes to the existing MAM solution to stream media files directly into Kinesis Video Streams, potentially causing more disruption to the current workflow. Additionally, Kinesis Video Streams is primarily designed for real-time video streaming and processing, which may not be the most efficient approach for processing pre-existing media files stored in a tape library. Lastly, setting up and managing Kinesis Video Streams, configuring Amazon Rekognition integration, implementing a stream consumer, and storing files in S3 introduces additional complexity and management overhead compared to the File Gateway approach.
The option that says: Set up a tape gateway appliance on-premises and connect it to your AWS Storage Gateway. Configure the MAM solution to fetch the media files from the current archive and push them into the tape gateway to be stored in Amazon Glacier. Using Amazon Rekognition, build a collection from the catalog of faces. Utilize an AWS Lambda function that invokes the Rekognition JavaScript SDK to have Rekognition process the video directly from the tape gateway in real time, retrieve the required metadata, and push the metadata into the MAM solution is incorrect. Although this solution uses the right combination of AWS Storage Gateway and Amazon Rekognition, take note that you can’t directly fetch the media files from your tape gateway in real time since this is backed up using Glacier. Although the on-premises data center is using a tape gateway, you can still set up a solution to use a file gateway in order to properly process the videos using Amazon Rekognition. Keep in mind that the tape gateway in the AWS Storage Gateway service is typically used as an archive solution.
The option that says: Use AWS DataSync to migrate all of the media files from the on-premises library into Amazon S3. Provision a large Amazon EC2 instance and allow it to access the S3 bucket. Install an open-source facial recognition tool on the instance, like OpenFace or OpenCV. Process the media files to retrieve the metadata and push this information into the MAM solution. Lastly, copy the media files to another S3 bucket is incorrect because this option requires provisioning and maintaining a large EC2 instance with open-source facial recognition tools. That increases management overhead and complexity compared to using fully managed services like Rekognition and Lambda.

References:
https://docs.aws.amazon.com/rekognition/latest/dg/collections.html
https://aws.amazon.com/storagegateway/file/

Check out this Amazon Rekognition Cheat Sheet:
https://tutorialsdojo.com/amazon-rekognition/

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/
atures that are detected in a collection. This is an example of a storage-based API operation because the service persists information on the server.
To store facial information, you must first create (CreateCollection) a face collection in one of the AWS Regions in your account. You specify this face collection when you call the IndexFaces operation. After you create a face collection and store facial feature information for all faces, you can search the collection for face matches. To search for faces in an image, call SearchFacesByImage. To search for faces in a stored video, call StartFaceSearch. To search for faces in a streaming video, call CreateStreamProcessor.

AWS Storage Gateway offers file-based, volume-based, and tape-based storage solutions. With a tape gateway, you can cost-effectively and durably archive backup data in GLACIER or DEEP_ARCHIVE. A tape gateway provides a virtual tape infrastructure that scales seamlessly with your business needs and eliminates the operational burden of provisioning, scaling, and maintaining a physical tape infrastructure.
You can run AWS Storage Gateway either on-premises as a VM appliance, as a hardware appliance, or in AWS as an Amazon Elastic Compute Cloud (Amazon EC2) instance. You deploy your gateway on an EC2 instance to provision iSCSI storage volumes in AWS. You can use gateways hosted on EC2 instances for disaster recovery, data mirroring, and providing storage for applications hosted on Amazon EC2.
Hence, the correct answer is: Integrate the file system of your local data center to AWS Storage Gateway by setting up a file gateway appliance on-premises. Utilize the MAM solution to extract the media files from the current data store and send them into the file gateway. Build a collection using Amazon Rekognition by populating a catalog of faces from the processed media files. Use an AWS Lambda function to invoke the Rekognition JavaScript SDK to fetch the media file from the Amazon S3 bucket that backs the file gateway, retrieve the needed metadata, and finally, persist the information into the MAM solution.
The option that says: Use Amazon Kinesis Video Streams to set up a video ingestion stream and with Amazon Rekognition, build a collection of faces. Stream the media files from the MAM solution into Kinesis Video Streams and configure Rekognition to process the streamed files. Launch a stream consumer to retrieve the required metadata, and push the metadata into the MAM solution. Finally, configure the stream to store the files in an Amazon S3 bucket is incorrect. This approach requires significant changes to the existing MAM solution to stream media files directly into Kinesis Video Streams, potentially causing more disruption to the current workflow. Additionally, Kinesis Video Streams is primarily designed for real-time video streaming and processing, which may not be the most efficient approach for processing pre-existing media files stored in a tape library. Lastly, setting up and managing Kinesis Video Streams, configuring Amazon Rekognition integration, implementing a stream consumer, and storing files in S3 introduces additional complexity and management overhead compared to the File Gateway approach.
The option that says: Set up a tape gateway appliance on-premises and connect it to your AWS Storage Gateway. Configure the MAM solution to fetch the media files from the current archive and push them into the tape gateway to be stored in Amazon Glacier. Using Amazon Rekognition, build a collection from the catalog of faces. Utilize an AWS Lambda function that invokes the Rekognition JavaScript SDK to have Rekognition process the video directly from the tape gateway in real time, retrieve the required metadata, and push the metadata into the MAM solution is incorrect. Although this solution uses the right combination of AWS Storage Gateway and Amazon Rekognition, take note that you can’t directly fetch the media files from your tape gateway in real time since this is backed up using Glacier. Although the on-premises data center is using a tape gateway, you can still set up a solution to use a file gateway in order to properly process the videos using Amazon Rekognition. Keep in mind that the tape gateway in the AWS Storage Gateway service is typically used as an archive solution.
The option that says: Use AWS DataSync to migrate all of the media files from the on-premises library into Amazon S3. Provision a large Amazon EC2 instance and allow it to access the S3 bucket. Install an open-source facial recognition tool on the instance, like OpenFace or OpenCV. Process the media files to retrieve the metadata and push this information into the MAM solution. Lastly, copy the media files to another S3 bucket is incorrect because this option requires provisioning and maintaining a large EC2 instance with open-source facial recognition tools. That increases management overhead and complexity compared to using fully managed services like Rekognition and Lambda.

References:
https://docs.aws.amazon.com/rekognition/latest/dg/collections.html
https://aws.amazon.com/storagegateway/file/

Check out this Amazon Rekognition Cheat Sheet:
https://tutorialsdojo.com/amazon-rekognition/

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

<a id="q26"></a>

## Q26

A company is migrating an interactive car registration web system hosted on its on-premises network to AWS Cloud. The current architecture of the system consists of a single NGINX web server and a MySQL database running on a Fedora server, which both reside in its on-premises data center. For the new cloud architecture, a load balancer must be used to evenly distribute the incoming traffic to the application servers. Amazon Route 53 must be used for both domain registration and domain management.
In this scenario, what would be the most efficient way to transfer the web application to AWS?

- **A.** 1. Use AWS DataSync to transfer the web files from the on-premises NGINX server to an Amazon S3 bucket. 2. Run the website directly out of Amazon S3. 3. Migrate the database using the AWS Database Migration Service and AWS Schema Conversion Tool (AWS SCT). 4. Use Route 53 and create an alias record pointing to the ELB.
- **B.** 1. Launch two NGINX EC2 instances in two Availability Zones. 2. Copy the web files from the on-premises web server to each Amazon EC2 web server, using Amazon S3 as the repository. 3. Migrate the database using the AWS Database Migration Service. 4. Create an ELB to front your web servers. 5. Use Route 53 and create an alias A record pointing to the ELB.
- **C.** 1. Use the AWS Transform MGN to create an EC2 AMI of the NGINX web server. 2. Configure auto-scaling to launch in two Availability Zones. 3. Launch a multi-AZ MySQL Amazon RDS instance in one availability zone only. 4. Import the data into Amazon RDS from the latest MySQL backup. 5. Create an ELB to front your web servers 6. Use Route 53 and create an A record pointing to the elastic load balancer.
- **D.** 1. Use AWS Transform to automatically migrate the existing NGINX web server from the on-premises Fedora server to AWS. 2. Configure Auto Scaling to launch two web servers in two Availability Zones. 3. Launch a Multi-AZ MySQL Amazon Relational Database Service (RDS) instance in one Availability Zone only. 4. Import the data into Amazon RDS from the latest MySQL backup. 5. Use Route 53 to create a private hosted zone and point a non-alias A record to the ELB.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** single NGINX + MySQL on Fedora; must use ELB + Route 53; most efficient

🪤 **Your trap:** Option contradicts itself ('Multi-AZ RDS in one AZ only') and imports a stale backup instead of migrating live data

🧠 **Rule:** Read every step: reject options with internal contradictions. Simple web + DB → EC2 in 2 AZs + DMS + ELB + Route 53 alias.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises: 1 NGINX web server + 1 MySQL DB (Fedora)
                    │
                    ▼ migrate lên AWS
Yêu cầu:  phải có Load Balancer phân tải đều
          phải dùng Route 53 cho domain registration + management
Hỏi: cách migrate hiệu quả NHẤT
```

Đây là **câu hỏi đánh lừa (trick question)** — mọi đáp án nhìn thoáng qua đều có cấu trúc hợp lý, điểm khác biệt then chốt nằm ở **các bước bị mâu thuẫn nội bộ hoặc sai chi tiết nhỏ** (loại Route 53 record, dùng backup cũ, MGN cho web server, host site động trên S3). Đáp án đúng: **B**. Anh chọn **C**.

#### Vì sao B đúng

Các bước của B đều nhất quán và đúng kỹ thuật:
1. **2 EC2 chạy NGINX ở 2 AZ** → đúng yêu cầu load balancing + high availability.
2. **Copy web files qua S3 làm repository trung gian** → cách hợp lý để đưa file tĩnh từ on-premises lên EC2.
3. **AWS DMS để migrate database** → DMS cho phép **source DB vẫn hoạt động bình thường trong lúc di chuyển**, giảm downtime — đúng với DB đang chạy (MySQL trên Fedora).
4. **Tạo ELB đứng trước web server.**
5. **Route 53 alias A record trỏ vào ELB** → đây là điểm mấu chốt: với **ELB/CloudFront/S3 luôn dùng A record kiểu Alias**; alias record là mở rộng của Route 53 cho phép ánh xạ tới ELB (target thay đổi IP theo thời gian) mà CNAME thường không làm được ở root domain.

Không có bước nào trong B tự mâu thuẫn hoặc dùng sai loại record.

#### Vì sao C (Anh chọn) trông hợp lý nhưng sai

C có vẻ "chuyên nghiệp" hơn vì nhắc tới AMI, Auto Scaling, Multi-AZ RDS — trông như một kiến trúc hiện đại hơn B. Nhưng có 2 lỗi:

1. **"Launch a multi-AZ MySQL Amazon RDS instance in one availability zone only"** — đây là **mâu thuẫn logic nội tại**: theo định nghĩa, **Multi-AZ deployment bắt buộc trải trên nhiều Availability Zone** (1 primary + 1 standby ở AZ khác). Nói "Multi-AZ nhưng chỉ 1 AZ" là tự phủ định chính nó — TD dùng chi tiết này để loại toàn bộ nhóm đáp án chứa câu này (bao gồm cả D).
2. **"Import the data into Amazon RDS from the latest MySQL backup"** — dùng **backup cũ nhất gần nhất** để import nghĩa là dữ liệu ghi thêm sau thời điểm backup đó sẽ **bị mất** khi cutover. Trong khi B dùng **DMS** để đồng bộ dữ liệu **liên tục, gần thời gian thực**, giảm mất dữ liệu và downtime hơn nhiều — "hiệu quả nhất" mà đề yêu cầu.
3. Bước cuối C dùng **"A record pointing to the elastic load balancer" — không có Alias** — với ELB, luôn phải dùng **Alias record**, không dùng A record thường (A record đơn giản chỉ ánh xạ tới một IP tĩnh, còn ELB có thể đổi IP).

#### Các lựa chọn sai khác

- **D:** Cùng lỗi "Multi-AZ RDS trong 1 AZ" như C, thêm nữa dùng **private hosted zone + non-alias A record** — private hosted zone chỉ dùng cho DNS resolution **nội bộ VPC**, không phù hợp cho domain public mà end-user truy cập.
- **A:** Đề xuất host website **trực tiếp trên S3** — nhưng hệ thống đăng ký xe (car registration) là website **động** (NGINX + MySQL xử lý logic, tương tác dữ liệu) → **S3 chỉ host được static website**, không chạy được ứng dụng động → sai hoàn toàn về kiến trúc.

#### So sánh nhanh

| Lựa chọn | Route 53 record cho ELB | Đồng bộ DB | Vấn đề khác |
|---|---|---|---|
| **B (đúng)** | Alias A record | DMS (liên tục, ít downtime) | Không có |
| C (Anh chọn) | A record (không alias) | Import từ backup cũ | "Multi-AZ trong 1 AZ" tự mâu thuẫn |
| D | Non-alias A record, private hosted zone | Import từ backup cũ | "Multi-AZ trong 1 AZ"; hosted zone sai loại |
| A | Alias record | DMS + SCT | Host web động trên S3 — sai kiến trúc |

#### Lưu ý thực tế

- Quy tắc Route 53 record type cần nhớ: **EC2 → A record KHÔNG Alias**; **ELB / CloudFront / S3 → A record CÓ Alias**; **RDS → CNAME, KHÔNG Alias**.

#### Quy tắc nhớ cho thi

- **Thấy "Multi-AZ … trong 1 AZ" hoặc bất kỳ câu tự mâu thuẫn nội tại** → loại ngay đáp án đó, không cần xét tiếp các bước còn lại.
- **Trỏ domain vào ELB** → luôn là **Alias A record**, A record thường không hợp.
- **Website động (có DB, logic xử lý)** → không thể host trực tiếp trên S3 (S3 chỉ static).
- **"Import từ backup mới nhất" khi DB vẫn đang hoạt động** → kém hơn dùng **AWS DMS** để đồng bộ liên tục, vì backup tĩnh sẽ làm mất dữ liệu ghi thêm sau đó.

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

<a id="q29"></a>

## Q29

A company has several virtual machines on its on-premises data center hosting its three-tier web application. The company wants to migrate the application to AWS to take advantage of the benefits of cloud computing. The following are the company requirements for the migration process:
– The virtual machine images from the on-premises data center must be imported to AWS.
– The changes on the on-premises servers must be synchronized to the AWS servers until the production cutover is completed.
– Have minimal downtime during the production cutover.
– The root volumes and data volumes (containing Terabytes of data) of the VMs must be migrated to AWS.
– The migration solution must have minimal operational overhead.
Which of the following options is the recommended solution to meet the company requirements?

- **A.** Use AWS Transform MGN to migrate the virtual machines to AWS. Install the AWS Replication Agent on each server in the application tiers to continuously replicate the root volumes and data volumes to AWS. Launch test instances from the replicated servers, validate the application, and then perform a cutover to launch updated Amazon EC2 instances.
- **B.** Use AWS Transform discovery and assessment capabilities to group the on-premises virtual machines as an application. Then use VM Import/Export with an AWS CLI script to import the VMs as AMIs. Schedule recurring VM imports to capture changes until cutover, and launch Amazon EC2 instances from the most recent imported AMIs.
- **C.** Write an AWS CLI script that uses VM Import/Export to migrate the virtual machines. Schedule the script to run at regular intervals to synchronize the changes from the on-premises environment to AWS. Launch Amazon EC2 instances based on the images created from VM Import/Export. After successful testing, re-run the script to perform a final replication before the cutover. Launch new instances based on the updated AMIs.
- **D.** Use AWS Transform MGN to migrate only the root volumes of the virtual machines to AWS. Import the data volumes separately by using the AWS CLI import-snapshot command. Launch Amazon EC2 instances from the migrated root volumes and attach the imported data volumes. After testing, perform a final replication before cutover and attach the updated data volumes.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** import VMs; sync changes until cutover; minimal downtime; TBs of root + data volumes; minimal overhead

🪤 **Your trap:** Scheduled VM Import/Export scripts = high overhead and no continuous sync

🧠 **Rule:** Continuous block-level replication + short cutover → AWS MGN (Replication Agent, test launch, cutover).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises VMs (3-tier app)
   │
   ▼ migrate lên AWS
Yêu cầu:
  - Import VM image lên AWS
  - Đồng bộ thay đổi on-premises → AWS liên tục ĐẾN LÚC cutover
  - Downtime cutover TỐI THIỂU
  - Migrate cả root volume + data volume (hàng TB)
  - Ops overhead TỐI THIỂU
```

Đáp án đúng: **A** (AWS Transform MGN — Replication Agent, continuous replication, test launch, cutover). Anh chọn **C** (viết script CLI dùng VM Import/Export, chạy lặp lại theo lịch).

#### Vì sao A đúng

- **AWS Transform MGN** (dịch vụ rehosting, replicate liên tục — hậu duệ của AWS Application Migration Service) cài **Replication Agent trên từng server nguồn**, agent này **liên tục đồng bộ block-level** thay đổi từ on-premises vào staging area trên AWS → đúng yêu cầu "sync liên tục đến khi cutover".
- MGN replicate cả **root volume và data volume** cùng lúc trong một luồng thống nhất, không cần tách riêng.
- Có thể **launch test instance** trước để validate app 3-tier, sau đó **cutover** để launch EC2 instance thật — cutover window ngắn vì dữ liệu đã đồng bộ gần như real-time trước đó → "minimal downtime".
- Toàn bộ vòng đời (replication, test launch, cutover) quản lý qua **console của MGN**, không cần viết script tự động hóa thủ công → "minimal operational overhead".

#### Vì sao C (Anh chọn) trông hợp lý nhưng sai

C dùng ý tưởng "viết script tự chạy lặp lại để đồng bộ" — nghe có vẻ giải quyết được vấn đề "phải sync liên tục", nhưng vấn đề nằm ở chính công cụ nền: **VM Import/Export**.

- **VM Import/Export không hỗ trợ đồng bộ gia tăng (incremental sync).** Mỗi lần muốn cập nhật thay đổi từ on-premises, phải **import lại toàn bộ VM** thành AMI mới — với dữ liệu hàng **terabyte**, việc import lại toàn bộ nhiều lần rất tốn thời gian và tài nguyên.
- Đây chính là lý do C tăng **operational overhead cao** (phải tự viết, tự lên lịch, tự theo dõi script) và **không đạt "minimal downtime"** thực sự, vì mỗi vòng import lại là một quá trình nặng, không phải continuous block-level replication như MGN.
- Nói cách khác: C cố gắng "giả lập" continuous sync bằng cách lặp lại một tác vụ vốn được thiết kế cho import một lần (one-time), dẫn đến vừa chậm vừa tốn công vận hành.

#### Các lựa chọn sai khác

- **B (AWS Transform discovery/assessment + VM Import/Export CLI script, "schedule recurring VM imports"):** Discovery & assessment chỉ hỗ trợ **lập kế hoạch** (nhóm VM thành application để hiểu dependency), không thay thế được một managed migration service cho việc replicate liên tục. Phần còn lại vẫn dựa vào VM Import/Export chạy lặp lại theo lịch → cùng nhược điểm cơ bản như C: import lại toàn bộ mỗi lần, nặng nề với dữ liệu TB-scale.
- **D (MGN chỉ cho root volume + `import-snapshot` riêng cho data volume):** Tách rời việc replicate root volume (qua MGN) và data volume (qua import-snapshot CLI riêng biệt) làm tăng **độ phức tạp** và rủi ro **trạng thái không đồng nhất** giữa 2 volume (root và data không cùng "chốt" tại một thời điểm). Trong khi đó, **MGN vốn đã hỗ trợ replicate luôn cả root và data volume** trong cùng một luồng — tách riêng ra là dư thừa, không cần thiết.

#### So sánh nhanh

| Lựa chọn | Cơ chế đồng bộ | Root + Data volume | Ops overhead |
|---|---|---|---|
| **A (đúng)** | MGN — continuous block-level replication | Cùng một luồng | Thấp |
| C (Anh chọn) | VM Import/Export, lặp lại theo lịch | Phải import lại toàn bộ VM mỗi lần | Cao |
| B | Discovery/assessment + VM Import/Export lặp lại | Như C | Cao |
| D | MGN (root) + import-snapshot riêng (data) | Tách rời, thiếu đồng bộ | Trung bình–cao, phức tạp hơn cần thiết |

#### Quy tắc nhớ cho thi

- **"Đồng bộ liên tục thay đổi on-premises đến lúc cutover, downtime tối thiểu"** → luôn nghĩ tới **AWS Transform MGN (Replication Agent + continuous replication + test launch + cutover)**.
- **VM Import/Export = import một lần (one-time), không hỗ trợ incremental sync** → nếu đề cần đồng bộ liên tục hoặc dữ liệu lớn (TB-scale) thay đổi thường xuyên, VM Import/Export (kể cả chạy lặp lại bằng script) luôn là phương án kém hơn MGN.
- **MGN đã replicate được cả root volume và data volume trong cùng một agent** → tách riêng data volume ra xử lý bằng công cụ khác là thừa và tăng rủi ro.
- **"Discovery and assessment" trong AWS Transform** → chỉ là bước lập kế hoạch/nhóm ứng dụng, không phải là cơ chế migrate/replicate.

### TD explanation

AWS Transform MGN, formerly known as AWS Application Migration Service, is designed for lift-and-shift server migrations from physical, virtual, or cloud-based source servers to AWS. It continuously replicates source servers into the target AWS account, which helps reduce long cutover windows and supports migration with minimal downtime. This makes it suitable for moving existing virtual machines to Amazon EC2 without manually rebuilding the application stack.

For this scenario, AWS Transform MGN meets the requirement because it can replicate the on-premises virtual machines, including their root and supported data volumes, into AWS. The AWS Replication Agent is installed on each source server so changes from the on-premises environment are continuously synchronized to the AWS staging area until cutover. The company can launch test instances first, validate the three-tier application, and then launch cutover instances that reflect the most up-to-date state of the source servers.
This approach also has minimal operational overhead compared with manual VM import workflows. AWS Transform MGN manages ongoing replication, test launches, cutover launches, and migration lifecycle actions from the service console. It is primarily intended for rehosting workloads, so it is the recommended service when the goal is to migrate existing virtual machines to AWS with continuous block-level replication and a short cutover window.
Hence, the correct answer is: Use AWS Transform MGN to migrate the virtual machines to AWS. Install the AWS Replication Agent on each server in the application tiers to continuously replicate the root volumes and data volumes to AWS. Launch test instances from the replicated servers, validate the application, and then perform a cutover to launch updated Amazon EC2 instances.

The option that says: Write an AWS CLI script that uses VM Import/Export to migrate the virtual machines. Schedule the script to run at regular intervals to synchronize the changes from the on-premises environment to AWS. Launch Amazon EC2 instances based on the images created from VM Import/Export. After successful testing, re-run the script to perform a final replication before the cutover. Launch new instances based on the updated AMIs is incorrect. AWS VM Import/Export does not support synching incremental changes from the on-premises environment to AWS. You will need to import the VM again as a whole after you make changes to the on-premises environment. This requires a lot of time and adds more operational overhead.
The option that says: Use AWS Transform MGN to migrate only the root volumes of the virtual machines to AWS. Import the data volumes separately by using the AWS CLI import-snapshot command. Launch Amazon EC2 instances from the migrated root volumes and attach the imported data volumes. After testing, perform a final replication before cutover and attach the updated data volumes is incorrect. Separating root volume migration from data volume migration adds complexity and increases the risk of inconsistent server state. AWS Transform MGN can replicate supported block devices as part of the source server replication process, so importing data volumes separately is not necessary for this requirement.
The option that says: Use AWS Transform discovery and assessment capabilities to group the on-premises virtual machines as an application. Then use VM Import/Export with an AWS CLI script to import the VMs as AMIs. Schedule recurring VM imports to capture changes until cutover, and launch Amazon EC2 instances from the most recent imported AMIs  is incorrect because discovery and assessment can help with planning, but VM Import/Export does not replace a managed migration service for ongoing replication and low-downtime cutover. This option only creates a manual import cycle, which is just more operationally heavy and less suitable for synchronizing terabytes of changing data until production cutover.

References:
https://docs.aws.amazon.com/mgn/latest/ug/what-is-mgn.html
https://aws.amazon.com/application-migration-service/
https://docs.aws.amazon.com/mgn/latest/ug/launch-cutover.html
https://docs.aws.amazon.com/mgn/latest/ug/launching-target-servers.html

Check out this AWS Transform MGN Cheat Sheet:
https://tutorialsdojo.com/aws-application-migration-service/

</details>

<a id="q42"></a>

## Q42

A global retail corporation is modernizing its data infrastructure by migrating its on-premises Microsoft SQL Server data warehouse, which contains approximately 60 TB of historical sales and inventory data, to Amazon Redshift. The warehouse receives incremental updates on a daily basis, with comprehensive data refreshes occurring at the end of each month. The entire migration must be completed within a 30-day window before the next scheduled monthly refresh is applied to the Redshift database. To avoid disrupting day-to-day business operations, the company has limited the available bandwidth for migration activities to only 50 Mbps of Internet connectivity.
Which of the following solutions BEST satisfies all the migration requirements while remaining the most cost-effective?

- **A.** Reserve a slot at an AWS Data Transfer Terminal facility using the Data Transfer Terminal console. Use the AWS Schema Conversion Tool (SCT) to process the on-premises data warehouse schema and prepare the data for Redshift. Upload the bulk historical data directly at the Data Transfer Terminal facility into Amazon S3. Once the data is available in S3, use AWS SCT and AWS DMS tasks to migrate the data into Redshift. Configure ongoing replication tasks with DMS to capture daily incremental updates from the data warehouse. Monitor and verify that the migration is complete before the cutover.
- **B.** Create a new Oracle Database on Amazon RDS. Configure AWS Site-to-Site VPN connection from the on-premises data center to the Amazon VPC. Configure replication from the on-premises database to RDS. Once replication is complete, create an AWS Schema Conversion Tool (SCT) project with AWS DMS task to migrate the Oracle database to Redshift. Monitor and verify if the data migration is complete before the cutover.
- **C.** Since you have a 30-day window for migration, configure VPN connectivity between AWS and the company's data center by provisioning a 1 Gbps AWS Direct Connect connection. Launch an Oracle Real Application Clusters (RAC) database on an Amazon EC2 instance and set it up to fetch and synchronize the data from the on-premises Oracle database. Once replication is complete, create an AWS DMS task on an AWS SCT project to migrate the Oracle database to Redshift. Monitor and verify if the data migration is complete before the cutover.
- **D.** Reserve a slot at an AWS Data Transfer Terminal facility using the Data Transfer Terminal console. Export all data from the on‑premises SQL Server data warehouse to local storage equipment and bring it to the facility for upload. Once the data is ingested into an Amazon S3 bucket, create an Oracle Amazon RDS instance to import the data. Create an AWS Schema Conversion Tool (SCT) project with AWS DMS task to migrate the Oracle database to Redshift. Copy the missing daily updates from Oracle in the data center to the RDS for Oracle database over the Internet. Monitor and verify if the data migration is complete before the cutover.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** DW → Redshift; 30-day window; only 50 Mbps; daily increments; cost-effective

🪤 **Your trap:** Pointless Oracle RDS hop + copying daily updates over the internet

🧠 **Rule:** Bulk offline load (Data Transfer Terminal/Snowball) + SCT for schema + DMS ongoing replication (CDC) for the increments.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises SQL Server DW (~60 TB)
        │
        ▼ migrate sang Amazon Redshift
Ràng buộc:
  - Cửa sổ migrate: 30 ngày (trước lần refresh cuối tháng kế tiếp)
  - Bandwidth Internet chỉ 50 Mbps
  - Có incremental update HÀNG NGÀY cần bắt kịp
Hỏi: giải pháp tốt nhất + cost-effective nhất
```

Đáp án đúng: **A** (Data Transfer Terminal để chuyển bulk data offline + SCT cho schema + DMS cho replication liên tục bắt incremental). Anh chọn **D** (Data Transfer Terminal + Oracle RDS trung gian + copy update qua Internet).

#### Vì sao A đúng

- **Ước lượng băng thông:** 60 TB qua 50 Mbps sẽ tốn rất nhiều ngày (vượt xa ngân sách thời gian trong cửa sổ 30 ngày, và không được vì công ty giới hạn bandwidth để không ảnh hưởng vận hành) → **bulk historical data không nên đi qua Internet** — đây là lý do dùng **AWS Data Transfer Terminal**: mang thiết bị lưu trữ vật lý đến facility, upload trực tiếp bằng kết nối tốc độ cao tại đó vào S3.
- **AWS SCT (Schema Conversion Tool)** xử lý schema của SQL Server DW, chuyển đổi cho tương thích Redshift — bước bắt buộc vì khác database engine (SQL Server → Redshift).
- Sau khi bulk data đã có trong S3 → dùng **SCT + AWS DMS task** để nạp dữ liệu vào Redshift.
- Quan trọng: **cấu hình DMS ongoing replication (CDC)** để bắt các **incremental update hàng ngày** phát sinh trong lúc bulk data đang được xử lý/nạp — đảm bảo dữ liệu không bị "hụt" giữa lúc snapshot ban đầu và lúc cutover thật.
- Không có bước trung gian dư thừa (không cần Oracle DB nào cả) → đây là con đường **ngắn nhất, ít thành phần nhất, tận dụng đúng combo SCT+DMS cho data warehouse migration** → cost-effective nhất trong 4 lựa chọn.

#### Vì sao D (Anh chọn) trông hợp lý nhưng sai

D cũng dùng đúng **Data Transfer Terminal** để giải quyết bài toán bandwidth cho phần bulk data — điểm này giống A. Nhưng D có 2 lỗi lớn:

1. **Thêm một Oracle RDS instance làm trung gian không cần thiết**: dữ liệu ingest vào S3 rồi lại phải "import vào Oracle RDS", sau đó mới SCT+DMS từ Oracle sang Redshift. Đây là một **hop dư thừa** — vì nguồn là **SQL Server**, không phải Oracle, việc tạo một Oracle RDS giữa đường không có lý do kỹ thuật rõ ràng, chỉ làm tăng chi phí (thêm RDS instance phải chạy, phải trả tiền) và độ phức tạp mà không giải quyết vấn đề gì thêm.
2. **"Copy the missing daily updates … over the Internet"**: đúng là cần bắt kịp incremental update, nhưng D làm bằng cách copy dữ liệu **thủ công qua Internet** (không phải CDC/replication tự động) — điều này lại đưa traffic incremental trở lại **giới hạn 50 Mbps** đã được quy định để tránh ảnh hưởng vận hành hàng ngày, và không có cơ chế đảm bảo đồng bộ liên tục như DMS ongoing replication task.

Ngoài ra, kỹ thuật: theo TD explanation, quy trình chuẩn khi dùng SCT + Data Transfer Terminal là phải **cấu hình data extraction agent trên server nguồn trước** — D bỏ qua bước này khi chuyển hướng qua Oracle RDS.

#### Các lựa chọn sai khác

- **B (Oracle RDS + Site-to-Site VPN + replication qua Internet):** Replicate 60 TB qua Internet (VPN vẫn đi qua Internet, chỉ mã hóa) với hạn chế 50 Mbps → mất nhiều ngày, có thể vượt cửa sổ 30 ngày, và có thể ảnh hưởng đến vận hành hàng ngày của công ty (đúng điều công ty muốn tránh khi giới hạn bandwidth).
- **C (Direct Connect 1 Gbps + Oracle RAC trên EC2):** Có thể đáp ứng yêu cầu tốc độ (1 Gbps giải quyết vấn đề bandwidth), nhưng **Direct Connect là hạ tầng kết nối dài hạn, đầu tư lớn — không cost-effective cho một lần migrate duy nhất**. Đề đã nhấn "remaining the most cost-effective" nên đây bị loại vì chi phí, dù kỹ thuật khả thi.

#### So sánh nhanh

| Lựa chọn | Bulk data (60TB) | Incremental update | Chi phí |
|---|---|---|---|
| **A (đúng)** | Data Transfer Terminal (offline) | DMS ongoing replication (CDC) | Thấp, không hop dư |
| D (Anh chọn) | Data Transfer Terminal (offline) | Copy tay qua Internet (50 Mbps) | Cao hơn (Oracle RDS dư + rủi ro băng thông) |
| B | Qua Internet/VPN (50 Mbps) | Replication liên tục | Chậm, rủi ro vượt 30 ngày |
| C | Direct Connect 1 Gbps | Oracle RAC sync | Cao (đầu tư Direct Connect cho 1 lần dùng) |

#### Quy tắc nhớ cho thi

- **"Dữ liệu rất lớn (TB) + bandwidth hạn chế + cửa sổ thời gian ngắn"** → nghĩ đến giải pháp **offline transfer** (Data Transfer Terminal, hoặc AWS Snowball trong các đề khác), không đi qua Internet cho phần bulk.
- **"Có incremental update cần bắt kịp sau khi bulk data đã chuyển"** → dùng **AWS DMS ongoing replication (CDC)**, không phải copy tay qua Internet.
- **Không cần database trung gian (như Oracle RDS) nếu SCT + DMS đã hỗ trợ trực tiếp source engine → target engine** — thêm hop trung gian không có lý do kỹ thuật là dấu hiệu đáp án gây nhiễu.
- **Direct Connect** phù hợp cho kết nối **dài hạn**, không cost-effective cho **migrate một lần**.

#### 📝 Ghi chú kỹ thuật

**AWS Data Transfer Terminal** là dịch vụ có thật (ra mắt cuối 2024): anh mang thiết bị lưu trữ của mình đến một địa điểm vật lý của AWS và upload thẳng lên S3 qua đường mạng tốc độ cao. Khác Snowball ở chỗ AWS không gửi thiết bị cho anh. Trong đề, vai trò của nó giống Snowball: chuyển khối dữ liệu lịch sử lớn khi băng thông chỉ có 50 Mbps. Phần còn lại (SCT + DMS + CDC) là mẫu migration data warehouse → Redshift quen thuộc.

### TD explanation

You can use the AWS Schema Conversion Tool (AWS SCT) to convert your existing database schema from one database engine to another. This tool allows you to convert both relational OLTP schemas and data warehouse schemas. The converted schema is compatible with various services, including Amazon Relational Database Service (Amazon RDS) for MySQL, MariaDB, Oracle, SQL Server, and PostgreSQL, as well as Amazon Aurora DB clusters and Amazon Redshift clusters. Additionally, the converted schema can be used with a database on an Amazon EC2 instance or stored as data in an Amazon S3 bucket.

Large-scale data migrations can include many terabytes of information and can be slowed by network performance and by the sheer amount of data that has to be moved. The AWS Data Transfer Terminal is a network-ready physical location where you can bring your data storage devices for fast data transfer to and from your AWS Cloud services. This facility simplifies the process of uploading remotely captured data, making it more accessible.
To use the Data Transfer Terminal, schedule a reservation at one of the physical facilities through the AWS Management Console. Arrive at your scheduled time and upload your data to your AWS Cloud services using your own devices. Once your scheduled reservation is complete and you leave, the facility is secured and prepared for the next reservation.
When you use AWS SCT and an AWS Data Transfer Terminal, you migrate your data in two stages. First, you use the AWS SCT to process the data locally and then move that data to your storage device. You then send the device to the AWS Data Transfer Terminal facility and then upload the data into an Amazon S3 bucket. Next, when the data is available on Amazon S3, you use AWS SCT to migrate the data to Amazon Redshift. Data extraction agents can work in the background while AWS SCT is closed. You manage your extraction agents by using AWS SCT. The extraction agents act as listeners. When they receive instructions from AWS SCT, they extract data from your data warehouse.
Therefore, the correct answer is: Reserve a slot at an AWS Data Transfer Terminal facility using the Data Transfer Terminal console. Use the AWS Schema Conversion Tool (SCT) to process the on-premises data warehouse schema and prepare the data for Redshift. Upload the bulk historical data directly at the Data Transfer Terminal facility into Amazon S3. Once the data is available in S3, use AWS SCT and AWS DMS tasks to migrate the data into Redshift. Configure ongoing replication tasks with DMS to capture daily incremental updates from the data warehouse. Monitor and verify that the migration is complete before the cutover. It avoids the bandwidth bottleneck by using the Data Transfer Terminal facility, directly targets Redshift without unnecessary Oracle intermediaries, and leverages SCT and DMS for schema conversion and ongoing replication. This solution is both time‑efficient and cost‑effective while meeting all migration requirements.
The option that says: Create a new Oracle Database on Amazon RDS. Configure AWS Site-to-Site VPN connection from the on-premises data center to the Amazon VPC. Configure replication from the on-premises database to RDS. Once replication is complete, create an AWS Schema Conversion Tool (SCT) project with AWS DMS task to migrate the Oracle database to Redshift. Monitor and verify if the data migration is complete before the cutover is incorrect. Replicating 60 TB worth of data over the public Internet will take several days over the 30-day migration window. It is also stated in the scenario that the company can only allocate 50 Mbps of Internet connection for the migration activity. Sending the data over the Internet could potentially affect business operations.
The option that says: Reserve a slot at an AWS Data Transfer Terminal facility using the Data Transfer Terminal console. Export all data from the on‑premises SQL Server data warehouse to local storage equipment and bring it to the facility for upload. Once the data is ingested into an Amazon S3 bucket, create an Oracle Amazon RDS instance to import the data. Create an AWS Schema Conversion Tool (SCT) project with AWS DMS task to migrate the Oracle database to Redshift. Copy the missing daily updates from Oracle in the data center to the RDS for Oracle database over the Internet. Monitor and verify if the data migration is complete before the cutover is incorrect because you typically need to configure the data extraction agent first on your on-premises server. In addition, you don’t need the data to be imported and exported via Amazon RDS. AWS DMS can directly migrate the data to Amazon Redshift.
The option that says: Since you have a 30-day window for migration, configure VPN connectivity between AWS and the company’s data center by provisioning a 1 Gbps AWS Direct Connect connection. Launch an Oracle Real Application Clusters (RAC) database on an Amazon EC2 instance and set it up to fetch and synchronize the data from the on-premises Oracle database. Once replication is complete, create an AWS DMS task on an AWS SCT project to migrate the Oracle database to Redshift. Monitor and verify if the data migration is complete before the cutover is incorrect. Although this is possible, the company wants to keep the cost low. Using a Direct Connect connection for a one-time migration is not a cost-effective solution.

References:
https://aws.amazon.com/getting-started/hands-on/migrate-oracle-to-amazon-redshift/
https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/agents.dw.html
https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/agents.html

Check out this AWS Database Migration Service Cheat Sheet:
https://tutorialsdojo.com/aws-database-migration-service/

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>
