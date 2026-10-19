# TD Set 2 — Timed retake (2026-10-16) — Wrong Answer Review (8 questions + 5 unsure-right)

Source: `td2_retake_export.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td2_retake_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q42](#q42) | ✅ 10-19 | ☐ | ☐ |
| A | [Q26](#q26) | ✅ 10-19 | ☐ | ☐ |
| B | [Q17](#q17) | ✅ 10-19 | ☐ | ☐ |
| B | [Q58](#q58) | ✅ 10-19 | ☐ | ☐ |
| C | [Q15](#q15) | ✅ 10-19 | ☐ | ☐ |
| C | [Q45](#q45) | ✅ 10-19 | ☐ | ☐ |
| C | [Q53](#q53) | ✅ 10-19 | ☐ | ☐ |
| C | [Q62](#q62) | ✅ 10-19 | ☐ | ☐ |
| D | [Q13](#q13) | ✅ 10-19 | ☐ | ☐ |
| D | [Q34](#q34) | ✅ 10-19 | ☐ | ☐ |
| D | [Q39](#q39) | ✅ 10-19 | ☐ | ☐ |
| D | [Q68](#q68) | ✅ 10-19 | ☐ | ☐ |
| D | [Q72](#q72) | ✅ 10-19 | ☐ | ☐ |

---

# Group A — Identity & directory (AD trust, IAM role vs SCP) (2)

<a id="q42"></a>

## Q42

A company is using Microsoft Active Directory to manage all employee accounts and devices. The IT department instructed the solutions architect to implement a single sign-on feature to allow the employees to use their existing Windows account password to connect and use the various AWS resources.



Which of the following options is the recommended way to extend the current Active Directory domain to AWS?

- **A.** Use AWS Directory Service to integrate your AWS resources with the existing Active Directory using trust relationship. Enable single sign-on using Managed Microsoft AD.
- **B.** Create users and groups with AWS IAM Identity Center along with AWS Organizations to help you manage SSO access and user permissions across all the AWS accounts.
- **C.** Use Amazon Cognito to authorize users to your applications using direct sign-in or through third-party apps, and access your apps' backend resources in AWS.
- **D.** Use IAM Roles to set up cross-account access and delegate access to resources that are in your AWS account.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** existing Microsoft AD, employees use their Windows password for AWS SSO

🪤 **Your trap:** Creating users in IAM Identity Center ignores the existing AD — Identity Center still needs Directory Service to reach Microsoft AD

🧠 **Rule:** Existing on-prem Microsoft AD → AWS Directory Service (Managed Microsoft AD + trust) → SSO; don't recreate users.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises                              AWS
┌──────────────────────┐   trust    ┌──────────────────────────┐
│ Microsoft AD         │ ◄────────► │ AWS Managed Microsoft AD │
│ (user + Windows pwd) │            │ (AWS Directory Service)  │
└──────────────────────┘            └──────────────────────────┘
                                         │ SSO
                                         ▼
                              AWS Management Console / CLI
                              + workload Windows
```

Yêu cầu chốt: **đã có Microsoft AD**, nhân viên dùng **chính password Windows** để SSO vào AWS, và hỏi cách **extend** AD domain hiện có sang AWS. Đáp án đúng: **A**. Anh chọn B (tạo user/group trong IAM Identity Center).

#### Vì sao A đúng

**AWS Directory Service for Microsoft AD** (Managed Microsoft AD) thiết lập **trust relationship** giữa AD on-premises và AWS Managed Microsoft AD. Nhờ trust, xác thực được kéo từ on-premises lên cloud: user vẫn nằm trong AD cũ, vẫn dùng password Windows cũ, và có SSO vào AWS Management Console, AWS CLI, cùng các workload Windows trên AWS.

Keyword "existing Microsoft AD" + "extend" → **Directory Service + trust**, không tạo lại danh tính.

#### Vì sao B (anh chọn) sai

B nghe rất hợp lý vì IAM Identity Center + Organizations đúng là cách quản lý SSO nhiều account. Nhưng lỗi nằm ở chữ **"Create users and groups"**:

- Tạo user/group mới trong Identity Center nghĩa là **tạo một danh sách người dùng thứ hai**, bỏ qua AD hiện có; nhân viên không dùng được password Windows sẵn có theo cách đề yêu cầu.
- TD giải thích: Identity Center một mình là **chưa đủ**; muốn tích hợp Microsoft AD vẫn phải qua **AWS Directory Service**. Identity Center tích hợp với Microsoft AD thông qua Directory Service nên **không cần tạo lại user và group**.

```
Sai (B):   Identity Center ── user/group tạo mới   (AD cũ bị bỏ qua)
Đúng (A):  AD cũ ──trust── Managed Microsoft AD ──► SSO
```

Nói cách khác: Identity Center là lớp "phân quyền SSO nhiều account", còn nguồn danh tính phải đến từ Directory Service khi công ty đã có AD.

#### Các đáp án sai còn lại

- **C (Amazon Cognito):** dùng cho federation/đăng nhập vào **web và mobile app** (kể cả social identity provider), không phải để extend AD sang AWS cho nhân viên. Công ty đã có Microsoft AD nên Directory Service là lựa chọn phù hợp hơn.
- **D (IAM Roles cross-account):** chỉ cho phép chia sẻ truy cập resource giữa các AWS account, không liên quan đến việc mở rộng AD domain hay dùng Windows password.

| Đáp án | Giải quyết việc gì | Dùng AD sẵn có? |
|---|---|---|
| **A. Directory Service + trust** | Extend AD sang AWS, SSO | Có |
| B. Identity Center tạo user mới | SSO nhiều account | Không (tạo user mới) |
| C. Cognito | Đăng nhập vào app | Không |
| D. IAM cross-account role | Truy cập chéo account | Không |

#### Quy tắc nhớ cho thi

- **Thấy "existing / on-premises Microsoft AD" + SSO bằng password Windows** → **AWS Directory Service (Managed Microsoft AD) + trust**
- **Thấy "Create users and groups" trong Identity Center khi đề đã có AD** → bẫy, **đừng tạo lại user**
- **Thấy Cognito** → app web/mobile, không phải nhân viên vào AWS console
- **Thấy IAM cross-account role** → chia sẻ giữa account, không phải bài toán directory

### TD explanation

Incorrect  

Because the company is using Microsoft Active Directory already, you can use **AWS Directory Service for Microsoft AD**  to create secure Windows trusts between your on-premises Microsoft Active Directory domains and your AWS Microsoft AD domain in the AWS Cloud. By setting up a trust relationship, you can integrate SSO to the AWS Management Console and the AWS Command Line Interface (CLI), as well as your Windows-based workloads.

 

![image](https://media.tutorialsdojo.com/sap_aws_directory_service.png)

 

**AWS Directory Service**  helps you to set up and run a standalone AWS Managed Microsoft AD directory hosted in the AWS Cloud. You can also use AWS Directory Service to connect your AWS resources with an existing on-premises Microsoft Active Directory. To configure AWS Directory Service to work with your on-premises Active Directory, you must first set up trust relationships to extend authentication from on-premises to the cloud.

 

Therefore, the correct answer is: **Use AWS Directory Service to integrate your AWS resources with the existing Active Directory using trust relationship. Enable single sign-on using Managed Microsoft AD.**

 

The option that says: **Use Amazon Cognito to authorize users to your applications using direct sign-in or through third-party apps, and access your apps’ backend resources in AWS**  is incorrect because Cognito is primarily used for federation to your web and mobile apps running on AWS. It allows you to authenticate users through social identity providers. But since the company is already using Microsoft AD, AWS Directory Service is the better choice here.

 

The option that says: **Create users and groups with AWS IAM Identity Center along with AWS Organizations to help you manage SSO access and user permissions across all the AWS accounts**  is incorrect because using the AWS IAM Identity Center service alone is not enough to meet the requirement. Although it can help you manage SSO access and user permissions across all your AWS accounts in AWS Organizations, you still have to use the AWS Directory Service to integrate your on-premises Microsoft AD. AWS IAM Identity Center integrates with Microsoft AD using AWS Directory Service so there is no need to create users and groups.

 

The option that says: **Use IAM Roles to set up cross-account access and delegate access to resources that are in your AWS account**  is incorrect because setting up cross-account access allows you to share resources in one AWS account with users in a different AWS account. Since the company is already using Microsoft AD then, the better choice to use here is the AWS Directory Service.

 

 

**References:**

 

[https://aws.amazon.com/directoryservice/](https://aws.amazon.com/directoryservice/ )

 

[https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-directory-connected.html](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-directory-connected.html)

 

 

**Check out this AWS Directory Service Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-directory-service/](https://tutorialsdojo.com/aws-directory-service/)

</details>

<a id="q26"></a>

## Q26

A company has several resources in its production environment that is shared among various business units of the company. A single business unit may have one or more AWS accounts that have resources in the production environment. There were a lot of incidents in which the developers from a specific business unit accidentally terminated the Amazon EC2 instances, Amazon EKS clusters, and Amazon Aurora Serverless databases which are owned by another business unit. The solutions architect has been tasked to come up with a solution to only allow a specific business unit that owns the EC2 instances, and other AWS resources, to terminate their own resources.



Which of the following is the most suitable multi-account strategy implementation to meet the company requirements?

- **A.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to individual Organization Units (OU). Create an IAM Role in the production account, which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the IAM policy to every member account of the OU.
- **B.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the SCP to the OUs, which will then be automatically inherited by its member accounts.
- **C.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns. Provide the cross-account access and the SCP to the individual member accounts to tightly control who can terminate the EC2 instances.
- **D.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create an IAM Role in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns. Create an `AWSServiceRoleForOrganizations` service-linked role for the individual member accounts of the OU to enable **trusted access** .

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** business units share a production account; developers terminate other units' resources

🪤 **Your trap:** 🔁 An SCP never grants access — the fix is an IAM role with resource-level (tag) permissions in the production account

🧠 **Rule:** Grant scoped access → IAM role in the target account + resource-level/tag conditions; SCPs only restrict.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations
 ├─ OU Business Unit 1 ── nhiều account ──┐
 ├─ OU Business Unit 2 ── nhiều account ──┼──► Production account
 └─ OU Business Unit 3 ── nhiều account ──┘     (EC2, EKS, Aurora Serverless dùng chung)

Sự cố: dev của BU này vô tình terminate resource của BU khác
Yêu cầu: chỉ BU SỞ HỮU mới được terminate resource của mình
```

Đáp án đúng: **A**. Anh chọn **B** (dùng SCP).

⚠️ **Lỗi lặp lại:** Đây là lần thứ hai anh sai đúng khái niệm này (cũng sai ở lần làm TD2 đầu tiên). Gốc lỗi: **SCP không bao giờ cấp quyền**, nó chỉ đặt trần (guardrail).

#### Vì sao A đúng

A dùng **IAM Role trong production account** với policy có **resource-level permission** để chỉ cho terminate resource do BU đó sở hữu, rồi cấp **cross-account access** cho các member account trong OU.

- Organizations + OU: gom account theo BU để quản lý.
- **IAM role + resource-level permission:** đây mới là thứ thực sự **cấp** quyền, và giới hạn theo từng resource. EC2 hỗ trợ resource-level permission (một phần): có thể điều kiện hóa action theo resource cụ thể được phép dùng.
- Cross-account access: member account của BU assume role trong production account.

#### Vì sao B (anh chọn) sai

B và C đều dùng **Service Control Policy** để "allow" resource-level terminate. Sai ở bản chất SCP:

- SCP đặt **quyền tối đa** (maximum available permissions) cho account trong OU, nhưng **không cấp quyền nào**. TD: "SCPs are similar to IAM permission policies except that they don't grant any permissions."
- Gắn SCP chỉ tạo guardrail. Vẫn phải có **identity-based hoặc resource-based policy** thì principal mới thực sự làm được gì.
- Thêm nữa, "tạo SCP trong production account" cũng lệch: SCP được quản lý ở Organizations và gắn vào root/OU/account, không phải một policy cấp quyền nằm trong production account.

```
SCP        = trần (cho phép TỐI ĐA những gì)   ── không cấp quyền
IAM policy = cấp quyền thật, theo resource      ── chịu giới hạn bởi trần SCP
Quyền hiệu lực = giao của hai bên
```

TD còn lưu ý: SCP chỉ allow/deny cả service, mà ta không muốn chặn hẳn BU dùng EC2, nên cần IAM policy mới tinh chỉnh được theo resource.

#### Các đáp án sai còn lại

- **C:** cũng là SCP (mỗi BU một SCP) để "allow" terminate resource của mình, sai cùng lý do: SCP không cấp quyền.
- **D:** có IAM role đúng hướng, nhưng phần cuối tạo service-linked role `AWSServiceRoleForOrganizations` để bật **trusted access** là sai mục đích. Role này chỉ cho phép Organizations tạo service-linked role cho các dịch vụ AWS khác, có sẵn ở mọi organization, không liên quan việc giới hạn terminate theo BU.

| Đáp án | Cơ chế | Vì sao đạt / trượt |
|---|---|---|
| **A** | IAM role + resource-level permission + cross-account | Cấp quyền thật, theo từng resource |
| B | SCP gắn cho OU | SCP không cấp quyền |
| C | SCP cho từng BU | SCP không cấp quyền |
| D | IAM role + AWSServiceRoleForOrganizations | Role cuối không giải quyết yêu cầu |

#### Quy tắc nhớ cho thi

- **Thấy "SCP" + "allow / grant / cho phép"** → **sai ngay**. SCP chỉ **giới hạn**, không **cấp**.
- **Cần cấp quyền hẹp theo resource / tag** → **IAM role (identity policy) + resource-level permission / condition**, ở account chứa resource
- **Cần chặn cứng toàn OU** (ví dụ cấm region, cấm service) → mới là chỗ dùng **SCP**
- Mnemonic: **"SCP = hàng rào, IAM = chìa khóa"**: có hàng rào mà không có chìa thì không ai vào được.

### TD explanation

Incorrect  

**AWS Organizations**  is an account management service that enables you to consolidate multiple AWS accounts into an *organization*  that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.

 

![image](https://media.tutorialsdojo.com/sap_scp_organization.jpg)

 

You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.

 

Resource-level permissions refer to the ability to specify which resources users are allowed to perform actions on. Amazon EC2 has partial support for resource-level permissions. This means that for certain Amazon EC2 actions, you can control when users are allowed to use those actions based on conditions that have to be fulfilled, or specific resources that users are allowed to use. For example, you can grant users permissions to launch instances, but only of a specific type, and only using a specific AMI.

 

The scenario on this question has a lot of AWS Accounts that need to be managed. AWS Organization solves this problem and provides you with control by assigning the different business units as individual Organization Units (OU). Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. However, SCPs alone are not sufficient for allowing access to the accounts in your organization. Attaching an SCP to an AWS Organizations entity just defines a guardrail for what actions the principals can perform. You still need to attach identity-based or resource-based policies to principals or resources in your organization’s accounts to actually grant permission to them.

 

Since SCPs only allow or deny the use of an AWS service, you don’t want to block OUs from completely using the EC2 service. Thus, you will need to provide cross-account access and the IAM policy to every member accounts of the OU.

 

Hence, the correct answer is: **Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to individual Organization Units (OU). Create an IAM Role in the production account, which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the IAM policy to every member account of the OU.**

 

The option that says: **Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create an IAM Role in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns.** **Create an `AWSServiceRoleForOrganizations` service-linked role for the individual member accounts of the OU to enable` trusted access`**  is incorrect because **AWSServiceRoleForOrganizations**  service-linked role is primarily used to only allow AWS Organizations to create service-linked roles for other AWS services. This service-linked role is present in all organizations and not just in a specific OU.

 

The following options are incorrect because an SCP policy simply specifies the services and actions that users and roles can use in the accounts:

 

**–** **Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns.** **Provide the cross-account access and the SCP to the individual member accounts to tightly control who can terminate the EC2 instances.**

 

**–** **Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit.** **Provide the cross-account access and the SCP to the OUs, which will then be automatically inherited by its member accounts.**

 

SCPs are similar to IAM permission policies except that they don’t grant any permissions.

 

 

**References:**

 

[https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html)

 

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html)

 

[https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)

 

 

**Check out these AWS Organizations and** **Comparison of AWS Services Cheat Sheets:**

 

[https://tutorialsdojo.com/aws-organizations/](https://tutorialsdojo.com/aws-organizations/)

 

[https://tutorialsdojo.com/comparison-of-aws-services/](https://tutorialsdojo.com/comparison-of-aws-services/)

 

 

**Service Control Policies (SCP) vs IAM Policies:**

 

[https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/](https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/)

</details>

---

# Group B — DNS & edge protection (Resolver endpoints, OAC + custom header on ALB) (2)

<a id="q17"></a>

## Q17

A company is using AWS Managed Active Directory Service to host the company AD in the AWS Cloud with a custom AD domain name private.tutorialsdojo.com. A pair of domain controllers are launched with the default configuration inside the VPC. A VPC interface endpoint was also created for the Amazon Kinesis using AWS Private Link to allow instances to connect to Kinesis service endpoints from inside the VPC. The solutions architect launched several EC2 instances in the VPC, however, the instances were not able to resolve the company’s custom AD domain name.



Which of the following steps should the Solutions Architect implement to allow the instances to resolve both AWS VPC endpoints and the AWS Managed Microsoft AD domain’s FQDN? (Select TWO.)

- **A.** Create a forwarding rule inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers.
- **B.** Create an inbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC.
- **C.** Reconfigure the DNS service on every client on the VPC to split DNS queries. Use the Active Directory servers for the custom AD domain and the VPC resolver for all other DNS queries.
- **D.** Create an outbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC.
- **E.** Create a conditional forwarder inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** A, B

🔑 **Key words:** VPC must resolve both AWS endpoints and the custom AD domain (Managed Microsoft AD)

🪤 **Your trap:** Inbound endpoint is for on-prem/other networks → VPC; resolving a custom domain FROM the VPC needs an outbound endpoint

🧠 **Rule:** Route 53 Resolver: queries leaving the VPC → OUTBOUND endpoint + forwarding rule to the domain controllers; inbound = into the VPC.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC
┌───────────────────────────────────────────────┐
│ EC2 instances ──► AmazonProvidedDNS (Resolver)│
│                       │                       │
│          ┌────────────┴─────────────┐         │
│          ▼                          ▼         │
│  tên nội bộ VPC /            private.tutorialsdojo.com
│  VPC interface endpoint      (domain của Managed Microsoft AD)
│  (Resolver tự trả lời)       ──► Resolver KHÔNG biết ──► cần forward
└───────────────────────────────────────────────┘
                                     │  forward ra ngoài VPC
                                     ▼
                         2 domain controller (AD DNS)
```

Yêu cầu: instance phải resolve được **cả** VPC endpoint **và** FQDN của AWS Managed Microsoft AD. Đáp án đúng: **A + D** (forwarding rule + outbound endpoint). Anh chọn A (đúng) + B (inbound endpoint, sai).

#### A + D hợp thành MỘT giải pháp

Route 53 Resolver tự trả lời tên nội bộ VPC và private hosted zone, còn domain khác thì hỏi public DNS. Domain AD tùy chỉnh nên Resolver không biết. Cách xử lý:

```
EC2 ─► AmazonProvidedDNS ─► Resolver rule khớp private.tutorialsdojo.com
                                 │ (forwarding rule, nằm trên OUTBOUND endpoint)
                                 ▼
                          IP của 2 domain controller ─► trả lời
```

- **D. Outbound endpoint:** là các ENI trong VPC, dùng để **đẩy query ra ngoài** tới DNS resolver khác. Phần "Set AmazonProvidedDNS làm DNS resolver cho VPC" giữ cho instance vẫn hỏi Resolver, nên tên VPC endpoint vẫn resolve bình thường.
- **A. Forwarding rule:** nêu rõ domain `private.tutorialsdojo.com` và IP của 2 domain controller. Rule được host trên outbound endpoint; nhiều rule khớp thì chọn rule **cụ thể nhất**.

Có outbound endpoint + forwarding rule, mọi resource trong VPC hỏi AmazonProvidedDNS sẽ resolve được cả domain AD lẫn resource AWS trong VPC (kể cả interface VPC endpoint).

#### Vì sao B (anh chọn) sai

B nhìn giống D chỉ khác một chữ, và vế "Set AmazonProvidedDNS" y hệt. Nhưng hướng của endpoint ngược:

```
INBOUND  : mạng ngoài (on-prem / corporate) ──► hỏi tên trong VPC
OUTBOUND : resource trong VPC ──► hỏi tên ở mạng ngoài (qua forwarding rule)
```

Bài này query xuất phát **từ trong VPC** đi hỏi DNS của AD, nên cần **outbound**. TD: inbound dùng để resolve tài nguyên AWS cho mạng bên ngoài; bài này cần outbound.

#### Các đáp án sai còn lại

- **C:** tự cấu hình split DNS trên từng client rất tốn công quản lý. Cách đúng chỉ cần dùng Resolver với forwarding, request sẽ được chuyển hợp lý.
- **E:** "conditional forwarder" được cấu hình **bên trong AD server**, không phải trên Route 53 Resolver endpoint. Trên Resolver, khái niệm tương đương là **forwarding rule** (đó là chỗ A khác E).

| Thành phần | Hướng | Dùng khi |
|---|---|---|
| Inbound endpoint | Ngoài ➜ VPC | On-prem cần resolve tên trong VPC |
| **Outbound endpoint + rule** | VPC ➜ ngoài | VPC cần resolve domain ở DNS khác (AD) |
| Conditional forwarder | Trong AD server | Cấu hình phía AD, không phải Resolver |

#### Quy tắc nhớ cho thi

- **Thấy "VPC resolve custom / AD / on-prem domain"** → **OUTBOUND endpoint + forwarding rule** trỏ tới IP DNS server đó
- **Thấy "on-prem resolve tên trong VPC"** → **INBOUND endpoint**
- Mnemonic: **"Outbound = Out of VPC"**: query đi ra khỏi VPC thì dùng outbound.
- **"Forwarding rule"** là từ của Route 53 Resolver; **"conditional forwarder"** là từ của AD/Windows DNS

### TD explanation

Incorrect  

When you create a VPC using Amazon VPC, **Route 53 Resolver**  automatically answers DNS queries for local VPC domain names for EC2 instances (ec2-192-0-2-44.compute-1.amazonaws.com) and records in private hosted zones (private.tutorialsdojo.com). For all other domain names, Resolver performs recursive lookups against public name servers.

 

You also can integrate DNS resolution between Resolver and DNS resolvers on your network by configuring forwarding rules. Your network can include any network that is reachable from your VPC, such as the following:

 

- The VPC itself
- Another peered VPC
- An on-premises network that is connected to AWS with AWS Direct Connect, a VPN, or a network address translation (NAT) gateway.

 

A Route 53 Resolver Endpoint is a customer-managed resolver consisting of one or more Elastic Network Interfaces (ENIs) deployed on your VPC. Resolver Endpoints are classified into two types:

 

- **Inbound Endpoint –**  provides DNS resolution of AWS resources, such as EC2 instances, for your corporate network.
- **Outbound Endpoint**  – provides resolution of specific DNS names that you configure using forwarding rules to your VPC.

 

Outbound Resolver Endpoints host Forwarding Rules that forward queries for specified domain names to specific IP addresses. You create forwarding rules when you want to forward DNS queries for specified domain names to DNS resolvers on your network.

 

To forward selected queries, you create Resolver rules that specify the domain names for the DNS queries that you want to forward (such as example.com), and the IP addresses of the DNS resolvers on your network that you want to forward the queries to. If a query matches multiple rules (tutorialsdojo.com, portal.tutorialsdojo.com), the Resolver chooses the rule with the most specific match (portal.tutorialsdojo.com) and forwards the query to the IP addresses that you specified in that rule.

 

![image](https://media.tutorialsdojo.com/sap_outbound_resolver.png)

 

When **Outbound Endpoint**  and **Forwarding Rule**  are created, any resource in the VPC that queries the AmazonProvidedDNS as its DNS resolver is able to seamlessly resolve for AWS Managed Microsoft AD domain’s FQDN, as well as any AWS resources on the VPC such as (interface) VPC Endpoints.

 

The option that says: **Create an outbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC**  is correct. You need an outbound endpoint to forward and resolve custom domain names inside your VPC.

 

The option that says: **Create a forwarding rule inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers**  is correct. The forwarding rules will handle queries for a given DNS domain and forward them to the AD server to resolve them.

 

The option that says: **Create an inbound endpoint on the Amazon Route 53 console. Set the AmazonProvidedDNS as the DNS resolver for the VPC**  is incorrect. An inbound endpoint is used for DNS resolution of AWS services. You need an outbound endpoint for this scenario.

 

The option that says: **Reconfigure the DNS service on every client on the VPC to split DNS queries. Use the Active Directory servers for the custom AD domain and the VPC resolver for all other DNS queries**  is incorrect. It is not recommended to manually configure resources to split DNS queries. This entails a lot of management overhead. You just need to set the Active Directory servers as the DNS servers and the requests will be forwarded to the VPC resolver accordingly.

 

The option that says: **Create a conditional forwarder inside the endpoint to forward any queries for private.tutorialsdojo.com to the IP addresses of the two domain controllers**  is incorrect. A conditional forwarder is configured inside the AD servers, not on the Route 53 resolver endpoint.

 

**References:**

 

[https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html#resolver-forwarding-outbound-queries-configuring](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html#resolver-forwarding-outbound-queries-configuring)

 

[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html)

 

[https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/](https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-your-directory-services-dns-resolution-with-amazon-route-53-resolvers/)

 

 

**Check out these Amazon VPC and Amazon Route 53 Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-vpc/](https://tutorialsdojo.com/amazon-vpc/)

 

[https://tutorialsdojo.com/amazon-route-53/](https://tutorialsdojo.com/amazon-route-53/)

</details>

<a id="q58"></a>

## Q58

A finance company plans to launch a new website to let users view tutorials promoting proper use of the mobile app. The website contains static media files stored in a private Amazon S3 bucket, while dynamic content is hosted on an AWS Fargate cluster. The Fargate tasks are accepting traffic behind an Application Load Balancer (ALB). To improve the user experience, static and dynamic content are served via an Amazon CloudFront distribution. An Amazon Route 53 Alias record has already been created to point the website URL to the CloudFront distribution. The company wants to ensure that access to both static and dynamic content is handled exclusively through CloudFront.



Which of the following options should the Solutions Architect implement to meet this requirement? (Select TWO.)

- **A.** Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the Application Load Balancer.
- **B.** Create a network ACL that will allow connections from CloudFront only. Associate the NACL to the Application Load Balancer subnets.
- **C.** Create an origin access control (OAC) and associate it with your distribution. Configure the S3 bucket policy to only access from the OAC.
- **D.** Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the CloudFront distribution.
- **E.** Configure the S3 bucket ACL to block all access except requests coming from the CloudFront distribution.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C · **You picked:** B, C

🔑 **Key words:** S3 static + ALB/Fargate dynamic behind CloudFront; block direct access to both origins

🪤 **Your trap:** A NACL can't allow 'CloudFront only' (too many changing IPs); twin options differ only in where the WAF web ACL is attached

🧠 **Rule:** Private S3 origin → OAC + bucket policy; ALB origin → CloudFront custom header + WAF web ACL on the ALB (not on the distribution).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
User ─► Route 53 Alias ─► CloudFront ─┬─► S3 (private bucket)  : static
                                      └─► ALB ─► Fargate tasks : dynamic

Yêu cầu: truy cập static VÀ dynamic CHỈ qua CloudFront
         => phải khóa cả 2 origin, mỗi origin một cách
```

Đáp án đúng: **A + C**. Anh chọn B + C: phần S3 (C) đúng, phần ALB sai (chọn NACL thay vì custom header + WAF).

#### Origin S3: C đúng

**Origin access control (OAC)** + bucket policy chỉ cho OAC đọc. OAC giúp CloudFront gửi request đã ký (SigV4) tới S3 riêng tư; người dùng không truy cập trực tiếp được bằng URL S3, buộc đi qua CloudFront. OAC là cơ chế được khuyến nghị, thay cho OAI (legacy).

Ba bước: tạo OAC gắn vào distribution, cấp quyền đọc cho OAC, gỡ quyền của mọi đối tượng khác.

#### Origin ALB: A đúng

Với custom origin như ALB, cách khóa là **custom header**:

```
CloudFront ── thêm header bí mật vào origin request ──► ALB
                                                          │ WAF web ACL gắn trên ALB
                                                          ▼
                                     có header ► cho qua | không có header ► chặn
```

Ai gọi thẳng vào ALB thì không có header nên bị WAF chặn. Chỉ request đã đi qua CloudFront (được thêm header) mới tới Fargate.

#### Vì sao B (anh chọn) sai

B là **network ACL cho phép CloudFront**. NACL lọc theo **IP**, mà CloudFront **không có dải IP cố định**. Nếu tự thêm IP của AWS thì phải cập nhật NACL mỗi khi AWS đổi dải IP. Thêm nữa NACL áp lên cả subnet của ALB nên ảnh hưởng mọi resource trong subnet đó. Nó cũng không phân biệt "request thật từ distribution của mình" với "request từ distribution CloudFront của người khác".

#### Cặp đáp án sinh đôi A vs D

A và D giống nhau từng chữ, chỉ khác **nơi gắn web ACL**:

| | Gắn web ACL vào | Kết quả |
|---|---|---|
| **A** | **ALB** | Đúng: header đã được CloudFront thêm trước khi tới ALB, WAF kiểm tra tại đây |
| D | **CloudFront distribution** | Sai: request viewer gửi tới CloudFront **chưa có header** (header do CloudFront thêm sau, ở chặng gọi origin), nên WAF có thể chặn ngay mọi kết nối mới |

Header được thêm ở chặng CloudFront ➜ origin, nên chỉ kiểm tra được ở phía origin (ALB), không phải ở cổng vào CloudFront.

#### Đáp án sai còn lại

- **E (S3 bucket ACL):** không thể cấu hình bucket ACL chỉ cho phép CloudFront; cần OAC cho mục đích này.

#### Lưu ý thực tế

- Header bí mật nên là giá trị khó đoán; nếu lộ, ai cũng giả được header để gọi thẳng ALB.
- Web ACL gắn vào ALB dùng phạm vi **regional**, khác với web ACL gắn vào CloudFront.

#### Quy tắc nhớ cho thi

- **Private S3 origin** → **OAC + bucket policy** (không dùng bucket ACL, OAI là legacy)
- **ALB / custom origin cần chỉ nhận từ CloudFront** → **custom header + WAF web ACL gắn trên ALB**
- **Thấy "NACL allow CloudFront"** → sai, **CloudFront không có IP cố định**
- **Hai đáp án chỉ khác "gắn WAF vào đâu"** → header thêm sau CloudFront nên gắn ở **ALB**, không phải distribution

### TD explanation

Incorrect  

**AWS WAF**  is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the values of query strings or the IP addresses that requests originate from, CloudFront responds to requests either with the requested content or with an HTTP status code `403(Forbidden)`. You can also configure CloudFront to return a custom error page when a request is blocked.

 

After you create an **AWS WAF web access control list (web ACL)** , create or update a web distribution to associate the distribution with the web ACL. You can associate as many CloudFront distributions as you want with the same web ACL or with different web ACLs.

 

On **Amazon CloudFront** , you can control user access to your private content in two ways:

 

1. Restrict access to files in CloudFront caches.
2. Restrict access to files in your origin by doing one of the following:

 

– Set up an origin access control (OAC) for your Amazon S3 bucket.

 

– Configure custom headers for a private HTTP server (a custom origin).

 

CloudFront provides two ways to send authenticated requests to an Amazon S3 origin: origin access control (OAC) and origin access identity (OAI). OAC helps you secure your origins, such as Amazon S3.

 

AWS recommends that you use OAC instead because it supports the following features:

 

- All Amazon S3 buckets in all AWS Regions, including opt-in Regions launched after December 2022
- Amazon S3 server-side encryption with AWS KMS (SSE-KMS)
- Dynamic requests (`PUT` and `DELETE`) to Amazon S3

 

Origin Access Identity (OAI) is considered a legacy, not-recommended mechanism due to its functional limitations.

 

You can secure the content in your Amazon S3 bucket so that users can access it through CloudFront, but cannot access it directly by using Amazon S3 URLs. This prevents someone from bypassing CloudFront and using the Amazon S3 URL to get content that you want to restrict access to. To require that users access your content through CloudFront URLs, you do the following tasks:

 

1. Create an origin access control and associate it with your CloudFront distribution.
2. Give the origin access control permission to read the files in your bucket.
3. Remove permission for anyone else to use Amazon S3 URLs to read the files.

 

![image](https://media.tutorialsdojo.com/sap_cloudfront_oia.png)

 

If you use a custom origin, you can optionally set up custom headers to restrict access. For CloudFront to get your files from a custom origin, the files must be accessible by CloudFront using a standard HTTP (or HTTPS) request. But by using custom headers, you can further restrict access to your content so that users can access it only through CloudFront, not directly. This step isn’t required to use signed URLs, but it is recommended. To require that users access content through CloudFront, change the following settings in your CloudFront distributions:

 

**Origin Custom Headers**  – Configure CloudFront to forward custom headers to your origin.

 

**Viewer Protocol Policy**  – Configure your distribution to require viewers to use HTTPS to access CloudFront.

 

**Origin Protocol Policy**  – Configure your distribution to require CloudFront to use the same protocol as viewers to forward requests to the origin.

 

Hence, the correct answers are:

 

**– Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the Application Load Balancer.**  After you create an AWS WAF web access control list (web ACL), create or update a web distribution to associate the distribution with the ALB. Associating the Web ACL with the ALB ensures that only requests from CloudFront will reach the ALB. Any request going to the ALB without the custom header will be denied by WAF.

 

**–**  **Create an origin access control (OAC) and associate it with your distribution. Configure the S3 bucket policy to only access from the OAC.**  OAC enables CloudFront to use SigV4-signed requests to access private S3 content, and the S3 bucket policy can explicitly allow access only from CloudFront via that OAC. This prevents users from retrieving objects directly from S3 and forces access through CloudFront.

 

The option that says: **Use CloudFront to add a custom header to all origin requests. Using AWS WAF, create a web rule that denies all requests without this custom header. Associate the web ACL to the CloudFront distribution**  is incorrect. If any new requests are going to CloudFront, they won’t have the custom header initially, so AWS WAF may block the request immediately. This could deny any new connections to CloudFront. Therefore, you need to associate the web ACL to the ALB, which is after CloudFront adds the custom header.

 

The option that says: **Create a network ACL that will allow connections from CloudFront only. Associate the NACL to the Application Load Balancer subnets**  is incorrect. This will limit all resources inside the ALB subnets to accept only traffic from the CloudFront distribution. However, there are no fixed IP addresses for Amazon CloudFront, and if you manually add AWS IP addresses, you will have to update the NACL as AWS updates its IP pool.

 

The option that says: **Configure the S3 bucket ACL to block all access except requests coming from the CloudFront distribution**  is incorrect. You can’t directly configure a bucket ACL to allow access only from Amazon CloudFront. You typically need an origin access control (OAC) for this setup.

 

 

**References:**

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html)

 

[https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/)

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html#forward-custom-headers-restrict-access](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-overview.html#forward-custom-headers-restrict-access)

 

 

**Check out these Amazon CloudFront and AWS WAF Cheat Sheets:**

 

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

 

[https://tutorialsdojo.com/aws-waf/](https://tutorialsdojo.com/aws-waf/)

</details>

---

# Group C — Read the deciding detail (push vs SMS, IaC, Multi-AZ failover, stateless tiers) (4)

<a id="q15"></a>

## Q15

A global real estate startup is looking for an option to add a cost-effective location-based alert to iOS and Android mobile apps. Users will receive push notifications on mobile devices regarding real estate offers in proximity to current locations, with delivery expected in under a minute. The existing mobile app has an initial 2 million users worldwide and is rapidly growing. The team considered using AWS Wavelength for edge processing of location data but chose a simpler queuing approach to reduce costs.



What is the most suitable architecture to use in this scenario?

- **A.** Set up an architecture where the mobile app will send the user's location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon Aurora database. Once the data has been processed, use AWS Device Farm to send out the offers to the mobile app.
- **B.** Set up an architecture where the mobile app will send the user's location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon DynamoDB table. Once the data has been processed, use Amazon SNS Mobile Push to send out the offers to the mobile app.
- **C.** Set up an architecture where there is an Auto Scaling group of On-Demand Amazon EC2 instances behind an Amazon API Gateway that retrieve the relevant offers from Amazon RDS. Once the data has been processed, use AWS AppSync to send out the offers to the mobile app.
- **D.** Set up an architecture where the mobile app sends each user's location to an Amazon SQS queue, and AWS Lambda functions process the queued messages and retrieve nearby offers from an Amazon Aurora Serverless database. After processing, publish the offers to Amazon SNS topics configured with SMS delivery for registered mobile numbers.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** push notifications to iOS/Android apps, cost-effective, under a minute

🪤 **Your trap:** SNS SMS sends text messages to phone numbers, not push notifications to the app

🧠 **Rule:** Mobile app push → SNS Mobile Push; read the delivery channel word (push vs SMS vs email).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Mobile app (iOS/Android)
   │ gửi vị trí
   ▼
 SQS queue ──► Xử lý (EC2 / Lambda) ──► DB lấy offer gần đó ──► ??? gửi offer về app
                                                                   │
                                  Yêu cầu: PUSH notification vào APP, < 1 phút, tiết kiệm chi phí
```

Từ khóa quyết định: **"push notifications to mobile app"** (kênh giao). Đáp án đúng: **B (SNS Mobile Push)**. Anh chọn D, dùng SNS với SMS delivery.

#### B đúng: SNS Mobile Push

Cả B và D đều có SQS ở đầu vào, nên phần "nhận vị trí" không phân biệt được. Chỗ khác nhau là **bước cuối**:

- **SNS Mobile Push** gửi push notification trực tiếp tới app trên iOS/Android; thông báo hiện dạng alert, badge hoặc âm thanh.
- SQS giữ vị trí của hàng triệu user (scalable, rẻ); DynamoDB scale tốt cho tra cứu offer.

#### D sai: SNS SMS không phải push

D có kiến trúc xử lý hợp lý (SQS + Lambda + Aurora Serverless), nhưng **SNS SMS gửi tin nhắn văn bản tới số điện thoại**, không phải push notification tới ứng dụng. Đề yêu cầu push tới app, nên D không đáp ứng. Ngoài ra SMS cần số điện thoại đã đăng ký, trong khi đề chỉ nói về người dùng app.

⚠️ Lỗi lặp lại: đọc lướt "SNS" rồi chọn, không đọc **kênh giao** (push / SMS / email). Cùng một service SNS nhưng khác protocol.

#### Các option còn lại

- **A sai:** **AWS Device Farm** là dịch vụ **test app** trên nhiều thiết bị, không gửi thông báo.
- **C sai:** **AWS AppSync** là GraphQL API, không dùng để push notification tới mobile; phải dùng SNS Mobile Push.

| Option | Bước gửi cuối | Gửi tới đâu | Phù hợp? |
|---|---|---|---|
| **B** | SNS Mobile Push | App trên thiết bị | Đúng |
| D | SNS SMS | Số điện thoại | Sai kênh |
| C | AppSync | (GraphQL API) | Sai dịch vụ |
| A | Device Farm | (dịch vụ test) | Sai dịch vụ |

#### Lưu ý thực tế

- Đề nhắc Wavelength nhưng chọn hướng queue đơn giản hơn để giảm chi phí; đừng bị phân tâm bởi từ khóa edge computing.

#### Quy tắc nhớ cho thi

- **Thấy "push notifications to iOS/Android app"** → **SNS Mobile Push**
- **Thấy "text message / phone number"** → SNS SMS
- **Thấy "Device Farm"** → test app, không phải gửi thông báo
- **Thấy "AppSync"** → GraphQL, không phải push
- Luôn đọc **kênh giao** trước khi chọn: push vs SMS vs email

### TD explanation

Incorrect  

With **Amazon SNS Mobile Push Notifications** , you have the ability to send push notification messages directly to apps on mobile devices. Push notification messages sent to a mobile endpoint can appear in the mobile app as message alerts, badge updates, or even sound alerts.

 

![image](https://media.tutorialsdojo.com/public/Amazon SNS Mobile push notifications-24SEP2026.png)

 

Hence, the correct answer is: **Set up an architecture where the mobile app will send the user’s location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon DynamoDB table. Once the data has been processed, use Amazon SNS Mobile Push to send out the offers to the mobile app.**  SQS is a highly scalable, cost-effective solution for carrying out utility tasks such as holding the location of millions of users. In addition, it uses a highly scalable DynamoDB table and a cost-effective AWS SNS Mobile Push service to send push notification messages directly to the mobile apps.

 

The option that says: **Set up an architecture where there is an Auto Scaling group of On-Demand Amazon EC2 instances behind an Amazon API Gateway that retrieve the relevant offers from Amazon RDS. Once the data has been processed, use AWS AppSync to send out the offers to the mobile app**  is incorrect. Although a combination of On-Demand EC2 instances and API Gateway can typically provide a scalable computing system, it is wrong to use AWS AppSync for push notifications to mobile devices. You should use Amazon SNS Mobile Push service instead.

 

The option that says: **Set up an architecture where the mobile app sends each user’s location to an Amazon SQS queue, and AWS Lambda functions process the queued messages and retrieve nearby offers from an Amazon Aurora Serverless database. After processing, publish the offers to Amazon SNS topics configured with SMS delivery for registered mobile numbers**  is incorrect because SNS SMS delivery is not the right mechanism for mobile app push notifications. Amazon SNS SMS delivers text messages to phone numbers instead of push notifications to the mobile application. Although Amazon SQS and AWS Lambda provide a scalable and cost-effective processing architecture, the SMS delivery method does not satisfy the requirement to send native push notifications to the iOS and Android apps.

 

The option that says: **Set up an architecture where the mobile app will send the user’s location to an Amazon SQS queue, and a fleet of On-Demand Amazon EC2 instances will retrieve the relevant offers from an Amazon Aurora database. Once the data has been processed, use AWS Device Farm to send out the offers to the mobile app**  is incorrect because AWS Device Farm is an app testing service and is not used to push notifications to various mobile devices. It only lets you test and interact with your Android, iOS, and web apps on many devices at once, or reproduce issues on a device in real time.

 

**References:**

 

[https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html)

 

[https://docs.aws.amazon.com/sns/latest/dg/mobile-push-pseudo.html](https://docs.aws.amazon.com/sns/latest/dg/mobile-push-pseudo.html)

 

[https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as-subscriber.html](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as-subscriber.html)

 

 

**Check out this Amazon SNS Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-sns/](https://tutorialsdojo.com/amazon-sns/)

</details>

<a id="q45"></a>

## Q45

A software development company implements cloud best practices on its AWS infrastructure. The solutions architect has been instructed to manage its AWS cloud Infrastructure as code (IAC) to automate its software build, test, and deploy process. The company follows a continuous integration and continuous delivery (CI/CD) practice to streamline its software development lifecycle. The company already uses AWS CodeArtifact to store and version its private software packages.



The company would like to have the ability to easily deploy exact copies of different versions of its cloud infrastructure, stage changes into different environments, revert back to previous versions, and identify the specific versions running in the VPC. Plus, all new public-facing applications should also have a global content delivery network (CDN) service.



Which of the following options is the recommended action to meet the company requirement?

- **A.** Use Amazon CloudWatch as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture.
- **B.** Use AWS CloudFormation to manage the cloud architecture and Amazon CloudFront as the CDN.
- **C.** Use Amazon CloudFront as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture.
- **D.** Use Amazon CloudWatch as the CDN and AWS CloudFormation to manage the cloud architecture.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** manage infrastructure as code for CI/CD + CDN

🪤 **Your trap:** Elastic Beanstalk deploys apps but doesn't manage infrastructure as code

🧠 **Rule:** Infrastructure as code → CloudFormation (or CDK); CDN → CloudFront; CloudWatch is never a CDN.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Yêu cầu                                         Dịch vụ phù hợp
─────────────────────────────────────────       ───────────────────────
Infrastructure as code (IaC)                ──►  ?
Deploy bản sao chính xác, nhiều version,
stage qua nhiều môi trường, rollback,
biết version nào đang chạy trong VPC        ──►  ?
Public-facing app cần global CDN            ──►  ?
```

Đáp án đúng: **B (CloudFormation + CloudFront)**. Anh chọn C (Elastic Beanstalk + CloudFront). CDN anh chọn đúng; sai ở phần quản lý hạ tầng.

#### B đúng

- **AWS CloudFormation**: mô tả và provision toàn bộ hạ tầng bằng một file text, là "single source of truth" cho môi trường, dùng được trên nhiều region/account. Template là code nên version được, dựng lại bản sao chính xác, stage vào môi trường khác, rollback về version trước.
- **Amazon CloudFront**: CDN toàn cầu, phân phối nội dung qua edge locations, người dùng được route tới edge có latency thấp nhất.

#### C sai: Elastic Beanstalk không phải IaC

Anh chọn Beanstalk vì nó cũng "deploy và quản lý". Nhưng Beanstalk tập trung **deploy ứng dụng** (upload code, nó lo môi trường), còn đề yêu cầu quản lý **toàn bộ hạ tầng như code** (IaC). Theo TD: với Beanstalk "you still can't manage the cloud infrastructure as application code"; lựa chọn đúng là CloudFormation.

⚠️ Cách phân biệt: Beanstalk = "tôi có app, lo hạ tầng giúp"; CloudFormation = "tôi mô tả hạ tầng bằng template".

#### A và D sai: CloudWatch không phải CDN

**CloudWatch** là dịch vụ monitoring/logging. Cả A và D dùng nó làm CDN nên loại ngay, bất kể phần còn lại.

| Option | CDN | Quản lý hạ tầng | Kết quả |
|---|---|---|---|
| **B** | CloudFront (đúng) | CloudFormation (đúng) | Đúng |
| C | CloudFront (đúng) | Beanstalk (không phải IaC) | Sai |
| A | CloudWatch (sai) | Beanstalk | Sai |
| D | CloudWatch (sai) | CloudFormation (đúng) | Sai |

#### Lưu ý thực tế

- Đề nhắc CodeArtifact (lưu package riêng) chỉ là bối cảnh, không ảnh hưởng đáp án.

#### Quy tắc nhớ cho thi

- **Thấy "infrastructure as code", "versioned, rollback, replicate environments"** → **CloudFormation** (hoặc CDK)
- **Thấy "global CDN"** → **CloudFront**; CloudWatch không bao giờ là CDN
- **Beanstalk** = deploy app, không phải IaC
- Loại đáp án bằng CDN trước (A, D có CloudWatch) rồi mới so IaC

### TD explanation

Incorrect  

**AWS CloudFormation**  provides a common language for you to describe and provision all the infrastructure resources in your cloud environment. CloudFormation allows you to use a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts. This file serves as the single source of truth for your cloud environment.

 

![image](https://media.tutorialsdojo.com/public/td-aws-cloudformation-diagram-1April2026.png)

 

**Amazon CloudFront**  is a web service that speeds up the distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you’re serving with CloudFront, the user is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.

 

Therefore, the correct answer is: **Use AWS CloudFormation to manage the cloud architecture and Amazon CloudFront as the CDN.**

 

The option that says: **Use Amazon CloudWatch as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture**  is incorrect. CloudWatch is typically not a CDN service.

 

The option that says: **Use Amazon CloudWatch as the CDN and AWS CloudFormation to manage the cloud architecture**  is incorrect. As with the case above, CloudWatch is not a CDN service.

 

The option that says: **Use Amazon CloudFront as the CDN and AWS Elastic Beanstalk to deploy and manage the cloud architecture**  is incorrect. Even though Elastic Beanstalk enables you to quickly deploy and manage applications in the AWS Cloud, you still can’t manage the cloud infrastructure as application code with it. The best option is simply to use CloudFormation.

 

 

**References:**

 

[https://aws.amazon.com/cloudformation/](https://aws.amazon.com/cloudformation/ )

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

 

 

**Check out this AWS CloudFormation Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-cloudformation/](https://tutorialsdojo.com/aws-cloudformation/)

 

 

**Elastic Beanstalk vs CloudFormation vs OpsWorks vs CodeDeploy:**

 

[https://tutorialsdojo.com/elastic-beanstalk-vs-cloudformation-vs-opsworks-vs-codedeploy/](https://tutorialsdojo.com/elastic-beanstalk-vs-cloudformation-vs-opsworks-vs-codedeploy/)

 

 

**Comparison of AWS Services Cheat Sheets:**

 

[https://tutorialsdojo.com/comparison-of-aws-services/](https://tutorialsdojo.com/comparison-of-aws-services/)

</details>

<a id="q53"></a>

## Q53

A company hosts its main web application on the AWS cloud which is composed of web servers and database servers. To ensure high availability, the web servers are deployed on an Auto Scaling group of Amazon EC2 instances across multiple Availability Zones with an Application Load Balancer in front. For the database, it is deployed on a Multi-Availability Zone configuration in Amazon RDS. During the RDS maintenance window, the operating system of the primary DB instance undergoes software patching that triggers the failover process.



What would happen to the database during failover?

- **A.** A new DB instance will be created and immediately replace the primary database.
- **B.** The canonical name record (CNAME) is changed from the primary database to standby database.
- **C.** The RDS DB instance will automatically reboot.
- **D.** The IP address of the primary DB instance is switched to the standby DB instance.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** D

🔑 **Key words:** RDS Multi-AZ primary fails — what happens

🪤 **Your trap:** The IP isn't moved — RDS flips the DNS record

🧠 **Rule:** RDS Multi-AZ failover → the CNAME is switched to the standby (apps reconnect to the same endpoint).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
App ──► DB endpoint (DNS name)
              │ CNAME
              ▼
   ┌────────────────────┐      sync replication      ┌────────────────────┐
   │ Primary  (AZ-a)    │ ─────────────────────────► │ Standby  (AZ-b)    │
   │  OS patching       │                            │                    │
   └────────────────────┘                            └────────────────────┘
          Failover xảy ra ──► CNAME đổi sang trỏ vào Standby
```

Câu hỏi: khi failover của RDS Multi-AZ, điều gì xảy ra? Đáp án đúng: **B (CNAME đổi sang standby)**. Anh chọn D (IP address chuyển sang standby).

#### B đúng

Multi-AZ tạo primary và đồng bộ dữ liệu (synchronous) sang standby ở AZ khác. Khi failover tự động, **CNAME record của DB instance được sửa để trỏ vào standby vừa được promote**. Ứng dụng vẫn dùng cùng một endpoint nên "không biết" chuyện gì xảy ra phía sau (cần kết nối lại).

#### D sai: IP không được chuyển

Anh nghĩ giống failover kiểu "IP ảo" truyền thống. Với RDS, thứ thay đổi là **bản ghi DNS (CNAME)**, không phải IP của primary được gán sang standby. Vì vậy ứng dụng phải dùng **DNS endpoint**, đừng hard-code IP.

⚠️ Chỗ dễ vấp: endpoint không đổi, địa chỉ phía sau đổi. Cache DNS lâu phía client có thể làm kết nối chậm hồi phục.

#### A và C sai

- **A sai:** không có DB instance mới nào được tạo; standby đã tồn tại sẵn và được promote.
- **C sai:** theo TD, RDS instance không tự reboot như một phần của việc này; thứ thay đổi là CNAME.

| Option | Phát biểu | Đánh giá |
|---|---|---|
| **B** | CNAME đổi sang standby | Đúng |
| D | IP chuyển sang standby | Sai (đổi DNS, không phải IP) |
| A | Tạo DB instance mới | Sai (standby có sẵn) |
| C | Instance tự reboot | Sai |

#### Quy tắc nhớ cho thi

- **Thấy "RDS Multi-AZ failover"** → **CNAME đổi sang standby**
- **Thấy "IP address switched"** → bẫy, loại
- Standby có sẵn, không "tạo mới"
- Ứng dụng luôn dùng **endpoint DNS**, không dùng IP

### TD explanation

Incorrect  

**Amazon RDS Multi-AZ**  deployments provide enhanced availability and durability for Database (DB) Instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable. In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby (or to a read replica in the case of Amazon Aurora), so that you can resume database operations as soon as the failover is complete.

 

![image](https://media.tutorialsdojo.com/sap_rds_multiaz.png)

 

When automatic failover occurs, your application can remain unaware of what’s happening behind the scenes. The CNAME record for your DB instance will be altered to point to the newly promoted standby.

 

Therefore, the correct answer is: **The canonical name record (CNAME) is changed from the primary database to standby database.**

 

The option that says: **The** **IP address of the primary DB instance is switched to the standby DB instance**  is incorrect because the Canonical Name Record (CNAME) will be changed and not the IP address.

 

The option that says: **The RDS DB instance will automatically reboot**  is incorrect because the RDS instance will not automatically reboot.

 

The option that says:**A new DB instance will be created and immediately replace the primary database**  is incorrect because there is no new DB instance that will be created.

 

 

**References:**

 

[https://aws.amazon.com/rds/details/multi-az/](https://aws.amazon.com/rds/details/multi-az/)

 

[https://aws.amazon.com/blogs/aws/amazon-rds-multi-az-deployment/](https://aws.amazon.com/blogs/aws/amazon-rds-multi-az-deployment/)

 

 

**Check out this Amazon RDS Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)

</details>

<a id="q62"></a>

## Q62

A hospital chain in London uses an online central hub for its doctors and nurses. The application interacts with millions of requests per day to fetch various medical data of their patients. The system is composed of a web tier, an application tier, and a database tier that receives large and unpredictable traffic demands. The Solutions Architect must ensure that this infrastructure is highly-available and scalable enough to handle web traffic fluctuations automatically.



Which of the following options should the solutions architect implement to meet the above requirements?

- **A.** Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.
- **B.** Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.
- **C.** Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with read replicas.
- **D.** Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with read replicas, and Multi-AZ enabled.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** large unpredictable traffic, millions of reads, web/app/DB tiers, scalable + available

🪤 **Your trap:** Stateful instances can't scale freely; Multi-AZ alone doesn't add read capacity (twin options differ in stateless + cache + replicas)

🧠 **Rule:** Scale web/app tiers → stateless ASG + ElastiCache for state; DB reads → read replicas, availability → Multi-AZ.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Users ──► Web tier ──► App tier ──► DB tier
          (ASG)        (ASG)        (RDS)
Hàng triệu request/ngày, đa số là đọc dữ liệu bệnh nhân
Traffic LỚN và KHÓ ĐOÁN ──► phải highly available + tự scale
```

Bốn option là các tổ hợp của 3 lựa chọn: **stateless hay stateful**, **có cache hay không**, **Multi-AZ hay read replicas (hay cả hai)**. Đáp án đúng: **D**. Anh chọn A (stateful + Multi-AZ only).

#### D đúng: đủ cả ba mảnh

- **Stateless instances trong ASG:** không lưu session trên instance nên instance nào cũng phục vụ được request, thêm/bớt instance thoải mái. Stateless app scale ngang được, scale-in an toàn sau khi drain task đang chạy.
- **ElastiCache Serverless** (làm "tier synchronization" / chia sẻ state, và phục vụ read): giữ dữ liệu dùng chung ngoài instance; TD nêu nó tự replicate qua nhiều AZ nên cũng sẵn sàng cao.
- **CloudWatch** theo dõi traffic và kích hoạt ASG scale-in/scale-out.
- **RDS read replicas + Multi-AZ:** read replicas gánh lượng đọc lớn; Multi-AZ lo availability. Hai thứ giải quyết hai vấn đề khác nhau.

#### A sai (anh chọn): hai lỗi

1. **Stateful instances:** session nằm trên từng instance nên không scale tự do được.
2. **Multi-AZ không tăng hiệu năng đọc.** Multi-AZ chỉ cải thiện **availability**. Đề có hàng triệu request đọc, không có replica hay cache thì DB thành điểm nghẽn.

Option A cũng không có cache cho web/app tier.

#### Các option còn lại

- **B sai:** stateless + cache tốt, nhưng DB chỉ Multi-AZ nên không tăng read capacity.
- **C sai:** vẫn stateful, và không có cache cho web/app tier.

| Option | Stateless | Cache | Read replicas | Multi-AZ |
|---|---|---|---|---|
| A | không | không | không | có |
| B | có | có | không | có |
| C | không | không | có | không nêu |
| **D** | có | có | có | có |

#### Lưu ý thực tế

- Đây là "twin options": B và D giống hệt nhau, chỉ khác ở DB. Khi hai option gần giống nhau, đọc **phần khác biệt cuối** để quyết định.

#### Quy tắc nhớ cho thi

- **Thấy "scale web/app tier tự động, traffic không đoán trước"** → **stateless ASG** + state ra ngoài (**ElastiCache**)
- **Thấy "read-heavy"** → **read replicas** (và/hoặc cache)
- **Multi-AZ** = availability, **read replica** = hiệu năng đọc; cần cả hai thì chọn option có cả hai
- Hai option giống nhau → so sánh chỗ khác nhau duy nhất

### TD explanation

Incorrect  

When users or services interact with an application, they will often perform a series of interactions that form a session. A session is unique data for users that persists between requests while they use the application. A stateless application is an application that does not need knowledge of previous interactions and does not store session information.

 

![image](https://media.tutorialsdojo.com/sap_spot_stateless_session.png)

 

For example, an application that, given the same input, provides the same response to any end user, is a stateless application. Stateless applications can scale horizontally because any of the available compute resources (such as EC2 instances and AWS Lambda functions) can service any request. Without stored session data, you can simply add more compute resources as needed. When that capacity is no longer required, you can safely terminate those individual resources, after running tasks have been drained. Those resources do not need to be aware of the presence of their peers—all that is required is a way to distribute the workload to them.

 

In this scenario, the best option is to use a combination of **Amazon**  **ElastiCache Serverless** , **Cloudwatch** , and **RDS Read Replica** .

 

Therefore, the correct answer is: **Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with read replicas, and Multi-AZ enabled.**  It uses stateless instances. The web server uses ElastiCache Serverless for read operations and relies on CloudWatch for monitoring traffic fluctuations. When variations in traffic occur, CloudWatch notifies the autoscaling group to perform scale-in or scale-out actions accordingly. ElastiCache Serverless is a robust cache solution that ensures high availability by automatically replicating data across multiple Availability Zones. Furthermore, it leverages read replicas for RDS to efficiently handle read-heavy workloads and utilizes Multi-AZ configurations to ensure high availability.

 

The option that says: **Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled**  is incorrect because it uses stateful instances. It also does not use any caching mechanism for web and application tiers, and multi-AZ RDS does not improve read performance.

 

The option that says: **Run the web and application tiers in stateful instances in an autoscaling group, using CloudWatch for monitoring. Run the database tier using RDS with read replicas**  is incorrect because it uses stateful instances and it does not use any caching mechanism for web and application tiers.

 

The option that says: **Run the web and application tiers in stateless instances in an autoscaling group, using Amazon ElastiCache Serverless for tier synchronization and CloudWatch for monitoring. Run the database tier using RDS with Multi-AZ enabled.**  is incorrect because multi-AZ RDS only improves Availability, not read performance.

 

 

**References** :

 

[https://aws.amazon.com/elasticache/](https://aws.amazon.com/elasticache/ )

 

[https://aws.amazon.com/rds/details/read-replicas/](https://aws.amazon.com/rds/details/read-replicas/)

 

[https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf](https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf)

 

 

**Check out these AWS Cheat Sheets:**

 

**[https://tutorialsdojo.com/amazon-elasticache/](https://tutorialsdojo.com/amazon-elasticache/)**

 

**[https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/](https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/)**

</details>

---

# Group D — Answered right but unsure — confirm the reasoning (5)

These were answered correctly in the retake; added on request to confirm the reasoning (Q42 was a real miss and stays in Group A).

<a id="q13"></a>

## Q13

A company wants to create a new service that will complement the launch of its new product. The site must be highly available and scalable to handle the unpredictable workload, and should also be stateless and REST compliant. The solution needs to have multiple persistent storage layers for service object metadata and durable storage for static content. All requests to the service should be authenticated and securely processed. The company also wants to keep the costs at a minimum. The team considered using an AWS Lambda authorizer for custom authentication logic but wants to minimize operational overhead.



Which of the following is the recommended solution that will meet the company requirements?

- **A.** Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
- **B.** Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create an Application Load Balancer in front of the Fargate service. Create a custom authenticator that will control access to the API. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an Amazon S3 bucket to store the static content and enable secure-signed requests for the objects. Proxy the data through the REST service.
- **C.** Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create a cross-zone Application Load Balancer in front of the Fargate service. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an encrypted Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.
- **D.** Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using the API Gateway custom authorizer. Store service object metadata in an Amazon ElastiCache Multi-AZ cluster. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** stateless REST, authenticate all requests, metadata store + durable static storage, minimum cost, minimal operational overhead

⚠️ **Watch:** Twin options: A = Cognito user pools + DynamoDB (Auto Scaling); D = custom (Lambda) authorizer + ElastiCache — custom code and a cache are not a durable metadata store

🧠 **Rule:** Serverless REST with built-in auth → API Gateway + Lambda + Cognito user pools authorizer; metadata → DynamoDB, static → S3.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──► [Xác thực?] ──► [Compute stateless REST] ──► [Metadata store]
                                       └──────────────► [Static content bền vững]

Từ khóa quyết định: stateless + REST, tải khó đoán, mọi request phải xác thực,
chi phí THẤP NHẤT, giảm operational overhead
```

Đáp án đúng: **A**. Anh chọn đúng. Cặp "twin" cần phân biệt: **A vs D** chỉ khác đúng 2 chỗ: **Cognito user pools + DynamoDB** (A) so với **API Gateway custom authorizer + ElastiCache** (D).

#### Vì sao A đúng

- **API Gateway + Lambda proxy integration:** serverless, tự scale theo tải khó đoán, trả tiền theo request, không phải vận hành server. Mỗi resource một Lambda, request thô được chuyển nguyên cho function.
- **Cognito user pools:** user directory có sẵn (sign-up/sign-in, MFA, social/SAML federation). API Gateway tích hợp trực tiếp, không tự viết code xác thực. Khớp ý "giảm operational overhead" mà đề nhấn mạnh sau khi nhắc Lambda authorizer.
- **DynamoDB + Auto Scaling:** metadata store bền vững, scale theo tải. Mô hình quen thuộc: S3 chứa object, DynamoDB làm index cho thuộc tính tra cứu.
- **S3 + presigned URL:** static content bền vững, bucket private, truy cập có thời hạn.

#### Cặp twin A vs D

| Tiêu chí | A | D |
|---|---|---|
| Xác thực | Cognito user pools (managed, nhiều tính năng) | Custom authorizer (tự viết logic, tự bảo trì) |
| Metadata store | DynamoDB (bền vững) | ElastiCache Multi-AZ (cache) |
| Hợp đề | Có | Không |

D sai vì hai điểm: (1) TD nói nên dùng Cognito user pools thay cho custom authorizer vì nó mạnh hơn và được thiết kế cho user access; đề còn nói rõ muốn tránh overhead của custom auth. (2) ElastiCache là in-memory cache, không phải persistent storage layer cho metadata mà đề yêu cầu.

#### Các option còn lại

- **B (Fargate + ALB + custom authenticator + proxy data qua service):** chạy được nhưng không rẻ nhất. TD: Lambda cho API stateless rẻ hơn Fargate. Thêm custom authenticator là tăng overhead, và proxy dữ liệu S3 qua service làm tốn thêm compute.
- **C (Fargate + ALB cross-zone + Cognito):** auth và storage đúng, nhưng Fargate chạy liên tục tốn hơn Lambda chỉ chạy khi có request. Fail ở "chi phí tối thiểu".

#### Quy tắc nhớ cho thi

- **Thấy "stateless REST + unpredictable + minimum cost"** → **API Gateway + Lambda**, không phải Fargate/ALB.
- **Thấy "authenticate users, giảm overhead"** → **Cognito user pools authorizer**, không phải custom authorizer.
- **Thấy "metadata / persistent store"** → **DynamoDB**; ElastiCache chỉ là cache.
- **Thấy "static content, bảo vệ"** → **S3 private + presigned URL**.

### TD explanation

Correct 

**Amazon API Gateway Lambda proxy**  **integration**  is a simple, powerful, and nimble mechanism to build an API with a setup of a single API method. The Lambda proxy integration allows the client to call a single Lambda function in the backend. The function accesses many resources or features of other AWS services, including calling other Lambda functions.

 

In Lambda proxy integration, when a client submits an API request, API Gateway passes to the integrated Lambda function the raw request as-is, except that the order of the request parameters is not preserved. This request data includes the request headers, query string parameters, URL path variables, payload, and API configuration data. The configuration data can include current deployment stage name, stage variables, user identity, or authorization context (if any).

 

A user pool is a user directory in **Amazon Cognito** . With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers. Whether your users sign in directly or through a third party, all members of the user pool have a directory profile that you can access through a Software Development Kit (SDK).

 

![image](https://media.tutorialsdojo.com/sap_cognito_user_pool.png)

 

User pools provide:

 

– Sign-up and sign-in services.

 

– A built-in, customizable web UI to sign in users.

 

– Social sign-in with Facebook, Google, Login with Amazon, and Sign in with Apple, as well as sign-in with SAML identity providers from your user pool.

 

– User directory management and user profiles.

 

– Security features such as multi-factor authentication (MFA), checks for compromised credentials, account takeover protection, and phone and email verification.

 

– Customized workflows and user migration through AWS Lambda triggers.

 

**Amazon S3**  is a simple key-based object store whose scalability and low cost make it ideal for storing large datasets or objects. When finding objects based on attributes or other metadata, a common solution is to build an external index such as a DynamoDB Table that maps queryable attributes to the S3 object key. DynamoDB is a NoSQL data store that can be used for storing the index itself.

 

One way of securing objects that are shared on S3 buckets is by using presigned URLs. When you create a presigned URL for your object, you must provide your security credentials, specify a bucket name, an object key, specify the HTTP method (GET to download the object), and expiration date and time. The presigned URLs are valid only for the specified duration.

 

Anyone who receives the presigned URL can then access the object. For example, if you have a video in your bucket and both the bucket and the object are private, you can share the video with others by generating a presigned URL.

 

Hence, the correct answer is:**Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket.**

 

The option that says: **Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create an Application Load Balancer in front of the Fargate service. Create a custom authenticator that will control access to the API. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an Amazon S3 bucket to store the static content and enable secure-signed requests for the objects. Proxy the data through the REST service** is incorrect. Although running Docker-based containers on Amazon Fargate is possible, this solution does not just offer the lowest possible cost to satisfy the given scenario. AWS Lambda is suited for creating serverless/stateless APIs and costs cheaper than AWS Fargate.

 

The option that says: **Package the REST service on a Docker-based container and run it using the AWS Fargate service. Create a cross-zone Application Load Balancer in front of the Fargate service. Control user access to the API by using Amazon Cognito user pools. Store service object metadata in an Amazon DynamoDB table with Auto Scaling enabled. Create an encrypted Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket** is incorrect. Running a Fargate cluster continuously is more expensive than running Lambda functions which only runs on-demand.

 

The option that says: **Configure Amazon API Gateway with the required resources and methods. Create unique Lambda functions to process each resource and configure the API Gateway methods with proxy integration to the respective Lambda functions. Control user access to the API by using the API Gateway custom authorizer. Store service object metadata in an Amazon ElastiCache Multi-AZ cluster. Create a secured Amazon S3 bucket to store the static content. Generate presigned URLs when referencing objects stored on the S3 bucket**  is incorrect because it is recommended to use Amazon Cognito user pools for user access controls compared to an API Gateway custom authorizer. It is more robust and offers more features because it is designed to handle user access.

 

 

**References:**

 

[https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)

 

[https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)

 

[https://aws.amazon.com/blogs/big-data/building-and-maintaining-an-amazon-s3-metadata-index-without-servers/](https://aws.amazon.com/blogs/big-data/building-and-maintaining-an-amazon-s3-metadata-index-without-servers/)

 

 

**Check out these AWS Comparison Cheat Sheets:**

 

[https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai/](https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai/)

 

[https://tutorialsdojo.com/ec2-container-service-ecs-vs-lambda/](https://tutorialsdojo.com/ec2-container-service-ecs-vs-lambda/)

</details>

<a id="q34"></a>

## Q34

A weather forecasting agency established a network of IoT devices in the ocean to help predict incoming typhoons. The IoT devices monitor the sea surface temperature and atmospheric pressure and send the data as messages to AWS IoT Core, which updates an Amazon DynamoDB table. On the weekly monitoring report, a system administrator notices that no new database updates are happening. The agency already uses AWS IoT Device Defender to audit device security policies and detect abnormal behavior, but this does not help diagnose connectivity interruptions.



What should the administrator do to troubleshoot the issue?

- **A.** Use AWS IoT SiteWise to collect the data directly from the IoT devices and send the aggregated data to IoT Core.
- **B.** Use AWS IoT Device Defender to add the Certificate Authority of the X.509 certificates used by the devices when connecting to AWS IoT Core, and establish connectivity.
- **C.** Trigger an AWS Lambda function adding updates to the DynamoDB table by integrating the IoT devices with IoT 1-Click.
- **D.** Register the IoT devices to AWS IoT Device Management and monitor the devices' health and ensure the devices are connected to AWS IoT Core.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D (you answered correctly)

🔑 **Key words:** IoT devices stopped updating DynamoDB; Device Defender already audits security; diagnose connectivity

⚠️ **Watch:** Device Defender = security audit/anomaly detection, SiteWise = industrial data collection, 1-Click = simple button devices

🧠 **Rule:** Fleet health / connectivity of IoT devices → AWS IoT Device Management (Fleet Hub, connectivity status).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
IoT devices (biển) ──► AWS IoT Core ──► DynamoDB
        │                    │
        └── KHÔNG còn bản ghi mới ở DynamoDB
        
Đã có: IoT Device Defender (audit bảo mật, phát hiện hành vi bất thường)
Cần: CHẨN ĐOÁN vì sao thiết bị không còn gửi dữ liệu (kết nối)
```

Đáp án đúng: **D (AWS IoT Device Management)**. Anh chọn đúng. Mấu chốt: đề nói thẳng Device Defender "không giúp chẩn đoán gián đoạn kết nối" nên phải tìm service khác chuyên monitor fleet.

#### Vì sao D đúng

AWS IoT Device Management dùng để register, organize, monitor, troubleshoot và remote-manage thiết bị ở quy mô lớn. Khi đăng ký thiết bị vào đây, admin theo dõi được health của từng thiết bị và xác nhận chúng còn kết nối tới IoT Core hay không. Từ đó biết nguyên nhân DynamoDB không cập nhật là do thiết bị mất kết nối hay do chỗ khác. Ngoài ra còn nhóm thiết bị (groups) theo chức năng/bảo mật để xem metrics hoặc thao tác hàng loạt.

#### Các option còn lại

| Option | Dịch vụ làm gì thật sự | Vì sao sai |
|---|---|---|
| A. IoT SiteWise | Thu thập và phân tích dữ liệu thiết bị công nghiệp | Không phải công cụ troubleshoot kết nối, không dùng để "gom dữ liệu từ IoT devices" cho kịch bản này |
| B. Device Defender thêm CA | Audit, cảnh báo, mitigation bảo mật | Không quản lý CA trong IoT Core, không thiết lập kết nối; đề đã loại sẵn Defender |
| C. Lambda + IoT 1-Click | 1-Click dành cho thiết bị nút bấm đơn giản | Ghi thẳng vào DynamoDB là bỏ qua IoT Core, không chẩn đoán được kết nối |

#### Quy tắc nhớ cho thi

- **Thấy "monitor / troubleshoot fleet, device health, connectivity"** → **IoT Device Management**.
- **Thấy "audit security policy, abnormal behavior"** → **IoT Device Defender**.
- **Thấy "industrial equipment data"** → **IoT SiteWise**.
- **Thấy "simple one-button device trigger Lambda"** → **IoT 1-Click**.
- Đáp án "đi đường vòng bỏ qua IoT Core" gần như luôn sai vì không giải quyết nguyên nhân.

### TD explanation

Correct 

AWS IoT Device Management is a service that makes it easy to securely register, organize, monitor, and remotely manage IoT devices at scale throughout their lifecycle. You can use IoT Device Management to upload and view device information and configuration, organize your device inventory, monitor your fleet of devices, troubleshoot individual devices, and remotely manage devices deployed across many locations, including updating device software over-the-air (OTA).

 

By registering the IoT devices to AWS IoT Device Management, the system administrator can monitor the health of the devices and ensure connectivity to AWS IoT Core. This will help identify if there are connectivity issues that might be causing the lack of updates in the DynamoDB table.

 

![image](https://media.tutorialsdojo.com/public/AWSIoTDeviceManagementConsole.jpg)

 

AWS IoT Device Management has a feature that allows you to group your device fleet based on function, security requirements, or other categories. This makes it easier to manage IoT devices at scale. The groupings allow policy management, viewing metrics, or performing actions on the entire group.

 

Therefore, the correct answer is: **Register the IoT devices to AWS IoT Device Management and monitor the devices’ health and ensure the devices are connected to AWS IoT Core.**

 

The option that says: **Use AWS IoT Device Defender to add the Certificate Authority of the X.509 certificates used by the devices when connecting to AWS IoT Core, and establish connectivity**  is incorrect. AWS IoT Defender is primarily used for security audit, alerting, and mitigation of IoT resources and does not directly manage Certificate Authority in AWS IoT Core. It is also not used for establishing connectivity between the devices and AWS IoT Core.

 

The option that says: **Use AWS IoT SiteWise to collect the data directly from the IoT devices and send the aggregated data to IoT Core** is incorrect. AWS IoT SiteWise is simply used for collecting and gaining insights to equipment data for industrial operations management. It is not used for collecting data from IoT devices.

 

The option that says: **Trigger an AWS Lambda function adding updates to the DynamoDB table by integrating the IoT devices with IoT 1-Click**  is incorrect. Triggering a Lambda function does not address the potential connectivity issue between the IoT devices and AWS IoT Core. Using it to directly update the DynamoDB table will bypass AWS IoT Core and is not the solution to the question.

 

**References:**

 

[https://aws.amazon.com/iot-device-management/faq/](https://aws.amazon.com/iot-device-management/faq/)

 

[https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html)

 

 

**Check out this AWS IoT Core Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-iot-core/](https://tutorialsdojo.com/aws-iot-core/)

</details>

<a id="q39"></a>

## Q39

A health insurance company has recently adopted a hybrid cloud architecture which connects their on-premises network and their cloud infrastructure in AWS. They have an ELB which has a set of EC2 instances behind them. As the cloud engineer of the company, your manager instructed you to ensure that the SSL key used to encrypt data is always kept secure at all times. In addition, the application logs should only be decrypted by a handful of key users.



In this scenario, which of the following meets all of the requirements?

- **A.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Use TCP load balancing on the ELB and configure your EC2 instances to retrieve the private key from a non-public S3 bucket on boot. 3. Persist your application server logs to a private S3 bucket using SSE.
- **B.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Upload the private key to the EC2 instances and configure it to offload the SSL traffic. 3. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.
- **C.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Configure the ELB to perform TCP load balancing. 3. Use an AWS CloudHSM instance to perform the SSL transactions. 4. Persist your application server logs to a private S3 bucket using SSE.
- **D.** 1. Use the ELB to distribute traffic to a set of EC2 instances. 2. Configure the ELB to perform TCP load balancing. 3. Use an AWS CloudHSM instance to perform the SSL transactions. 4. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C (you answered correctly)

🔑 **Key words:** SSL key must always be secure; logs decryptable only by a few key users

⚠️ **Watch:** Twin options: C = logs in a private S3 bucket with SSE; D = logs on an ephemeral volume encrypted with a random AES key (lost when the instance stops)

🧠 **Rule:** Keep the SSL private key in a HSM → TCP pass-through on the ELB + CloudHSM does the SSL; logs → private S3 with SSE (durable).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client ──HTTPS──► ELB ──► EC2 instances
                           │
                           ├─ SSL private key  ─► phải LUÔN an toàn
                           └─ Application logs ─► chỉ vài key users giải mã được
```

Đáp án đúng: **C** (TCP load balancing + CloudHSM làm SSL + logs lên private S3 với SSE). Anh chọn đúng. Cặp twin cần soi kỹ: **C vs D** giống hệt phần 1 đến 3, chỉ khác bước 4 (nơi lưu log).

#### Vì sao C đúng

- **ELB làm TCP load balancing:** traffic SSL đi xuyên qua (pass-through) tới EC2, ELB không giải mã nên private key không phải nằm trên ELB.
- **CloudHSM thực hiện SSL transaction:** private key của web server nằm trong HSM (FIPS 140-2 Level 3), không bao giờ nằm trên EC2 hay S3. Đây là cách offload SSL/TLS chuẩn của CloudHSM, vừa giảm tải web server vừa tăng bảo mật.
- **Logs lên private S3 + SSE:** lưu bền vững, mã hóa at rest, và quyền giải mã/đọc giới hạn cho số ít user được cấp quyền.

#### Cặp twin C vs D

| | C | D |
|---|---|---|
| SSL key | CloudHSM | CloudHSM |
| Nơi lưu log | Private S3 + SSE (bền vững) | Ephemeral volume + AES key ngẫu nhiên |
| Kết quả | Đạt | Loại |

D sai vì ephemeral volume chỉ là lưu trữ tạm, không phải durable storage (TD: "ephemeral volume is just temporary storage"). Instance dừng/terminate thì log mất, và key AES ngẫu nhiên cũng không có cơ chế giới hạn "chỉ vài key users giải mã". Đề chỉ muốn log được lưu bền vững và bảo mật.

#### Các option còn lại

- **A:** lấy private key từ S3 bucket lúc boot. TD: không bao giờ lưu private key nhạy cảm trong S3, ngay cả bucket private. Key bị kéo về EC2 nên không còn "always secure".
- **B:** upload private key lên EC2 để offload SSL (key nằm trên instance, có thể bị lộ) và log đặt trên ephemeral volume (mất khi instance dừng). Sai cả hai yêu cầu.

#### Quy tắc nhớ cho thi

- **Thấy "SSL private key phải luôn an toàn"** → **CloudHSM** + ELB **TCP** (không terminate SSL ở ELB).
- **Thấy "key trong S3 / trên EC2"** → loại.
- **Thấy "logs cần bền vững + giới hạn người giải mã"** → **private S3 + SSE**, không phải ephemeral volume.
- **Thấy "ephemeral"** → tạm thời, mất dữ liệu khi instance dừng.

### TD explanation

Correct 

**AWS CloudHSM**  is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud. With CloudHSM, you can manage your own encryption keys using FIPS 140-2 Level 3 validated HSMs. CloudHSM offers you the flexibility to integrate with your applications using industry-standard APIs, such as PKCS#11, Java Cryptography Extensions (JCE), and Microsoft CryptoNG (CNG) libraries.

 

You can use **AWS CloudHSM to offload SSL/TLS**  processing for your web servers. Using CloudHSM for this processing reduces the burden on your web server and provides extra security by storing your web server’s private key in CloudHSM. Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are used to confirm the identity of web servers and establish secure HTTPS connections over the Internet.

 

![image](https://media.tutorialsdojo.com/sap_hsm_ssl_offload.png)

 

AWS CloudHSM automates time-consuming HSM administrative tasks for you, such as hardware provisioning, software patching, high availability, and backups. You can scale your HSM capacity quickly by adding and removing HSMs from your cluster on-demand. AWS CloudHSM automatically load balances requests and securely duplicates keys stored in any HSM to all of the other HSMs in the cluster.

 

CloudHSM provides a better and more secure way of offloading the SSL processing for the web servers and ensures the application logs are durably and securely stored.

 

In this scenario, the following option is the best choice because it uses CloudHSM and the application server logs are persisted in an S3 bucket with a Server Side Encryption (SSE):

 

**1. Use the ELB to distribute traffic to a set of EC2 instances.** 
  **2. Configure the ELB to perform TCP load balancing.** 
  **3. Use an AWS CloudHSM instance to perform the SSL transactions.** 
  **4. Persist your application server logs to a private S3 bucket using SSE.**

 

The following sets of options are incorrect because the ephemeral volume is just temporary storage and hence, not a suitable option for durable storage:

 

**1. Use the ELB to distribute traffic to a set of EC2 instances.** 
  **2. Upload the private key to the EC2 instances and configure it to offload the SSL traffic.** 
  **3. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.**

 

as well as this option:

 

**1. Use the ELB to distribute traffic to a set of EC2 instances.** 
  **2. Configure the ELB to perform TCP load balancing.** 
  **3. Use an AWS CloudHSM instance to perform the SSL transactions.** 
  **4. Persist your application server logs to an ephemeral volume that has been encrypted using a randomly generated AES key.**

 

The following option is incorrect because you should never store sensitive private keys in S3:

 

**1. Use the ELB to distribute traffic to a set of EC2 instances.** 
  **2. Use TCP load balancing on the ELB and configure your EC2 instances to retrieve the private key from a non-public S3 bucket on boot.** 
  **3. Persist your application server logs to a private S3 bucket using SSE.**

 

 

**References:**

 

[https://aws.amazon.com/cloudhsm/](https://aws.amazon.com/cloudhsm/)

 

[https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload-overview.html](https://docs.aws.amazon.com/cloudhsm/latest/userguide/ssl-offload-overview.html)

</details>

<a id="q68"></a>

## Q68

A company is running thousands of virtualized Linux and Microsoft Windows servers on its on-premises data center. The virtual servers host a range of Java and PHP applications that use MySQL and Oracle databases. There are also several department services hosted on an external data center. The company uses SAN storage to provide iSCSI disks to its physical servers. The company wants to migrate its data center to the AWS Cloud, but the technical documentation of the systems is incomplete and outdated. The Solutions Architect was tasked to analyze the current environment and estimate the cost of migrating the resources to the cloud.



Which of the following should the Solutions Architect do to effectively plan the cloud migration? (Select THREE.)

- **A.** Use the AWS Transform discovery tool to gather information about the running virtual machines and running applications inside the servers.
- **B.** Use Amazon Inspector to scan and assess the applications deployed on the on-premises virtual machines and save the generated report to an Amazon S3 bucket.
- **C.** Use AWS Transform migration assessment jobs and workspaces to estimate migration costs, generate right-sizing recommendations, produce reports, and support migration planning.
- **D.** Use AWS X-Ray to analyze the applications running on the servers and identify possible errors that may be encountered during the migration.
- **E.** Use AWS Transform MGN to automate the migration of the on-premises virtual machines to the AWS Cloud.
- **F.** Generate a migration readiness assessment report with the AWS Cloud Adoption Readiness Tool (CART) to highlight gaps in organizational skills and processes.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, C, F (you answered correctly)

🔑 **Key words:** incomplete documentation, analyze current environment, estimate migration cost, plan migration (Select THREE)

⚠️ **Watch:** Inspector/X-Ray don't discover inventory; MGN executes the migration, it doesn't plan or estimate cost

🧠 **Rule:** Plan a migration → discovery (AWS Transform discovery) + assessment/cost (Transform assessments) + readiness (CART).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Thousands of VMs (Linux + Windows) on-prem + external DC, tài liệu thiếu/cũ
        │
        ▼
 Chưa migrate. Việc cần làm lúc này = LẬP KẾ HOẠCH:
   1. Biết có gì        (discovery inventory)
   2. Ước tính chi phí  (assessment / right-sizing)
   3. Biết tổ chức đã sẵn sàng chưa (readiness)
```

Đáp án đúng: **A, C, F** (Select THREE). Anh chọn đúng cả ba.

#### Ba lựa chọn ghép thành MỘT quy trình lập kế hoạch

| Bước | Option | Vai trò |
|---|---|---|
| Khám phá | **A. AWS Transform discovery tool** | Tự động discover server inventory (VMware vCenter, Hyper-V, imported servers). Giải quyết vấn đề "tài liệu cũ và thiếu". |
| Ước tính | **C. AWS Transform migration assessment** | Cost estimate, right-sizing tự động, so sánh nhiều kịch bản, tạo report. Khớp yêu cầu "estimate the cost". |
| Sẵn sàng | **F. CART** | Khảo sát 16 câu, đánh giá readiness qua 6 perspective (business, people, process, platform, operations, security), chỉ ra gap về kỹ năng và quy trình. |

#### Ba option sai

- **B. Amazon Inspector:** dịch vụ đánh giá bảo mật và compliance, không phải công cụ discovery inventory hay ước tính chi phí. TD: không hữu ích để đánh giá ứng dụng ở on-prem data center.
- **D. AWS X-Ray:** debug và trace ứng dụng phân tán đang chạy production (microservices). Không giúp lập kế hoạch migration.
- **E. AWS Transform MGN:** dùng để THỰC HIỆN migrate VM. Đề đang ở giai đoạn phân tích trước khi migrate, nên MGN chưa phải bước lúc này.

📝 **Ghi chú kỹ thuật:** tên dịch vụ trong đề (AWS Transform) là cách gọi theo TD của bộ đề này. Điều cần nhớ là phân loại chức năng: discovery, assessment, readiness thuộc nhóm "plan"; MGN thuộc nhóm "execute".

#### Quy tắc nhớ cho thi

- **Thấy "tài liệu thiếu, cần biết đang chạy gì"** → **discovery tool**.
- **Thấy "estimate migration cost, right-sizing"** → **migration assessment**.
- **Thấy "organizational readiness, skills/process gaps"** → **CART**.
- **Thấy "plan migration"** → loại **MGN** (execute), **Inspector** (security), **X-Ray** (tracing).
- Select THREE: kiểm tra ba đáp án cover ba mặt khác nhau (inventory, cost, readiness), đừng chọn trùng chức năng.

### TD explanation

Correct 

The scenario requires tools of services that will help to effectively plan the cloud migration, so the answers should be focused on planning.

 

**AWS Transform**  is a service designed to accelerate and simplify the transformation of infrastructure, applications, and code through an intelligent AI experience. It offers specialized tools that streamline modernization and migration efforts across various workloads.

 

With AWS Transform, you can:

 

– Modernize and migrate IBM z/OS and Fujitsu GS21 to AWS

 

– Migrate VMware workloads to Amazon EC2

 

– Modernize .NET applications to Linux-ready cross-platform .NET

 

– Assess workloads for migration readiness

 

![image](https://media.tutorialsdojo.com/public/AWS Transform-16JUN2026.png)

 

AWS Transform assists in offloading labor-intensive and complex transformation tasks during the discovery, planning, and execution phases to AI agents with expertise in various languages, frameworks, and infrastructures. This approach allows your teams to focus on innovation while efficiently transforming complex, large-scale projects through a unified web experience.

 

**The AWS Transform discovery tool**  assists you in automatically discovering the server inventory within your organization in preparation for migration. This tool supports VMware vCenter, Microsoft Hyper-V, and imported servers. To utilize the discovery tool, you need to configure one or more discovery sources, allow the tool to run, and then review the results displayed in the Discovered Inventory pane.

 

Once you configure a discovery source, the tool will begin collecting information. The time required for the discovery tool to completely analyze your network depends on the size of your environment. For businesses utilizing a directional migration approach, you can leverage the Migration Portfolio Assessment (MPA) files generated by the tool after the server collection is completed.

 

The **AWS Cloud Adoption Readiness Tool (CART)**  helps organizations of all sizes develop efficient and effective plans for cloud adoption and enterprise cloud migrations. This 16-question online survey and assessment report detail your cloud migration readiness across six perspectives, including business, people, process, platform, operations, and security. Once you complete a CART survey, you can provide your contact details to download a customized cloud migration assessment that charts your readiness and what you can do to improve it. This tool is designed to help organizations assess their progress with cloud adoption and identify gaps in organizational skills and processes.

 

**AWS Transform assessments**  evaluate the cost, feasibility, and business value of migrating on-premises infrastructure to AWS. These assessments provide automated right-sizing recommendations, multi-scenario comparisons, and interactive refinement through chat.

 

You can apply migration assessments for several objectives:

 

– Get cost estimates for Amazon RDS for SQL Server, Amazon EC2, Amazon EBS, Amazon S3, and Amazon FSx

 

– Receive automated right-sizing recommendations

 

– Assess business value and sustainability impact

 

– Compare multiple migration scenarios side by side

 

– Refine assessments interactively through chat

 

– Generate executive presentations and detailed reports

 

Therefore, the correct answers are:

 

**– Use the AWS Transform Discovery Tool to gather information about the running virtual machines and running applications inside the servers.**

 

**– Generate a migration readiness assessment report with the AWS Cloud Adoption Readiness Tool (CART) to highlight gaps in organizational skills and processes.**

 

**– Use AWS Transform migration assessment jobs and workspaces to estimate migration costs, generate right-sizing recommendations, produce reports, and support migration planning.**

 

The option that says: **Use AWS Transform MGN to automate the migration of the on-premises virtual machines to the AWS Cloud**  is incorrect because MGN is primarily used for the actual migration of your on-premises virtual machines to the AWS Cloud and not for planning. Take note that in the scenario, the Solutions Architect was tasked to analyze the existing on-premises architecture first before doing the actual migration to AWS.

 

The option that says: **Use AWS X-Ray to analyze the applications running on the servers and identify possible errors that may be encountered during the migration**  is incorrect because AWS X-Ray is typically used to debug production and distributed applications, such as those built using a microservices architecture. This is not helpful for planning the migration.

 

The option that says: **Use Amazon Inspector to scan and assess the applications deployed on the on-premises virtual machines and save the generated report to an Amazon S3 bucket**  is incorrect because Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. This is not helpful for assessing the applications on the on-premises data center.

 

 

**References:**

 

[https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html)

 

[https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html)

 

[https://docs.aws.amazon.com/transform/latest/launchguide/resources.html](https://docs.aws.amazon.com/transform/latest/launchguide/resources.html)

 

[https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html)

 

 

**Check out this AWS Migration Strategies Cheat Sheet:**

 

[https://tutorialsdojo.com/aws-migration-strategies-the-7-rs/](https://tutorialsdojo.com/aws-migration-strategies-the-7-rs/)

</details>

<a id="q72"></a>

## Q72

A company stores several terabytes of data on an Amazon S3 bucket. The data will be made available to respective partner companies, however, the management doesn’t want the partner companies to access the files directly from Amazon S3 URLs. The solutions architect has been asked to ensure that all confidential files shared via Amazon S3 should only be accessible through CloudFront.



Which of the following options could satisfy this requirement?

- **A.** Create an Origin Access Control (OAC) and associate it with your CloudFront distribution. Change the permissions on your Amazon S3 bucket so that only the origin access control has read permission.
- **B.** Write individual policies for each S3 bucket containing the confidential documents that would grant CloudFront access.
- **C.** Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and the target bucket as the Amazon Resource Name (ARN).
- **D.** Assign an IAM user that is granted access to objects in the S3 bucket to CloudFront.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A (you answered correctly)

🔑 **Key words:** files only through CloudFront, not direct S3 URLs

⚠️ **Watch:** A distribution ID is not a valid IAM principal; IAM users can't be assigned to CloudFront

🧠 **Rule:** Private S3 origin behind CloudFront → Origin Access Control + bucket policy allowing only the OAC.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Partner ──X──► https://bucket.s3.amazonaws.com/file   (phải bị chặn)
Partner ─────► CloudFront ──(OAC)──► S3 bucket        (cách duy nhất)

Yêu cầu: file confidential CHỈ truy cập được qua CloudFront
```

Đáp án đúng: **A**. Anh chọn đúng.

#### Vì sao A đúng

```
1. Tạo Origin Access Control (OAC), gắn vào CloudFront distribution
2. Bucket S3 để private, bucket policy chỉ cho phép OAC đọc
   → CloudFront đọc được S3, URL S3 trực tiếp thì không
```

OAC là "danh tính" đặc biệt của CloudFront để truy cập S3 origin. Khi bucket chỉ cấp quyền đọc cho OAC, CloudFront có quyền truy cập độc quyền và user không dùng được direct S3 URL. Kết hợp thêm signed URL/signed cookies nếu muốn giới hạn người xem ở tầng CloudFront (TD đề cập cách này).

#### Các option còn lại

- **B (policy riêng cho từng bucket cấp quyền CloudFront):** TD: không cần viết policy riêng cho từng bucket theo kiểu đó, và cách nêu không chặn được truy cập S3 trực tiếp. Thiếu khái niệm OAC.
- **C (bucket policy với CloudFront distribution ID làm Principal):** distribution ID không phải một IAM principal hợp lệ. TD kết luận cách này không ngăn được truy cập trực tiếp qua S3 URL.
- **D (gán IAM user cho CloudFront):** IAM user không gán cho CloudFront được; TD: cách này không cho CloudFront quyền truy cập độc quyền vào bucket.

📝 **Ghi chú kỹ thuật:** ngoài đời, bucket policy của OAC thật ra dùng service principal của CloudFront kèm condition trên distribution ARN. Nhưng cách tạo OAC rồi giới hạn quyền đọc chỉ cho OAC (option A) mới là đáp án đúng theo đề, còn option C ghi "distribution ID làm Principal" thì sai.

#### Lưu ý thực tế

- Bucket vẫn phải chặn public access để direct URL thật sự bị từ chối.
- OAC là cơ chế mới thay cho OAI (Origin Access Identity) cũ; thấy hai thuật ngữ trong đề thì ưu tiên OAC.

#### Quy tắc nhớ cho thi

- **Thấy "chỉ truy cập qua CloudFront, không qua S3 URL"** → **OAC + bucket policy chỉ cho OAC**.
- **Thấy "S3 presigned URL"** → tạm thời cho từng object, không ép đi qua CloudFront.
- **Thấy "IAM user cho CloudFront" hoặc "distribution ID làm Principal"** → loại.

### TD explanation

Correct 

To restrict access to content that you serve from **Amazon S3**  buckets, you create **CloudFront signed URLs**  or **signed cookies**  to limit access to files in your Amazon S3 bucket, and then you create a special CloudFront user called an origin access control (OAC) and associate it with your distribution. Then you configure permissions so that CloudFront can use the OAC to access and serve files to your users, but users can’t use a direct URL to the S3 bucket to access a file there. Taking these steps helps you maintain secure access to the files that you serve through CloudFront.

 

In general, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you can either allow everyone to have access to the files there, or you can restrict access. If you limit access by using, for example, CloudFront signed URLs or signed cookies, you also won’t want people to be able to view files by simply using the direct URL for the file. Instead, you want them to only access the files by using the CloudFront URL, so your protections work.

 

![image](https://media.tutorialsdojo.com/sap_cloudfront_oia.png)

 

Typically, if you’re using an Amazon S3 bucket as the origin for a CloudFront distribution, you grant everyone permission to read the objects in your bucket. This allows anyone to access your objects either through CloudFront or using the Amazon S3 URL. CloudFront doesn’t expose Amazon S3 URLs, but your users might have those URLs if your application serves any objects directly from Amazon S3 or if anyone gives out direct links to specific objects in Amazon S3.

 

Therefore, the correct answer is: **Create an Origin Access Control (OAC) and associate it with your CloudFront distribution. Change the permissions on your Amazon S3 bucket so that only the origin access control has read permission.**  It gives CloudFront exclusive access to the S3 bucket and prevents other users from accessing the public content of S3 directly via S3 URL.

 

The option that says: **Write an S3 bucket policy that assigns the CloudFront distribution ID as the Principal and the target bucket as the Amazon Resource Name (ARN)**  is incorrect. Creating a bucket policy is unnecessary and it does not prevent other users from accessing the public content of S3 directly via S3 URL.

 

The option that says: **Assign an IAM user that is granted access to objects in the S3 bucket to CloudFront**  is incorrect. This does not give CloudFront exclusive access to the S3 bucket.

 

The option that says: **Write individual policies for each S3 bucket containing the confidential documents that would grant CloudFront access**  is incorrect. You do not need to create any individual policies for each bucket.

 

 

**References** :

 

[https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

 

[https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-access-to-amazon-s3/](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-access-to-amazon-s3/)

 

 

**Check out this Amazon CloudFront Cheat Sheet:**

 

[https://tutorialsdojo.com/amazon-cloudfront/](https://tutorialsdojo.com/amazon-cloudfront/)

 

 

**S3 Pre-signed URLs vs CloudFront Signed URLs vs Origin Access Control (OAC)**

 

[https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai-origin-access-control-oac/](https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai-origin-access-control-oac/)

 

 

**Comparison of AWS Services Cheat Sheets:**

 

[https://tutorialsdojo.com/comparison-of-aws-services/](https://tutorialsdojo.com/comparison-of-aws-services/)

</details>
