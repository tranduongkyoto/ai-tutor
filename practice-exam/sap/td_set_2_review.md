# TD Set 2 — Wrong Answer Review (32 questions)

Source: `TD_SAP_Review_Set2_Full.md` (Q# = shuffled web order). Question, options and explanation are verbatim; 🔑/🪤/🧠 are study notes. Summary: `td_set_2_analysis.md`.

## How to use

1. Read the question, pick your answer **before** opening the answer block.
2. Open **Answer & explanation**; focus on why each wrong option fails.
3. Tick the pass columns in the tracker below. Redo misses after 3–4 days, then again after ~1 week.

## Tracker

| Group | Q | Pass 1 | Pass 2 | Pass 3 |
|---|---|---|---|---|
| A | [Q2](#q2) | ✅ 10-02 | ✅ 10-05 | ☐ |
| A | [Q15](#q15) | ✅ 10-02 | ✅ 10-05 | ☐ |
| A | [Q26](#q26) | ✅ 10-02 | ✅ 10-05 | ☐ |
| A | [Q28](#q28) | ✅ 10-02 | ✅ 10-05 | ☐ |
| A | [Q31](#q31) | ✅ 10-02 | ✅ 10-05 | ☐ |
| A | [Q41](#q41) | ✅ 10-02 | ✅ 10-05 | ☐ |
| A | [Q62](#q62) | ✅ 10-02 | ✅ 10-05 | ☐ |
| A | [Q66](#q66) | ✅ 10-02 | ✅ 10-05 | ☐ |
| A | [Q75](#q75) | ✅ 10-02 | ✅ 10-05 | ☐ |
| B | [Q1](#q1) | ✅ 10-02 | ✅ 10-05 | ☐ |
| B | [Q37](#q37) | ✅ 10-02 | ✅ 10-05 | ☐ |
| B | [Q44](#q44) | ✅ 10-02 | ✅ 10-05 | ☐ |
| B | [Q49](#q49) | ✅ 10-02 | ✅ 10-05 | ☐ |
| C | [Q7](#q7) | ✅ 10-02 | ✅ 10-05 | ☐ |
| C | [Q9](#q9) | ✅ 10-02 | ✅ 10-05 | ☐ |
| C | [Q14](#q14) | ✅ 10-02 | ✅ 10-05 | ☐ |
| C | [Q23](#q23) | ✅ 10-02 | ✅ 10-05 | ☐ |
| C | [Q45](#q45) | ✅ 10-02 | ✅ 10-05 | ☐ |
| C | [Q68](#q68) | ✅ 10-02 | ✅ 10-05 | ☐ |
| D | [Q17](#q17) | ✅ 10-02 | ✅ 10-05 | ☐ |
| D | [Q18](#q18) | ✅ 10-02 | ✅ 10-05 | ☐ |
| D | [Q27](#q27) | ✅ 10-02 | ✅ 10-05 | ☐ |
| D | [Q34](#q34) | ✅ 10-02 | ✅ 10-05 | ☐ |
| E | [Q3](#q3) | ✅ 10-02 | ✅ 10-05 | ☐ |
| E | [Q24](#q24) | ✅ 10-02 | ✅ 10-05 | ☐ |
| E | [Q32](#q32) | ✅ 10-02 | ✅ 10-05 | ☐ |
| E | [Q38](#q38) | ✅ 10-02 | ✅ 10-05 | ☐ |
| E | [Q50](#q50) | ✅ 10-02 | ✅ 10-05 | ☐ |
| E | [Q59](#q59) | ✅ 10-02 | ✅ 10-05 | ☐ |
| F | [Q43](#q43) | ✅ 10-02 | ✅ 10-05 | ☐ |
| F | [Q56](#q56) | ✅ 10-02 | ✅ 10-05 | ☐ |
| F | [Q67](#q67) | ✅ 10-02 | ✅ 10-05 | ☐ |

---

# Group A — Identity, access & federation (9)

<a id="q2"></a>

## Q2

There was a major incident that occurred in your company wherein the web application that you are supporting unexpectedly went down in the production environment. Upon investigation, it was found that a junior DevOps engineer terminated the EC2 instance in production which caused the disruption of service. Only the Solutions Architects should be allowed to stop or terminate instances in the production environment. You also found out that there are a lot of developers who have full access to your production AWS account.
Which of the following options will fix this security vulnerability in your cloud architecture and prevent this kind of failure from happening again? (Select TWO.)

- **A.** Modify the IAM policy of the developers to require MFA before deleting EC2 instances.
- **B.** Add tags to the EC2 instances in the production environment and assign the developers a role with a policy that denies terminating the instance based on the tag.
- **C.** Replace the Security Group of all of the EC2 instances in Production to prevent developers from accessing it.
- **D.** Modify the associated IAM Role assigned to the developers by removing the policy that allows them to terminate EC2 instances in production.
- **E.** Attach a PowerUserAccess AWS managed policy to the developers.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D · **You picked:** A, D

🔑 **Key words:** junior engineer terminated prod EC2; only architects may stop/terminate (Select TWO)

🪤 **Your trap:** MFA is an extra login factor — it does not prevent an authorized user from terminating

🧠 **Rule:** Prevent destructive actions → remove the permission or tag-based IAM Deny. MFA ≠ authorization.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Developers (full access)              Production EC2
┌───────────────────────┐             ┌───────────────────────┐
│ IAM policy hiện tại:   │   ───X───►  │ terminate instance    │
│ cho phép terminate EC2 │  (vô tình)  │ → outage               │
└───────────────────────┘             └───────────────────────┘

Yêu cầu: CHỈ Solutions Architects được stop/terminate ở prod
         → ngăn chuyện này LẶP LẠI (Select TWO)
```

Đáp án đúng: **B (tag-based Deny policy)** + **D (gỡ quyền terminate khỏi IAM Role của developers)**. Anh chọn đúng D, nhưng chọn A (MFA) thay vì B.

#### B đúng — Deny theo tag là lớp bảo vệ có thể mở rộng

```
IAM policy cho developers:
  Effect: Deny
  Action: ec2:TerminateInstance, ec2:StopInstances
  Resource: *
  Condition: ec2:ResourceTag/Environment = "production"
```

Tag `Environment=production` gắn trên instance, sau đó policy Deny dựa theo tag này. Cách này **scale tốt**: thêm instance mới vào prod chỉ cần gắn đúng tag, không phải sửa policy thủ công từng lần. Đây là lý do TD gọi nó "scalable, secure approach".

#### D đúng — gỡ thẳng quyền terminate khỏi Role

Developers hiện có full access (bao gồm quyền terminate EC2 trong prod). Sửa lại IAM Role, bỏ hẳn action `ec2:TerminateInstance`/`ec2:StopInstances` ra khỏi policy đính kèm → developers không còn khả năng thực hiện hành động đó nữa, bất kể resource nào.

B và D cùng giải quyết vấn đề nhưng theo hai hướng bổ sung nhau: D thu hẹp quyền ở gốc (role), B thêm lớp chặn theo tag để kiểm soát chi tiết hơn theo môi trường — TD chọn cả hai vì đề là Select TWO và hai lựa chọn này không mâu thuẫn, cùng hướng tới loại bỏ khả năng terminate ở prod.

#### A sai — vì sao MFA trông hợp lý nhưng không chặn được hành vi

**MFA chỉ là một lớp xác thực khi ĐĂNG NHẬP**, không phải một cơ chế ủy quyền (authorization) cho hành động cụ thể. Một khi developer đã đăng nhập thành công (có MFA hay không), IAM vẫn kiểm tra policy để quyết định cho phép hay từ chối `TerminateInstance`. Nếu policy vẫn cho phép hành động này, MFA không ngăn được gì — junior engineer trong tình huống này **không phải kẻ tấn công giả mạo danh tính**, mà là người dùng hợp lệ thực hiện nhầm một hành động được phép. MFA giải quyết bài toán "ai đang đăng nhập", không giải quyết bài toán "người này được làm gì".

```
Authentication (MFA)  →  xác minh DANH TÍNH khi login
Authorization (IAM policy) → xác minh HÀNH ĐỘNG được phép hay không
Vấn đề của đề bài nằm ở Authorization, không phải Authentication
```

#### Các lựa chọn sai còn lại

- **C — đổi Security Group:** Security Group chỉ kiểm soát traffic mạng (inbound/outbound), không liên quan gì đến quyền gọi EC2 API như TerminateInstance.
- **E — gắn PowerUserAccess:** policy này cấp quyền rộng hơn (gần như full access trừ IAM), đi ngược hoàn toàn với yêu cầu thắt chặt quyền.

| Lựa chọn | Lớp kiểm soát | Có chặn được terminate không |
|---|---|---|
| **B. Tag-based Deny** | Authorization, scalable theo tag | Có |
| **D. Gỡ quyền khỏi Role** | Authorization, gốc rễ | Có |
| A. MFA | Authentication | Không |
| C. Security Group | Network | Không liên quan |
| E. PowerUserAccess | Authorization nhưng mở rộng quyền | Ngược hướng |

#### Quy tắc nhớ cho thi

- **"Người dùng hợp lệ lỡ tay làm sai"** → sửa IAM policy/role (authorization), không phải MFA
- **MFA** → chỉ trả lời câu hỏi "ai đang login", không trả lời "được làm gì"
- **"Chỉ muốn chặn một nhóm resource (vd: production)"** → Deny theo Condition tag, scale tốt hơn sửa thủ công từng resource

### TD explanation

To help you manage your instances, images, and other Amazon EC2 resources, you can optionally assign your own metadata to each resource in the form of tags. Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have many resources of the same type—you can quickly identify a specific resource based on the tags you’ve assigned to it. For example, you could define a set of tags for your account’s Amazon EC2 instances that help you track each instance’s owner and stack level.

Take note that MFA is just an additional layer of security but it won’t totally prevent the users from terminating the EC2 instances.
Adding tags to the EC2 instances in the production environment and assign the developers a role with a policy that denies terminating the instance based on the tag is correct because it leverages resource tags for identification and IAM roles/policies for access control, following the principle of least privilege and providing a scalable, secure approach to prevent unauthorized termination of production instances while adhering to AWS best practices.
Modifying the associated IAM Role assigned to the developers by removing the policy that allows them to terminate EC2 instances in production is correct because changing the IAM Role assigned to the developers to revoke their privilege of terminating EC2 instances will certainly prevent the issue from happening again.
Modifying the IAM policy of the developers to require MFA before deleting EC2 instances is incorrect because MFA is just an additional layer of security given to the users when logging into AWS and accessing the resources. However, an MFA alone cannot prevent the users from performing resource level actions, such as terminating the instance.
Replacing the Security Group of all of the EC2 instances in Production to prevent developers from accessing it is incorrect because a security group is mainly used to secure and control the traffic coming in and out of the EC2 instances. In this scenario, it is best to modify the IAM policy of all of the developers and add tags to the instances in the production environment.
Attaching a PowerUserAccess AWS managed policy to the developers is incorrect because it will only provide more permissive access to terminate EC2 instances.

References:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html
https://aws.amazon.com/iam/details/mfa/
https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html

Check out these Amazon EC2 and AWS IAM Cheat Sheets:
https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q15"></a>

## Q15

A multinational healthcare company plans to launch a new MedTech information website. The solutions architect decided to use Amazon CloudFormation to deploy a three-tier web application that consists of a web tier, an application tier, and a database tier that will utilize Amazon DynamoDB for storage. The solutions architect must secure any credentials that are used to access the database tier. The company already uses AWS CloudTrail Lake data store to audit API activity and track credential usage across its AWS accounts.
Which of the following options will allow the application instances access to the DynamoDB tables without exposing API credentials?

- **A.** Create an IAM User in the CloudFormation template and assign permissions to read and write from the DynamoDB table. Then retrieve the values of the access and secret keys using CloudFormation's GetAtt function, and pass them to the application instance through user-data.
- **B.** Create an IAM Role and assign the required permissions to read and write from the DynamoDB table. Have the instance profile property of the application instance reference the role.
- **C.** Create an IAM Role that grants access to the DynamoDB table. Use the AWS::SSM::Parameter resource that creates an SSM parameter in AWS Systems Manager Parameter Store containing the Amazon Resource Name of the IAM role. Have the instance profile property of the application instance reference the role.
- **D.** Have the user enter the access and secret keys of an existing IAM User that has permissions to read and write from the DynamoDB table instead of using the Parameter section in the CloudFormation template.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** CloudFormation 3-tier, DynamoDB, no exposed API credentials

🪤 **Your trap:** Storing the role ARN in Parameter Store adds nothing — the instance profile already binds the role

🧠 **Rule:** EC2 → AWS service access = IAM role via instance profile. Nothing else needed.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
CloudFormation stack (3-tier)
┌─────────────┐   ┌──────────────────┐   ┌─────────────┐
│ Web tier    │──►│ App tier (EC2)    │──►│ DynamoDB    │
└─────────────┘   └──────────────────┘   └─────────────┘
                   Cần đọc/ghi DynamoDB
                   KHÔNG được lộ API credentials (access/secret key)
```

Đáp án đúng: **B — IAM Role + instance profile, không cần gì thêm**. Anh chọn C (thêm SSM Parameter Store lưu ARN của role) — bước thừa không cần thiết.

#### B đúng — instance profile đã làm hết việc cần làm

```
AWS::IAM::Role  (permissions: dynamodb:GetItem, PutItem, ...)
      │
      ▼
AWS::IAM::InstanceProfile  (reference role)
      │
      ▼
EC2 instance (property: IamInstanceProfile)
      │
      ▼
App code gọi AWS SDK → SDK tự lấy temporary credentials từ instance metadata
```

EC2 instance chỉ cần có **instance profile** trỏ tới role đã gán quyền DynamoDB. SDK trên instance tự động lấy **temporary credentials** (xoay vòng tự động) từ metadata service — không bao giờ cần access key/secret key tĩnh, không cần lưu trữ hay truyền tay bất kỳ thông tin nào thêm.

#### C sai — vì sao thêm SSM Parameter trông "chắc chắn hơn" nhưng thực ra thừa

Lưu ARN của role vào SSM Parameter Store **không làm thay đổi cách EC2 lấy quyền**. Instance vẫn phải dùng instance profile để "mặc" role đó vào — việc đọc ARN từ Parameter Store rồi làm gì tiếp theo? Không có cơ chế nào để instance "tự gán" role cho chính nó chỉ từ một ARN đọc được lúc runtime. Đây là bước thêm không giải quyết vấn đề gì và không thay thế được property `IamInstanceProfile` bắt buộc trên resource EC2/launch template.

#### Các lựa chọn sai còn lại

- **A — IAM User + GetAtt lấy access/secret key rồi nhét vào user-data:** vi phạm thẳng yêu cầu "không lộ API credentials" — user-data là plaintext, dễ bị đọc lại qua metadata hoặc log.
- **D — nhập tay access/secret key của IAM User có sẵn:** cùng lỗi với A, lại còn thủ công, không tự động hóa, không xoay vòng được.

| Lựa chọn | Có lộ credentials không | Cần bước thừa |
|---|---|---|
| **B. IAM Role + instance profile** | Không (temporary, tự xoay) | Không |
| A. IAM User + GetAtt vào user-data | Có | — |
| C. Role + ARN trong SSM Parameter | Không | Có, thừa |
| D. Nhập tay access/secret key | Có | — |

#### Lưu ý thực tế

CloudTrail Lake trong đề chỉ là bối cảnh để audit API activity — không ảnh hưởng tới lựa chọn đáp án, vì bất kể dùng Role hay User, CloudTrail đều ghi lại được. Đừng để chi tiết này làm phức tạp câu hỏi.

#### Quy tắc nhớ cho thi

- **"EC2 cần gọi AWS service, không lộ credentials"** → IAM Role + instance profile, hết
- **Thấy "lưu ARN của role vào Parameter Store/S3/đâu đó"** → thường là bước thừa, kiểm tra kỹ xem có cần không
- **Access key/secret key xuất hiện trong user-data hoặc GetAtt** → luôn sai khi đề nhấn mạnh "không lộ credentials"

### TD explanation

Applications that run on an EC2 instance must include AWS credentials in their AWS API requests. You could have your developers store AWS credentials directly within the EC2 instance and allow applications in that instance to use those credentials. But developers would then have to manage the credentials and ensure that they securely pass the credentials to each instance and update each EC2 instance when it’s time to rotate the credentials. That’s a lot of additional work.
Instead, you can and should use an IAM role to manage temporary credentials for applications that run on an EC2 instance. When you use a role, you don’t have to distribute long-term credentials (such as a user name and password or access keys) to an EC2 instance. Instead, the role supplies temporary permissions that applications can use when they make calls to other AWS resources. When you launch an EC2 instance, you specify an IAM role to associate with the instance. Applications that run on the instance can then use the role-supplied temporary credentials to sign API requests.
An IAM role is similar to a user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials (password or access keys) associated with it. Instead, if a user assumes a role, temporary security credentials are created dynamically and provided to the user. The scenario requires the instance to have access to DynamoDB tables without having to use the API credentials. In such scenarios, always think of creating IAM Roles rather than IAM Users.

Therefore, the correct answer is: Create an IAM Role and assign the required permissions to read and write from the DynamoDB table. Have the instance profile property of the application instance reference the role. It uses an IAM Role with the appropriate permissions to access the resource, and it references that Role in the instance profile property of the application instance.
The option that says: Create an IAM User in the CloudFormation template and assign permissions to read and write from the DynamoDB table. Then retrieve the values of the access and secret keys using CloudFormation’s GetAtt function, and pass them to the application instance through user-data is incorrect because you should never expose the Access and Secret Keys while accessing AWS resources, and using an IAM Role is a simply more secure way of accessing the resources than using IAM Users with security credentials.
The option that says: Create an IAM Role that grants access to the DynamoDB table. Use the AWS::SSM::Parameter resource that creates an SSM parameter in AWS Systems Manager Parameter Store containing the Amazon Resource Name of the IAM role. Have the instance profile property of the application instance reference the role is incorrect because storing the ARN of the IAM Role in the AWS Systems Manager Parameter Store is not the proper way to attach the role to the application instance. You have to use the instance profile property (AWS::IAM::InstanceProfile) instead.
The option that says: Have the user enter the access and secret keys of an existing IAM User that has permissions to read and write from the DynamoDB table instead of using the Parameter section in the CloudFormation template is incorrect because you should never just expose the Access and Secret Keys while accessing the AWS resources, and using IAM Role is a more secure way of accessing the resources than using IAM Users with security credentials.
References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q26"></a>

## Q26

A company is implementing cloud best practices for its infrastructure. The Solutions Architect is using AWS CloudFormation templates for infrastructure-as-code of its two-tier web application. The application frontend is hosted on an Auto Scaling group of Amazon EC2 instances while the database is an Amazon RDS for MySQL instance. For security purposes, the database password must be rotated every 60 days.
Which of the following solutions is the MOST secure way to store and retrieve the database password for the web application?

- **A.** On the CloudFormation template, create an AWS Secrets Manager secret resource for the database password. Modify the application to retrieve the database password from Secrets Manager when it launches. Use a dynamic reference for the secret resource to be placed as the value of the MasterUserPassword property of the AWS::RDS::DBInstance resource.
- **B.** On the CloudFormation template, create an AWS Secrets Manager secret resource for the database password. Add a UserData property to reference the secret resource in the initialization script of the Auto Scaling group’s launch template using the Ref intrinsic function. Use the Ref intrinsic function to reference the secret resource as the value of the MasterUserPassword property in the AWS::RDS::DBInstance resource.
- **C.** On the CloudFormation template, create a database password parameter. Add a UserData property to reference the password parameter in the initialization script of the Auto Scaling group’s launch template using the Ref intrinsic function. Save the password inside the EC2 instance upon its launch. Use the Ref intrinsic function to reference the parameter as the value of the MasterUserPassword property in the AWS::RDS::DBInstance resource.
- **D.** On the CloudFormation template, create an encrypted parameter using AWS Systems Manager Parameter Store for the database password. Add a UserData property to reference the encrypted parameter in the initialization script of the Auto Scaling group’s launch template. Use the Fn::GetAtt intrinsic function to reference the encrypted parameter as the value of the MasterUserPassword property in the AWS::RDS::DBInstance resource.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** 🔁 CloudFormation; DB password rotated every 60 days; MOST secure

🪤 **Your trap:** Ref on a Secrets Manager secret returns its ARN, not the password; UserData exposes it

🧠 **Rule:** Secret into a CFN property → dynamic reference {{resolve:secretsmanager:...}}; app reads Secrets Manager at runtime.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
CloudFormation stack (2-tier)
┌──────────────┐          ┌──────────────────────┐
│ ASG EC2      │ ───────► │ RDS MySQL             │
│ (web app)    │          │ MasterUserPassword = ?│
└──────────────┘          └──────────────────────┘
Yêu cầu: password rotate mỗi 60 ngày, MOST secure
```

Đáp án đúng: **A — Secrets Manager secret resource + dynamic reference vào `MasterUserPassword`, app đọc Secrets Manager lúc runtime**. Anh chọn B (Secrets Manager nhưng dùng `Ref` qua UserData).

#### A đúng — hai chỗ dùng Secrets Manager cho hai mục đích khác nhau

```
Secret (Secrets Manager)
   │
   ├──► MasterUserPassword property (RDS)
   │     dùng: {{resolve:secretsmanager:secret-id:SecretString:password}}
   │     (dynamic reference — CloudFormation KHÔNG log giá trị thật)
   │
   └──► App code gọi Secrets Manager API lúc KHỞI ĐỘNG
         (không qua UserData, không qua CloudFormation property)
```

Mấu chốt: **dynamic reference** (`{{resolve:secretsmanager:...}}`) khác hẳn `Ref`. Dynamic reference được CloudFormation resolve tại thời điểm thực thi stack mà **không ghi giá trị secret vào template hay log** — đúng tinh thần "Secrets Manager ensures the secret isn't logged or persisted by CloudFormation". Còn ứng dụng thì gọi thẳng Secrets Manager API khi launch để lấy password hiện hành, nên khi secret tự động rotate (Secrets Manager hỗ trợ sẵn rotation cho RDS), app vẫn lấy được giá trị mới nhất mà không cần redeploy.

#### B sai — vì sao `Ref` qua UserData trông giống A nhưng không an toàn

**`Ref` trên một `AWS::SecretsManager::Secret` resource không trả về password** — nó trả về ARN/tên của secret. Nhưng vấn đề lớn hơn nằm ở chỗ khác: B đặt secret vào **UserData của launch template**. UserData được lưu trong EC2 instance metadata và **có thể đọc lại được** (qua `curl 169.254.169.254/latest/user-data` hoặc console), nghĩa là bất kỳ ai có quyền truy cập instance đều thấy được giá trị nhạy cảm đã từng đi qua đó. Đây chính xác là lỗi mà TD explanation chỉ ra: "Using the user data scripts to retrieve the database password may expose the password to the environment of the operating system of the EC2 instance." Cách an toàn hơn là để app tự gọi Secrets Manager runtime, không đi qua UserData.

#### Các lựa chọn sai còn lại

- **C — Parameter thường (không phải Secrets Manager/SSM SecureString):** phải gõ password vào template hoặc console → lộ ngay từ bước tạo, không có rotation.
- **D — SSM Parameter Store (encrypted) qua UserData + `Fn::GetAtt`:** Parameter Store **lưu được** password mã hóa, nhưng **không tự sinh và không hỗ trợ auto-rotation** như Secrets Manager; vẫn đi qua UserData nên vẫn lộ.

| Lựa chọn | Cơ chế lưu | Qua UserData? | Auto-rotation |
|---|---|---|---|
| **A. Secrets Manager + dynamic reference** | Secrets Manager | Không | Có |
| B. Secrets Manager + Ref qua UserData | Secrets Manager | Có (lộ) | Có nhưng vô nghĩa vì đã lộ |
| C. CFN Parameter thường | Plaintext trong template | Có | Không |
| D. SSM Parameter Store encrypted | SSM | Có (lộ) | Không |

#### ⚠️ Lỗi lặp lại

Đây là câu Secrets Manager thứ 3 anh vấp (TD Set 1, TD Set 5, và giờ TD Set 2). Điểm chung của cả 3 lần: nhầm giữa **"secret resource tồn tại"** với **"secret được dùng an toàn"**. Có Secrets Manager resource chưa đủ — phải kiểm tra **cách secret đó đi tới đâu**: dynamic reference (an toàn, không log) hay `Ref`/UserData (lộ ra ngoài). Lần tới gặp câu Secrets Manager, luôn hỏi: "giá trị secret có đi qua UserData hoặc log console không?"

#### Quy tắc nhớ cho thi

- **"Secret vào property của resource khác (MasterUserPassword...)"** → dynamic reference `{{resolve:secretsmanager:...}}`, không phải `Ref`
- **UserData chứa secret** → luôn là dấu hiệu SAI khi đề nhấn "MOST secure"
- **"Password cần auto-rotate"** → Secrets Manager, không phải SSM Parameter Store (Parameter Store không tự sinh/rotate password)
- **`Ref` trên `AWS::SecretsManager::Secret`** → trả về ARN/tên secret, không phải giá trị bên trong

### TD explanation

AWS Secrets Manager integrates with AWS CloudFormation so you can create and retrieve secrets securely using CloudFormation. This integration makes it easier to automate provisioning your AWS infrastructure. For example, without any code changes, you can generate unique secrets for your resources with every execution of your CloudFormation template. This also improves the security of your infrastructure by storing secrets securely, encrypting automatically, and enabling rotation more easily. Secrets Manager helps you protect the secrets needed to access your applications, services, and IT resources.
CloudFormation helps you model your AWS resources as templates and execute these templates to provision AWS resources at scale. Some AWS resources require secrets as part of the provisioning process. For example, to provision a MySQL database, you must provide the credentials for the database superuser. You can use Secrets Manager, the AWS dedicated secrets management service, to create and manage such secrets.
Secrets Manager makes it easier to rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. You can reference Secrets Manager in your CloudFormation templates to create unique secrets with every invocation of your template. By default, Secrets Manager encrypts these secrets with encryption keys that you own and control. Secrets Manager ensures the secret isn’t logged or persisted by CloudFormation by using a dynamic reference to the secret. You can configure Secrets Manager to rotate your secrets automatically without disrupting your applications. Secrets Manager offers built-in integrations for rotating credentials for all Amazon RDS databases and supports extensibility with AWS Lambda so you can meet your custom rotation requirements.

Dynamic references provide a compact, powerful way for you to specify external values that are stored and managed in other services, such as the Systems Manager Parameter Store, in your stack templates. When you use a dynamic reference, CloudFormation retrieves the value of the specified reference when necessary during stack and change set operations.
Secrets Manager resource types supported in CloudFormation:
AWS::SecretsManager::Secret — Create a secret and store it in Secrets Manager.
AWS::SecretsManager::ResourcePolicy — Create a resource-based policy and attach it to a secret. Resource-based policies enable you to control access to secrets.
AWS::SecretsManager::SecretTargetAttachment — Configure Secrets Manager to rotate the secret automatically.
AWS::SecretsManager::RotationSchedule — Define the Lambda function that will be used to rotate the secret.
Therefore, the correct answer is: On the CloudFormation template, create an AWS Secrets Manager secret resource for the database password. Modify the application to retrieve the database password from Secrets Manager when it launches. Use a dynamic reference for the secret resource to be placed as the value of the MasterUserPassword property of the AWS::RDS::DBInstance resource. You can use dynamic references in CloudFormation to specify external values that are stored and managed in other services, such as AWS SSM Parameter Store or AWS Secrets Manager. Your application can then retrieve the database password resource on AWS Secrets Manager when it needs to.
The option that says: On the CloudFormation template, create a database password parameter. Add a UserData property to reference the password parameter in the initialization script of the Auto Scaling group’s launch template using the Ref intrinsic function. Save the password inside the EC2 instance upon its launch. Use the Ref intrinsic function to reference the parameter as the value of the MasterUserPassword property in the AWS::RDS::DBInstance resource is incorrect. Using a normal parameter in CloudFormation is not secure. This will require you to either store the password on the template itself or input it on the AWS web console.
The option that says: On the CloudFormation template, create an AWS Secrets Manager secret resource for the database password. Add a UserData property to reference the secret resource in the initialization script of the Auto Scaling group’s launch template using the Ref intrinsic function. Use the Ref intrinsic function to reference the secret resource as the value of the MasterUserPassword property in the AWS::RDS::DBInstance resource is incorrect. Using the user data scripts to retrieve the database password may expose the password to the environment of the operating system of the EC2 instance. It is more secure to configure the application to retrieve the secret resource when the application launches so it is not exposed to anything outside the application.
The option that says: On the CloudFormation template, create an encrypted parameter using AWS Systems Manager Parameter Store for the database password. Add a UserData property to reference the encrypted parameter in the initialization script of the Auto Scaling group’s launch template. Use the Fn::GetAtt intrinsic function to reference the encrypted parameter as the value of the MasterUserPassword property in the AWS::RDS::DBInstance resource is incorrect. AWS Systems Manager Parameter can store an encrypted password, however, it cannot generate a password that can be referenced in AWS CloudFormation. It also doesn’t support automatic rotation of the parameter.

References:
https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_cloudformation.html
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html
https://aws.amazon.com/blogs/security/how-to-create-and-retrieve-secrets-managed-in-aws-secrets-manager-using-aws-cloudformation-template/

Check out these AWS Secrets Manager and AWS CloudFormation Cheat Sheets:
https://tutorialsdojo.com/aws-secrets-manager/

</details>

<a id="q28"></a>

## Q28

A leading call center company has its headquarters in Seattle. Its corporate web portal is deployed to AWS. The AWS cloud resources are linked to its corporate data center via a link aggregation group (LAG), which terminates at the same AWS Direct Connect endpoint and is connected on a private virtual interface (VIF) in your VPC. The portal must authenticate against their on-premises LDAP server. Each Amazon S3 bucket can only be accessed by a logged-in user if it belongs to that user. 
Which of the following options should the solutions architect implement in AWS to meet the company requirements? (Select TWO.)

- **A.** Authenticate against LDAP using an identity broker you created, and have it call IAM Security Token Service (STS) to retrieve IAM federated user credentials. The application then gets the IAM federated user credentials from the identity broker to access the appropriate S3 bucket.
- **B.** Create an identity broker that assumes an IAM role, and retrieve temporary AWS security credentials via IAM Security Token Service (STS). The application gets the AWS temporary security credentials from the identity broker to gain access to the appropriate S3 bucket.
- **C.** The application first authenticates against LDAP, and then uses the LDAP credentials to log in to IAM service. Finally, it can now use the IAM temporary credentials to access the appropriate S3 bucket.
- **D.** The application first authenticates against LDAP to retrieve the name of an IAM role associated with the user. It then assumes that role via a call to IAM Security Token Service (STS). Afterward, the application can now use the temporary credentials from the role to access the appropriate S3 bucket.
- **E.** Use a Direct Connect Gateway instead of a single Direct Connect connection. Set up a Transit VPC which will authenticate against their on-premises LDAP server.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** D, E

🔑 **Key words:** portal authenticates against on-prem LDAP; per-user S3 buckets (Select TWO)

🪤 **Your trap:** Picked D (right) + E: Direct Connect Gateway / Transit VPC is networking, not authentication

🧠 **Rule:** LDAP → custom identity broker → STS (GetFederationToken / AssumeRole) → temporary credentials.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem Data Center                    AWS
┌──────────────┐  Direct Connect   ┌───────────────────────┐
│ LDAP server   │ ───(LAG, VIF)──► │ Web portal             │
└──────────────┘                   │  → S3 bucket riêng     │
                                    │    cho từng user       │
                                    └───────────────────────┘
Yêu cầu: portal authenticate bằng LDAP, mỗi user chỉ vào được bucket của mình (Select TWO)
```

Đáp án đúng: **A + D — cả hai đều là một luồng "identity broker/role xác định bằng LDAP → STS → temporary credentials" hợp lệ, khác nhau ở CÁCH lấy credentials cuối**. Anh chọn D (đúng) + E (sai, không liên quan authentication).

#### A và D hợp thành bức tranh đầy đủ — hai biến thể hợp lệ của cùng một mẫu

```
LDAP xác thực user
      │
      ▼
┌─────────────────┐        ┌─────────────────┐
│ A: Identity      │        │ D: Role name      │
│ broker tự gọi STS│   HOẶC │ lấy từ LDAP,       │
│ → federated user  │        │ app tự AssumeRole  │
│ credentials       │        │ → temp credentials │
└─────────────────┘        └─────────────────┘
      │                           │
      └──────────► Truy cập S3 bucket của user
```
Cả hai đều tuân thủ đúng trình tự bắt buộc: **xác thực LDAP trước → gọi STS lấy temporary credentials → dùng credentials đó truy cập S3**. A dùng identity broker đứng giữa gọi STS thay app; D để app tự biết role cần assume (lấy tên role từ LDAP) rồi tự gọi `AssumeRole`. TD xếp cả hai là đúng vì đề Select TWO và không loại trừ lẫn nhau — cả hai đều giải quyết đúng bài toán "xác thực trước, cấp quyền tạm thời sau, không dùng IAM User tĩnh".

#### D — anh đã chọn đúng, không có gì cần sửa ở phần này

#### E sai — vì sao Direct Connect Gateway/Transit VPC trông "liên quan" nhưng là bẫy

Direct Connect Gateway chỉ cải thiện **tính sẵn sàng (availability)** của kết nối mạng on-prem ↔ AWS (gộp nhiều VIF, nhiều Direct Connect connection). Transit VPC là chiến lược **routing** để nối nhiều VPC phân tán về mặt địa lý. **Không cái nào xử lý authentication** — đây là lớp network, trong khi bài toán của đề là lớp identity/access. Đây đúng là bẫy "nghe có vẻ hạ tầng đúng chủ đề (Direct Connect đã xuất hiện trong đề) nhưng sai domain".

#### Các lựa chọn sai còn lại

- **B — identity broker assume role rồi mới xác thực LDAP:** sai thứ tự. Phải LDAP xác thực TRƯỚC, rồi mới lấy credentials từ STS. B bỏ qua bước LDAP hoàn toàn trong luồng mô tả.
- **C — dùng LDAP credentials để "login vào IAM":** không tồn tại cơ chế này. Không thể lấy username/password LDAP rồi đăng nhập trực tiếp vào IAM — IAM không hiểu LDAP credentials.

| Lựa chọn | Có xác thực LDAP trước không | Cách lấy AWS credentials |
|---|---|---|
| **A. Identity broker** | Có | STS → federated user credentials |
| **D. App tự AssumeRole** | Có | STS AssumeRole bằng role tên lấy từ LDAP |
| B. Broker assume role trước | Không (sai thứ tự) | — |
| C. LDAP login IAM | Không | Không tồn tại |
| E. DX Gateway/Transit VPC | Không liên quan | — |

#### Quy tắc nhớ cho thi

- **"Portal/app xác thực bằng on-prem LDAP, cần truy cập AWS resource"** → identity broker hoặc app tự AssumeRole, luôn qua STS, luôn LDAP trước
- **Direct Connect Gateway / Transit VPC** → chỉ là network/availability, không bao giờ trả lời câu hỏi về authentication
- **"Dùng LDAP credentials login thẳng vào IAM"** → luôn sai, không có cơ chế này

### TD explanation

Lightweight Directory Access Protocol (LDAP) is a standard communications protocol used to read and write data to and from Active Directory. You can manage your user identities in an external system outside of AWS and grant users who sign in from those systems access to perform AWS tasks and access your AWS resources. The distinction is where the external system resides—in your data center or an external third party on the web.
For enterprise identity federation, you can authenticate users in your organization’s network, and then provide those users access to AWS without creating new AWS identities for them and requiring them to sign in with a separate user name and password. This is known as the single sign-on (SSO) approach to temporary access. AWS STS supports open standards like Security Assertion Markup Language (SAML) 2.0, with which you can use Microsoft AD FS to leverage your Microsoft Active Directory.

This scenario has the following attributes:

– The identity broker application has permissions to access IAM’s token service (STS) API to create temporary security credentials.
– The identity broker application is able to verify that employees are authenticated within the existing authentication system.
– Users are able to get a temporary URL that gives them access to the AWS Management Console (which is referred to as single sign-on).

The option that says: Authenticate against LDAP using an identity broker you created, and have it call IAM Security Token Service (STS) to retrieve IAM federated user credentials. The application then gets the IAM federated user credentials from the identity broker to access the appropriate S3 bucket is correct because it follows the correct sequence. It develops an identity broker that authenticates users against LDAP, gets the security token from STS, and then accesses the S3 bucket using the IAM federated user credentials.
Likewise, the option that says: The application first authenticates against LDAP to retrieve the name of an IAM role associated with the user. It then assumes that role via call to IAM Security Token Service (STS). Afterwards, the application can now use the temporary credentials from the role to access the appropriate S3 bucket is correct because it follows the correct sequence. It authenticates users using LDAP, gets the security token from STS, and then accesses the S3 bucket using the temporary credentials.
The option that says: Create an identity broker that assumes an IAM role, and retrieve temporary AWS security credentials via IAM Security Token Service (STS). The application gets the AWS temporary security credentials from the identity broker to gain access to the appropriate S3 bucket is incorrect because the users need to be authenticated using LDAP first, not STS. Also, the temporary credentials to log into AWS are provided by STS, not identity broker.
The option that says: The application first authenticates against LDAP, and then uses the LDAP credentials to log in to IAM service. Finally, it can now use the IAM temporary credentials to access the appropriate S3 bucket is incorrect because you cannot use the LDAP credentials to log into IAM.
The option that says: Use a Direct Connect Gateway instead of a single Direct Connect connection. Set up a Transit VPC which will authenticate against their on-premises LDAP server is incorrect because using a Direct Connect Gateway will only improve the availability of your on-premises network connection and using a transit VPC is just a common strategy for connecting multiple, geographically disperse VPCs and remote networks in order to create a global network transit center. These two things will not meet the requirement.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q31"></a>

## Q31

A leading fast-food chain has recently adopted a hybrid cloud infrastructure that extends its data centers into AWS Cloud. The solutions architect has been tasked to allow on-premises users, who are already signed in using their corporate accounts, to manage AWS resources without creating separate IAM users for each of them. This is to avoid having two separate login accounts and memorizing multiple credentials. 
Which of the following is the best way to handle user authentication in this hybrid architecture?

- **A.** Authenticate through your on-premises SAML 2.0-compliant identity provider (IDP) using STS and AssumeRoleWithWebIdentity to retrieve temporary security credentials, which enables your users to log in to the AWS console using a browser.
- **B.** Integrate the company’s authentication process with Amazon AppFlow and allow Amazon STS to retrieve temporary AWS credentials using OAuth 2.0 to enable your members to log in to the AWS Console.
- **C.** Authenticate using your on-premises SAML 2.0-compliant identity provider (IDP), retrieve temporary credentials using STS, and grant federated access to the AWS console via the AWS IAM Identity Center.
- **D.** Retrieve AWS temporary security credentials with Web Identity Federation using STS and AssumeRoleWithWebIdentity to enable users to log in to the AWS console.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** A

🔑 **Key words:** on-prem users already signed in to corporate SAML IdP; no separate IAM users

🪤 **Your trap:** AssumeRoleWithWebIdentity is for web identity providers (Google, Facebook), not SAML

🧠 **Rule:** Corporate SAML IdP → IAM Identity Center / AssumeRoleWithSAML. Social login → WebIdentity / Cognito.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem corporate network          AWS
┌──────────────────┐               ┌─────────────────┐
│ Users đã login    │   SSO, 1 lần  │ AWS Console       │
│ bằng corporate    │ ────────────► │ (không tạo thêm   │
│ account (SAML IdP)│               │  IAM User)        │
└──────────────────┘               └─────────────────┘
Yêu cầu: single sign-on, không maintain 2 bộ login
```

Đáp án đúng: **C — SAML IdP → STS → federated access qua AWS IAM Identity Center**. Anh chọn A (SAML + `AssumeRoleWithWebIdentity`) — đúng phần IdP nhưng sai API.

#### C đúng — SAML doanh nghiệp đi với IAM Identity Center, không đi với WebIdentity API

```
On-prem SAML 2.0 IdP (Active Directory, ADFS...)
         │ SAML assertion
         ▼
    AWS STS  (AssumeRoleWithSAML, đứng sau IAM Identity Center)
         │ temporary credentials
         ▼
   AWS Management Console (federated access)
```

IAM Identity Center (trước đây là AWS SSO) là dịch vụ được thiết kế riêng để kết nối với **SAML 2.0-compliant identity provider** doanh nghiệp (AD FS, Azure AD, Okta...), xử lý toàn bộ luồng SSO: user login một lần ở on-prem IdP → nhận SAML assertion → STS cấp temporary credentials → vào thẳng AWS Console mà không cần tạo IAM User riêng. Đây chính là use case chuẩn cho "corporate accounts, single sign-on, hybrid".

#### A sai — vì sao SAML đúng nhưng `AssumeRoleWithWebIdentity` lại sai

Đây là bẫy dễ nhầm vì cả A và C đều có cụm "SAML 2.0-compliant IdP" ở đầu câu — trông như cùng một giải pháp. Khác biệt nằm ở **API được gọi để lấy temporary credentials**:

```
SAML 2.0 corporate IdP   →  STS AssumeRoleWithSAML   (qua IAM Identity Center hoặc trực tiếp)
Web Identity Provider     →  STS AssumeRoleWithWebIdentity
(Google, Facebook, Amazon Cognito, OIDC...)
```

`AssumeRoleWithWebIdentity` là API dành riêng cho **Web Identity Federation** — tức các nhà cung cấp định danh công khai kiểu OIDC (Google, Facebook, Amazon, hoặc Cognito Identity Pools), không phải cho SAML. Gọi sai API này với một SAML assertion sẽ không hoạt động; API đúng cho SAML là `AssumeRoleWithSAML`. Vì vậy dù "nguồn" IdP đúng (SAML), "đường ống" xử lý (WebIdentity) sai hoàn toàn.

#### Các lựa chọn sai còn lại

- **B — tích hợp với Amazon AppFlow + OAuth 2.0:** AppFlow là dịch vụ **chuyển dữ liệu** giữa các SaaS app và AWS (ví dụ Salesforce ↔ S3), không phải dịch vụ authentication. OAuth 2.0 cũng không nằm trong luồng SAML federation.
- **D — Web Identity Federation + `AssumeRoleWithWebIdentity`:** đúng API nhưng sai domain — Web Identity Federation dành cho social login (Facebook, Google), không áp dụng cho corporate SAML IdP.

| Lựa chọn | IdP đúng loại? | API/dịch vụ đúng? |
|---|---|---|
| **C. SAML + IAM Identity Center** | Có | Có |
| A. SAML + AssumeRoleWithWebIdentity | Có | Sai (API dành cho WebIdentity) |
| B. AppFlow + OAuth 2.0 | Không | Không (AppFlow ≠ auth) |
| D. WebIdentity + AssumeRoleWithWebIdentity | Không (cần social IdP) | Đúng API nhưng sai ngữ cảnh |

#### ⚠️ Liên hệ

Câu này và nhiều câu SAP khác đều xoay quanh một trục: **"ai là identity provider" quyết định API nào được gọi**. SAML 2.0 (doanh nghiệp, AD FS) luôn đi với `AssumeRoleWithSAML` / IAM Identity Center. Web Identity Provider (Google, Facebook, Cognito) luôn đi với `AssumeRoleWithWebIdentity`. Hai nhánh này không bao giờ trộn lẫn trong đáp án đúng — thấy một câu ghép "SAML" với "WebIdentity" gần như chắc chắn là bẫy.

#### Quy tắc nhớ cho thi

- **"Corporate/on-prem SAML IdP, single sign-on"** → IAM Identity Center + `AssumeRoleWithSAML`
- **"Social login (Google, Facebook) hoặc Cognito"** → `AssumeRoleWithWebIdentity`
- **Thấy "SAML" đi chung với "WebIdentity" trong cùng một đáp án** → gần như luôn sai, đây là hai luồng federation khác nhau
- **Amazon AppFlow** → data integration giữa SaaS và AWS, không phải authentication

### TD explanation

In this scenario, you need to provide temporary access to AWS resources to the existing users, but you should not create new IAM users for them to avoid having to maintain two login accounts. This means that you need to set up a single-sign on authentication for your users so they only need to sign-in once in their on-premises network and can also access the AWS cloud at the same time.

You can use a role to configure your SAML 2.0-compliant identity provider (IdP) and AWS to permit your federated users to access the AWS Management Console. The role grants the user permission to carry out tasks in the console.
Therefore, the correct answer is: Authenticate using your on-premises SAML 2.0-compliant identity provider (IDP), retrieving temporary credentials using STS, and granting federated access to the AWS console via the AWS IAM Identity center. It gives federated access to the users to AWS resources by using SAML 2.0 identity provider and it uses on-premises single sign-on (SSO) endpoint to authenticate users, which gives them access tokens prior to providing the federated access.
The option that says: Integrate the company’s authentication process with Amazon AppFlow and allow Amazon STS to retrieve temporary AWS credentials using OAuth 2.0 to enable your members to log in to the AWS Console is incorrect. Amazon AppFlow is used to securely transfer data between Software-as-a-Service (SaaS) applications like Salesforce, SAP, Zendesk, Slack, and ServiceNow, and AWS services. It is not used for authentication. Additionally, OAuth 2.0 is not applicable in this scenario. We are not using Web Identity Federation as it is used with public identity providers such as Facebook, Google, etc.
The option that says: Authenticate through your on-premises SAML 2.0-compliant identity provider (IDP) using STS and AssumeRoleWithWebIdentity to retrieve temporary security credentials, which enables your users to log in to the AWS console using a browser is incorrect. The use of AssumeRoleWithWebIdentity is wrong which is only for Web Identity Federation (Facebook, Google, and other social logins). Even though it uses SAML 2.0 identity provider, the requirement is to provide a single sign-on to users, which means that the users should not sign in to the AWS console using any security credentials but through their corporate identity provider.
The option that says: Retrieve AWS temporary security credentials with Web Identity Federation using STS and AssumeRoleWithWebIdentity to enable users to log in to the AWS console is incorrect. We are not using Web Identity Federation as it is used with public identity providers such as Facebook, Google, etc.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html
https://aws.amazon.com/identity/federation/
https://aws.amazon.com/blogs/security/how-to-establish-federated-access-to-your-aws-resources-by-using-active-directory-user-attributes/

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q41"></a>

## Q41

A logistics company is developing a new application that will be used for all its departments. All of the company’s AWS accounts are under OrganizationA in its AWS Organizations. A certain feature of the application must allow AWS resource access from a third-party account that is under AWS Organizations named OrganizationB. The company wants to follow security best practices and grant “least privilege” access using an API or CLI to the third-party account. After access is configured, the security team will use Amazon Detective to investigate unusual activity involving the third-party account.
Which of the following options is the recommended way to securely allow OrganizationB to access AWS resources on OrganizationA?

- **A.** The third-party account should create an External ID that will be given to OrganizationA. The logistics company should then create an IAM role with the required access and put the External ID in the IAM role’s trust policy. The third-party account should use the IAM role’s ARN and External ID when requesting access to OrganizationA’s AWS resources.
- **B.** The logistics company must create an IAM user with an IAM policy allowing only the required access. The logistics company should then send the AWS credentials to the third-party account to allow login and perform only specific tasks.
- **C.** The third-party AWS Organization must integrate with the AWS Identity Center of the logistics company. Then create custom IAM policies for the third-party account to only access specific resources under OrganizationA.
- **D.** The logistics company should create an IAM role and attach an IAM policy allowing only the required access. The third-party account should then use AWS STS to assume the IAM role’s Amazon Resource Name (ARN) when requesting access to OrganizationA’s AWS resources.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** third-party account in another Organization; least privilege via API/CLI

🪤 **Your trap:** Role + AssumeRole works but without External ID is open to the confused-deputy problem

🧠 **Rule:** Third party assumes your role → trust policy with sts:ExternalId condition.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
OrganizationA (logistics company)        OrganizationB (third-party)
┌───────────────────────┐                ┌───────────────────────┐
│ IAM Role               │ ◄── AssumeRole │ Third-party account    │
│ trust policy: ai được   │    qua API/CLI │                        │
│ assume role này?        │                │                        │
└───────────────────────┘                └───────────────────────┘
Yêu cầu: least privilege, bảo mật, Amazon Detective theo dõi hoạt động bất thường
```

Đáp án đúng: **A — role + External ID trong trust policy**. Anh chọn D (role + AssumeRole nhưng KHÔNG có External ID) — thiếu đúng một điều kiện bảo mật quan trọng.

#### A đúng — External ID chặn đứng bài toán "confused deputy"

```
Trust policy của Role (OrganizationA):
{
  "Principal": { "AWS": "arn:aws:iam::<OrgB-account-id>:root" },
  "Condition": {
    "StringEquals": { "sts:ExternalId": "<random-string-do-OrgB-tao>" }
  }
}

OrganizationB gọi AssumeRole với:
  RoleArn   = arn:...:role/...
  ExternalId = <chuỗi đã thỏa thuận trước>
```

**Confused deputy problem** xảy ra khi role của OrganizationA bị bên thứ ba KHÔNG LIÊN QUAN lừa assume (ví dụ: OrganizationB chia sẻ ARN của role này cho một khách hàng khác của họ, hoặc một actor khác đoán được ARN). Nếu trust policy chỉ check Principal (account ID của OrgB) mà không có thêm điều kiện, thì **bất kỳ ai trong account OrgB** có quyền gọi AssumeRole đều vào được — kể cả khi OrgB vô tình để lộ quyền này cho một bên thứ tư. External ID là một bí mật dùng chung chỉ giữa OrgA và OrgB, đóng vai trò như "mật khẩu thứ hai" xác nhận đúng ngữ cảnh ("tôi đang assume role này thay mặt đúng khách hàng A"), ngăn chặn chính xác kịch bản bị lợi dụng gián tiếp này.

#### D sai — vì sao thiếu External ID là lỗ hổng thực sự, không phải chi tiết vặt

D dùng đúng mô hình IAM Role + STS AssumeRole (đúng hướng, không dùng IAM User tĩnh), nhưng **bỏ qua trust policy condition**. TD nêu rõ: "Without the External ID on the IAM role's trust policy, it is possible that other AWS accounts can assume that IAM role." Đây không phải lỗi lý thuyết — nó là một threat model thật trong multi-tenant: nếu OrganizationA chỉ trust theo account ID của OrganizationB, và OrganizationB (vì lý do nào đó, ví dụ compromise hoặc nhầm lẫn nội bộ) để một identity khác trong account của họ gọi AssumeRole, thì identity đó cũng vào được tài nguyên của OrganizationA. Đề bài còn nhấn "least privilege" và nhắc tới Amazon Detective để điều tra hoạt động bất thường — ngữ cảnh này gợi ý rõ ràng cần thêm lớp kiểm soát chặt hơn so với AssumeRole trần.

#### Các lựa chọn sai còn lại

- **B — IAM User tĩnh, gửi credentials cho bên thứ ba:** vi phạm best practice cơ bản nhất — long-term credentials có thể bị rò rỉ, không xoay vòng, không least privilege.
- **C — tích hợp IAM Identity Center giữa hai Organization:** không phải cơ chế dành cho truy cập xuyên tổ chức của bên thứ ba qua API/CLI; IAM Identity Center dùng cho SSO nội bộ, và tích hợp kiểu này còn tạo rủi ro OrganizationB users login thẳng và thấy account của OrganizationA — phức tạp và kém kiểm soát hơn.

| Lựa chọn | Dùng role tạm thời? | Có External ID? | Rủi ro |
|---|---|---|---|
| **A. Role + External ID** | Có | Có | Thấp — chặn confused deputy |
| D. Role không External ID | Có | Không | Trung bình — account khác có thể assume |
| B. IAM User + gửi credentials | Không | — | Cao — leak long-term credentials |
| C. Tích hợp IAM Identity Center | — | — | Phức tạp, lộ thông tin account khác |

#### ⚠️ Lỗi lặp trong nhóm | Liên hệ

Câu này cùng nhóm "misunderstanding quyền cross-account/cross-org" với Q66 và Q75 (SCP). Điểm chung: khi đề nói "least privilege" hoặc "most secure" cho truy cập bên thứ ba, luôn kiểm tra xem đáp án có đủ **điều kiện ràng buộc bổ sung** không (External ID, tag condition...), không chỉ dừng ở "có dùng Role hay không".

#### Quy tắc nhớ cho thi

- **"Third-party / multi-tenant assume role của tôi"** → luôn cần `sts:ExternalId` trong trust policy, không chỉ Principal
- **"Confused deputy"** → dấu hiệu nhận biết: role bị bên không liên quan lợi dụng thông qua một bên trung gian hợp lệ
- **Đưa access/secret key cho bên ngoài** → luôn sai, luôn ưu tiên role + STS

### TD explanation

At times, you need to give third-party access to your AWS resources (delegate access). One important aspect of this scenario is the External ID, optional information that you can use in an IAM role trust policy to designate who can assume the role. The external ID allows the user who is assuming the role to assert the circumstances in which they are operating. It also provides a way for the account owner to permit the role to be assumed only under specific circumstances.
In a multi-tenant environment where you support multiple customers with different AWS accounts, AWS recommends using one external ID per AWS account. This ID should be a random string generated by the third party.
To require that the third party provide an external ID when assuming a role, update the role’s trust policy with the external ID of your choice. To provide an external ID when you assume a role, use the AWS CLI or AWS API to assume that role.
For example, let’s say that you decide to hire a third-party company called Example Corp to monitor your AWS account and help optimize costs. In order to track your daily spending, Example Corp needs to access your AWS resources. Example Corp also monitors many other AWS accounts for other customers.

Do not give Example Corp access to an IAM user and its long-term credentials in your AWS account. Instead, use an IAM role and its temporary security credentials. An IAM role provides a mechanism to allow a third party to access your AWS resources without needing to share long-term credentials.
Therefore, the correct answer is: The third-party account should create an External ID that will be given to OrganizationA. The logistics company should then create an IAM role with the required access and put the External ID in the IAM role’s trust policy. The third-party account should use the IAM role’s ARN and External ID when requesting access to OrganizationA’s AWS resources. An External ID in an IAM role’s trust policy is a recommended best practice to ensure that the external party can assume your role only when it is acting on your behalf.
The option that says: The third-party AWS Organization must integrate with the AWS Identity Center of the logistics company. Then create custom IAM policies for the third-party account to only access specific resources under OrganizationA is incorrect. This is not recommended as this will add unnecessary complexity, and there is a possibility for OrganizationB users to log in and view the accounts on OrganizationA.
The option that says: The logistics company must create an IAM user with an IAM policy allowing only the required access. The logistics company should then send the AWS credentials to the third-party account to allow login and perform only specific tasks is incorrect. This is possible but not recommended because AWS credentials may get leaked or exposed. It is recommended to use STS to generate a temporary token when requesting access to AWS resources.
The option that says: The logistics company should create an IAM role and attach an IAM policy allowing only the required access. The third-party account should then use AWS STS to assume the IAM role’s Amazon Resource Name (ARN) when requesting access to OrganizationA’s AWS resources is incorrect. This is possible but not the most secure way among the options. Without the External ID on the IAM role’s trust policy, it is possible that other AWS accounts can assume that IAM role.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html
https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/

Check out these AWS Organizations and AWS IAM Cheat Sheets:
https://tutorialsdojo.com/aws-organizations/
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q62"></a>

## Q62

A multinational software provider in the US hosts both of its development and test environments in the AWS cloud. The CTO decided to use separate AWS accounts in hosting each environment. The solutions architect has enabled Consolidated Billing to link each of the accounts’ bill to a Master AWS account. To make sure that each account is kept within the budget, the administrators in the master account must have the power to stop, delete, and/or terminate resources in both development and test environment AWS accounts. 
Which of the following options is the recommended action to meet the requirements for this scenario?

- **A.** First, create IAM users in the master account. Then in the Dev and Test accounts, generate cross-account roles that have full admin permissions while granting access for the master account.
- **B.** By linking all accounts under Consolidated Billing, you will be able to provide IAM users in the master account access to Dev and Test account resources.
- **C.** IAM users with full admin permissions will be created in the master account. In both Dev and Test accounts, generate cross-account roles that would grant the master account access to Dev and Test account resources through permissions inherited from the master account.
- **D.** In the master account, you are to create IAM users and a cross-account role that has full admin permissions to the Dev and Test accounts.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** admins in management account must stop/terminate resources in Dev and Test accounts

🪤 **Your trap:** Permissions are not inherited from the management account; the role must carry its own admin policy

🧠 **Rule:** Cross-account role lives in the TARGET account (Dev/Test) with its own permissions and trusts the management account.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Master account (Consolidated Billing)
┌───────────────────┐
│ IAM users (admins)  │
└───────────────────┘
        │ cần stop/delete/terminate resources
        ▼
┌───────────────┐        ┌───────────────┐
│ Dev account    │        │ Test account   │
└───────────────┘        └───────────────┘
Yêu cầu: admin ở master account quản lý resource ở Dev/Test
```

Đáp án đúng: **A — IAM Users ở master account; cross-account Role với full admin permissions được tạo TRONG Dev và Test account, trust về phía master**. Anh chọn C (role cũng tạo trong Dev/Test, nhưng mô tả quyền "inherited từ master account" — sai cơ chế).

#### A đúng — role sống ở account bị truy cập, mang quyền của chính nó

```
Master account                     Dev / Test account (TARGET)
┌───────────────┐                  ┌─────────────────────────┐
│ IAM User admin │ ── AssumeRole ─►│ Cross-account Role        │
└───────────────┘                  │ (full admin — quyền RIÊNG │
                                    │  của chính role này,      │
                                    │  trust policy cho phép     │
                                    │  master account assume)    │
                                    └─────────────────────────┘
```

Nguyên tắc cross-account access trong AWS: **role phải được tạo trong account mà bạn muốn truy cập** (ở đây là Dev và Test), với một policy permission gắn trực tiếp vào role đó (full admin), và trust policy của role cho phép principal từ master account assume nó. Người dùng (IAM User) chỉ cần tồn tại ở master account — không cần tạo user riêng trong từng account con.

#### C sai — vì sao "permissions inherited from master account" là một khái niệm không tồn tại

C mô tả đúng vị trí tạo role (trong Dev/Test), nhưng sai ở cách mô tả quyền: **"cross-account roles that would grant the master account access to Dev and Test account resources through permissions inherited from the master account"**. Không có cơ chế "kế thừa quyền" xuyên AWS account. Mỗi account là một permission boundary độc lập — IAM permissions **không tự động truyền** từ account này sang account khác chỉ vì có quan hệ Consolidated Billing hay trust relationship. Role trong Dev/Test account phải được gắn **policy riêng của chính nó** (ví dụ AdministratorAccess) để có quyền full admin trên resource của account đó; AssumeRole chỉ cho phép "mặc" role này, không "mượn" quyền từ nơi khác.

```
SAI: Master account quyền admin ──(kế thừa)──► Dev account role
                                  (không tồn tại cơ chế này)

ĐÚNG: Dev account role có sẵn policy AdministratorAccess của RIÊNG NÓ
      Master account chỉ AssumeRole để "mặc" role đó
```

#### Các lựa chọn sai còn lại

- **D — tạo role trong MASTER account:** sai vị trí hoàn toàn. Cross-account role để truy cập resource ở Dev/Test phải nằm TRONG Dev/Test, không phải trong master.
- **B — dựa vào Consolidated Billing để cấp access:** Consolidated Billing chỉ gộp hóa đơn thanh toán, hoàn toàn không liên quan đến access control/permissions giữa các account.

| Lựa chọn | Role tạo ở đâu | Quyền đến từ đâu |
|---|---|---|
| **A. Đúng** | Dev/Test (target) | Policy gắn trực tiếp vào role đó |
| C. Role đúng chỗ, sai cơ chế quyền | Dev/Test | "Inherited" — không tồn tại |
| D. Role sai chỗ | Master | — |
| B. Dựa vào Consolidated Billing | Không có role | Billing ≠ access |

#### Quy tắc nhớ cho thi

- **"Account A cần quản lý resource ở account B"** → role nằm TRONG account B, trust policy cho phép account A assume
- **"Permissions inherited across accounts"** → luôn là bẫy, IAM permissions không xuyên account tự động
- **Consolidated Billing** → chỉ gộp bill, không cấp access

### TD explanation

You share resources in one account with users in a different account. By setting up cross-account access in this way, you don’t need to create individual IAM users in each account. In addition, users don’t have to sign out of one account and sign into another in order to access resources that are in different AWS accounts.

Therefore, the correct answer is: First, create IAM users in the master account. Then in the Dev and Test accounts, generate cross-account roles that have full admin permissions while granting access for the master account. The cross-account role is created in Dev and Test accounts, and the users are created in the Master account that are given that role.
The option that says: In the master account, you are to create IAM users and a cross-account role that has full admin permissions to the Dev and Test accounts is incorrect. A cross-account role should be created in Dev and Test accounts, not Master account.
The option that says: IAM users with full admin permissions will be created in the master account. In both Dev and Test accounts, generate cross-account roles that would grant the master account access to Dev and Test account resources through permissions inherited from the master account is incorrect. The permissions cannot be inherited from one AWS account to another.
The option that says: By linking all accounts under Consolidated Billing, you will be able to provide IAM users in the master account access to Dev and Test account resources is incorrect. Consolidated billing does not give access to resources in this fashion.

References:
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html

Check out this AWS IAM Cheat Sheet:
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

</details>

<a id="q66"></a>

## Q66

A leading commercial bank has multiple AWS accounts that are consolidated using AWS Organizations. The bank uses AWS Firewall Manager to centrally manage firewall rules across all its AWS accounts. The cybersecurity team already centrally manages Firewall Policies for web applications via Firewall Manager. The bank is building an online portal for foreclosed real estate properties that it owns. The online portal is designed to use SSL for better security. The bank would like to implement a separation of responsibilities between the DevOps team and its cybersecurity team. The DevOps team is entitled to manage and log in to the Amazon EC2 instances, while the cybersecurity team has exclusive access to the application’s X.509 certificate, which contains the private key and is stored in AWS Certificate Manager (ACM).
Which of the following options would satisfy the company requirements?

- **A.** Configure an IAM policy that authorizes access to the certificate store only for the cybersecurity team and then add a configuration to terminate the SSL on the ELB.
- **B.** Set up a Service Control Policy (SCP) that authorizes access to the certificate store only for the cybersecurity team and then add a configuration to terminate the SSL on the ELB.
- **C.** Use the AWS Config service to configure the EC2 instances to retrieve the X.509 certificate upon boot from an AWS CloudHSM that is managed by the cybersecurity team.
- **D.** Upload the X.509 certificate to an Amazon S3 bucket owned by the cybersecurity team and accessible only by the IAM role of the EC2 instances. Use the AWS Systems Manager Session Manager as the HTTPS session manager for the application.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** 🔁 only the cybersecurity team may access the ACM certificate; DevOps manages EC2

🪤 **Your trap:** An SCP never grants access to a team — it only limits what IAM can allow in an account

🧠 **Rule:** Grant/limit access for a team → IAM policy. SCP = account-level guardrail. Terminate SSL on the ELB.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations
┌─────────────────────────────────────────────┐
│  DevOps team        Cybersecurity team        │
│  ┌───────────┐      ┌──────────────────┐     │
│  │ Login & manage│   │ Quyền độc quyền trên │     │
│  │ EC2 instances │   │ X.509 cert (ACM,    │     │
│  └───────────┘      │ chứa private key)     │     │
│                      └──────────────────┘     │
│         SSL terminate ở đâu?  ELB hay EC2?     │
└─────────────────────────────────────────────┘
Yêu cầu: tách biệt trách nhiệm — DevOps không được đụng vào cert
```

Đáp án đúng: **A — IAM policy giới hạn quyền truy cập certificate store chỉ cho cybersecurity team, + terminate SSL tại ELB**. Anh chọn B (SCP) — nhầm công cụ cấp quyền.

#### A đúng — hai quyết định độc lập cộng lại thành giải pháp

```
Quyết định 1 (nơi lưu/truy cập cert):
  IAM policy → chỉ cybersecurity team có quyền đọc cert trong ACM

Quyết định 2 (nơi SSL kết thúc):
  Terminate SSL tại ELB
    → cert CHỈ tồn tại ở ELB, không bao giờ đi xuống EC2
    → DevOps quản lý EC2 thoải mái mà không bao giờ chạm vào cert
```

Nếu terminate SSL ở EC2 thay vì ELB, cert (bao gồm private key) buộc phải nằm trên chính instance mà DevOps đang quản lý — vi phạm ngay yêu cầu tách biệt. Terminate ở ELB giữ cert tách hẳn khỏi tầng EC2, kết hợp với IAM policy giới hạn quyền đọc ACM, tạo ra ranh giới trách nhiệm rõ ràng đúng như đề yêu cầu.

#### B sai — vì sao SCP không bao giờ là công cụ "cấp quyền" cho một team

**SCP (Service Control Policy) không bao giờ GRANT (cấp) quyền** — SCP chỉ là một guardrail ở cấp account/OU, xác định **trần quyền tối đa** (maximum available permissions) mà IAM trong account đó được phép cấp. Nói cách khác: SCP = "cái gì KHÔNG được làm", còn ai thực sự ĐƯỢC làm gì vẫn phải định nghĩa bằng IAM policy (identity-based hoặc resource-based). TD nói thẳng: "A service control policy (SCP) simply determines what services and actions can be delegated... It does not grant any permissions, unlike an IAM Policy." Việc đề nói "set up SCP that authorizes access... only for cybersecurity team" tự mâu thuẫn ngay trong câu chữ — SCP không "authorize" ai cả.

```
IAM Policy  → CẤP quyền thực tế cho user/role (positive grant)
SCP         → GIỚI HẠN trần quyền ở cấp account/OU (chỉ Deny hoặc filter,
               không bao giờ tự nó cho phép một hành động)
```

#### Các lựa chọn sai còn lại

- **C — AWS Config lấy cert từ CloudHSM lúc boot:** AWS Config chỉ dùng để assess/audit cấu hình, không cấp quyền hay cấu hình runtime. CloudHSM quản lý encryption keys, không phải nơi lưu SSL certificate.
- **D — lưu cert trong S3 bucket + Session Manager làm "HTTPS session manager":** lưu X.509 cert trong S3 là rủi ro bảo mật (nên dùng ACM, đúng chỗ của nó); Session Manager chỉ phục vụ remote access an toàn tới instance, không xử lý SSL/HTTPS session gì cả.

| Lựa chọn | Công cụ cấp quyền | SSL terminate ở đâu | Đúng cơ chế? |
|---|---|---|---|
| **A. IAM policy + ELB** | IAM (đúng) | ELB | Có |
| B. SCP + ELB | SCP (sai — không grant) | ELB | Không |
| C. AWS Config + CloudHSM | Không cấp quyền gì | — | Không |
| D. S3 + Session Manager | — | Không xử lý SSL | Không |

#### ⚠️ Lỗi lặp lại

Đây là lần thứ 2 anh nhầm SCP = công cụ cấp quyền (cùng pattern với Q75 trong set này, và từng vấp ở TD Set 1 Q40, TD Set 5). Ghi nhớ cứng: **mọi đáp án viết "SCP that allows/authorizes/grants access"** gần như chắc chắn SAI — vì SCP về bản chất chỉ Deny hoặc giới hạn, không bao giờ tự mình cấp quyền access cho ai.

#### Quy tắc nhớ cho thi

- **"SCP ... allows/grants/authorizes access"** → cụm từ này luôn là tín hiệu SAI, loại ngay
- **Cần giới hạn quyền cho MỘT team cụ thể trong account** → IAM policy, không phải SCP
- **"Tách biệt trách nhiệm, không ai khác chạm vào cert"** → terminate SSL ở nơi team kia không quản lý (ELB, không phải EC2 do DevOps quản lý)

### TD explanation

In this scenario, the best solution is to set the appropriate IAM policy to both the DevOps and cybersecurity teams and then add a configuration to terminate the SSL on the ELB.
Take note that you can either terminate the SSL on the ELB side or on the EC2 instance. If you choose the former, the X.509 certificate will only be present in the ELB and if you choose the latter, the X.509 certificate will be stored inside the EC2 instance.
Since we don’t want the DevOps team to have access to the certificate, it is best to terminate the SSL on the ELB level rather than the EC2.

Therefore, the correct answer is: Configure an IAM policy that authorizes access to the certificate store only for the cybersecurity team and then add a configuration to terminate the SSL on the ELB.
The option that says: Use the AWS Config service to configure the EC2 instances to retrieve the X.509 certificate upon boot from an AWS CloudHSM that is managed by the cybersecurity team is incorrect. The AWS Config service simply enables you to assess, audit, and evaluate the configurations of your AWS resources. It does not grant any permission or access. In addition, CloudHSM is a managed hardware security module (HSM) in the AWS Cloud that handles encryption keys and not SSL certificates.
The option that says: Upload the X.509 certificate to an Amazon S3 bucket owned by the cybersecurity team and accessible only by the IAM role of the EC2 instances. Use the AWS Systems Manager Session Manager as the HTTPS session manager for the application is incorrect because the Systems Manager Session Manager service simply provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys. This service does not handle SSL connections. It is also a security risk to store X.509 certificates in an S3 bucket. It should be stored in the AWS Certificate Manager.
The option that says: Set up a Service Control Policy (SCP) that authorizes access to the certificate store only for the cybersecurity team and then adding a configuration to terminate the SSL on the ELB is incorrect. A service control policy (SCP) simply determines what services and actions can be delegated by administrators to the users and roles in the accounts to which the SCP is applied. It does not grant any permissions, unlike an IAM Policy.

References:
https://docs.aws.amazon.com/IAM/latest/APIReference/API_UploadServerCertificate.html
https://aws.amazon.com/blogs/aws/elastic-load-balancer-support-for-ssl-termination/

Check out these AWS Elastic Load Balancing (ELB) and IAM Cheat Sheets:
https://tutorialsdojo.com/aws-elastic-load-balancing-elb/
https://tutorialsdojo.com/aws-identity-and-access-management-iam/

Service Control Policies (SCP) vs IAM Policies:
https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/

</details>

<a id="q75"></a>

## Q75

A company has several resources in its production environment that is shared among various business units of the company. A single business unit may have one or more AWS accounts that have resources in the production environment. There were a lot of incidents in which the developers from a specific business unit accidentally terminated the Amazon EC2 instances, Amazon EKS clusters, and Amazon Aurora Serverless databases which are owned by another business unit. The solutions architect has been tasked to come up with a solution to only allow a specific business unit that owns the EC2 instances, and other AWS resources, to terminate their own resources. 
Which of the following is the most suitable multi-account strategy implementation to meet the company requirements?

- **A.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to individual Organization Units (OU). Create an IAM Role in the production account, which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the IAM policy to every member account of the OU.
- **B.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns. Provide the cross-account access and the SCP to the individual member accounts to tightly control who can terminate the EC2 instances.
- **C.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create an IAM Role in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns. Create an AWSServiceRoleForOrganizations service-linked role for the individual member accounts of the OU to enable trusted access.
- **D.** Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the SCP to the OUs, which will then be automatically inherited by its member accounts.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** 🔁 only the owning business unit may terminate its resources in shared prod account

🪤 **Your trap:** 'SCP that allows access' is never correct — SCPs only filter permissions

🧠 **Rule:** Resource-level terminate permission → IAM role in prod account (tag/owner conditions) assumed cross-account by the OU's accounts.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
AWS Organizations
┌─────────────────────────────────────────────────┐
│ Production account (shared)                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐ │
│  │ BU-A EC2  │  │ BU-B EC2  │  │ BU-C Aurora/EKS   │ │
│  └──────────┘  └──────────┘  └──────────────────┘ │
│  tag owner=A   tag owner=B   tag owner=C          │
└─────────────────────────────────────────────────┘
OU-A / OU-B / OU-C (ngoài production account) chứa account của từng BU
Sự cố: dev BU khác lỡ terminate resource của BU không phải mình
Yêu cầu: chỉ BU SỞ HỮU mới được terminate resource của chính họ
```

Đáp án đúng: **A — OU để nhóm account theo BU; IAM Role trong production account (có resource-level permission theo owner) cấp cross-account access cho từng member account của OU**. Anh chọn D (SCP với policy "allows access... resource-level permission") — lại là bẫy "SCP cấp quyền".

#### A đúng — IAM Role với resource-level permission là nơi thực sự "cấp" quyền terminate

```
Production account
  IAM Role (một role, có resource-level condition theo owner/tag)
      │  trust policy cho phép mọi member account trong OU đó assume
      │
      ▼
BU-A account ──AssumeRole──► chỉ terminate được resource GẮN owner=BU-A
BU-B account ──AssumeRole──► chỉ terminate được resource GẮN owner=BU-B
```

Resource-level permission trên EC2/EKS/Aurora cho phép policy chỉ áp dụng cho resource thỏa điều kiện cụ thể (ví dụ theo tag owner). IAM Role đặt trong production account, mang chính policy này, rồi cấp cross-account access cho từng account thành viên của OU — mỗi BU chỉ assume được quyền tương ứng với resource họ sở hữu. Đây đúng tinh thần resource-level, least privilege.

#### D sai — vì sao "SCP cho phép... resource-level permission" tự mâu thuẫn

Giống hệt bẫy ở Q66: **SCP không bao giờ GRANT quyền**, nó chỉ là guardrail giới hạn trần quyền tối đa ở cấp Organization/OU/account. TD nói rõ: "SCPs only allow or deny the use of an AWS service" và "Attaching an SCP ... just defines a guardrail for what actions the principals can perform. You still need to attach identity-based or resource-based policies ... to actually grant permission to them." D mô tả SCP "which has a policy that allows access to the EC2 instances... including resource-level permission to terminate" — đây là một việc SCP không làm được. Thêm nữa, nếu dùng SCP để chặn terminate theo kiểu "deny toàn bộ trừ chủ sở hữu", sẽ phải chặn luôn cả EC2 service ở cấp OU, điều này không khả thi khi các BU vẫn cần dùng EC2 bình thường cho resource của chính họ.

```
SCP  →  trần giới hạn (KHÔNG BAO GIỜ tự cấp quyền)
IAM Role/Policy (identity hoặc resource-based)  →  nơi THỰC SỰ cấp quyền terminate
```

#### Các lựa chọn sai còn lại

- **C — Role đúng vị trí nhưng thêm `AWSServiceRoleForOrganizations` service-linked role:** service-linked role này chỉ phục vụ cho AWS Organizations tự tạo các service-linked role khác (dùng nội bộ dịch vụ), tồn tại ở toàn bộ Organization chứ không giới hạn theo OU cụ thể — không liên quan gì đến việc cấp quyền terminate theo owner.
- **B — SCP riêng cho từng BU, cấp qua member account:** cùng lỗi gốc với D — SCP "allows access" không tồn tại cơ chế này, dù có tách theo từng BU cũng không sửa được bản chất sai.

| Lựa chọn | Công cụ cấp quyền thực sự | Resource-level theo owner? |
|---|---|---|
| **A. IAM Role trong prod account** | IAM (đúng) | Có |
| B. SCP riêng từng BU | SCP (sai — không grant) | Tuyên bố có, nhưng SCP không làm được |
| C. IAM Role + service-linked role thừa | IAM nhưng thêm bước vô nghĩa | Có ở phần Role, nhưng SLR không liên quan |
| D. SCP ở production account | SCP (sai — không grant) | Tuyên bố có, nhưng SCP không làm được |

#### ⚠️ Lỗi lặp lại

Đây là lần thứ 2 trong set này (cùng với Q66) và từng vấp ở TD Set 1 Q40 và TD Set 5 — cùng một lỗi tư duy: coi SCP như một policy "cấp quyền" có thể viết Allow và tạo ra access mới. Thực tế SCP luôn ở vai trò **hạn chế** (filter những gì IAM được phép Allow), không bao giờ tự nó là nguồn cấp quyền. Khi thấy đề dùng SCP để "cho phép", "cấp quyền", "authorize" một hành động cụ thể như terminate — loại ngay, bất kể phần còn lại của câu nghe hợp lý thế nào.

#### Quy tắc nhớ cho thi

- **"SCP ... allows/grants/authorizes ... terminate/access"** → luôn sai, SCP chỉ Deny/giới hạn trần quyền
- **"Resource-level permission theo owner, cấp cho nhiều account trong OU"** → IAM Role đặt ở account chứa resource, cấp cross-account access theo OU/member account
- **AWSServiceRoleForOrganizations** → chỉ phục vụ nội bộ AWS Organizations tạo service-linked role, không liên quan access control cho end-user

### TD explanation

AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.

You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.
Resource-level permissions refer to the ability to specify which resources users are allowed to perform actions on. Amazon EC2 has partial support for resource-level permissions. This means that for certain Amazon EC2 actions, you can control when users are allowed to use those actions based on conditions that have to be fulfilled, or specific resources that users are allowed to use. For example, you can grant users permissions to launch instances, but only of a specific type, and only using a specific AMI.
The scenario on this question has a lot of AWS Accounts that need to be managed. AWS Organization solves this problem and provides you with control by assigning the different business units as individual Organization Units (OU). Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. However, SCPs alone are not sufficient for allowing access to the accounts in your organization. Attaching an SCP to an AWS Organizations entity just defines a guardrail for what actions the principals can perform. You still need to attach identity-based or resource-based policies to principals or resources in your organization’s accounts to actually grant permission to them.
Since SCPs only allow or deny the use of an AWS service, you don’t want to block OUs from completely using the EC2 service. Thus, you will need to provide cross-account access and the IAM policy to every member accounts of the OU.
Hence, the correct answer is: Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to individual Organization Units (OU). Create an IAM Role in the production account, which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the IAM policy to every member account of the OU.
The option that says: Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create an IAM Role in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns. Create an AWSServiceRoleForOrganizations service-linked role for the individual member accounts of the OU to enable trusted access is incorrect because AWSServiceRoleForOrganizations service-linked role is primarily used to only allow AWS Organizations to create service-linked roles for other AWS services. This service-linked role is present in all organizations and not just in a specific OU.
The following options are incorrect because an SCP policy simply specifies the services and actions that users and roles can use in the accounts:
– Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account for each business unit which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources that it owns. Provide the cross-account access and the SCP to the individual member accounts to tightly control who can terminate the EC2 instances.
– Use AWS Organizations to centrally manage all of your accounts. Group your accounts, which belong to a specific business unit, to an individual Organization Unit (OU). Create a Service Control Policy in the production account which has a policy that allows access to the EC2 instances and other resources, including resource-level permission to terminate the resources owned by a particular business unit. Provide the cross-account access and the SCP to the OUs, which will then be automatically inherited by its member accounts.
SCPs are similar to IAM permission policies except that they don’t grant any permissions.

References:
https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html

Check out these AWS Organizations and Comparison of AWS Services Cheat Sheets:
https://tutorialsdojo.com/aws-organizations/
https://tutorialsdojo.com/comparison-of-aws-services/

Service Control Policies (SCP) vs IAM Policies:
https://tutorialsdojo.com/service-control-policies-scp-vs-iam-policies/

</details>

---

# Group B — Edge & data protection (4)

<a id="q1"></a>

## Q1

As part of the Corporate Social Responsibility of the tech company, the development team created an online learning system for a public university. The application architecture uses an Application Load Balancer in front of two On-Demand EC2 instances located in two Availability Zones. The only remaining requirement is to secure the new website with an HTTPS connection. 
Which of the following option is the most cost-effective and easiest way to complete the online learning system?

- **A.** Generate a Public Certificate in ACM. Configure the Application Load Balancer to use the Public Certificate to handle HTTPS requests.
- **B.** Generate a Private Certificate in ACM. Configure the Application Load Balancer to use the Private Certificate to handle HTTPS requests.
- **C.** Generate a Private Certificate in ACM. Configure the two EC2 instances to use the Private Certificate to handle HTTPS requests.
- **D.** Generate a Public Certificate in ACM. Configure the two EC2 instances to use the Public Certificate to handle HTTPS requests.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** ALB + 2 EC2; add HTTPS; most cost-effective and easiest

🪤 **Your trap:** Private certificate needs ACM Private CA → monthly fee

🧠 **Rule:** Public site on ALB/CloudFront/API GW → free public ACM certificate. Cannot export ACM public certs to EC2.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Internet
   │
   ▼
Application Load Balancer  ← cần HTTPS ở đây
   │           │
   ▼           ▼
EC2 (AZ-1)   EC2 (AZ-2)   ← On-Demand, không cần cài cert
```

Yêu cầu: thêm HTTPS cho website public, với chi phí **thấp nhất** và cách làm **dễ nhất**. Đáp án đúng: **A (Public Certificate trong ACM, gắn vào ALB)**. Anh chọn **B (Private Certificate, gắn vào ALB)** — sai vì tốn phí không cần thiết.

#### Vì sao A đúng

ACM cấp hai loại chứng chỉ:

- **Public Certificate:** miễn phí hoàn toàn, chỉ cần verify quyền sở hữu domain (DNS hoặc email). Dùng được trực tiếp với **CloudFront, ELB (ALB/NLB/CLB), API Gateway**.
- **Private Certificate:** cần một **ACM Private CA**, tính phí **theo tháng cho mỗi CA đang hoạt động** cộng thêm phí theo số chứng chỉ phát hành mỗi tháng.

Website này là **public**, không có yêu cầu nào về PKI nội bộ hay xác thực mTLS giữa các service private. Vậy chỉ cần Public Certificate: generate trong ACM → attach vào ALB listener 443. Không tốn phí, không cần quản lý CA → vừa rẻ nhất vừa dễ nhất.

#### Vì sao B (lựa chọn của Anh) sai

B cũng gắn certificate vào đúng chỗ — ALB — về mặt kỹ thuật **vẫn chạy được**. Nhưng B dùng **Private Certificate**, nghĩa là phải dựng một ACM Private CA, phát sinh **phí vận hành hàng tháng** dù bạn không cần tính riêng tư/nội bộ gì cả. Private Certificate chỉ hợp lý khi:

- Bạn cần PKI nội bộ cho các service không public (ví dụ mTLS giữa microservices trong VPC)
- Client (browser công khai) không thể tự động tin tưởng Private CA của bạn — họ sẽ thấy cảnh báo "untrusted certificate" trừ khi bạn tự cài root CA vào máy client, điều không khả thi với người dùng public.

Vậy B vừa tốn tiền hơn vừa không phù hợp với ngữ cảnh "trường đại học public, người dùng là trình duyệt công khai".

#### Các lựa chọn sai còn lại

- **C — Private Certificate gắn vào EC2:** vừa tốn phí Private CA, vừa phải tự cài đặt/quản lý cert trên từng instance (mất "dễ nhất"), vừa không cần thiết vì ALB đã terminate SSL được.
- **D — Public Certificate gắn vào EC2:** **không khả thi về mặt kỹthuật**. Chứng chỉ Public của ACM **không export được** để cài lên EC2 — nó chỉ tích hợp trực tiếp với CloudFront, ELB, API Gateway. Muốn SSL trên EC2 phải tự tạo/import cert khác (ví dụ Let's Encrypt) hoặc dùng Private Certificate của ACM (cho export).

| Lựa chọn | Loại cert | Nơi gắn | Chi phí | Khả thi? |
|---|---|---|---|---|
| **A (đúng)** | Public | ALB | Miễn phí | Có |
| B (Anh chọn) | Private | ALB | Phí CA hàng tháng | Có nhưng tốn tiền thừa |
| C | Private | EC2 | Phí CA + công quản lý | Có nhưng đắt & phức tạp |
| D | Public | EC2 | — | Không export được lên EC2 |

#### Lưu ý thực tế

- Nhớ rõ bảng "nơi dùng được Public ACM cert": **CloudFront, ELB, API Gateway** — ba cái này thôi. Không phải EC2, không phải trực tiếp trên server tự quản lý.
- Chỉ Private Certificate (từ ACM Private CA) mới **export** được để dùng ngoài 3 dịch vụ trên, ví dụ cài lên EC2 hay thiết bị on-premises.

#### Quy tắc nhớ cho thi

- **"Public-facing website + ALB/CloudFront/API Gateway" → Public Certificate ACM, miễn phí.**
- **"Private Certificate" → luôn gắn với từ khóa "phí hàng tháng", chỉ chọn khi đề nói rõ cần PKI nội bộ hoặc cần cài cert lên EC2/on-premises.**
- **"Gắn cert Public của ACM lên EC2" → luôn là bẫy, không khả thi.**

### TD explanation

With AWS Certificate Manager, you can generate public or private SSL/TLS certificates that you can use to secure your site. Public SSL/TLS certificates provisioned through AWS Certificate Manager are free. You pay only for the AWS resources that you create to run your application. For private certificates, the ACM Private Certificate Authority (CA) is priced along two dimensions: (1) You pay a monthly fee for the operation of each private CA until you delete it and (2) you pay for the private certificates you issue each month.

Public certificates generated from ACM can be used on Amazon CloudFront, Elastic Load Balancing, or Amazon API Gateway but not directly on EC2 instances, unlike private certificates.
Hence, generating a Public Certificate in ACM and configuring the Application Load Balancer to use the Public Certificate to handle HTTPS requests is correct in this scenario as a public certificate does not cost anything and you can configure this certificate with the Application Load Balancer.
The option that says: Generate a Private Certificate in ACM. Configure the Application Load Balancer to use the Private Certificate to handle HTTPS requests is incorrect because this solution entails an additional cost. Remember that you have to pay a monthly fee for the operation of each private CA until you delete it. A more cost-effective solution is to use a public certificate instead since this is free of charge.
The option that says: Generate a Public Certificate in ACM. Configure the two EC2 instances to use the Public Certificate to handle HTTPS requests is incorrect because you cannot export public certificates from ACM and use them with your EC2 instances. You can only use the public certificate from ACM in Amazon CloudFront, Elastic Load Balancing, and Amazon API Gateway.
The option that says: Generate a Private Certificate in ACM. Configure the two EC2 instances to use the Private Certificate to handle HTTPS requests is incorrect. Although you can export private certificates from ACM and use them with EC2 instances, using this type of certificate still costs more than a public certificate.

References:
https://aws.amazon.com/certificate-manager/pricing/
https://aws.amazon.com/certificate-manager/faqs/

Check out this AWS Billing and Cost Management Cheat Sheet:
https://tutorialsdojo.com/aws-billing-and-cost-management/

How can I add certificates for websites to the ELB using Amazon Certificate Manager?
https://youtu.be/pTQrAZbHmRU

</details>

<a id="q37"></a>

## Q37

A company is building a new cryptocurrency trading platform that will be hosted on the AWS cloud. The solutions architect needs to set up the designed architecture in a single VPC. The solution should mitigate distributed denial-of-service (DDoS) attacks to secure the company’s applications and systems. The solution should also include a notification for incoming Layer 3 or Layer 4 attacks such as SYN floods and UDP reflection attacks. The system should also be protected against SQL injection, cross-site scripting, and other Layer 7 attacks. 
Which of the following solutions should the solutions architect implement together to meet the above requirement? (Select TWO.)

- **A.** Place your servers behind a CloudFront web distribution and improve your cache hit ratio.
- **B.** Use AWS Shield Advanced which provides enhanced DDoS attack detection and monitoring for application-layer traffic to your AWS resources.
- **C.** Set up rule-based filtering using the AWS Network Firewall service.
- **D.** Send network logs to Amazon Fraud Detector to detect DDoS attacks and send notifications to security teams.
- **E.** Use AWS WAF to define customizable web security rules that control which traffic can access your web applications.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** A, B

🔑 **Key words:** L3/L4 DDoS notification + SQLi/XSS protection (Select TWO)

🪤 **Your trap:** Picked B (right) + A: CloudFront cache hit ratio does not block L7 attacks

🧠 **Rule:** L3/L4 DDoS + alerts → Shield Advanced; SQLi/XSS → WAF.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Internet (traffic bình thường + kẻ tấn công)
        │
        ▼
 ┌─────────────────────────────┐
 │   Cryptocurrency platform    │   1 VPC duy nhất
 │                              │
 │  Cần: báo động L3/L4 DDoS    │
 │       (SYN flood, UDP reflect)│
 │  Cần: chặn L7 (SQLi, XSS)    │
 └─────────────────────────────┘
```

Chọn **HAI** giải pháp phối hợp. Đáp án đúng: **B (Shield Advanced)** + **E (WAF)**. Anh chọn đúng B, nhưng pick thứ hai là **A (CloudFront + cache hit ratio)** — chính pick này phá hỏng bộ giải pháp vì nó không giải quyết yêu cầu L7.

#### Vì sao B + E đúng — hai mảnh ghép bổ sung cho nhau

Yêu cầu có **hai phần tách biệt**:

1. **Phát hiện + cảnh báo tấn công L3/L4** (SYN flood, UDP reflection) → đây là đúng phạm vi của **AWS Shield Advanced**: cung cấp enhanced detection/monitoring cho traffic ở tầng network/transport, kèm visibility và thông báo khi có tấn công.
2. **Chặn tấn công L7** (SQL injection, XSS) → đây là đúng phạm vi của **AWS WAF**: định nghĩa rule tùy chỉnh để lọc request HTTP độc hại trước khi tới ứng dụng.

Hai dịch vụ này **giải quyết hai tầng khác nhau** của cùng một yêu cầu, không dịch vụ nào một mình đủ — đó là lý do "Select TWO" và cả hai phải đúng mới tạo thành một giải pháp hoàn chỉnh.

#### Vì sao A (lựa chọn thứ hai của Anh) sai, dù nghe "liên quan DDoS"

CloudFront đúng là có vai trò trong phòng thủ DDoS (hấp thụ traffic, cache ở edge), nhưng option A chỉ nói **"đặt sau CloudFront và cải thiện cache hit ratio"** — đây là một hành động **tối ưu performance**, không phải một cơ chế **phát hiện/cảnh báo L3-L4 hay chặn L7**. Cải thiện cache hit ratio không ngăn SYN flood, không cảnh báo khi bị UDP reflection, và hoàn toàn không chặn SQLi/XSS. Option này còn thiếu luôn các tính năng CloudFront thực sự hữu ích cho bảo mật (geoblocking, enforce HTTPS). Vì vậy dù "trông có vẻ đúng hướng", nó không đáp ứng được yêu cầu cụ thể trong đề — và vì đây là câu 2-lựa-chọn, việc chọn sai 1 trong 2 khiến cả cặp giải pháp không đầy đủ.

#### Các lựa chọn sai còn lại

- **C — AWS Network Firewall:** dùng để quản lý rule filtering cho **nhiều VPC/nhiều account** trong một Organization. Đề bài chỉ nói **một VPC duy nhất**, nên không phù hợp quy mô.
- **D — Amazon Fraud Detector:** dịch vụ machine learning để phát hiện **gian lận giao dịch** (fraud), không phải để phát hiện/giảm thiểu DDoS.

| Lựa chọn | Giải quyết gì | Vấn đề |
|---|---|---|
| **B (đúng)** | Phát hiện & cảnh báo DDoS L3/L4 | — |
| **E (đúng)** | Chặn SQLi/XSS tầng L7 | — |
| A | Cache hit ratio, không phải bảo mật | Không đáp ứng notification L3/L4 lẫn chặn L7 |
| C | Multi-VPC/multi-account firewall rules | Sai quy mô (chỉ 1 VPC) |
| D | Phát hiện gian lận giao dịch | Không liên quan DDoS |

#### Lưu ý thực tế

- Shield **Standard** đã bật miễn phí cho mọi account, bảo vệ cơ bản L3/L4. Shield **Advanced** mới có detection/monitoring nâng cao cho application-layer traffic, DDoS cost protection, và visibility/report chi tiết — đây là điểm phân biệt khi đề nhấn "enhanced detection and monitoring".
- AWS Network Firewall nhắm tới việc quản lý tập trung rule cho **nhiều VPC/account trong Organization**, không phải công cụ WAF-cấp-ứng-dụng.

#### Quy tắc nhớ cho thi

- **"L3/L4 DDoS + cần notification/monitoring"** → **AWS Shield Advanced**.
- **"SQLi, XSS, chặn request độc hại tầng ứng dụng"** → **AWS WAF**.
- **"Nhiều VPC/account cần rule filtering tập trung"** → AWS Network Firewall (không phải khi chỉ có 1 VPC).
- **"Chỉ cải thiện cache/performance của CloudFront"** → không tự động là giải pháp bảo mật, đọc kỹ option có thật sự nói tới detection/blocking hay không.

### TD explanation

A Distributed Denial of Service (DDoS) attack is a malicious attempt to make a targeted system, such as a website or application, unavailable to end users. To achieve this, attackers use a variety of techniques that consume network or other resources, interrupting access for legitimate end-users.

AWS provides flexible infrastructure and services that help customers implement strong DDoS mitigations and create highly available application architectures that follow AWS Best Practices for DDoS Resiliency. These include services such as Amazon Route 53, Amazon CloudFront, Elastic Load Balancing, and AWS WAF to control and absorb traffic and deflect unwanted requests. These services integrate with AWS Shield, a managed DDoS protection service that provides always-on detection and automatic inline mitigations to safeguard web applications running on AWS.
AWS WAF is a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow or block to your web applications by defining customizable web security rules. You can use AWS WAF to create custom rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that are designed for your specific application. New rules can be deployed within minutes, letting you respond quickly to changing traffic patterns. Also, AWS WAF includes a full-featured API that you can use to automate the creation, deployment, and maintenance of web security rules.
In this scenario, AWS Shield Advanced and AWS WAF are the two services that can provide optimal DDoS attack mitigation and protection against Layer 7 security risks to your cloud infrastructure.
Therefore the correct answers are:
– Use AWS Shield Advanced which provides enhanced DDoS attack detection and monitoring for application-layer traffic to your AWS resources.
– Use AWS WAF to define customizable web security rules that control which traffic can access your web applications.
The option that says: Send network logs to Amazon Fraud Detector to detect DDoS attacks and send notifications to security teams is incorrect. Amazon Fraud Detector uses machine learning that automates the detection of potentially fraudulent activities online. It is designed to predict fraudulent transactions based on previous data sets that were used to create a model. It is not designed to detect and mitigate DDoS attacks. AWS Shield is a more suitable service for this scenario.
The option that says: Place your servers behind a CloudFront web distribution and improve your cache hit ratio is incorrect. Although CloudFront can help mitigate DDoS attacks, improving the cache hit ratio of your CloudFront distribution is still not enough to totally protect your infrastructure. This option also fails to mention the geoblocking and HTTPS protocol support features of CloudFront. Using AWS Shield Advanced and AWS WAF will provide more effective protection against DDoS.
The option that says: Set up rule-based filtering using the AWS Network Firewall service is incorrect. AWS Network Firewall is primarily used to manage multiple firewall rules across hundreds of Amazon VPCs and AWS Accounts that are usually under a single AWS Organization. It is explicitly mentioned in the scenario that the company is using its sole AWS account, and the solution is only running on a single Amazon VPC. Hence, using the AWS Network Firewall service is not suitable for this case.

References:
https://aws.amazon.com/answers/networking/aws-ddos-attack-mitigation/
https://d0.awsstatic.com/whitepapers/Security/DDoS_White_Paper.pdf
https://aws.amazon.com/network-firewall

Check out these AWS WAF and AWS Shield Cheat Sheets:
https://tutorialsdojo.com/aws-waf/
https://tutorialsdojo.com/aws-shield/

</details>

<a id="q44"></a>

## Q44

An international insurance company has clients all across the globe. The company has financial files that are stored in an Amazon S3 bucket which is behind CloudFront. At present, their clients can access their data by directly using an S3 URL or using their CloudFront distribution. The company wants to deliver their content to a specific client in California and they need to make sure that only that client can access the data. 
Which of the following options is a valid solution that meets the above requirements? (Select TWO.)

- **A.** Use CloudFront signed URLs to ensure that only their client can access the files. Create an origin access control (OAC) and give it permission to read the files in the bucket. Remove permission to use Amazon S3 URLs to read the files for anyone else.
- **B.** Use CloudFront signed URLs to ensure that only their client can access the files. Enable field-level encryption in your CloudFront distribution.
- **C.** Use CloudFront Signed Cookies to ensure that only their client can access the files. Enable HTTPS in your CloudFront distribution.
- **D.** Create a new S3 bucket in US West (N. California) region and upload the files. Set up an origin access control (OAC) and give it permission to read the files in the bucket. Enable HTTPS in your CloudFront distribution.
- **E.** Create a new S3 bucket in US West (N. California) region and upload the files. Use S3 pre-signed URLs to ensure that only their client can access the files. Remove permission to use Amazon S3 URLs to read the files for anyone else.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, E · **You picked:** A, D

🔑 **Key words:** only one specific client may access files; S3 behind CloudFront (Select TWO)

🪤 **Your trap:** Picked A (right) + D: OAC forces CloudFront path but anyone with the CloudFront URL still gets in

🧠 **Rule:** Restrict to a specific client → signed URLs (CloudFront or S3 pre-signed) + block direct S3 access.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Clients (nhiều người) ──┬──► S3 URL trực tiếp ──► S3 bucket (financial files)
                         │
                         └──► CloudFront distribution ──► S3 bucket (origin)

Yêu cầu: CHỈ một client cụ thể ở California được phép truy cập dữ liệu.
Hiện tại: cả S3 URL lẫn CloudFront URL đều truy cập được → phải khóa CẢ HAI đường.
```

Chọn **HAI** giải pháp. Đáp án đúng: **A (CloudFront signed URL + OAC, khóa S3 URL)** + **E (bucket mới ở N. California + S3 pre-signed URL, khóa S3 URL công khai)**. Anh chọn đúng A, nhưng pick thứ hai là **D (bucket N. California + OAC, enable HTTPS)** — pick này phá hỏng giải pháp vì **D không chứng thực được "chỉ một client cụ thể"**.

#### Vì sao A đúng — chặn cả 2 đường vào

A giải quyết đầy đủ bài toán gốc (S3 sau CloudFront, hiện có 2 đường truy cập):

1. **CloudFront signed URL**: tạo URL có chữ ký, chỉ người có URL đó (do công ty cấp riêng cho client California) mới truy cập được qua CloudFront.
2. **OAC (Origin Access Control)**: đảm bảo bucket S3 chỉ nhận request đến **từ CloudFront**, không ai gọi trực tiếp vào origin.
3. **Remove permission dùng S3 URL trực tiếp**: chặn nốt đường vòng — vì nếu không làm bước này, ai cũng gõ thẳng S3 URL là vào được, bất chấp CloudFront có signed URL hay không.

Ba yếu tố này **cùng nhau** mới tạo thành một giải pháp đầy đủ — thiếu bất kỳ yếu tố nào, client khác vẫn có đường lách.

#### Vì sao E đúng — nửa còn lại của bộ giải pháp (bucket mới + pre-signed URL)

TD coi E là lựa chọn đúng thứ hai: tạo **bucket mới tại US West (N. California)** (theo đúng ngữ cảnh "deliver content to client ở California"), dùng **S3 pre-signed URL** để chỉ người có URL (được cấp riêng, có hạn dùng) mới tải được object, và **remove permission S3 URL công khai** cho những người khác. Đây là một con đường khác (không đi qua CloudFront) nhưng vẫn đạt mục tiêu "chỉ client đó truy cập được" nhờ cơ chế pre-signed URL + chặn truy cập trực tiếp.

#### Vì sao D (lựa chọn của Anh) sai — thiếu thành phần "chỉ MỘT client"

D cũng tạo bucket mới + OAC + HTTPS — nghe rất giống A/E, nhưng **thiếu đúng mảnh quan trọng nhất**: OAC chỉ đảm bảo request phải đi qua CloudFront ("chỉ dùng CloudFront URL, không dùng S3 URL trực tiếp"), **chứ không giới hạn AI được dùng CloudFront URL đó**. Nói cách khác:

- OAC = khóa cửa sau (S3 trực tiếp)
- Nhưng cửa trước (CloudFront URL) vẫn mở cho **bất kỳ ai** có URL, vì không có signed URL/signed cookie để xác thực.

→ Bất kỳ client nào biết CloudFront URL vẫn truy cập được, không riêng gì client California. TD xác nhận: D "có thể là giải pháp hợp lệ NẾU đề cập thêm Signed URL hoặc Signed Cookies" — nhưng đề không nói, nên D không đủ.

#### Lựa chọn sai còn lại

- **C — Signed Cookies + HTTPS:** Signed Cookies phù hợp hơn khi cần cấp quyền truy cập **nhiều file cùng lúc** (ví dụ cả bộ file HLS video), không tối ưu cho "một client, một tập file cụ thể". Quan trọng hơn, **không có bước chặn S3 URL trực tiếp**, nên vẫn có thể bị bypass.
- **B — Signed URL + field-level encryption:** field-level encryption mã hóa field dữ liệu nhạy cảm (ví dụ số thẻ) ở tầng request, không liên quan đến việc giới hạn ai truy cập. Thiếu bước chặn S3 URL trực tiếp → vẫn bypass được.

| Lựa chọn | Chặn S3 URL trực tiếp? | Giới hạn đúng 1 client? | Đạt yêu cầu |
|---|---|---|---|
| **A (đúng)** | Có (OAC + remove permission) | Có (signed URL) | Đạt |
| **E (đúng)** | Có (remove permission) | Có (pre-signed URL) | Đạt |
| D (Anh chọn) | Có (OAC) | **Không** | Thiếu |
| C | Không | Một phần | Thiếu |
| B | Không | Một phần | Thiếu |

#### Lưu ý thực tế

- OAC chỉ kiểm soát **nguồn gốc request** (phải từ CloudFront), hoàn toàn khác với việc kiểm soát **danh tính người dùng cuối**. Hai khái niệm này hay bị đề thi đánh tráo.
- Signed URL phù hợp cho một số lượng file giới hạn/một client cụ thể; Signed Cookies phù hợp khi cần cấp quyền cho nhiều file cùng lúc (subscription-based access).

#### Quy tắc nhớ cho thi

- **"Chỉ 1 client cụ thể được xem" + "S3 phía sau CloudFront"** → cần cả Signed URL/Cookie (hoặc pre-signed URL) **VÀ** chặn truy cập trực tiếp (OAC + remove S3 permission).
- **"Có OAC nhưng không có Signed URL/Cookie"** → chỉ chặn được cửa sau, không giới hạn được ai dùng CloudFront URL → sai nếu đề yêu cầu giới hạn 1 người dùng cụ thể.
- **"Nhiều file cùng lúc, kiểu subscription"** → Signed Cookies; **"một vài file/một client"** → Signed URL hoặc pre-signed URL.

### TD explanation

Many companies that distribute content over the internet want to restrict access to documents, business data, media streams, or content that is intended for selected users, for example, users who have paid a fee. To securely serve this private content by using CloudFront, you can do the following:
– Require that your users access your private content by using special CloudFront signed URLs or signed cookies.
– Require that your users access your Amazon S3 content by using CloudFront URLs, not Amazon S3 URLs. Requiring CloudFront URLs isn’t necessary, but it is recommended to prevent users from bypassing the restrictions that you specify in signed URLs or signed cookies.

All objects and buckets by default are private. The presigned URLs are useful if you want your user/customer to be able to upload a specific object to your bucket, but you don’t require them to have AWS security credentials or permissions. You can generate a presigned URL programmatically using the AWS SDK for Java or the AWS SDK for .NET. If you are using Microsoft Visual Studio, you can also use AWS Explorer to generate a presigned object URL without writing any code. Anyone who receives a valid presigned URL can then programmatically upload an object.
Therefore, the correct answer is: Create a new S3 bucket in US West (N. California) region and upload the files. Use S3 pre-signed URLs to ensure that only their client can access the files. Remove permission to use Amazon S3 URLs to read the files for anyone else and Use CloudFront signed URLs to ensure that only their client can access the files. Create an origin access control (OAC) and give it permission to read the files in the bucket. Remove permission to use Amazon S3 URLs to read the files for anyone else. Using a presigned URL to your S3 bucket will prevent other users from getting your private data which is intended to a certain client. A combination of Signed URL and OAC is also a valid solution that meets the requirement.
The option that says: Use CloudFront Signed Cookies to ensure that only their client can access the files. Enable HTTPS in your CloudFront distribution is incorrect. The signed cookies feature is primarily used if you want to provide access to multiple restricted files, for example, all of the files for a video in HLS format or all of the files in the subscribers’ area of website. In addition, this solution is not complete since the users can bypass the restrictions by simply using the direct S3 URLs.
The option that says: Use CloudFront signed URLs to ensure that only their client can access the files. Enable field-level encryption in your CloudFront distribution is incorrect. Although this solution is valid, the users can still bypass the restrictions in CloudFront by simply connecting to the direct S3 URLs.
The option that says: Create a new S3 bucket in US West (N. California) region and upload the files. Set up an origin access control (OAC) and give it permission to read the files in the bucket. Enable HTTPS in your CloudFront distribution is incorrect. An Origin Access Control (OAC) will only require your client to only access the files by using the CloudFront URL and not through a direct S3 URL. This can be a possible solution if it mentions the use of Signed URL or Signed Cookies.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

S3 Pre-signed URLs vs CloudFront Signed URLs vs Origin Access Control (OAC)
https://tutorialsdojo.com/s3-pre-signed-urls-vs-cloudfront-signed-urls-vs-origin-access-identity-oai-origin-access-control-oac/

Comparison of AWS Services Cheat Sheets:
https://tutorialsdojo.com/comparison-of-aws-services/

</details>

<a id="q49"></a>

## Q49

A company wants to improve data protection for the sensitive information stored on its AWS account – both in transit and at rest. Data protection in transit simply means that the data should be secured while it travels to and from Amazon S3. Data protection at rest means that the stored data on disk must be secured in S3 data centers. The data can be protected in transit by using SSL or by using client-side encryption. To secure data at rest, there are a variety of available Server-Side Encryption that can be used in S3. The company currently uses Mountpoint for Amazon S3 to provide high-performance file access to its S3 buckets, and its now evaluating server‑side encryption options to protect its data at rest.
Which of the following best describes how the S3-Managed Keys (SSE-S3) encryption method works?

- **A.** SSE-S3 provides strong multi-factor encryption in which each object is encrypted with a unique key. It also encrypts the key itself with a master key that it rotates regularly.
- **B.** In SSE-S3, you will be able to manage the AWS KMS keys and S3 manages the encryption for reading and writing objects in your S3 bucket.
- **C.** In SSE-S3, a randomly generated data encryption key is returned which is used by the client to encrypt the object data.
- **D.** SSE-S3 provides separate permissions to use an API key that provides added protection against unauthorized access of your objects in S3.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** how SSE-S3 works

🪤 **Your trap:** 'You manage KMS keys' describes SSE-KMS, not SSE-S3

🧠 **Rule:** SSE-S3: unique key per object, encrypted by AWS-managed rotated root key. SSE-KMS: your KMS key. SSE-C: you supply key.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Object upload vào S3 bucket
        │
        ▼
Server-Side Encryption (SSE) tại S3:
   ┌─────────────┬─────────────┬─────────────┐
   │   SSE-S3     │  SSE-KMS    │   SSE-C     │
   │ S3 tự quản   │ bạn quản    │ bạn tự cấp  │
   │ lý key       │ KMS key     │ key riêng   │
   └─────────────┴─────────────┴─────────────┘
```

Công ty dùng Mountpoint for S3, đang đánh giá cơ chế SSE để bảo vệ dữ liệu at-rest. Câu hỏi: **SSE-S3 hoạt động như thế nào?** Đáp án đúng: **A**. Anh chọn **B** — mô tả sai, vì B thực chất đang nói về **SSE-KMS**.

#### Vì sao A đúng

TD explanation trích gần như nguyên văn tài liệu AWS: *"Server-side encryption with Amazon S3-managed encryption keys (SSE-S3) uses strong multi-factor encryption. Amazon S3 encrypts each object with a unique key. As an additional safeguard, it encrypts the key itself with a master key that it rotates regularly."* Cơ chế gồm 2 lớp:

```
Object  ──encrypt──►  Unique data key (riêng cho từng object)
                            │
                            ▼
                   Master key (AWS quản lý, tự động rotate định kỳ)
                   ──encrypt──► data key được bọc bởi master key
```

Tất cả key — cả data key lẫn master key — đều do **AWS/S3 quản lý hoàn toàn**, dùng AES-256. Người dùng không cần làm gì ngoài việc bật SSE-S3 (hoặc để default encryption xử lý).

#### Vì sao B (lựa chọn của Anh) sai — nhầm với SSE-KMS

B viết: *"bạn sẽ quản lý được KMS keys, còn S3 lo việc encrypt/decrypt."* Đây chính là mô tả của **SSE-KMS** — nơi key nằm trong AWS KMS và **bạn** (customer) có quyền kiểm soát key (tạo, xoay vòng, thu hồi quyền, xem audit trail qua CloudTrail). Trong khi đó, **SSE-S3 không hề liên quan tới KMS** — toàn bộ vòng đời key (data key + master key) đều do S3 tự quản lý nội bộ, người dùng không nhìn thấy hay can thiệp được. Nhầm hai cơ chế này là lỗi rất phổ biến vì cả hai đều "server-side" và đều AES-256, chỉ khác ở **ai giữ quyền kiểm soát key**.

#### Các lựa chọn sai còn lại

- **C — "randomly generated data encryption key... client dùng để encrypt":** đây mô tả kiểu cơ chế **client-side encryption** (client tự giữ/encrypt bằng key), không phải SSE-S3 — SSE nghĩa là **S3** thực hiện encrypt/decrypt phía server, client không tham gia vào quá trình mã hóa.
- **D — "separate permissions using an API key":** SSE-S3 không dùng khái niệm "API key" để bảo vệ object; đây là mô tả sai hoàn toàn, không khớp với bất kỳ cơ chế SSE nào của S3.

| Cơ chế | Ai giữ/quản lý key | Đặc điểm |
|---|---|---|
| **SSE-S3 (đúng)** | S3 tự quản lý toàn bộ (data key + master key) | Đơn giản nhất, không cấu hình thêm |
| SSE-KMS (mô tả trong B) | Bạn quản lý KMS key (policy, rotation, audit) | Kiểm soát chi tiết hơn, có CloudTrail |
| SSE-C | Bạn tự cung cấp key cho mỗi request | S3 không lưu key, bạn chịu trách nhiệm |

#### 📝 Ghi chú kỹ thuật

Cụm **"strong multi-factor encryption"** trong đáp án A nghe giống **multi-factor authentication (MFA)**, nhưng ở đây **không liên quan gì đến MFA**. Đây là cách AWS diễn đạt việc SSE-S3 dùng **nhiều lớp mã hóa chồng lên nhau** (data key riêng cho từng object + master key bọc data key đó, rotate định kỳ) — tức "multiple factors/layers of encryption", không phải "xác thực đa yếu tố". Từ ngữ này xuất hiện nguyên văn trong tài liệu AWS cũ, nên dù hơi gây hiểu lầm, đây vẫn là cách diễn đạt chính thức mô tả đúng cơ chế 2 lớp của SSE-S3 — không phải lỗi hay bẫy của đề, cứ giữ nguyên đáp án A theo đúng facts AWS mô tả.

#### Quy tắc nhớ cho thi

- **"S3 tự quản lý hết, bạn không đụng vào key"** → **SSE-S3**.
- **"Bạn quản lý/kiểm soát KMS key, xem audit trail"** → **SSE-KMS**.
- **"Bạn tự cấp key qua request, S3 không lưu"** → **SSE-C**.
- **"multi-factor encryption" trong SSE-S3** → không phải MFA, chỉ là 2 lớp key (data key + master key).

### TD explanation

With Amazon S3 default encryption, you can set the default encryption behavior for an S3 bucket so that all new objects are encrypted when they are stored in the bucket. The objects are encrypted using server-side encryption with either Amazon S3-managed keys (SSE-S3) or AWS KMS keys stored in AWS Key Management Service (SSE-KMS).
When you configure your bucket to use default encryption with SSE-KMS, you can also enable S3 Bucket Keys to decrease request traffic from Amazon S3 to AWS Key Management Service (AWS KMS) and reduce the cost of encryption. When you use server-side encryption, Amazon S3 encrypts an object before saving it to disk and decrypts it when you download the object.
Server-side encryption with Amazon S3-managed encryption keys (SSE-S3) uses strong multi-factor encryption. Amazon S3 encrypts each object with a unique key. As an additional safeguard, it encrypts the key itself with a master key that it rotates regularly. Amazon S3 server-side encryption uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt your data.

Therefore, the correct answer is: SSE-S3 provides strong multi-factor encryption in which each object is encrypted with a unique key. It also encrypts the key itself with a master key that it rotates regularly.
The option that says: SSE-S3 provides separate permissions to use an API key that provides added protection against unauthorized access of your objects in S3 is incorrect. SSE-S3 does not simply use API keys but rather encryption keys.
The option that says: In SSE-S3, you will be able to manage the AWS KMS keys and S3 manages the encryption for reading and writing objects in your S3 bucket is incorrect. KMS keys are being used in SSE-KMS and not in SSE-S3.
The option that says: In SSE-S3, a randomly generated data encryption key is returned which is used by the client to encrypt the object data is incorrect. SSE-S3 does not just use a randomly generated data encryption key.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

---

# Group C — DR / HA / database resilience (6)

<a id="q7"></a>

## Q7

A company has an Oracle Real Application Clusters (RAC) database on their on-premises data center which they want to migrate to AWS. The Chief Information Security Officer (CISO) instructed the solutions architects to automate the patch management process of the operating system in which the database runs, as well as to set up scheduled backups to comply with the company’s disaster recovery plan. 
Which of the following should the solutions architect implement to meet the company requirements with the least amount of effort?

- **A.** Launch a Lambda function that would automate the creation of snapshots of the database in the EC2 instance. Use the CodeDeploy and CodePipeline service to automate the patch management process of the database.
- **B.** Migrate the database to Amazon Aurora and enable automated backups for your Aurora RAC cluster. Patching is automatically handled in Aurora during the system maintenance window.
- **C.** Migrate the database to a cluster of EBS-backed Amazon EC2 instances across multiple AZs. Automate the creation of EBS snapshots from EBS volumes of the EC2 instance by using Amazon Data Lifecycle Manager. Install the SSM Agent to the EC2 instance and automate the patch management process using AWS Systems Manager Patch Manager.
- **D.** Migrate the database to Amazon RDS which provides a multi-AZ failover feature for your RAC cluster. This will also reduce the RPO and RTO in the event of system failure since RDS offers features such as patch management and maintenance of the underlying host.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** Oracle RAC; automate OS patching + scheduled backups; least effort

🪤 **Your trap:** RDS (and Aurora) do not support Oracle RAC

🧠 **Rule:** Oracle RAC → EC2 + Data Lifecycle Manager snapshots + SSM Patch Manager.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises: Oracle RAC (Real Application Clusters)
Yêu cầu: tự động hoá patch OS + backup theo lịch, LEAST EFFORT

RAC = nhiều node DB dùng chung 1 storage (shared-disk cluster)
      ┌────────┐  ┌────────┐
      │ Node 1 │  │ Node 2 │
      └───┬────┘  └───┬────┘
          └─────┬──────┘
          Shared storage (cần quyền truy cập OS/disk cấp thấp)
```

Đáp án đúng: **C** (EC2 + Data Lifecycle Manager + SSM Patch Manager). Anh chọn **D** (RDS Multi-AZ).

#### Vì sao C đúng

Oracle RAC đòi hỏi quyền kiểm soát ở tầng OS và storage (shared-disk cluster, cluster interconnect) mà RDS/Aurora — vốn là managed service ẩn hết phần OS — không cung cấp. Muốn chạy RAC trên AWS, chỉ còn cách tự dựng trên **EC2** (self-managed), và TD explanation nói rõ: *"Amazon RDS does not support certain features in Oracle such as Multitenant Database, Real Application Clusters (RAC)..."*.

Với yêu cầu "tự động hoá patch + backup, ít công sức nhất" trên nền EC2, hai dịch vụ khớp sẵn:

```
Backup theo lịch   → Amazon Data Lifecycle Manager (tự động tạo EBS snapshot)
Patch OS tự động   → AWS Systems Manager Patch Manager (cần cài SSM Agent)
```

Đây là tổ hợp managed-automation tốt nhất có thể đạt được khi buộc phải tự quản lý OS (vì RAC).

#### Vì sao D (lựa chọn của anh) sai — và vì sao nó liên quan trực tiếp đến Q68

**D sai vì Amazon RDS không hỗ trợ Oracle RAC**, bất kể Multi-AZ hay không. RDS là dịch vụ managed, AWS kiểm soát toàn bộ tầng OS/storage bên dưới — không có chỗ để chạy cluster shared-disk như RAC. Đề bài nói "Multi-AZ failover feature for your RAC cluster" nghe hợp lý vì Multi-AZ đúng là cơ chế HA của RDS, nhưng **RAC cluster không thể tồn tại trong RDS** — option này tự mâu thuẫn ngay từ giả định.

Đây chính là cùng một lỗi khái niệm sẽ gặp lại ở **Q68** (bài DB Oracle HA): câu đó có hẳn một option "Create Oracle RAC in Amazon RDS" làm mồi nhử, và đáp án đúng ở đó là RDS Multi-AZ (không có RAC) — tức là ngược hướng với bài này. Hai bài này là hai mặt của cùng một rule:

```
RAC + RDS/Aurora  →  LUÔN LUÔN SAI (RDS/Aurora không hỗ trợ RAC)
Muốn chạy RAC thật →  BẮT BUỘC tự dựng trên EC2
```

#### Các phương án sai khác

- **B (Aurora "RAC cluster")** sai cùng lý do với D — Aurora cũng không hỗ trợ RAC. TD explanation liệt kê B và D vào cùng nhóm incorrect vì "an Amazon RDS database does not support Oracle RAC" (Aurora dùng chung engine-family logic).
- **A (Lambda snapshot + CodeDeploy/CodePipeline)** sai vì CodeDeploy/CodePipeline là dịch vụ CI/CD (deploy ứng dụng), không phải công cụ patch OS. Dùng sai nhóm dịch vụ cho đúng mục đích.

| Phương án | Nền tảng | RAC được hỗ trợ? | Patch tự động | Backup tự động |
|---|---|---|---|---|
| **C (đúng)** | EC2 | Có (tự quản lý) | SSM Patch Manager | Data Lifecycle Manager |
| B | Aurora | Không | Managed (nhưng vô nghĩa vì không chạy được RAC) | Managed |
| D | RDS | Không | Managed (nhưng vô nghĩa vì không chạy được RAC) | Managed |
| A | EC2 | Có | Sai công cụ (CodeDeploy/CodePipeline) | Lambda tự viết |

#### Quy tắc nhớ cho thi

- **Thấy "Oracle RAC"** → loại ngay mọi option có RDS hoặc Aurora, bất kể feature gì đi kèm (Multi-AZ, backup, RAC cluster...).
- **RAC chỉ chạy được trên EC2** (self-managed OS/storage).
- **Patch OS tự động trên EC2** → SSM Patch Manager (không phải CodeDeploy/CodePipeline — đó là CI/CD).
- **Backup EBS tự động theo lịch** → Amazon Data Lifecycle Manager (DLM).

### TD explanation

Amazon RDS does not support certain features in Oracle such as Multitenant Database, Real Application Clusters (RAC), Unified Auditing, Database Vault, and many more.
AWS Systems Manager Patch Manager automates the process of patching managed instances with security-related updates. For Linux-based instances, you can also install patches for non-security updates. You can patch fleets of Amazon EC2 instances or your on-premises servers and virtual machines (VMs) by operating system type. This includes supported versions of Windows Server, Ubuntu Server, Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), CentOS, Amazon Linux, and Amazon Linux 2. You can scan instances to see only a report of missing patches, or you can scan and automatically install all missing patches.

Hence, the option that says: Migrate the database to a cluster of EBS-backed Amazon EC2 instances across multiple AZs. Automate the creation of EBS snapshots from EBS volumes of the EC2 instance by using Amazon Data Lifecycle Manager. Install the SSM Agent to the EC2 instance and automate the patch management process using AWS Systems Manager Patch Manager is correct. Oracle RAC is supported via the deployment using Amazon EC2. AWS Systems Manager Patch Manager automates the process of patching managed instances with security-related updates.
The following options are both incorrect because an Amazon RDS database does not support Oracle RAC:
1. Migrate the database to Amazon RDS which provides a multi-AZ failover feature for your RAC cluster. This will also reduce the RPO and RTO in the event of system failure since RDS offers features such as patch management and maintenance of the underlying host.
2. Migrate the database to Amazon Aurora and enable automated backups for your Aurora RAC cluster. Patching is automatically handled in Aurora during the system maintenance window
The option that says: Launch a Lambda function that would automate the creation of snapshots of the database in the EC2 instance. Use the CodeDeploy and CodePipeline service to automate the patch management process of the database is incorrect because CodeDeploy and CodePipeline are CI/CD services and are not suitable for patch management. You should use AWS Systems Manager Patch Manager instead.

References:
https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html
https://aws.amazon.com/rds/oracle/faqs/

Check out this Amazon RDS Cheat Sheet:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

<a id="q9"></a>

## Q9

An e-commerce company is running a three-tier application on AWS. The application includes a web tier as frontend, an application tier as backend, and the database tier that stores the transactions and users’ data. The database is currently hosted on an extra-large instance with 128 GB of memory. The company is also considering using Amazon Managed Grafana to monitor the performance of its application infrastructure. 
For the company’s business continuity and disaster recovery plan, the Solutions Architect must ensure a Recovery Time Objective (RTO) of 5 minutes and a Recovery Point Objective (RPO) of 1 hour on the backup site in the event that the application goes down. There is also a requirement for the backup site to be at least 250 miles away from the primary site. 
Which of the following solutions must the Solutions Architect implement to meet the company’s disaster recovery requirements while keeping the cost at a minimum?

- **A.** On the backup region, create a scaled-down version of the fully functional environment with one Amazon EC2 instance of the web server and application server in their own Auto Scaling groups behind Application Load Balancers. Create a standby database instance that replicates data from the primary database. In case of disaster, scale the instances to meet the demand and update the Amazon Route 53 record to point to the backup region.
- **B.** Create a frequently scheduled backup of the application and database that will be stored on an Amazon S3 bucket. Configure S3 Cross-Region Replication (CRR) on the bucket to copy the backups to another region. In case of disaster, use an AWS CloudFormation template to quickly replicate the same resources to the backup region and restore the data from the S3 bucket.
- **C.** Use a pilot light strategy for the backup region. Configure the primary database to replicate data to a large standby instance in the backup region. In case of a disaster, vertically resize the database instance to meet the full demand. Create an AWS CloudFormation template to quickly provision the same web servers, application servers, and load balancers on the backup region. Update the Amazon Route 53 records to point to the backup region.
- **D.** Use a multi-region strategy for the backup region to comply with the tight RTO and RPO requirements. Create a fully functional web, application, and database tier on the backup region with the same capacity as the primary region. Set the database on the backup region on standby mode. In case of disaster, update the Amazon Route 53 record to point to the backup region.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** RTO 5 minutes, RPO 1 hour, ≥250 miles away, minimal cost

🪤 **Your trap:** Pilot light needs CloudFormation to build web/app tiers after disaster → exceeds 5 min

🧠 **Rule:** RTO hours → backup/restore; tens of min → pilot light; minutes → warm standby; ~0 → multi-site.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Primary region                      DR region (≥250 miles)
┌─────────────────────┐             ┌─────────────────────┐
│ Web + App (full)     │             │ ???                 │
│ DB (xlarge, 128GB)   │  replicate │                       │
└─────────────────────┘             └─────────────────────┘

Yêu cầu: RTO = 5 phút, RPO = 1 giờ, chi phí TỐI THIỂU
```

Đáp án đúng: **A (warm standby)**. Anh chọn **C (pilot light)**.

⚠️ **Lỗi lặp lại:** Đây là lần thứ hai trong đợt ôn lẫn giữa pilot light và warm standby (TD Set 1 Q10 cũng về DR). Cần khắc kỹ bảng RTO/RPO bên dưới.

#### DR ladder — 4 chiến lược theo thứ tự RTO/RPO giảm dần

```
Backup & Restore   Pilot Light        Warm Standby        Multi-site active-active
RPO: giờ           RPO: phút          RPO: giây            RPO: ~0
RTO: ≤24h          RTO: giờ           RTO: phút             RTO: ~0
                                                              
Chỉ backup data    DB luôn chạy,      Toàn bộ stack chạy    Chạy full tải
khôi phục khi cần  app server TẮT,    ở quy mô THU NHỎ,     ở NHIỀU region
                    bật lên khi cần    scale up khi cần       cùng lúc
```

| Chiến lược | RTO | RPO | Chi phí |
|---|---|---|---|
| Backup & restore | giờ → ≤24h | giờ | Thấp nhất |
| Pilot light | giờ | phút | Thấp |
| **Warm standby** | **phút** | **giây** | Trung bình |
| Multi-site active-active | gần 0 | gần 0 | Cao nhất |

#### Vì sao A (warm standby) đúng

Yêu cầu RTO 5 phút buộc phải loại bỏ mọi chiến lược cần "dựng hạ tầng từ đầu" sau khi disaster xảy ra, vì CloudFormation + khởi động EC2 + join Auto Scaling + đợi healthy thường mất nhiều phút đến hàng giờ — không kịp 5 phút.

**A (warm standby)** đáp ứng vì:
- EC2 web/app server **đã chạy sẵn** ở DR region (dù quy mô nhỏ — chỉ 1 instance trong ASG), nên không mất thời gian "cold start".
- DB standby **đã replicate sẵn** từ primary.
- Khi disaster: chỉ cần **scale ASG lên** (nhanh, vài phút) + đổi Route 53 record — không phải build mới từ CloudFormation.
- Vì fleet luôn ở quy mô "scaled-down" (1 instance), chi phí thấp hơn nhiều so với chạy full capacity (multi-site).

#### Vì sao C (lựa chọn của anh) sai — pilot light trông hợp lý nhưng vẫn trễ RTO

Pilot light nghe có vẻ đáp ứng vì DB cũng được replicate liên tục (giống A). Điểm khác biệt mấu chốt:

> *"Pilot Light cannot process requests without additional action taken first... Pilot Light will require you to turn on servers, possibly deploy additional (non-core) infrastructure and then scale up."*

Trong C, web/app server ở DR region **chưa tồn tại** — phải dùng CloudFormation để **provision mới** khi disaster xảy ra, rồi mới scale. Bước "tạo template + chạy CloudFormation + chờ EC2/ALB ready" tốn nhiều phút đến hàng giờ, vượt xa RTO 5 phút. Pilot light chỉ đạt RTO ở mức "giờ", không phải "phút".

#### Các phương án sai khác

- **B (backup & restore qua S3 CRR + CloudFormation)**: RTO ở mức ≤24h — xa nhất so với yêu cầu 5 phút. Chỉ là backup, không có gì chạy sẵn ở DR region.
- **D (multi-site active-active)**: Đáp ứng RTO/RPO (thậm chí dư thừa) nhưng **chạy full capacity ở cả 2 region cùng lúc** → chi phí cao nhất, vi phạm yêu cầu "cost tối thiểu". Đề hỏi chiến lược rẻ nhất vẫn đạt được RTO/RPO, không phải chiến lược an toàn nhất.

#### Lưu ý thực tế

- Pilot light vs warm standby dễ nhầm vì cả hai đều "replicate dữ liệu liên tục" — khác biệt nằm ở **app/web tier**: pilot light tắt (phải bật + deploy), warm standby luôn bật (chỉ cần scale).
- "250 miles" chỉ là điều kiện chọn Region đủ xa, không ảnh hưởng đến việc chọn chiến lược DR — dễ bị phân tâm nếu đọc vội.

#### Quy tắc nhớ cho thi

- **RTO tính bằng PHÚT** → warm standby (app/web đã chạy sẵn, chỉ cần scale).
- **RTO tính bằng GIỜ, RPO bằng PHÚT** → pilot light (DB chạy sẵn, app phải bật/deploy thêm).
- **RTO/RPO gần 0** → multi-site active-active (tốn kém nhất).
- **Chỉ cần backup, RTO ≤24h** → backup and restore (rẻ nhất).
- **Thấy "CloudFormation phải chạy lúc disaster"** → đó là dấu hiệu của pilot light hoặc backup/restore, KHÔNG phải warm standby.

### TD explanation

Having backups and redundant workload components in place is the start of your DR strategy. RTO and RPO are your objectives for the restoration of your workload. Set these based on business needs.
Recovery Time Objective (RTO) is defined by the organization. RTO is the maximum acceptable delay between the interruption of service and restoration of service. This determines what is considered an acceptable time window when service is unavailable.
Recovery Point Objective (RPO) is defined by the organization. RPO is the maximum acceptable amount of time since the last data recovery point. This determines what is considered an acceptable loss of data between the last recovery point and the interruption of service.
When architecting a multi-region disaster recovery strategy for your workload, you should choose one of the following multi-region strategies. They are listed in increasing order of complexity, and decreasing order of RTO and RPO. DR Region refers to an AWS Region other than the one primarily used for your workload (or any AWS Region if your workload is on-premises).

– Backup and restore (RPO in hours, RTO in 24 hours or less): Back up your data and applications using point-in-time backups into the DR Region. Restore this data when necessary to recover from a disaster.
– Pilot light (RPO in minutes, RTO in hours): Replicate your data from one region to another and provision a copy of your core workload infrastructure. Resources required to support data replication and backup such as databases and object storage are always on. Other elements such as application servers are loaded with application code and configurations, but are switched off and are only used during testing or when Disaster Recovery failover is invoked.
– Warm standby (RPO in seconds, RTO in minutes): Maintain a scaled-down but fully functional version of your workload always running in the DR Region. Business-critical systems are fully duplicated and are always on, but with a scaled down fleet. When the time comes for recovery, the system is scaled up quickly to handle the production load.
– Multi-region (multi-site) active-active (RPO near zero, RTO potentially zero): Your workload is deployed to, and actively serving traffic from, multiple AWS Regions. This strategy requires you to synchronize data across Regions.
The difference between Pilot Light and Warm Standby can sometimes be difficult to understand. Both include an environment in your DR Region with copies of your primary region assets. The distinction is that Pilot Light cannot process requests without additional action taken first, while Warm Standby can handle traffic (at reduced capacity levels) immediately. Pilot Light will require you to turn on servers, possibly deploy additional (non-core) infrastructure and then scale up. In Warm Standby, it only requires you to scale up your resources since all the necessary components are already deployed and running). You can choose between these two disaster recovery strategies based on your RTO and RPO needs.
Therefore, the correct answer is: On the backup region, create a scaled-down version of the fully functional environment with one Amazon EC2 instance of the web server and application server in their own Auto Scaling groups behind Application Load Balancers. Create a standby database instance that replicates data from the primary database. In case of disaster, scale the instances to meet the demand and update the Amazon Route 53 record to point to the backup region.
The option that says: Create a frequently scheduled backup of the application and database that will be stored on an Amazon S3 bucket. Configure S3 Cross-Region Replication (CRR) on the bucket to copy the backups to another region. In case of disaster, use an AWS CloudFormation template to quickly replicate the same resources to the backup region and restore the data from the S3 bucket is incorrect. Basically, this is just a backup and restore strategy that has RPO in hours and RTO in 24 hours or less. Even with using CloudFormation, provisioning resources and restoring the backups from an Amazon S3 bucket may take a long time. Take note that the required RTO is only 5 minutes.
The option that says: Use a pilot light strategy for the backup region. Configure the primary database to replicate data to a large standby instance in the backup region. In case of a disaster, vertically resize the database instance to meet the full demand. Create an AWS CloudFormation template to quickly provision the same web servers, application servers, and load balancers on the backup region. Update the Amazon Route 53 records to point to the backup region is incorrect. Although this reduces the recovery time because the database instance is already replicated, you may still miss the 5 minute RTO because provisioning the needed servers and load balancers may take several minutes.
The option that says: Use a multi-region strategy for the backup region to comply with the tight RTO and RPO requirements. Create a fully functional web, application, and database tier on the backup region with the same capacity as the primary region. Set the database on the backup region on standby mode. In case of disaster, update the Amazon Route 53 record to point to the backup region is incorrect. Although this meets the RTO and RPO requirements, keeping a multi-region strategy is very expensive. With the given cost-effectiveness requirement, using the warm standby strategy is the most suitable one to use in this scenario.

References:
https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html
https://aws.amazon.com/blogs/aws/new-whitepaper-use-aws-for-disaster-recovery/
https://d1.awsstatic.com/whitepapers/Storage/Backup_and_Recovery_Approaches_Using_AWS.pdf

Backup and Restore vs Pilot Light vs Warm Standby vs Multi-Site:
https://tutorialsdojo.com/backup-and-restore-vs-pilot-light-vs-warm-standby-vs-multi-site/

Check out this AWS Cheat Sheets:
https://tutorialsdojo.com/aws-cheat-sheets/

</details>

<a id="q14"></a>

## Q14

An online stock trading application is deployed to multiple Availability Zones in the us-east-1 region (N. Virginia) and uses RDS to host the database. Considering the massive financial transactions that the trading application handles, the company has hired you to be a consultant to make sure that the system is scalable, highly-available, and disaster resilient. In the event of failure, the Recovery Time Objective (RTO) must be less than 2 hours and the Recovery Point Objective (RPO) must be 10 minutes to meet the compliance requirements set by the regulators. 
In this scenario, which Disaster Recovery strategy can be used to achieve the RTO and RPO requirements in the event of system failure? (Select TWO.)

- **A.** Take hourly database backups and export to an S3 bucket with transaction logs stored in S3 every 5 minutes. Set up a Cross-Region Replication (CRR) to another AWS Region.
- **B.** Configure your database to use synchronous “source-replica” replication between multiple Availability Zones.
- **C.** Take 15-minute database backups stored in Glacier with transaction logs stored in S3 every 5 minutes.
- **D.** Set up an AWS Backup plan for the Amazon RDS database with the continuous backups for point-in-time recovery (PITR) option enabled
- **E.** Store hourly database backups to an EC2 instance store volume with transaction logs stored in an S3 bucket every 5 minutes.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A, D · **You picked:** B, D

🔑 **Key words:** RTO < 2h, RPO 10 min, disaster resilient (Select TWO)

🪤 **Your trap:** Picked D (right) + B: synchronous Multi-AZ replication is HA, not a backup and not Region-safe

🧠 **Rule:** Multi-AZ = availability. DR = backups + logs (or replica) in another Region.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Stock trading app, nhiều AZ trong us-east-1, dùng RDS
Yêu cầu: RTO < 2 giờ, RPO = 10 phút  (Select TWO — 2 đáp án phải CÙNG tạo thành 1 giải pháp DR)
```

Đáp án đúng: **A + D**. Anh chọn **B + D** — đúng D, sai B.

⚠️ **Lỗi lặp lại:** Giống Q9, đây lại là lỗi nhầm giữa **High Availability (HA)** và **Disaster Recovery (DR)**. Multi-AZ là HA trong 1 Region; DR đòi hỏi bản sao ở Region khác hoặc nơi lưu trữ độc lập Region.

#### Vì sao A + D hợp thành MỘT giải pháp DR hoàn chỉnh

```
A: Backup giờ + transaction log 5 phút  → S3 → CRR sang Region khác
D: AWS Backup continuous backup (PITR) cho RDS

   → A lo phần "copy dữ liệu sang Region khác" (yêu cầu DR thực sự)
   → D lo phần "point-in-time recovery" chính xác tới giây, đáp ứng RPO 10 phút
```

**A đúng** vì S3 Cross-Region Replication đưa backup + transaction log sang Region khác — đúng bản chất của DR (chống mất cả Region). RPO 10 phút được đáp ứng nhờ log mỗi 5 phút; RTO <2h đáp ứng được vì restore từ backup hourly + replay log.

**D đúng** vì AWS Backup's continuous backup cho RDS hỗ trợ PITR chính xác đến giây (trong 35 ngày) — cơ chế "full backup + liên tục ghi transaction log" đúng là thứ cho phép đạt RPO 10 phút với RTO hợp lý.

Hai đáp án này **bổ sung cho nhau**: A giải quyết yêu cầu "khác Region" (compliance đòi dữ liệu cách xa), D giải quyết yêu cầu "point-in-time" chính xác. Không cái nào tự nó là giải pháp DR đầy đủ.

#### Vì sao B (lựa chọn của anh) sai dù đúng là một kỹ thuật HA thật

**B sai vì synchronous Multi-AZ replication là cơ chế HIGH AVAILABILITY, không phải DISASTER RECOVERY.** TD explanation nói thẳng: *"it provides a highly available architecture but it doesn't provide any durable storage nor DB snapshots."*

Lý do kỹ thuật: Multi-AZ chỉ nhân bản trong cùng 1 Region (các AZ khác nhau của us-east-1). Nếu toàn bộ Region us-east-1 gặp sự cố diện rộng (hiếm nhưng là đúng kịch bản "disaster" DR hướng tới), Multi-AZ **không có bản sao nào ở nơi khác để fail over**. Ngoài ra Multi-AZ không tạo ra bản backup/snapshot độc lập — nếu dữ liệu bị lỗi logic (xoá nhầm, ransomware...) thì lỗi đó cũng được replicate sync sang standby ngay lập tức, không có điểm phục hồi (recovery point) nào để quay lại.

#### Các phương án sai khác

- **C (Glacier backup 15 phút)**: Retrieval từ Glacier mất 3–5 giờ → vượt RTO <2h ngay lập tức.
- **E (EC2 instance store)**: Instance store là **ephemeral** (mất dữ liệu khi instance dừng/terminate) — không phù hợp lưu backup lâu dài, dù transaction log vẫn ở S3.

| Phương án | Loại | Cross-Region? | Đáp ứng RTO/RPO? |
|---|---|---|---|
| **A** | Backup + CRR | Có | Có |
| **D** | AWS Backup PITR | Tùy cấu hình (có thể cross-Region) | Có |
| B | Multi-AZ sync replication | Không (cùng Region) | Không (không phải DR) |
| C | Backup trên Glacier | Có nhưng retrieval chậm | Không (RTO vỡ) |
| E | Backup trên instance store | Không bền vững | Không (dữ liệu dễ mất) |

#### Quy tắc nhớ cho thi

- **Multi-AZ / synchronous replication** → luôn là **HA trong 1 Region**, KHÔNG BAO GIỜ tính là DR đơn độc, dù đề có nhắc "disaster".
- **DR thật sự** → cần backup/replica ở **Region khác** (CRR, snapshot copy cross-Region, AWS Backup cross-Region copy).
- **RPO sát nút (phút/giây)** → cần continuous backup / PITR, không phải backup theo lịch đơn thuần.
- **Glacier** → luôn gắn với retrieval chậm (giờ) → loại ngay khi đề có RTO ngắn.

### TD explanation

Point-in-time recovery (PITR) is the process of restoring a database to the state it was in at a specified date and time.
When automated backups are turned on for your DB instance, Amazon RDS automatically performs a full daily snapshot of your data. The snapshot occurs during your preferred backup window. It also captures transaction logs to Amazon S3 every 5 minutes (as updates to your DB instance are made). Archiving the transaction logs is an important part of your DR process and PITR. When you initiate a point-in-time recovery, transactional logs are applied to the most appropriate daily backup in order to restore your DB instance to the specific requested time.

With S3 Cross-Region Replication (CRR), you can replicate objects (and their respective metadata and object tags) into other AWS Regions for reduced latency, compliance, security, disaster recovery, and other use cases. S3 CRR is configured to a source S3 bucket and replicates objects into a destination bucket in another AWS Region.
Amazon S3 CRR automatically replicates data between buckets across different AWS Regions. With CRR, you can set up replication at a bucket level, a shared prefix level, or an object level using S3 object tags. You can use CRR to provide lower-latency data access in different geographic regions. CRR can also help if you have a compliance requirement to store copies of data hundreds of miles apart. You can use CRR to change account ownership for the replicated objects to protect data from accidental deletion.
AWS Backup is a fully-managed service that makes it easy to centralize and automate data protection across AWS services, in the cloud and on-premises. Using this service, you can configure backup policies and monitor activity for your AWS resources in one place. It allows you to automate and consolidate backup tasks that were previously performed service-by-service and remove the need to create custom scripts and manual processes. With a few clicks in the AWS Backup console, you can automate your data protection policies and schedules.
AWS Backup supports continuous backups and point-in-time recovery (PITR) in addition to snapshot backups.
With continuous backups, you can restore your AWS Backup-supported resource by rewinding it back to a specific time that you choose within 1 second of precision (going back a maximum of 35 days). Continuous backup works by first creating a full backup of your resource and then constantly backing up your resource’s transaction logs. PITR restore works by accessing your full backup and replaying the transaction log to the time that you tell AWS Backup to recover.

In this scenario, you have to use durable storage, database backups, and continuous backups for point-in-time recovery (PITR) to satisfy the RTO and RPO requirements. Hence,
The option that says: Take hourly database backups and export to an S3 bucket with transaction logs stored in S3 every 5 minutes. Set up a Cross-Region Replication (CRR) to another AWS Region  is correct as this solution meets the 2-hour RTO as well as the 10-minute RPO requirement.
The option that says: Set up an AWS Backup plan for the Amazon RDS database with the continuous backups for point-in-time recovery (PITR) option enabled is correct as AWS Backup has a native feature that you can enable to satisfy the point-in-time recovery (PITR) requirement.
The option that says: Store hourly database backups to an EC2 instance store volume with transaction logs stored in an S3 bucket every 5 minutes is incorrect because an instance store volume is ephemeral and it is not suitable to store the database backups.
The option that says: Take 15-minute database backups stored in Glacier with transaction logs stored in S3 every 5 minutes is incorrect because the RTO is at least 3 hours, which means that Amazon Glacier is not the ideal solution to use. Note that the standard retrieval time for Glacier is 3 to 5 hours and with that time, you will surely miss your RTO.
The option that says: Configure your database to use synchronous “source-replica” replication between multiple Availability Zones is incorrect because it provides a highly available architecture but it doesn’t provide any durable storage nor DB snapshots.

References:
https://www.slideshare.net/AmazonWebServices/disaster-recovery-options-with-aws
https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/
https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html

Check out this AWS Well-Architected Framework Cheat Sheet:
https://tutorialsdojo.com/aws-well-architected-framework-disaster-recovery/

RPO and RTO Explained:

</details>

<a id="q23"></a>

## Q23

A shipping firm runs its web applications on its on-premises data center. The servers have a dependency on non-x86 hardware and the management plans to use AWS to scale its on-premises data storage. However, the backup application is only able to write to POSIX-compatible block-based storage. There is a total of 1,000 TB of data files that need to be mounted to a single folder on the file server. Existing users must also be able to access portions of this data while the backups are taking place. 
Which of the following backup solutions would be most appropriate to meet the above requirements?

- **A.** Provision Gateway Stored Volumes from AWS Storage Gateway.
- **B.** Provision Gateway Cached Volumes from AWS Storage Gateway.
- **C.** Use Amazon S3 as the target for your data backups.
- **D.** Use Amazon Glacier as the target for your data backups.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** 1,000 TB on one mount; POSIX block storage; users read portions during backup

🪤 **Your trap:** Stored volumes keep full data on-prem (max 512 TB per TD)

🧠 **Rule:** Data too large for on-prem, hot subset local → Volume Gateway cached volumes. Full local low-latency copy → stored volumes.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises data center               AWS
┌──────────────────────┐
│ Non-x86 server        │
│ Backup app chỉ ghi    │   Storage Gateway   ┌───────────────┐
│ được POSIX block      │ ─────────────────► │ Volume Gateway │
│ storage (iSCSI)       │                     └───────────────┘
│ Tổng 1,000 TB,         │
│ mount vào 1 folder     │
│ Users vẫn phải đọc     │
│ dữ liệu khi backup     │
│ đang chạy              │
└──────────────────────┘
```

Yêu cầu chính: (1) 1,000 TB **một mount point**, (2) POSIX block storage, (3) user vẫn truy cập được pha dữ liệu khi backup đang diễn ra.

Đáp án đúng: **B (Gateway Cached Volumes)**. Anh chọn **A (Gateway Stored Volumes)**.

#### Vì sao B đúng

Volume Gateway có hai chế độ, khác nhau ở **nơi lưu bản chính (primary copy)**:

```
Cached volumes:                      Stored volumes:
Primary data → S3 (AWS)              Primary data → on-premises disk
Cache nóng   → local disk (nhỏ)      Backup async → S3 (EBS snapshot)

→ Dung lượng tối đa LỚN hơn          → Dung lượng giới hạn bởi
  vì data thật nằm ở S3                disk vật lý tại chỗ
  (TD: lên đến 1,024 TB)               (TD: tối đa 512 TB)
```

Với 1,000 TB cần gộp vào **một volume/mount duy nhất**, chỉ Cached volumes đủ hạn mức (1,024 TB). Dữ liệu được lưu chủ yếu trên S3, phần truy cập thường xuyên (hot data) được cache cục bộ — người dùng vẫn đọc được phần dữ liệu đó ngay cả khi phần còn lại đang được backup/đồng bộ lên cloud.

#### Vì sao A (lựa chọn của anh) sai dù rất gần đúng

**A sai vì Gateway Stored Volumes chỉ hỗ trợ tối đa 512 TB** — không đủ cho yêu cầu 1,000 TB trong một mount. Bản chất khác biệt: stored volumes giữ **toàn bộ** dữ liệu ở local disk (để có latency thấp nhất), và chỉ backup không đồng bộ (asynchronous) lên S3 dưới dạng EBS snapshot — vì toàn bộ data nằm tại chỗ nên bị giới hạn bởi dung lượng ổ cứng on-premises thực tế, và TD giới hạn ở mức 512 TB/volume.

Nhầm lẫn dễ xảy ra vì cả hai mode đều là "POSIX block storage qua iSCSI" — đúng yêu cầu (2) và tương thích backup app. Nhưng con số dung lượng (1,000 TB) mới là yếu tố quyết định chọn cached thay vì stored.

#### Các phương án sai khác

- **C (S3 trực tiếp)**: S3 là **object storage**, không phải block storage POSIX-compatible — backup app của công ty không ghi được vào S3 trực tiếp theo kiểu file-system/iSCSI.
- **D (Glacier)**: Cùng vấn đề với C (không phải block storage), lại còn retrieval chậm (3–5 giờ), hoàn toàn không phù hợp với yêu cầu truy cập dữ liệu đang hoạt động.

| Phương án | Loại storage | Giới hạn dung lượng | Phù hợp iSCSI/POSIX? |
|---|---|---|---|
| **B. Cached volumes** | Block (qua iSCSI) | ~1,024 TB | Có |
| A. Stored volumes | Block (qua iSCSI) | 512 TB | Có nhưng thiếu dung lượng |
| C. S3 trực tiếp | Object | Không giới hạn kiểu này | Không (sai loại storage) |
| D. Glacier | Object (lạnh) | Không giới hạn kiểu này | Không + chậm |

#### Lưu ý thực tế

- Bài này (Q23) và Q45 cùng nói về Storage Gateway nhưng hỏi hai góc khác nhau: Q23 là **chọn loại volume khi backup lên cloud** (cached vs stored theo dung lượng), còn Q45 là **cách khôi phục nhanh nhất khi disaster xảy ra** (restore snapshot sang EBS thay vì dựng lại Storage Gateway). Đừng lẫn hai ngữ cảnh.

#### Quy tắc nhớ cho thi

- **Thấy số TB rất lớn (>512 TB) cần một volume/mount duy nhất** → Cached volumes (giới hạn cao hơn vì data chính nằm trên S3).
- **Cần latency thấp nhất, giữ toàn bộ dữ liệu tại chỗ, dung lượng vừa phải** → Stored volumes.
- **Backup app chỉ ghi được block storage (POSIX/iSCSI)** → loại ngay S3/Glacier (object storage).

### TD explanation

AWS Storage Gateway connects an on-premises software appliance with cloud-based storage to provide seamless integration with data security features between your on-premises IT environment and the AWS storage infrastructure. You can use the service to store data in the AWS Cloud for scalable and cost-effective storage that helps maintain data security. Gateway-Cached volumes can support volumes of 1,024TB in size, whereas Gateway-stored volume supports volumes of 512 TB size.

Therefore, the correct answer is: Provision Gateway Cached Volumes from AWS Storage Gateway is correct because it supports volumes of up to 1,024 TB in size, and the frequently accessed data is stored on the on-premises server while the entire data is backed up over AWS.
The option that says: Use Amazon Glacier as the target for your data backups is incorrect. The data stored in Amazon Glacier is not available immediately. Retrieval jobs typically require 3-5 hours to complete.
The option that says: Provision Gateway Stored Volumes from AWS Storage Gateway is incorrect. Gateway stored volumes can only store up to 512 TB worth of data.
The option that says: Use Amazon S3 as the target for your data backups is incorrect. Amazon S3 is designed for object storage and not ideal for POSIX compliant data.
References:
https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html
https://docs.aws.amazon.com/storagegateway/latest/vgw/StorageGatewayConcepts.html#storage-gateway-stored-volume-concepts

Check out this AWS Storage Gateway Cheat Sheet:
https://tutorialsdojo.com/aws-storage-gateway/

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

<a id="q45"></a>

## Q45

A BPO company uses a multitiered, java-based content management system (CMS) hosted on an on-premises data center. The CMS has a JBoss Application server present in the application tier. The database tier consists of an Oracle database which is regularly backed up to S3 using the Oracle RMAN backup utility. The application’s static files and content are kept on a 512 GB Storage Gateway volume which is attached to the application server via an iSCSI interface. The solutions architect was tasked to create a disaster recovery solution for the application and its data.
Which AWS-based disaster recovery strategy will give you the best RTO?

- **A.** Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Also provision an EBS volume containing static content obtained from Storage Gateway, and attach the volume to the JBoss EC2 server.
- **B.** Use RDS for your Oracle database and EC2 for the JBoss application server. Restore the RMAN Oracle backups from Amazon Glacier, and provision an EBS volume containing static content obtained from Storage Gateway. The volume will be attached to the JBoss EC2 server.
- **C.** Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Attach an AWS Storage Gateway running on Amazon EC2 as an iSCSI volume to the JBoss EC2 server to access the static content.
- **D.** Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Use an AWS Storage Gateway-VTL running on Amazon EC2 as your source for restoring static content.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** DR with best RTO; static content on Storage Gateway volume

🪤 **Your trap:** Running Storage Gateway on EC2 and attaching via iSCSI adds a layer; restoring to EBS is faster

🧠 **Rule:** Recover Volume Gateway data in AWS → restore its snapshot to an EBS volume and attach.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises CMS                         AWS (DR target)
┌───────────────────────┐
│ JBoss app server        │   → cần: EC2 + khôi phục nhanh nhất (best RTO)
│ Oracle DB (RMAN backup   │
│   → đã đẩy lên S3)       │   → cần: EC2 restore từ S3 backup
│ Static files trên         │
│   Storage Gateway volume  │   → cần: khôi phục nhanh thành local storage
│   512GB, mount qua iSCSI  │
└───────────────────────┘
```

Yêu cầu: chiến lược DR cho **RTO tốt nhất**. Đáp án đúng: **A**. Anh chọn **C**.

#### Vì sao A đúng

```
A: Restore DB từ S3  → EC2 Oracle
   Snapshot của Storage Gateway volume  → restore trực tiếp thành EBS volume
   → gắn EBS đó vào JBoss EC2 server
```

Theo TD explanation: *"If you are restoring an AWS Storage Gateway volume snapshot, you can choose to restore the snapshot as an AWS Storage Gateway volume **or as an Amazon EBS volume**."* Vì dữ liệu tĩnh (static content) trên Storage Gateway volume đã được backup dưới dạng **EBS snapshot** (cơ chế nền của Volume Gateway — stored volumes dùng iSCSI nhưng backup async thành EBS snapshot), nên cách nhanh nhất để lấy lại dữ liệu đó trên AWS là **restore snapshot thẳng thành EBS volume** rồi attach vào EC2 — không cần dựng lại tầng Storage Gateway nào cả.

Đây là bản chất "ít lớp trung gian nhất = RTO tốt nhất": EBS volume là block storage gắn trực tiếp vào EC2, instant-ready sau khi restore.

#### Vì sao C (lựa chọn của anh) sai — thêm một lớp không cần thiết

**C sai vì nó dựng lại một AWS Storage Gateway chạy trên EC2 rồi mới attach qua iSCSI**, tức là tái tạo nguyên vẹn kiến trúc gateway (vốn được thiết kế cho mô hình hybrid on-prem ↔ cloud liên tục), thay vì khôi phục thẳng dữ liệu. TD giải thích: *"there is no need to attach the Storage Gateway as an iSCSI volume; you can just easily and quickly create an EBS volume from the Storage Gateway."*

Lớp Storage Gateway thêm vào đây hoàn toàn dư thừa trong kịch bản DR (không còn on-premises để đồng bộ) — nó chỉ làm chậm RTO vì phải cấu hình, khởi động dịch vụ gateway, rồi mới mount qua iSCSI, so với việc restore trực tiếp ra EBS và attach ngay.

#### Các phương án sai khác

- **B (RDS + Glacier)**: Sai vì RMAN backup đang nằm ở **S3**, không phải Glacier — restore từ Glacier tốn 3–5 giờ, phá vỡ yêu cầu RTO tốt nhất. (Lưu ý thêm: dùng RDS cho Oracle ở đây không bị TD gắn cờ sai trực tiếp, nhưng điểm loại chính là nguồn backup Glacier chậm.)
- **D (Storage Gateway-VTL cho static content)**: VTL (Virtual Tape Library) dùng để backup dạng tape ảo, phục vụ phần mềm backup tương thích tape — không phải cơ chế tối ưu để khôi phục static files nhanh; TD nói thẳng "restoring the content from Virtual Tape Library will not fit into the RTO".

| Phương án | Cách khôi phục static content | RTO |
|---|---|---|
| **A (đúng)** | Snapshot → restore thẳng thành **EBS volume** → attach | Nhanh nhất |
| C | Dựng lại Storage Gateway trên EC2 → attach qua iSCSI | Chậm hơn (thừa lớp) |
| D | Khôi phục từ Storage Gateway-VTL | Chậm (không phù hợp mục đích) |
| B | Restore DB từ Glacier (nên RDS/EC2 không phải điểm sai chính) | Chậm (Glacier 3–5h) |

#### Lưu ý thực tế

- Bài này và **Q23** đều xoay quanh Storage Gateway nhưng khác pha: Q23 hỏi **lúc backup lên cloud** nên chọn loại volume gì theo dung lượng (cached vs stored); Q45 hỏi **lúc khôi phục (restore)** nên dùng cơ chế nào cho nhanh nhất (EBS trực tiếp, không dựng lại gateway).
- Storage Gateway volume snapshot về bản chất chính là **EBS snapshot** — đây là lý do restore thẳng ra EBS luôn là đường tắt nhanh nhất khi không cần duy trì mô hình hybrid nữa.

#### Quy tắc nhớ cho thi

- **Khôi phục dữ liệu từ Storage Gateway volume snapshot trên AWS (không cần hybrid nữa)** → restore thẳng thành **EBS volume**, bỏ qua lớp Storage Gateway.
- **RMAN/Oracle backup nằm ở S3** → restore trực tiếp từ S3 luôn nhanh hơn Glacier.
- **VTL** → gắn với backup dạng tape ảo, không phải lựa chọn tối ưu RTO cho restore file tĩnh.

### TD explanation

Recovery Manager (RMAN) is an Oracle Database client that performs backup and recovery tasks on your databases and automates the administration of your backup strategies. It greatly simplifies backing up, restoring, and recovering database files.
By using stored volumes, you can store your primary data locally, while asynchronously backing up that data to AWS. Stored volumes provide your on-premises applications with low-latency access to their entire datasets. At the same time, they provide durable, offsite backups. You can create storage volumes and mount them as iSCSI devices from your on-premises application servers. Data written to your stored volumes is stored on your on-premises storage hardware. This data is asynchronously backed up to Amazon S3 as Amazon Elastic Block Store (Amazon EBS) snapshots.
If you are restoring an AWS Storage Gateway volume snapshot, you can choose to restore the snapshot as an AWS Storage Gateway volume or as an Amazon EBS volume. AWS Backup integrates with both services, and any AWS Storage Gateway snapshot can be restored to either an AWS Storage Gateway volume or an Amazon EBS volume.

The option that says: Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Also provision an EBS volume containing static content obtained from Storage Gateway, and attach the volume to the JBoss EC2 server is correct because it deploys the Oracle database on an EC2 instance by restoring the backups from S3 which can provide a faster recovery time, and it generates the EBS volume of static content from Storage Gateway.
The option that says: Use RDS for your Oracle database and EC2 for the JBoss application server. Restore the RMAN Oracle backups from Amazon Glacier, and provision an EBS volume containing static content obtained from Storage Gateway. The volume will be attached to the JBoss EC2 server is incorrect because restoring the backups from Amazon Glacier will be slower than S3 and will not meet the RTO.
The option that says: Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Attach an AWS Storage Gateway running on Amazon EC2 as an iSCSI volume to the JBoss EC2 server to access the static content is incorrect because there is no need to attach the Storage Gateway as an iSCSI volume; you can just easily and quickly create an EBS volume from the Storage Gateway. Then, you can generate snapshots from the EBS volumes for better recovery time.
The option that says: Provision EC2 servers for both your JBoss application and Oracle database, and then restore the database backups from an S3 bucket. Use an AWS Storage Gateway-VTL running on Amazon EC2 as your source for restoring static content is incorrect as restoring the content from Virtual Tape Library will not fit into the RTO.

References:
https://docs.aws.amazon.com/storagegateway/latest/userguide/StorageGatewayConcepts.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RMAN.html
https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-storage-gateway.html

Check out this AWS Storage Gateway Cheat Sheet:
https://tutorialsdojo.com/aws-storage-gateway/

</details>

<a id="q68"></a>

## Q68

A popular news website that uses an Oracle database is currently deployed in the company’s on-premises network. Due to its growing number of readers, the company decided to move its infrastructure to AWS, where it can further improve the performance of the website. The company is also considering using AWS License Manager to track and manage its Oracle database licenses on AWS. 
The company earns from the advertisements placed on the website, so the Solutions Architect was instructed to ensure that the website remains available in case of database server failures. The company’s team of content writers constantly uploads new articles every day, including the wee hours of the morning, to cover breaking news. 
How can the Solutions Architect implement a highly available architecture to meet the requirements?

- **A.** Create an Oracle database instance in Amazon RDS with Recovery Manager (RMAN) which performs backup and recovery tasks on your database and automates the administration of your backup strategies.
- **B.** Create an Oracle database in Amazon RDS with Multi-AZ deployments.
- **C.** Create an Oracle Real Application Clusters (RAC) in Amazon RDS which provides a shared cache architecture that overcomes the limitations of traditional shared-nothing and shared-disk approaches to provide highly scalable and available database solutions for the news website.
- **D.** Create an Oracle database in Amazon RDS with Read Replicas.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** A

🔑 **Key words:** Oracle; stay available on DB failure; writes 24/7

🪤 **Your trap:** RMAN is backup (and not user-run on RDS); read replicas can't take writes; RAC unsupported on RDS

🧠 **Rule:** DB high availability with continuous writes → RDS Multi-AZ.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises Oracle DB  →  migrate lên AWS
Website kiếm tiền từ ads → PHẢI available khi DB server fail
Content writer ghi bài LIÊN TỤC 24/7 (kể cả nửa đêm) → cần vẫn GHI được khi failover
```

Đáp án đúng: **B (RDS Multi-AZ)**. Anh chọn **A (RDS + RMAN)**.

#### Vì sao B đúng

```
Primary AZ                    Standby AZ
┌─────────────┐  sync repl   ┌─────────────┐
│ Oracle RDS   │ ───────────► │ Oracle RDS   │
│ (ghi + đọc)  │               │ (standby)    │
└─────────────┘               └─────────────┘
        │ fail                        │
        └──────── auto failover ──────┘
        Endpoint KHÔNG ĐỔI → app tiếp tục ghi bình thường
```

RDS Multi-AZ tạo instance chính + đồng bộ dữ liệu tới standby ở AZ khác; khi instance chính gặp sự cố hạ tầng, RDS **tự động failover** sang standby và **endpoint giữ nguyên** — ứng dụng (content writers) không cần can thiệp thủ công, viết bài vẫn tiếp tục được ngay sau failover. Đây đúng là yêu cầu "stay available for continuous writes khi DB fail".

#### Vì sao A (lựa chọn của anh) sai — và mối liên hệ trực tiếp với Q7

**A sai vì RMAN (Recovery Manager) là công cụ BACKUP/RECOVERY, không phải cơ chế HIGH AVAILABILITY.** RMAN giúp backup và khôi phục dữ liệu Oracle, nhưng không cung cấp failover tự động khi database đang chạy gặp sự cố — nó chỉ hữu ích để khôi phục sau khi đã mất dữ liệu, không giữ cho ứng dụng "available" liên tục.

Thêm nữa — đây là điểm quan trọng hơn: TD explanation xếp A vào cùng nhóm sai với RAC: *"the following options are incorrect because Oracle RMAN and RAC are not supported in RDS."* Việc RDS là managed service có nghĩa là bạn **không tự chạy RMAN theo kiểu thủ công** như trên EC2 — AWS tự quản lý backup/snapshot nội bộ. Đây chính xác là cùng chủ đề với **Q7**: RDS ẩn hết phần OS/engine-internals, nên các công cụ Oracle cấp thấp như RMAN (tự vận hành) hay RAC (cluster shared-disk) đều không áp dụng được trên RDS.

```
Q7:  Oracle RAC    + RDS/Aurora → SAI (không hỗ trợ)
Q68: Oracle RMAN    + RDS        → SAI (RDS tự quản lý backup, không chạy RMAN thủ công)
Q68: Oracle RAC     + RDS        → SAI (option C, cùng lý do Q7)

Rule chung: RDS/Aurora = managed → không hỗ trợ tool/feature cần
            quyền truy cập OS/engine-internals (RAC, RMAN thủ công, v.v.)
```

#### Các phương án sai khác

- **C (Oracle RAC trong RDS)**: Sai cùng lý do Q7 — RDS không hỗ trợ RAC dưới bất kỳ hình thức nào.
- **D (Read Replicas)**: Read Replica chỉ **đọc**, không nhận ghi. Nếu primary down và app failover sang read replica, content writers **không thể ghi bài mới** — vi phạm thẳng yêu cầu "viết bài liên tục kể cả lúc DB fail".

| Phương án | Failover tự động? | Vẫn ghi được sau failover? | RDS hỗ trợ? |
|---|---|---|---|
| **B. Multi-AZ** | Có | Có | Có |
| A. RMAN | Không (chỉ backup/restore) | — | RDS tự quản lý, không chạy RMAN thủ công |
| C. RAC | — | — | Không hỗ trợ |
| D. Read Replica | Có thể promote nhưng chậm hơn, và trong lúc đó không ghi được | Không (read-only) | Có nhưng sai mục đích |

#### Quy tắc nhớ cho thi

- **"Available khi DB fail" + "vẫn phải GHI được"** → RDS/Aurora **Multi-AZ** (không phải Read Replica — read replica chỉ đọc).
- **RMAN / RAC xuất hiện cùng RDS trong option** → gần như luôn là bẫy, vì RDS là managed service, không hỗ trợ các công cụ/feature cấp hệ điều hành của Oracle.
- Nhớ cặp quy tắc: **RAC → chỉ EC2**; **RMAN thủ công → chỉ EC2** (RDS tự có cơ chế backup/snapshot riêng, không cần RMAN do người dùng vận hành).

### TD explanation

Amazon RDS Multi-AZ deployments provide enhanced availability and durability for Database (DB) Instances, making them a natural fit for production database workloads. When you provision a Multi-AZ DB Instance, Amazon RDS automatically creates a primary DB Instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). Each AZ runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable.
In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby (or to a read replica in the case of Amazon Aurora), so that you can resume database operations as soon as the failover is complete. Since the endpoint for your DB Instance remains the same after a failover, your application can resume database operations without the need for manual administrative intervention.

Therefore, the correct answer is: Create an Oracle database in Amazon RDS with Multi-AZ deployments. This ensures high availability even if the primary database instance goes down.
The option that says: Create an Oracle database in Amazon RDS with Read Replicas is incorrect because the content writers won’t be able to upload their articles to the Read Replicas in the event that the primary database goes down.
The following options are incorrect because Oracle RMAN and RAC are not supported in RDS:
– Create an Oracle database instance in Amazon RDS with Recovery Manager (RMAN) which performs backup and recovery tasks on your database and automates the administration of your backup strategies
– Create an Oracle Real Application Clusters (RAC) in Amazon RDS which provides a shared cache architecture that overcomes the limitations of traditional shared-nothing and shared-disk approaches to provide highly scalable and available database solutions for the news website.

References:
https://aws.amazon.com/rds/details/multi-az/
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html

Check out this Amazon RDS Cheat Sheet:
https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

</details>

---

# Group D — Networking (4)

<a id="q17"></a>

## Q17

A technology company runs an industrial chain orchestration software on the AWS cloud. It consists of a web application tier that is currently deployed on a fixed fleet of Amazon EC2 instances. The database tier is deployed on Amazon RDS. The web and database tiers are deployed in the public and private subnet of the VPC respectively. The company wants to improve the service to make it more cost-effective, scalable, highly available and should require minimal human intervention. 
Which of the following actions should the solutions architect implement to improve the availability and load balancing of this cloud architecture? (Select TWO.)

- **A.** Launch a load balancer in front of all the web servers then create a Non-Alias Record in Route 53 which maps to the DNS name of the load balancer.
- **B.** Place an Application Load Balancer in front of all the web servers. Create a new Alias Record in Route 53 which maps to the DNS name of the load balancer.
- **C.** Create a CloudFront distribution whose origin points to the private IP addresses of your web servers. Also set up a CNAME record in Route 53 mapped to your CloudFront distribution.
- **D.** Set up a NAT instance in your VPC. Update your route table by creating a default route via the NAT instance with all subnets associated with it. Configure a DNS A Record in Route 53 pointing to the NAT instance's public IP address.
- **E.** Create a Non-Alias Record in Route 53 with a Multivalue Answer Routing configuration and add all the IP addresses for your web servers.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, E · **You picked:** B, C

🔑 **Key words:** improve availability and load balancing of web tier (Select TWO)

🪤 **Your trap:** Picked B (right) + C: CloudFront origin cannot be a private IP address

🧠 **Rule:** ALB behind Route 53 ALIAS record; Route 53 multivalue answer = DNS-level health-checked load balancing.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC
┌───────────────────── Public subnet ──────────────────────┐
│ Web tier: fixed fleet EC2 instances (chưa có load balancer) │
└──────────────────────────────────────────────────────────┘
┌───────────────────── Private subnet ─────────────────────┐
│ DB tier: Amazon RDS                                        │
└──────────────────────────────────────────────────────────┘

Yêu cầu: cải thiện availability + load balancing, cost-effective,
         scalable, minimal human intervention. (Select TWO)
```

Đáp án đúng: **B + E**. Anh chọn **B + C** — đúng B, sai C.

#### Vì sao B + E hợp thành MỘT giải pháp cải thiện availability

```
B: ALB trước các web server  +  Route 53 ALIAS record trỏ tới ALB
E: Route 53 Multivalue Answer Routing (trả nhiều IP, có health check)

   → B là lớp load balancing "chuẩn" (ALB chủ động phân phối traffic)
   → E là lớp bổ sung ở tầng DNS (Route 53 tự loại IP không healthy
     khỏi câu trả lời DNS)
```

**B đúng** vì ALB phân phối tải đều cho các web server; nếu một server down, traffic tự động chuyển sang server còn lại — loại bỏ downtime không cần thiết. Route 53 ALIAS record (không phải CNAME) là cách chuẩn để trỏ domain về DNS name của ALB, kể cả ở zone apex.

**E đúng** vì TD explanation nói rõ: *"Multivalue answer routing lets you configure Amazon Route 53 to return multiple values... multivalue answer routing also lets you check the health of each resource, so Route 53 returns only value for healthy resources... the ability to return multiple health-checkable IP addresses is a way to use DNS to improve availability and load balancing."* Đây là một cách độc lập (không cần ALB) để cải thiện availability — Route 53 tự động loại IP không khỏe ra khỏi response DNS.

Hai đáp án B và E là **hai giải pháp riêng biệt cùng đạt mục tiêu "cải thiện availability và load balancing"** — đề không yêu cầu chúng phối hợp kỹ thuật với nhau, chỉ cần cả hai đều là cách hợp lệ để giải quyết vấn đề nêu ra.

#### Vì sao C (lựa chọn của anh) sai — CloudFront không nhận private IP làm origin

**C sai vì CloudFront origin phải là Public IP/DNS name, không được là địa chỉ IP riêng (private).** TD explanation: *"You should use a Public IP address, not a Private IP address when using an EC2 origin."* Về bản chất, CloudFront là dịch vụ chạy ở các edge location toàn cầu, hoàn toàn bên ngoài VPC — nó cần kết nối tới origin qua Internet công khai, nên không thể route tới một private IP nằm trong subnet riêng của VPC.

Ngoài ra, ngay cả khi origin là public IP, option C vẫn **chỉ trỏ CloudFront thẳng tới một EC2 server cụ thể** — nếu server đó down, cả site mất khả dụng, vì CloudFront ở đây không đóng vai trò load balancer giữa nhiều server.

#### Các phương án sai khác

- **A (Non-Alias record trỏ tới LB)**: Dùng load balancer là đúng hướng, nhưng phải dùng **Alias Record**, không phải Non-Alias (CNAME) — CNAME không dùng được ở zone apex và kém tối ưu hơn ALIAS cho tài nguyên AWS.
- **D (NAT instance + DNS A record)**: NAT instance dùng để cho EC2 ở **private subnet** truy cập Internet, không liên quan gì tới việc cải thiện availability của web tier đang chạy ở **public subnet**. Sai hoàn toàn về mục đích sử dụng.

| Phương án | Cơ chế | Vấn đề |
|---|---|---|
| **B. ALB + Alias record** | Load balancing chủ động | Đúng |
| **E. Multivalue answer routing** | DNS trả nhiều IP có health check | Đúng |
| A. LB + Non-Alias record | Load balancing nhưng sai loại DNS record | Phải dùng Alias, không phải CNAME |
| C. CloudFront → private IP | CDN caching | Private IP không hợp lệ làm origin |
| D. NAT instance | Outbound Internet cho private subnet | Sai mục đích (web tier ở public subnet) |

#### Lưu ý thực tế

⚠️ **Lỗi lặp lại:** Cùng nhóm chủ đề DR/HA như Q9, Q14 — ở đây là nhầm "công cụ CDN/NAT" với "công cụ load balancing/availability". Luôn tách rõ: ALB và Multivalue Answer Routing mới trực tiếp cải thiện availability của một fleet server; CloudFront là caching/CDN, NAT là outbound gateway — không phải công cụ HA cho inbound traffic.

#### Quy tắc nhớ cho thi

- **Trỏ domain tới tài nguyên AWS (ALB, S3 website, CloudFront...) ở zone apex hoặc muốn tối ưu** → Alias Record, không phải CNAME/Non-Alias.
- **CloudFront origin** → luôn phải là Public IP/DNS, không bao giờ là Private IP.
- **Route 53 Multivalue Answer Routing** → không thay thế load balancer hoàn toàn, nhưng vẫn là cách hợp lệ cải thiện availability nhờ health check ở tầng DNS.
- **NAT instance/gateway** → chỉ dùng cho outbound traffic từ private subnet, không liên quan đến HA của web tier public-facing.

### TD explanation

Amazon Route 53 alias records provide a Route 53–specific extension to DNS functionality. Alias records let you route traffic to selected AWS resources, such as CloudFront distributions and Amazon S3 buckets. They also let you route traffic from one record in a hosted zone to another record.
Unlike a CNAME record, you can create an alias record at the top node of a DNS namespace, also known as the zone apex. For example, if you register the DNS name tutorialsdojo.com, the zone apex is tutorialsdojo.com. You can’t create a CNAME record for tutorialsdojo.com, but you can create an alias record for tutorialsdojo.com that routes traffic to www.tutorialsdojo.com (take note of the www subdomain).
You can also type the domain name for the resource. For example:
–  CloudFront distribution domain name: dtut0rial5d0j0.cloudfront.net
–  Elastic Beanstalk environment CNAME: tutorialsdojo.elasticbeanstalk.com
–  ELB load balancer DNS name:tutorialsdojo-1.us-east-2.elb.amazonaws.com
–  S3 website endpoint: s3-website.us-east-2.amazonaws.com
–  Resource record set in this hosted zone: www.tutorialsdojo.com
–  VPC endpoint: tutorialsdojo.us-east-2.vpce.amazonaws.com
–  API Gateway custom regional API: d-tut5d0j0c0m.execute-api.us-west-2.amazonaws.com

Multivalue answer routing lets you configure Amazon Route 53 to return multiple values, such as IP addresses for your web servers, in response to DNS queries. You can specify multiple values for almost any record, but multivalue answer routing also lets you check the health of each resource, so Route 53 returns only value for healthy resources. It’s not a substitute for a load balancer, but the ability to return multiple health-checkable IP addresses is a way to use DNS to improve availability and load balancing.
The option that says: Place an Application Load Balancer in front of all the web servers. Create a new Alias Record in Route 53 which maps to the DNS name of the load balancer is correct because if the web servers are behind an ELB, the load on the web servers will be uniformly distributed which means that if any of the web servers go offline, the web traffic would be routed to other web servers. In this way, there would be no unnecessary downtime. You can also use Route 53 to set the ALIAS record that points to the ELB endpoint.
The option that says: Create a Non-Alias Record in Route 53 with a Multivalue Answer Routing configuration and add all the IP addresses for your web servers is correct. Although a Multivalue answer routing is not a substitute for a load balancer, its ability to return multiple health-checkable IP addresses can still improve the availability and load balancing of your system.
The option that says: Create a CloudFront distribution whose origin points to the private IP addresses of your web servers. Also set up a CNAME record in Route 53 mapped to your CloudFront distribution is incorrect as it is using Amazon CloudFront, which is directly pointing to the web server as its origin. You should use a Public IP address, not a Private IP address when using an EC2 origin. In addition, if the EC2 instances go down, the entire website would also become unavailable in this scenario.
The option that says: Set up a NAT instance in your VPC. Update your route table by creating a default route via the NAT instance with all subnets associated with it. Configure a DNS A Record in Route 53 pointing to the NAT instance’s public IP address is incorrect as a NAT instance is mainly used to allow an EC2 instance launched on a private subnet to access the Internet via a public subnet. In addition, the issue is mainly on the web servers which are hosted on the public subnet and not on the private subnet.
The option that says: Launch a load balancer in front of all the web servers then create a Non-Alias Record in Route 53 which maps to the DNS name of the load balancer is incorrect. Although it is recommended to use a load balancer in front of your EC2 instances, you need to use an Alias Record in Route 53 and not a Non-Alias Record.

References:
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-alias.html
https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html

Check out this Amazon Route 53 Cheat Sheet:
https://tutorialsdojo.com/amazon-route-53/

</details>

<a id="q18"></a>

## Q18

A telecommunications company has several Amazon EC2 instances inside an AWS VPC. To improve data leak protection, the company wants to restrict the internet connectivity of its EC2 instances. The EC2 instances that are launched on a public subnet should be able to access product updates and patches from the Internet. The packages are accessible through the third-party provider via their URLs. The company wants to explicitly deny any other outbound connections from the VPC instances to hosts on the Internet. 
Which of the following options would the solutions architect consider implementing to meet the company requirements?

- **A.** Move all instances from the public subnets to the private subnets. Additionally, remove the default routes from your routing tables and replace them instead with routes that specify your package locations.
- **B.** Use network ACL rules that allow network access to your specific package destinations. Add an implicit deny for all other cases.
- **C.** You can use a forward web proxy server in your VPC and manage outbound access using URL-based rules. Default routes are also removed.
- **D.** Create security groups with the appropriate outbound access rules that will let you retrieve software packages from the Internet.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** allow only package-update URLs outbound; deny all else

🪤 **Your trap:** NACLs and security groups filter IP/port, never URLs

🧠 **Rule:** URL/domain-based egress filtering → forward web proxy (or AWS Network Firewall).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
VPC
┌─────────────── Public subnet ───────────────┐
│ EC2 instances                                │
│   → CHỈ được phép gọi ra: vendor update URLs │
│   → PHẢI deny mọi outbound khác               │
└───────────────────────────────────────────────┘

Yêu cầu: filter outbound theo URL cụ thể (domain-based), không phải theo IP/port
```

Đáp án đúng: **C (forward web proxy)**. Anh chọn **B (NACL)**.

#### Vì sao C đúng

```
EC2 instance ──► Forward proxy (Squid...) ──► chỉ cho qua URL whitelist ──► Internet
                       │
                       └─ default route bị xoá, outbound bắt buộc đi qua proxy
```

TD explanation: *"A forward proxy server acts as an intermediary for requests from internal users and servers... Companies usually implement proxy solutions to provide URL and web content filtering..."* và *"You can limit outbound web connections from your VPC to the internet, using a web proxy (such as a squid server) with custom domain whitelists."*

Điểm mấu chốt: proxy hoạt động ở **tầng ứng dụng (Layer 7)**, nên nó đọc được **HTTP request** và biết URL/domain đang được gọi tới — từ đó mới lọc được theo URL cụ thể như yêu cầu đề bài. Đồng thời phải xoá default route để bắt buộc mọi outbound đi qua proxy, không có đường vòng.

#### Vì sao B (lựa chọn của anh) sai — NACL chỉ lọc được IP/port, không đọc được URL

**B sai vì Network ACL hoạt động ở tầng mạng (Layer 3/4) — nó chỉ nhìn thấy IP address, protocol, và port, hoàn toàn không đọc được nội dung HTTP request nên không thể biết URL nào đang được gọi.** TD explanation nói thẳng: *"NACLs cannot filter requests based on URLs."*

Lý do trông "hợp lý" khi chọn B: NACL hỗ trợ allow/deny rule theo thứ tự ưu tiên, nghe giống như có thể "whitelist rồi deny tất cả còn lại" — nhưng bản chất rule NACL chỉ match được theo **CIDR + port**, trong khi vendor cung cấp update qua URL có thể trỏ tới nhiều IP (CDN, load balancer động) không cố định → không thể whitelist bền vững bằng IP.

#### Các phương án sai khác

- **A (chuyển sang private subnet + sửa route table)**: Route table chỉ quyết định **gói tin đi đâu** (ví dụ qua Internet Gateway hay NAT), nó không có khả năng lọc theo nội dung/URL. TD: *"the routing table does not have the filtering logic. It only connects the subnets with Internet gateway."*
- **D (Security Group)**: Cùng vấn đề với NACL — Security Group cũng chỉ lọc theo IP/port (Layer 3/4), không đọc được URL. TD: *"A security group cannot filter requests based on URLs."*

| Phương án | Tầng hoạt động | Lọc được theo URL? |
|---|---|---|
| **C. Forward web proxy** | Application (L7) | Có |
| A. Private subnet + route table | Network (L3, routing) | Không |
| B. Network ACL | Network/Transport (L3/L4) | Không |
| D. Security Group | Network/Transport (L3/L4) | Không |

#### Lưu ý thực tế

- Đây là một trap kinh điển của SAP exam: khi đề nhắc "URL-based" hoặc "domain-based filtering", NACL và Security Group gần như luôn bị loại ngay vì cả hai đều hoạt động dưới tầng HTTP. Chỉ có proxy (Squid...) hoặc dịch vụ domain-filtering chuyên dụng (ví dụ AWS Network Firewall với domain list) mới đọc được tầng ứng dụng.

#### Quy tắc nhớ cho thi

- **Thấy "allow/deny theo URL hoặc domain"** → loại ngay NACL và Security Group (cả hai chỉ lọc IP/port).
- **URL/domain-based egress filtering** → forward web proxy (Squid...) hoặc AWS Network Firewall domain list.
- **Route table** → chỉ định tuyến gói tin, không có logic filter nội dung.

### TD explanation

A forward proxy server acts as an intermediary for requests from internal users and servers, often caching content to speed up subsequent requests. Companies usually implement proxy solutions to provide URL and web content filtering, IDS/IPS, data loss prevention, monitoring, and advanced threat protection. AWS customers often use a VPN or AWS Direct Connect connection to leverage existing corporate proxy server infrastructure, or build a forward proxy farm on AWS using software such as Squid proxy servers with internal Elastic Load Balancing (ELB).
You can limit outbound web connections from your VPC to the internet, using a web proxy (such as a squid server) with custom domain whitelists or DNS content filtering services. The solution is scalable, highly available, and deploys in a fully automated way.

Therefore, the correct answer is: You can use a forward web proxy server in your VPC and manage outbound access using URL-based rules. Default routes are also removed. A proxy server filters requests from the client, and allows only those that are related to the product updates, and in this case helps filter all other requests except the ones for the product updates.
The option that says: Move all instances from the public subnets to the private subnets. Additionally, remove the default routes from your routing tables and replace them instead with routes that specify your package locations is incorrect. Even though moving the instances in a private subnet is a good idea, the routing table does not have the filtering logic. It only connects the subnets with Internet gateway.
The option that says: Using network ACL rules that allow network access to your specific package destinations then adding an implicit deny for all other cases is incorrect. NACLs cannot filter requests based on URLs.
The option that says: Creating security groups with the appropriate outbound access rules that will let you retrieve software packages from the Internet is incorrect. A security group cannot filter requests based on URLs.

References:
https://docs.aws.amazon.com/cli/latest/userguide/cli-http-proxy.html
https://aws.amazon.com/blogs/security/how-to-set-up-an-outbound-vpc-proxy-with-domain-whitelisting-and-content-filtering/

Check out this Amazon VPC Cheat Sheet:
https://tutorialsdojo.com/amazon-vpc/

</details>

<a id="q27"></a>

## Q27

A company that manages hundreds of AWS client accounts has created a central logging service running on an Auto Scaling group of Amazon EC2 instances. The logging service receives logs from the client AWS accounts through the connectivity provided by AWS PrivateLink. The interface endpoint for this is available on each of the client AWS accounts. The EC2 instances hosting the logging service are spread on multiple subnets with a Network Load Balancer in front to spread the incoming load. Upon testing, the clients are unable to submit logs through the VPC endpoint.
Which of the following solutions will most likely resolve the issue? (Select TWO.)

- **A.** Ensure that the NACL associated with the logging service subnets allows communication to and from the interface endpoint. Ensure that the NACL associated with the interface endpoint subnet allows communication to and from the EC2 instances running the logging service.
- **B.** Ensure that the security group attached to the EC2 instances hosting the logging service allows inbound traffic from the NLB’s security group. Also, ensure that the security group attached to the NLB allows inbound traffic from the interface endpoint subnet.
- **C.** Ensure that the Auto Scaling group is associated with a launch template that includes the latest Amazon Machine Image (AMI) and that the EC2 instances are using instance types that are optimized for log processing.
- **D.** Ensure that the NACL associated with the logging service subnet allows communication to and from the NLB subnets. Ensure that the NACL associated with the NLB subnets allows communication to and from the EC2 instances subnets running the logging service.
- **E.** Ensure that the security group attached to the EC2 instances hosting the logging service allows inbound traffic from the IP address block of the clients.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D · **You picked:** D, E

🔑 **Key words:** PrivateLink → NLB → EC2 logging service; clients can't submit logs (Select TWO)

🪤 **Your trap:** Picked D (right) + E: instance SG must allow the NLB, not the clients' IP block

🧠 **Rule:** Endpoint → NLB → instances: open SGs and NACLs hop by hop (NLB SG from endpoint subnet; instance SG from NLB).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Client Account (từng account khách hàng)          Logging-service Account
┌─────────────────────┐                           ┌───────────────────────────┐
│ App gửi log          │                          │  Subnet A       Subnet B   │
└─────────┬────────────┘                          │  ┌─────────┐   ┌─────────┐ │
          │ PrivateLink                            │  │ EC2 (log)│   │EC2 (log)│ │
          ▼                                        │  └────▲────┘   └────▲────┘ │
  Interface Endpoint (ENI, NACL theo subnet)        │       │  SG         │      │
          │                                        │       └──────┬──────┘      │
          └──────────────────────────────────────► │         NLB (nhiều subnet) │
                                                     │         SG của NLB         │
                                                     └───────────────────────────┘
Yêu cầu: client KHÔNG submit log được qua VPC endpoint → sửa đúng 2 chỗ (Select TWO)
```

Đường đi thật sự là **endpoint → NLB → EC2 instances**, phải mở đúng theo từng chặng (hop-by-hop) ở cả SG lẫn NACL. Đáp án đúng: **B (SG đúng hop)** + **D (NACL đúng hop)**. Anh chọn đúng D, chọn thêm E (SG instance mở cho IP client) — đây là chặng sai.

#### Vì sao D đúng (NACL)

NLB **không có SG của riêng nó theo nghĩa "pass-through"** ở tầng NACL — traffic từ endpoint đi vào subnet của NLB, rồi NLB forward sang subnet chứa EC2. NACL là stateless theo từng subnet, nên phải mở **NACL của subnet logging-service ⇄ NACL của subnet NLB**, không phải NACL ⇄ interface endpoint subnet trực tiếp. Traffic không "nhảy cóc" từ endpoint subnet thẳng tới EC2 subnet; nó luôn đi qua NLB subnet trước.

#### Vì sao B đúng (Security Group)

Khi NLB forward request tới target, **source IP mà target nhìn thấy chính là private IP của NLB node** (không phải IP gốc của client hay của endpoint). Vì vậy:
- SG của EC2 instance (logging service) phải **allow inbound từ SG của NLB**.
- SG của NLB phải **allow inbound từ subnet chứa interface endpoint** (để nhận traffic đi vào từ phía client).

Đây đúng là nguyên tắc "mở theo từng hop": endpoint → NLB (SG chiều 1) → EC2 (SG chiều 2).

#### Vì sao E — pick của anh — sai

**E nói: SG của EC2 allow inbound từ IP block của client.** Điều này sai về bản chất kỹ thuật: EC2 instance **không bao giờ thấy IP gốc của client** khi traffic đi qua NLB — nó chỉ thấy IP của NLB node. Hơn nữa, tài liệu AWS nêu rõ: **không được dùng SG của client làm source trong SG của target** khi target đứng sau NLB gắn PrivateLink; phải dùng CIDR/SG của chính NLB. Dù anh add đúng IP client vào SG, traffic vẫn bị chặn vì source thực tế không khớp (NLB IP ≠ client IP).

#### Các phương án sai khác

- **A sai:** đề xuất mở NACL giữa logging-service subnet và **interface endpoint subnet trực tiếp**, bỏ qua NLB ở giữa — sai hop, không khớp đường đi thực tế của traffic (endpoint → NLB → EC2).
- **C sai:** AMI mới nhất / instance type tối ưu không liên quan gì tới vấn đề connectivity; đề mô tả lỗi kết nối, không phải lỗi hiệu năng xử lý log.

#### So sánh nhanh 2 lựa chọn NACL (A vs D)

| | Chặng mở NACL | Đúng/sai |
|---|---|---|
| A | logging-service subnet ⇄ endpoint subnet (bỏ qua NLB) | Sai hop |
| D | logging-service subnet ⇄ NLB subnet | Đúng hop |

#### Lưu ý thực tế

- NLB **không hỗ trợ SG riêng theo cách "attach vào NLB resource"** ở một số tình huống cấu hình cũ, nhưng khi NLB **có** SG (tính năng NLB security groups), SG đó chính là cái cần mở ở cả 2 chiều trong câu này — đề bài giả định NLB có SG.
- Khi debug "client không gọi được qua PrivateLink", luôn kiểm tra theo thứ tự: Interface Endpoint SG → NACL subnet endpoint → NACL subnet NLB → SG NLB → SG target (EC2) → NACL subnet target.

#### Quy tắc nhớ cho thi

- **Thấy "PrivateLink + NLB + target không nhận được traffic"** → **mở SG/NACL theo từng hop: endpoint → NLB → target**, không nối tắt.
- **Thấy "allow SG của client làm source cho SG của target sau NLB"** → luôn sai, vì target chỉ thấy IP của NLB node.
- **Thấy NACL "từ logging-service subnet tới endpoint subnet"** → kiểm tra có bỏ qua NLB ở giữa không — nếu có NLB, đáp án đó sai.

### TD explanation

When you create an Amazon VPC endpoint interface with AWS PrivateLink, an Elastic Network Interface is created inside of the subnet that you specify. This interface VPC endpoint (interface endpoint) inherits the network ACL of the associated subnet. You must associate a security group with the interface endpoint to protect incoming and outgoing requests.

When you associate a Network Load Balancer with an endpoint service, the Network Load Balancer forwards requests to the registered target as if the target was registered by IP address. In this case, the source IP addresses are the private IP addresses of the load balancer nodes. If you have access to the Amazon VPC endpoint service, you must verify that the security group rules and the rules within the network ACL associated with the Network Load Balancer’s targets:
– Allow communication from the private IP address of the Network Load Balancer.
– Don’t allow communication from the IP address of the client or the interface endpoint.
To allow communication between clients and the Amazon VPC endpoint, you must create rules within the network ACL associated with the client’s subnet and the subnet associated with the interface endpoint. Be aware of this limit:
– You cannot use the security groups for clients as a source in the security groups for the targets. Instead, use the client CIDR blocks as sources in the target security groups.
If you register targets by IP address and do not want to grant access to the entire VPC CIDR, you can grant access to the private IP addresses used by the load balancer nodes. There is one IP address per load balancer subnet.
Therefore, the correct answer are:
– Ensure that the NACL associated with the logging service subnet allows communication to and from the NLB subnets. Ensure that the NACL associated with the NLB subnets allows communication to and from the EC2 instances subnets running the logging service.
– Ensure that the security group attached to the EC2 instances hosting the logging service allows inbound traffic from the NLB’s security group. Also, ensure that the security group attached to the NLB allows inbound traffic from the interface endpoint subnet.
The option that says: Ensure that the NACL associated with the logging service subnets allows communication to and from the interface endpoint. Ensure that the NACL associated with the interface endpoint subnet allows communication to and from the EC2 instances running the logging service is incorrect because the rules within the network ACL associated with the Network Load Balancer’s targets should not allow direct communication from the IP address of the client or the interface endpoint. A better approach is to ensure that the NACL associated with the NLB subnets allows communication to and from the EC2 instances subnets running the logging service.
The option that says: Ensure that the security group attached to the EC2 instances hosting the logging service allows inbound traffic from the IP address block of the clients is incorrect because the security group attached to the EC2 instances must permit the inbound traffic from the NLB subnet IPs and not the IP address block of the clients. The security group rules associated with the Network Load Balancer’s targets should not allow direct access from the IP address of the client or the interface endpoint.
The option that says: Ensure that the Auto Scaling group is associated with a launch template that includes the latest Amazon Machine Image (AMI) and that the EC2 instances are using instance types that are optimized for log processing is incorrect because the issue described in the scenario is more likely related to connectivity, not the configuration of the EC2 instances. Therefore, while it’s generally good practice to use the latest AMI and appropriate instance types, this may not resolve the specific issue in the scenario. The most likely solutions involve checking the security groups of the interface endpoints and ensuring the Network Load Balancer is correctly configured.

References:
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-troubleshooting.html
https://aws.amazon.com/premiumsupport/knowledge-center/security-network-acl-vpc-endpoint/
https://aws.amazon.com/premiumsupport/knowledge-center/security-group-load-balancer/
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html#target-security-groups

Application Load Balancer vs Network Load Balancer vs Classic Load Balancer:
https://tutorialsdojo.com/application-load-balancer-vs-network-load-balancer-vs-classic-load-balancer/

</details>

<a id="q34"></a>

## Q34

An enterprise plans to create a new cloud deployment that will be used by several project teams. The network must be designed so that it allows autonomy for the administrators of the individual AWS accounts to modify their route tables freely. However, the company wants to monitor outbound traffic so it is required to have a centralized and controlled egress Internet connection for all accounts. As more teams are expected to join this deployment, the organization is expected to grow into thousands of AWS accounts.
Which of the following options should the Solutions Architect implement to meet the company requirements?

- **A.** Create a shared transit gateway. Have each spoke VPC connect to the transit gateway. In a central VPC, deploy a Gateway Load Balancer (GWLB) that fronts a fleet of firewall appliances with routing to the public internet.
- **B.** Create a centralized transit VPC. Have the VPCs on each AWS account connect to the transit VPC using a VPN connection. Control the outbound Internet traffic using firewall appliances.
- **C.** Create a centralized shared VPC. On this VPC, create a subnet that will be associated with each AWS account.  Use a fleet of proxy servers to control the outbound Internet traffic.
- **D.** Create a shared services VPC. On this VPC, host the central assets which include a fleet of firewalls that have a route to the public Internet. Have each spoke VPC connect to the central VPC using VPC peering.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** thousands of accounts; central controlled egress; accounts edit own route tables

🪤 **Your trap:** Transit VPC + VPN doesn't scale; peering limits; shared VPC participants can't edit route tables

🧠 **Rule:** Central egress/inspection at scale → shared Transit Gateway + GWLB-fronted firewalls in a central VPC.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Account 1    Account 2    Account 3  ...  (hàng nghìn accounts, mỗi account tự sửa route table)
  VPC           VPC           VPC
   │             │             │
   └──────┬──────┴──────┬──────┘
          ▼              ▼
        Shared Transit Gateway (hub)
                │
                ▼
        Central VPC
        ┌─────────────────────────────┐
        │  Gateway Load Balancer (GWLB)│
        │   → fleet firewall appliance │
        │   → route ra Internet        │
        └─────────────────────────────┘
Yêu cầu: (1) account tự sửa route table của mình, (2) egress Internet TẬP TRUNG + giám sát được, (3) scale tới hàng nghìn account
```

Đáp án đúng: **A (shared Transit Gateway + GWLB central egress)**. Anh chọn **B (transit VPC qua VPN)** — mô hình cũ, không scale.

#### Vì sao A đúng

Transit Gateway là **hub-and-spoke** chuẩn của AWS cho multi-account networking: mỗi spoke VPC chỉ cần **1 attachment** tới TGW để liên lạc với mọi VPC khác, và TGW hỗ trợ **tới hàng nghìn VPC attachment** — khớp với "thousands of AWS accounts" trong đề. Quan trọng hơn: dùng TGW **không bắt các account phải từ bỏ quyền tự quản route table riêng của VPC họ** — attachment chỉ thêm route trỏ ra TGW, admin từng account vẫn tự do sửa phần còn lại trong route table của họ.

Trong **central VPC**, đặt **Gateway Load Balancer (GWLB)** đứng trước fleet firewall/appliance: GWLB hoạt động ở layer 3/4, cho một **điểm vào/ra duy nhất** để toàn bộ traffic egress đi qua kiểm tra (inspection) trước khi ra Internet — đúng yêu cầu "monitor outbound traffic" tập trung.

**Anh từng gặp đúng mô hình GWLB này** ở TD Set 5 (Pass 2, Q62 — "virtual appliances scale dynamically qua centralized networking account") và đã chọn đúng **C, D (ASG launch template + GWLB/PrivateLink)**. Logic giống hệt ở đây: appliance/firewall cần scale + traffic layer 3 → GWLB, không phải ALB/NLB thường.

#### Vì sao B — pick của anh — sai

**Transit VPC qua VPN connection** là kiến trúc **cũ (pre-Transit-Gateway)**: mỗi spoke VPC phải thiết lập VPN tunnel riêng tới transit VPC. Vấn đề:
- VPN chạy qua Internet public (dù mã hoá), **chậm hơn AWS network backbone** mà TGW dùng trực tiếp (peering/attachment nội bộ AWS, không qua Internet).
- Quản lý hàng nghìn VPN connection (mỗi account 1 tunnel) cực kỳ phức tạp, tốn routing overhead và không scale tốt như TGW route table.
- TD explanation nói thẳng: dùng VPN cho kết nối nội bộ giữa các VPC là **không cần thiết** khi đã có network backbone của AWS.

#### Các phương án sai khác

- **C sai:** Shared VPC với subnet share cho từng account bị giới hạn **100 shared subnets** — không đủ cho hàng nghìn account. Quan trọng hơn: **participant trong shared subnet không tự sửa được route table** của VPC đó (chỉ owner mới sửa được) → vi phạm thẳng yêu cầu "autonomy for route table".
- **D sai:** Shared services VPC kết nối bằng **VPC Peering** bị giới hạn **50 peering connection cho mỗi VPC** theo mặc định — không đủ scale tới hàng nghìn account, và peering cũng không có transitive routing (mỗi peering là point-to-point riêng).

#### So sánh nhanh

| Phương án | Cách kết nối | Giới hạn chặn đường | Account tự sửa route table? |
|---|---|---|---|
| **A. TGW + GWLB** | TGW attachment | Scale tới hàng nghìn VPC | Có |
| B. Transit VPC + VPN | VPN tunnel | Chậm, khó quản lý ở scale lớn | Có, nhưng phức tạp |
| C. Shared VPC + subnet | Subnet sharing | Giới hạn 100 shared subnets | **Không** |
| D. Shared VPC + Peering | VPC Peering | Giới hạn 50 peering/VPC | Có, nhưng không scale |

#### Lưu ý thực tế

- Nếu firewall appliance hỗ trợ **two-arm mode** (1 interface public, 1 interface private), có thể bỏ luôn NAT Gateway — appliance tự làm NAT + inspection cùng lúc.
- GWLB dùng GENEVE encapsulation để giữ nguyên thông tin gói tin gốc khi chuyển tới appliance — đây là lý do ALB/NLB thường không thay thế được GWLB cho use case firewall/IPS.

#### Quy tắc nhớ cho thi

- **Thấy "hàng nghìn account" + "account tự sửa route table" + "central egress"** → **shared Transit Gateway + GWLB** trong central VPC.
- **Thấy "transit VPC + VPN"** → gần như luôn là kiến trúc cũ, không scale bằng TGW.
- **Thấy "shared VPC subnet"** → participant **không** sửa được route table của VPC đó.
- **Thấy "VPC Peering" cho rất nhiều VPC** → nhớ giới hạn 50 peering/VPC, không transitive.

### TD explanation

AWS Transit Gateway is a highly available and scalable service used to consolidate the AWS VPC routing configuration for a region with a hub-and-spoke architecture. Each spoke VPC only needs to connect to the Transit Gateway to gain access to other connected VPCs. Transit Gateway across different regions can peer with each other to enable VPC communications across regions. With a large number of VPCs, Transit Gateway provides simpler VPC-to-VPC communication management over VPC Peering.
Transit Gateway enables customers to connect thousands of VPCs. You can attach all your hybrid connectivity (VPN and Direct Connect connections) to a single Transit Gateway— consolidating and controlling your organization’s entire AWS routing configuration in one place. Transit Gateway controls how traffic is routed among all the connected spoke networks using route tables. This hub and spoke model simplifies management and reduces operational costs because VPCs only connect to the Transit Gateway to gain access to the connected networks.
Deploying a Gateway Load Balancer (GWLB) in a central VPC provides a scalable, easy-to-manage layer that fronts a fleet of firewall appliances. The GWLB simplifies the deployment of third-party virtual appliances in AWS, providing a single entry and exit point for traffic and thus facilitating the centralized inspection and control of outbound Internet traffic as required by the scenario.
If resources in private subnets need access to the Internet, introducing a NAT Gateway is a common solution. The NAT Gateway allows instances in a private subnet to connect to the Internet or other AWS services while preventing the Internet from initiating a connection with those instances.

Alternatively, if your firewall appliance supports two-arm mode, you may eliminate the need for a NAT Gateway. In two-arm mode, the appliance can perform both inspection and NAT with two network interfaces: one connected to a public subnet and the other to a private subnet.
Therefore, the correct answer is: Create a shared transit gateway. Have each spoke VPC connect to the transit gateway. In a central VPC, deploy a Gateway Load Balancer (GWLB) that fronts a fleet of firewall appliances with routing to the public internet.
The option that says: Create a centralized transit VPC. Have the VPCs on each AWS account connect to the transit VPC using a VPN connection. Control the outbound Internet traffic using firewall appliances is incorrect. Using a VPN connection for connecting within Amazon VPCs or with the transit is not needed. You can use the AWS network backbone which is much faster than setting up a VPN connection.
The option that says: Create a centralized shared VPC. On this VPC, create a subnet that will be associated with each AWS account. Use a fleet of proxy servers to control the outbound Internet traffic is incorrect. The default limit for shared VPC subnets is 100. Additionally, on this setup, the participants on the shared subnets will not be able to modify their own route tables.
The option that says: Create a shared services VPC. On this VPC, host the central assets which include a fleet of firewalls that have a route to the public Internet. Have each spoke VPC connect to the central VPC using VPC peering is incorrect. There is a default limit of 50 VPC peering for each VPC. This is not enough to handle peering for thousands of AWS accounts.

References:
https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-egress-to-internet.html
https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html
https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway.html

Check out these AWS Transit Gateway and Amazon VPC Cheat Sheets:
https://tutorialsdojo.com/aws-transit-gateway/
https://tutorialsdojo.com/amazon-vpc/

</details>

---

# Group E — Service fit (serverless, data, app design) (6)

<a id="q3"></a>

## Q3

A company runs a popular blogging platform that is hosted on AWS. Bloggers from all around the world upload millions of entries per month, and the average blog entry size is 300 KB. The access rate to blog entries drops to a negligible level six months after publishing and after a year, bloggers rarely access a blog. The blog entries have a high update rate during the first 3 months after the blogger has published it and this drops to no updates after 6 months. The company wants to use CloudFront to improve the load times of the blogging platform. 
Which of the following is an ideal cloud implementation for this scenario?

- **A.** Create two different CloudFront distributions: one with US-Europe price class for your US/Europe users and another one with all edge locations included for your remaining users.
- **B.** Create a CloudFront distribution and set the Restrict Viewer Access Forward Query string to true with a minimum TTL of 0.
- **C.** Store two copies of each entry in two different S3 buckets, and let each bucket have its own CloudFront distribution where S3 access is permitted to that CloudFront identity only.
- **D.** You can use one S3 source bucket that is partitioned according to the month a blog entry was submitted, and store the entry in that partition. Create a CloudFront distribution with access permissions to S3 and is restricted only to it.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** D · **You picked:** A

🔑 **Key words:** blog entries updated in first 3 months, quiet after 6; CloudFront load time

🪤 **Your trap:** Price-class split distributions don't improve load time

🧠 **Rule:** Content with age-dependent change rate → partition the origin (by month) so cache behaviors/TTLs differ.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Blog entry mới        Tháng 1-3            Tháng 4-6         Sau 12 tháng
   ┌───────┐         update nhiều         gần như hết        gần như không ai xem
   │ Upload│  ────►  update  ───►         update    ───►
   └───────┘

Yêu cầu: dùng CloudFront để cải thiện LOAD TIME, biết trước pattern update/access theo TUỔI bài viết
```

Đáp án đúng: **D (partition bucket theo tháng + 1 CloudFront distribution)**. Anh chọn **A (2 distribution theo price class)** — không liên quan tới tốc độ load.

#### Vì sao D đúng

Cốt lõi của câu hỏi là: **CloudFront chỉ cải thiện tốc độ nếu object được cache hiệu quả** (ít phải quay lại origin để revalidate). Khi **partition S3 origin theo tháng xuất bản**, ta có thể gán **cache behavior/TTL khác nhau cho từng partition** dựa vào biết trước tần suất update:
- Bài mới (0–3 tháng, update nhiều) → TTL ngắn, buộc CloudFront check lại origin thường xuyên để không serve bản cũ.
- Bài cũ (>6 tháng, không còn update) → TTL dài, CloudFront serve thẳng từ edge cache mà gần như không bao giờ phải quay về origin.

Kết quả: phần lớn traffic (bài cũ, chiếm đa số theo thời gian) được serve cực nhanh từ cache, còn bài mới vẫn đúng nội dung. Đây chính là cách "control cache behavior accordingly" mà TD explanation nói tới — tối ưu **load time dựa trên vòng đời nội dung**, đúng trọng tâm câu hỏi.

#### Vì sao A — pick của anh — sai

**Price class chỉ quyết định CloudFront dùng edge location nào** (ví dụ US-Europe only vs toàn cầu) để **tối ưu CHI PHÍ**, không liên quan gì đến **tốc độ cache hit/miss**. Tách 2 distribution theo vùng địa lý người dùng không giải quyết được vấn đề cốt lõi: bài viết cũ vẫn bị TTL mặc định chi phối như bài mới, không có cơ chế nào làm cache "thông minh hơn" theo tuổi nội dung. Nói cách khác, A tối ưu sai trục (địa lý/chi phí) trong khi đề hỏi về **load time dựa trên pattern update**.

#### Các phương án sai khác

- **B sai:** set **minimum TTL = 0** nghĩa là CloudFront **luôn phải revalidate với origin mỗi lần có request** — kể cả bài viết đã 6 tháng không ai sửa. Điều này triệt tiêu hoàn toàn lợi ích cache, làm chậm đi chứ không nhanh hơn.
- **C sai:** lưu 2 bản copy ở 2 bucket + 2 distribution riêng chỉ là **nhân đôi hạ tầng và chi phí lưu trữ**, không thay đổi cách CloudFront cache hay TTL — không cải thiện load time.

#### So sánh nhanh

| Phương án | Trục tối ưu | Giải quyết đúng vấn đề (load time theo tuổi content)? |
|---|---|---|
| **D. Partition theo tháng** | Cache behavior/TTL theo tuổi nội dung | Có |
| A. 2 distribution theo price class | Vùng địa lý / chi phí | Không |
| B. minTTL = 0 | Luôn tươi (fresh) | Không — làm chậm hơn |
| C. 2 bucket + 2 distribution | Nhân bản hạ tầng | Không |

#### Lưu ý thực tế

- CloudFront còn hỗ trợ set TTL **theo Cache-Control/Expires header trả về từ origin**, không chỉ qua cấu hình distribution — một cách khác để đạt cùng mục tiêu là origin (S3) trả header TTL khác nhau theo "tuổi" object, nhưng đề bài chọn hướng partition bucket vì nó rõ ràng, dễ quản lý theo batch tháng.
- Khi content "hết hạn" trong cache, CloudFront chỉ forward lại request tới origin ở **lần truy cập tiếp theo** sau khi TTL hết — không tự động refresh nền.

#### Quy tắc nhớ cho thi

- **Thấy "CloudFront cải thiện load time" + nội dung có pattern update theo tuổi** → nghĩ ngay tới **partition origin + TTL khác nhau theo nhóm nội dung**.
- **Thấy "price class"** → chỉ ảnh hưởng **chi phí/vùng phủ edge**, không ảnh hưởng tốc độ cache hit.
- **Thấy "minimum TTL = 0"** → luôn đi kèm "luôn mới nhất" nhưng **chậm hơn**, không phải đáp án cho câu hỏi tối ưu tốc độ.

### TD explanation

You can control how long your objects stay in a CloudFront cache before CloudFront forwards another request to your origin. Reducing the duration allows you to serve dynamic content. Increasing the duration means your users get better performance because your objects are more likely to be served directly from the edge cache. A longer duration also reduces the load on your origin.
Typically, CloudFront serves an object from an edge location until the cache duration that you specified passes—that is, until the object expires. After it expires, the next time the edge location gets a user request for the object, CloudFront forwards the request to the origin server to verify that the cache contains the latest version of the object.

Therefore, the correct answer is: You can use one S3 source bucket that is partitioned according to the month a blog entry was submitted, and store the entry in that partition. Create a CloudFront distribution with access permissions to S3 and is restricted only to it. The content is only accessed by CloudFront, and if the content is partitioned at the origin based on the month it was uploaded, you can control the cache behavior accordingly and keep only the latest updated content in the CloudFront cache so that it can be accessed with fast load-time, hence, improving the performance.
The option that says: Store two copies of each entry in two different S3 buckets, and letting each bucket have its own CloudFront distribution where S3 access is permitted to that CloudFront identity only is incorrect. Maintaining two separate buckets is not going to improve the load time for the users.
The option that says: Create a CloudFront distribution and setting the Restrict Viewer Access Forward Query string to true with a minimum TTL of 0 is incorrect. Setting minimum TTL of 0 will enforce loading of the content from origin every time, even if it has not been updated over 6 months.
The option that says: Create two different CloudFront distributions: one with US-Europe price class for your US/Europe users and another one with all edge locations included for your remaining users is incorrect. The location-wise distribution is not going to improve the load time for the users.

References:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html

Check out this Amazon CloudFront Cheat Sheet:
https://tutorialsdojo.com/amazon-cloudfront/

</details>

<a id="q24"></a>

## Q24

A manufacturing company is developing a system to monitor and analyze equipment performance using IoT devices. They plan to use AWS IoT Core to collect data from 500 sensors across their production lines.
The collected data must be enriched with additional context before being stored in an Amazon S3 data lake. Sensor data is collected every 10 seconds. The enriched data should be available in the data lake within 20 minutes of collection.
Which approach would best fulfill these requirements in the MOST cost-effective and scalable manner?

- **A.** Use AWS IoT Core Basic Ingest to forward sensor data to Amazon Kinesis Data Streams. Deploy an Auto Scaling group of EC2 instances to enrich and process the data, and use the S3 PutObject API to upload the processed data in Amazon S3.
- **B.** Use AWS IoT Core Basic Ingest for data collection. Configure an AWS IoT rule action to send data to Amazon Data Firehose. Set up Data Firehose with an AWS Lambda function for data enrichment and a buffer interval of 300 seconds.
- **C.** Ingest data over MQTT protocol using AWS IoT Core. Use an IoT rule action to trigger an AWS Step Functions workflow that enriches data using an AWS Lambda function and delivers results to Amazon S3.
- **D.** Use AWS IoT Core to send data to an Amazon Timestream table for temporary storage. Deploy an AWS Lambda function to query Timestream, enrich the data, and upload it to Amazon S3.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B · **You picked:** C

🔑 **Key words:** 500 IoT sensors every 10s; enrich; in S3 within 20 min; most cost-effective

🪤 **Your trap:** Step Functions per data point = expensive + complex. (You answered this same question correctly in the chapter drill — a regression, not a repeat miss.)

🧠 **Rule:** Stream → transform → S3 with minutes of latency → IoT rule → Data Firehose + Lambda transform (buffered).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
500 sensors ──(mỗi 10s)──► AWS IoT Core (Basic Ingest)
                                   │
                           IoT Rule Action
                                   │
                                   ▼
                         Amazon Data Firehose
                          (buffer 300s = 5 phút)
                                   │
                         AWS Lambda (enrich data)
                                   │
                                   ▼
                            Amazon S3 data lake

Yêu cầu: enriched data phải có trong S3 trong vòng 20 PHÚT kể từ lúc thu thập, MOST COST-EFFECTIVE + scalable
```

Đáp án đúng: **B (IoT Rule → Data Firehose + Lambda enrichment, buffer 300s)**. Anh chọn **C (Step Functions workflow mỗi lần nhận data)**.

#### Vì sao B đúng

**AWS IoT Core Basic Ingest** cho phép device publish thẳng vào IoT Rules Engine mà không cần duy trì connection — giảm overhead cho 500 sensor gửi dữ liệu liên tục mỗi 10 giây. Rule action route dữ liệu sang **Amazon Data Firehose** — dịch vụ **fully managed, tự scale theo throughput, không cần quản trị**, đúng tiêu chí "cost-effective + scalable" trong đề.

Firehose hỗ trợ gắn **Lambda để transform/enrich từng batch** trước khi ghi xuống S3. Quan trọng là **buffer interval 300 giây (5 phút)**: Firehose gom dữ liệu thành batch rồi mới xử lý + ghi 1 lần, thay vì xử lý từng record riêng lẻ — vừa rẻ hơn (ít lần invoke Lambda, ít PUT request tới S3) vừa **vẫn nằm gọn trong cửa sổ 20 phút** yêu cầu (5 phút buffer + một chút thời gian xử lý/enrich, còn dư nhiều margin so với 20 phút).

#### Vì sao C — pick của anh — sai

**Step Functions là công cụ orchestration cho workflow phức tạp, nhiều bước, chạy không thường xuyên** — không phải để xử lý stream tần suất cao. Ở đây dữ liệu đến **mỗi 10 giây từ 500 sensor**, nghĩa là có thể hàng chục nghìn lần kích hoạt workflow mỗi giờ. Mỗi lần start một Step Functions execution đều tính phí theo **số lần state transition** — chi phí tăng tuyến tính theo khối lượng, trong khi Firehose buffer theo batch giúp **giảm số lần xử lý xuống rất nhiều** cho cùng khối lượng dữ liệu. TD explanation cũng nói rõ: Step Functions "primarily used for complex, long-running workflows", không phải high-frequency/simple transform như enrich dữ liệu sensor.

#### Các phương án sai khác

- **A sai:** Kinesis Data Streams + Auto Scaling group EC2 để enrich dữ liệu rồi tự gọi `PutObject` — đây là tự quản lý hạ tầng compute (EC2, scaling policy, patching...), **operational overhead cao hơn hẳn** so với dùng Lambda + Firehose managed hoàn toàn.
- **D sai:** Amazon Timestream là **database time-series để query**, không phải công cụ streaming/transform. Dùng Timestream làm nơi "tạm chứa" rồi Lambda tự query + enrich + upload S3 là **tái tạo lại chức năng mà Firehose đã làm sẵn**, tốn thêm logic quản lý thủ công.

#### So sánh nhanh

| Phương án | Cơ chế xử lý | Overhead vận hành | Phù hợp tần suất cao (mỗi 10s)? |
|---|---|---|---|
| **B. Firehose + Lambda (buffer 300s)** | Batch theo buffer | Thấp (fully managed) | Có |
| A. Kinesis + EC2 ASG | Tự scale EC2 | Cao (tự quản lý server) | Có nhưng tốn công |
| C. Step Functions mỗi event | 1 workflow / data point | Cao (phí theo transition) | Không — quá tốn kém |
| D. Timestream + Lambda query | Lambda tự query rồi enrich | Trung bình–cao | Không tối ưu, sai mục đích dịch vụ |

#### Lưu ý thực tế

- Một câu tương tự ở chủ đề này (**"IoT Core Basic Ingest + Firehose + Lambda enrichment"**) anh từng làm **đúng** ở lần drill trước — cho thấy mấu chốt "stream → buffer → transform → S3" đã nắm được; câu này khác ở chỗ đáp án nhiễu là **Step Functions** thay vì EC2/Kinesis, nên bẫy nằm ở việc nhận diện đúng khi nào Step Functions KHÔNG phù hợp (tần suất cao, đơn giản) chứ không phải khi nào nó phù hợp (nhiều bước, phức tạp, ít tần suất).

#### Quy tắc nhớ cho thi

- **Thấy "stream dữ liệu tần suất cao → transform → S3, có vài phút tới vài chục phút độ trễ chấp nhận được"** → **IoT/Kinesis → Data Firehose + Lambda transform (buffered)**.
- **Thấy "Step Functions" đi kèm "mỗi event/mỗi 10 giây/high-frequency"** → gần như luôn là đáp án nhiễu — Step Functions hợp cho workflow nhiều bước, ít tần suất, không hợp cho streaming đơn giản.
- **Thấy "Timestream"** → chỉ dùng khi cần **query time-series data**, không phải công cụ ingest/transform stream.

### TD explanation

AWS IoT is a managed cloud platform that allows connected devices to securely and easily interact with cloud applications and other devices. It provides secure communication, data processing, and device management for Internet of Things (IoT) solutions. AWS IoT Core, which is mentioned in the question, is the central component of AWS IoT that provides the communication infrastructure for connecting IoT devices to the AWS cloud.
Amazon Data Firehose is a fully managed service for delivering real-time streaming data to destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, and Splunk. It can automatically scale to match the throughput of your data and requires no ongoing administration. It can also batch, compress, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.
AWS Lambda is a serverless compute service that allows you to run code without managing servers. You can create Lambda functions to perform specific tasks, which can be triggered by various AWS services or called directly. Lambda automatically scales based on workload size. In data processing, it can be used to transform, enrich, or analyze data flowing through services like Amazon Data Firehose.

To efficiently manage data collection from a network of 500 sensors, it is recommended that AWS IoT Core Basic Ingest be used. This method is specifically designed for high-volume data ingestion, allowing devices to publish messages directly to the AWS IoT Rules Engine without maintaining a persistent connection, which helps reduce overhead.
Configuring an AWS IoT rule action allows data to be routed to Amazon Data Firehose, a fully managed service that streams real-time data to destinations like Amazon S3. Data Firehose automatically scales to meet throughput demands and requires no ongoing administration while also supporting data transformation through AWS Lambda which could be use to the enrich data before storing to Amazon S3.
Setting a buffer interval of 300 seconds (5 minutes) is a good choice for processing data in batches, making it cost-effective for delivery to Amazon S3 within the required 20-minute window. Each buffered batch are processed by a Lambda function and sent back to Firehose. Firehose then sends the data to Amazon S3 once the specified buffering size or buffering interval is reached, whichever comes first.
Hence, the correct answer is: Use AWS IoT Core Basic Ingest for data collection. Configure an AWS IoT rule action to send data to Amazon Data Firehose. Set up Data Firehose with an AWS Lambda function for data enrichment and a buffer interval of 900 seconds.
The option that says: Ingest data over MQTT protocol using AWS IoT Core. Use an IoT rule action to trigger an AWS Step Functions workflow that enriches data using an AWS Lambda function and delivers results to Amazon S3 is incorrect. While Step Functions and Lambda would work, it introduces more complexity and adds unncessary overhead. Moreover, triggering a Step Functions workflow for every data point that comes in (every 10 seconds) would be expensive and potentially slow. Step Functions are primarily used for complex, long-running workflows rather than high-frequency, simple data processing.
The option that says: Use AWS IoT Core to send data to an Amazon Timestream table for temporary storage. Deploy an AWS Lambda function to query Timestream, enrich the data, and upload it to Amazon S3 is incorrect because Amazon Timestream is more suited for time-series data querying rather than real-time processing and enrichment of IoT data. Also, you’d need to manage the logic for both querying Timestream and handling the S3 upload in a Lambda function, which has more overhead than using Amazon Data Firehose.
The option that says: Use AWS IoT Core Basic Ingest to forward sensor data to Amazon Kinesis Data Streams. Deploy an Auto Scaling group of EC2 instances to enrich and process the data, and use the S3 PutObject API to upload the processed data in Amazon S3 is incorrect. Using EC2 instances for data processing only introduces unnecessary operational overhead. While Kinesis Data Streams could handle the data ingestion, managing an Auto Scaling group of EC2 instances would be more complex to setup than using managed services like AWS Lambda and Amazon Data Firehose.

References:
https://aws.amazon.com/blogs/iot/ingesting-enriched-iot-data-into-amazon-s3-using-amazon-kinesis-data-firehose/
https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html
https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html
https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

Check out these AWS Cheat Sheets:
https://tutorialsdojo.com/aws-lambda/
https://tutorialsdojo.com/amazon-kinesis/
https://tutorialsdojo.com/amazon-s3/
https://tutorialsdojo.com/aws-iot-core/

</details>

<a id="q32"></a>

## Q32

A car parts manufacturing company installed IP cameras along an assembly line. These cameras are part of the quality inspection process, capturing images of each car part and detecting defects by comparing images with baseline references. To improve detection accuracy, the company used Amazon SageMaker AI to train a machine learning (ML) model containing baseline images and common defects.
Upon detection, workers must receive feedback from a Linux server in an on-premises data center that hosts an API for the IP cameras. The company requires the solution to remain operational even when factory internet connectivity is unavailable.
Which of the following options is the recommended solution for deploying the ML model that meets these requirements?

- **A.** Deploy an AWS Outposts server in the local data center to create an AWS private cloud. Deploy SageMaker AI on this server for ML training, and leverage Amazon Rekognition's computer vision capabilities to detect defects in manufactured car parts.
- **B.** Use SageMaker Ground Truth to label defect images, then deploy the trained model directly to the IP cameras for real-time inference and feedback via the Linux server API.
- **C.** Deploy the AWS IoT Greengrass client software to another local server. Run ML inference on the Greengrass server from the ML model trained from SageMaker AI. Use Greengrass components to interact with the Linux server API whenever a defect is detected.
- **D.** Use SageMaker Edge Manager to deploy and manage the ML model directly on IP cameras, enabling defect detection and transmitting results to the Linux server API.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** D

🔑 **Key words:** SageMaker model at factory; works without internet; call on-prem Linux API

🪤 **Your trap:** SageMaker Edge Manager on cameras doesn't provide the local server runtime to call the API

🧠 **Rule:** Offline edge ML inference on a local server → IoT Greengrass (+ Greengrass components).

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Factory (on-prem, có thể MẤT Internet)
┌────────────────────────────────────────────────┐
│  IP cameras ──► ??? local inference ──► Linux   │
│                                          server  │
│                                          API     │
└────────────────────────────────────────────────┘
          ▲
          │ (cloud — chỉ dùng để TRAIN model)
   Amazon SageMaker AI (train model)

Yêu cầu: inference phải chạy ĐƯỢC khi mất Internet, và phải gọi được API trên server Linux local
```

Đáp án đúng: **C (AWS IoT Greengrass trên local server + Greengrass components gọi Linux API)**. Anh chọn **D (SageMaker Edge Manager trên camera)**.

#### Vì sao C đúng

**AWS IoT Greengrass** là edge runtime: nó cho phép **deploy model đã train trên cloud (SageMaker AI) xuống chạy local**, kể cả khi mất kết nối Internet — đúng yêu cầu "remain operational even when factory internet connectivity is unavailable". Quan trọng hơn, Greengrass chạy trên **một local server riêng** (không phải chạy ngay trên camera), nên nó có đủ tài nguyên compute để chạy inference phức tạp, và có **Greengrass components** — module phần mềm có thể tương tác với hệ thống bên ngoài, bao gồm **gọi API trên Linux server on-prem** khi phát hiện defect. Điều này khớp chính xác với luồng: camera chụp ảnh → Greengrass server chạy inference → phát hiện lỗi → component gọi API trên Linux server.

#### Vì sao D — pick của anh — sai

**SageMaker Edge Manager** chỉ giúp **deploy và quản lý vòng đời model trên edge device** (optimize, version, giám sát) — nó **không cung cấp runtime/hạ tầng để chạy một local server xử lý logic nghiệp vụ** (gọi API ra ngoài, orchestrate hành động khi phát hiện lỗi). Hơn nữa, đề nói rõ model phải chạy "even when internet connectivity is unavailable" **và** phải **"receive feedback from a Linux server"** — tức cần một thành phần software chạy trên server đó để làm cầu nối. SageMaker Edge Manager cũng không thực tế khi deploy thẳng **lên IP camera** (phần cứng hạn chế, không đủ cho workload ML phức tạp) — đúng như TD explanation chỉ ra.

#### Các phương án sai khác

- **A sai:** AWS Outposts hỗ trợ chạy một số service tại chỗ (ECS, IoT Greengrass, SageMaker Edge), nhưng **không hỗ trợ chạy Amazon Rekognition cục bộ** — phương án này đề xuất dùng Rekognition trên Outposts, điều AWS không hỗ trợ.
- **B sai:** **SageMaker Ground Truth chỉ dùng để gắn nhãn (label) dữ liệu training**, không phải để deploy hay chạy inference — không thể "deploy trained model directly to the IP cameras" bằng Ground Truth.

#### So sánh nhanh

| Phương án | Vai trò thực sự của service | Đáp ứng yêu cầu offline + gọi API local? |
|---|---|---|
| **C. IoT Greengrass (local server)** | Edge runtime chạy inference + components | Có |
| A. Outposts + Rekognition | Outposts không hỗ trợ Rekognition local | Không |
| B. Ground Truth | Chỉ dùng để label dữ liệu | Không |
| D. SageMaker Edge Manager (trên camera) | Quản lý model trên device, không phải local server runtime | Không |

#### Lưu ý thực tế

- Greengrass có thể chạy mô hình được train ở **SageMaker AI hoặc Amazon Lookout for Vision** — cả hai đều hợp lệ cho bài toán computer-vision defect detection kiểu này.
- Điểm mấu chốt để phân biệt C và D: câu hỏi nói **"Linux server trong on-premises data center"** chứ không nói chạy trực tiếp trên camera — đây là tín hiệu rõ cho thấy cần một edge **server/runtime** (Greengrass), không phải quản lý model trên **thiết bị đầu cuối** (Edge Manager trên camera).

#### Quy tắc nhớ cho thi

- **Thấy "ML inference phải chạy offline trên local server" + "train trên SageMaker cloud"** → **AWS IoT Greengrass** (+ Greengrass components để gọi API ngoài).
- **Thấy "SageMaker Ground Truth"** → chỉ là **labeling tool**, không deploy/inference được.
- **Thấy "SageMaker Edge Manager"** → quản lý model **trên device**, không cấp hạ tầng server để chạy logic nghiệp vụ phức tạp (gọi API, orchestrate).
- **Thấy "Outposts + Rekognition"** → bẫy, Outposts **không** chạy Rekognition tại chỗ.

### TD explanation

AWS IoT Greengrass is an open-source Internet of Things (IoT) edge runtime and cloud service that helps you build, deploy and manage IoT applications on your devices. You can use AWS IoT Greengrass to build software that enables your devices to act locally on the data that they generate, run predictions based on machine learning models, and filter and aggregate device data. AWS IoT Greengrass enables your devices to collect and analyze data closer to where that data is generated, react autonomously to local events, and communicate securely with other devices on the local network.
AWS IoT Greengrass components are software modules that you deploy to Greengrass core devices. Components can represent applications, runtime installers, libraries, or any code that you would run on a device. You can define components that depend on other components. For example, you might define a component that installs Python and then define that component as a dependency of your components that run Python applications.

With AWS IoT Greengrass, you can perform machine learning (ML) inference on your edge devices on locally generated data using cloud-trained models. You benefit from the low latency and cost savings of running local inference yet still take advantage of cloud computing power for training models and complex processing.
AWS IoT Greengrass makes the steps required to perform inference more efficient. You can train your inference models anywhere and deploy them locally as machine learning components. For example, you can build and train deep-learning models in Amazon SageMaker AI or computer vision models in Amazon Lookout for Vision.
Therefore, the correct answer is: Deploy the AWS IoT Greengrass client software to another local server. Run ML inference on the Greengrass server from the ML model trained from SageMaker AI. Use Greengrass components to interact with the Linux server API whenever a defect is detected. AWS IoT Greengrass makes it easy to perform machine learning inference locally on devices, using models that are created, trained, and optimized in the cloud. AWS IoT Greengrass provides prebuilt components for common use cases which includes interacting with external APIs.
The option that says: Deploy an AWS Outposts server in the local data center to create an AWS private cloud. Deploy SageMaker AI on this server for ML training, and leverage Amazon Rekognition’s computer vision capabilities to detect defects in manufactured car parts is incorrect. Although AWS Outposts support running some AWS services such as ECS, IoT Greengrass, and SageMaker Edge, it does not support running Amazon Rekognition locally.
The option that says: Use SageMaker Ground Truth to label defect images, then deploy the trained model directly to the IP cameras for real-time inference and feedback via the Linux server API is incorrect. Amazon SageMaker Ground Truth is only used for labeling training datasets, not for deploying or running ML models. It only prepares data for training and does not support real-time inference or integration with local systems, such as the Linux server API.
The option that says: Use SageMaker Edge Manager to deploy and manage the ML model directly on IP cameras, enabling defect detection and transmitting results to the Linux server API is incorrect because this service is primarily designed for managing models on edge devices, but it does not provide the necessary infrastructure for real-time local ML inference on a server. Deploying ML models directly on IP cameras is impractical for complex ML workloads due to hardware limitations.

References:
https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-components.html
https://docs.aws.amazon.com/greengrass/v2/developerguide/perform-machine-learning-inference.html
https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html

Check out this Amazon SageMaker AI Cheat Sheet:
https://tutorialsdojo.com/amazon-sagemaker/

</details>

<a id="q38"></a>

## Q38

A company runs its internal tool on AWS. It is used for logistics and shipment tracking for the company’s warehouse. With the current system process, the application receives an order and it sends an email to the employees with the information needed for the package shipment. After the employees prepare the order and ship the package, they reply to the email so that the application can mark the order as shipped. The company wants to migrate to a serverless application model to stop relying on emails and minimize the operational overhead for the application.
Which of the following options should the Solutions Architect implement to meet the company requirements?

- **A.** Create AWS Batch jobs corresponding to different tasks needed to ship a package. Write an AWS Lambda function with AWS Batch as the trigger to create and print the shipping label for the package. Once the package is scanned and leaves the warehouse, trigger another Lambda function to move the AWS Batch job to the next stage of the shipping process.
- **B.** Store order information on an Amazon SQS queue when a new order is created. Schedule an AWS Lambda function to poll the queue every 5 minutes and start processing if any orders are found. Use another Lambda function to print the shipping labels for the package. Once the package is scanned and leaves the warehouse, use Amazon Pinpoint to send a notification to customers regarding the status of their order.
- **C.** Store the order information on an Amazon DynamoDB table. Create an AWS Step Functions workflow that will be triggered for every new order. Have the workflow mark the order as “in progress” and print the shipping label for the package. Once the package is scanned and leaves the warehouse, trigger an AWS Lambda function to mark the order as “shipped” and complete the Step Functions workflow.
- **D.** Use an Amazon EFS volume to store the new order information. Configure an instance to pull the order information from the EFS share and print the shipping label for the package. Once the package is scanned and leaves the warehouse, remove the order information on the EFS share by using an Amazon API Gateway call to the instances.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** C · **You picked:** B

🔑 **Key words:** replace email order workflow; serverless; least overhead

🪤 **Your trap:** Lambda polling SQS every 5 min + Pinpoint doesn't track order state

🧠 **Rule:** Multi-step workflow with state → Step Functions + DynamoDB.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Hiện tại:  Order mới ──► gửi EMAIL cho nhân viên ──► nhân viên ship hàng ──► REPLY email ──► mark shipped
                                   (thủ công, không có state machine rõ ràng)

Yêu cầu:  chuyển sang SERVERLESS, bỏ email, MINIMIZE operational overhead
          → cần theo dõi trạng thái order qua nhiều bước: "in progress" → "shipped"
```

Đáp án đúng: **C (DynamoDB lưu state + Step Functions orchestrate workflow)**. Anh chọn **B (SQS + Lambda poll mỗi 5 phút + Pinpoint)**.

#### Vì sao C đúng

Bản chất bài toán là **một workflow nhiều bước có trạng thái (state)**: order mới → in progress (in tem vận chuyển) → chờ sự kiện "package scanned, leaves warehouse" → shipped. Đây chính xác là use case AWS Step Functions được thiết kế cho: **orchestration nhiều bước, track state qua từng bước, tích hợp Lambda cho từng task**. Lưu order trên **DynamoDB** cho phép Step Functions đọc/ghi trạng thái order (in progress/shipped) một cách tin cậy, có audit trail rõ ràng — đúng tinh thần "Step Functions maintains the application state" mà TD explanation nêu. Khi event "package scanned" xảy ra, một Lambda được trigger để mark "shipped" và **complete workflow** — khớp hoàn toàn với luồng nghiệp vụ gốc (chờ nhân viên xác nhận đã ship), chỉ là thay email reply bằng một sự kiện serverless thực sự.

#### Vì sao B — pick của anh — sai

**Lambda được lên lịch poll SQS mỗi 5 phút** nghe có vẻ hợp lý nhưng có vấn đề về hiệu quả: Lambda vẫn **chạy đều đặn mỗi 5 phút dù hàng đợi rỗng** — tốn chi phí/overhead không cần thiết khi không có order mới, trái với mục tiêu "minimize operational overhead". Quan trọng hơn: cách này **không theo dõi được trạng thái order qua nhiều bước** (in progress/shipped) một cách có cấu trúc — SQS chỉ là hàng đợi tin nhắn, không phải nơi lưu trạng thái lâu dài của một order đang "treo" chờ xác nhận ship. Amazon Pinpoint ở bước cuối chỉ gửi **thông báo cho customer**, không giải quyết bài toán cốt lõi là "ứng dụng cần biết đơn hàng đã được đánh dấu shipped" để cập nhật hệ thống nội bộ.

#### Các phương án sai khác

- **A sai:** AWS Batch dùng để chạy **batch job độc lập** (vd: báo cáo, phân tích), **không phải công cụ orchestration workflow** nhiều bước có điều kiện/trạng thái như Step Functions.
- **D sai:** Dùng **Amazon EFS + instance** để lưu và xử lý order **cần có EC2 instance chạy liên tục** → tăng operational overhead (patch, scale, quản lý), hoàn toàn trái với yêu cầu "serverless" và "minimize operational overhead" của đề.

#### So sánh nhanh

| Phương án | Theo dõi state qua nhiều bước? | Thực sự serverless/ít overhead? |
|---|---|---|
| **C. DynamoDB + Step Functions** | Có — built-in state tracking | Có |
| A. AWS Batch | Không — chỉ chạy job rời rạc | Có (serverless) nhưng sai công cụ |
| B. SQS + Lambda poll 5 phút + Pinpoint | Yếu — SQS không lưu state lâu dài | Lambda chạy dư thừa khi queue rỗng |
| D. EFS + EC2 instance | Có thể tự làm nhưng thủ công | Không — cần quản lý EC2 |

#### Lưu ý thực tế

- Step Functions có 2 loại workflow: **Standard** (giá theo state transition, phù hợp quy trình dài có chờ đợi như "chờ scan khi ship") và **Express** (giá theo thời gian + số lần invoke, phù hợp workflow ngắn tần suất cao). Với use case "chờ nhân viên ship rồi mới hoàn tất" — vốn có thể kéo dài — **Standard Workflow** là lựa chọn tự nhiên hơn.
- Step Functions có thể **chờ một sự kiện bên ngoài (callback pattern/waitForTaskToken)** để tạm dừng workflow cho tới khi có Lambda gọi lại báo "package scanned" — đúng cơ chế thay thế cho việc "chờ email reply" trong hệ thống cũ.

#### Quy tắc nhớ cho thi

- **Thấy "nhiều bước có trạng thái, cần theo dõi order/process đang ở đâu"** → **Step Functions** (+ DynamoDB để persist state).
- **Thấy "Lambda poll SQS theo lịch cố định (vd mỗi 5 phút)"** → thường là đáp án nhiễu vì tốn tài nguyên vô ích khi hàng đợi rỗng, và không track state tốt bằng Step Functions.
- **Thấy "EFS + EC2" cho yêu cầu "serverless"** → luôn sai, vì vẫn cần quản lý instance.
- **Thấy "AWS Batch" cho bài toán orchestration nhiều bước có điều kiện** → sai, Batch chỉ chạy job rời rạc.

### TD explanation

AWS Step Functions is a serverless orchestration service that lets you combine AWS Lambda functions and other AWS services to build business-critical applications. Orchestration centrally manages a workflow by breaking it into multiple steps, adding flow logic, and tracking the inputs and outputs between the steps. As your applications execute, Step Functions maintains the application state, tracking exactly which workflow step your application is in and storing an event log of data that is passed between application components.
Step Functions is based on state machines and tasks. A state machine is a workflow. A task is a state in a workflow that represents a single unit of work that another AWS service performs. Each step in a workflow is a state.
With Step Functions’ built-in controls, you examine the state of each step in your workflow to make sure that your application runs in order and as expected. Depending on your use case, you can have Step Functions call AWS services, such as AWS Lambda, to perform tasks.
Step Functions is ideal for coordinating session-based applications. You can use Step Functions to coordinate all of the steps of a checkout process on an e-commerce site, for example. Step Functions can read and write from Amazon DynamoDB as needed to manage inventory records.

You can use Step Functions to make decisions about how best to process data, for example, to do post-processing of groups of satellite images to determine the amount of trees per acre of land. Depending on the size and resolution of the image, this Step Functions workflow will determine whether to use AWS Lambda or AWS Fargate to complete the post-processing of each file in order to optimize runtime and costs.

Using AWS Step Functions, you define your workflows as state machines, which transform complex code into easy-to-understand statements and diagrams. Building apps and confirming that they are implementing your desired functionality is quicker and easier.
Therefore, the correct answer is: Store the order information on an Amazon DynamoDB table. Create an AWS Step Functions workflow that will be triggered for every new order. Have the workflow mark the order as “in progress” and print the shipping label for the package. Once the package is scanned and leaves the warehouse, trigger an AWS Lambda function to mark the order as “shipped” and complete the Step Functions workflow. Step Functions is suitable to orchestrate this workflow to update a DynamoDB table for the order progress as well trigger AWS Lambda functions for various actions.
The option that says: Create AWS Batch jobs corresponding to different tasks needed to ship a package. Write an AWS Lambda function with AWS Batch as the trigger to create and print the shipping label for the package. Once the package is scanned and leaves the warehouse, trigger another Lambda function to move the AWS Batch job to the next stage of the shipping process is incorrect. AWS Batch is not designed to orchestrate a workflow. AWS Batch is used to run batch jobs such as transaction reporting or analysis reporting, which usually run as stand-alone jobs.
The option that says: Store order information on an Amazon SQS queue when a new order is created. Schedule an AWS Lambda function to poll the queue every 5 minutes and start processing if any orders are found. Use another Lambda function to print the shipping labels for the package. Once the package is scanned and leaves the warehouse, use Amazon Pinpoint to send a notification to customers regarding the status of their order is incorrect. This may be possible; however, polling the SQS every 5 minutes is not efficient compared to writing to the DynamoDB table. If there are no orders for the past 5 minutes, the Lambda function will still run.
The option that says: Use an Amazon EFS volume to store the new order information. Configure an instance to pull the order information from the EFS share and print the shipping label for the package. Once the package is scanned and leaves the warehouse, remove the order information on the EFS share by using an Amazon API Gateway call to the instances is incorrect. Using an EFS share will require EC2 instances and will increase the operational overhead needed to manage the infrastructure. This is not a serverless solution.

References:
https://aws.amazon.com/step-functions/use-cases/
https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
https://aws.amazon.com/step-functions/features/
https://aws.amazon.com/getting-started/hands-on/create-a-serverless-workflow-step-functions-lambda/

Check out the AWS Step Functions Cheat Sheet:
https://tutorialsdojo.com/aws-step-functions/

</details>

<a id="q50"></a>

## Q50

A call center company uses its custom application to process and store call recordings in its on-premises data center. The recordings are stored on an NFS share. An offshore team is contracted to transcribe about 2% of the call recordings to be used for quality assurance purposes. It could take up to 3 days before the recordings are completely transcribed. The application that processes the calls and manages the transcription queue is hosted on Linux servers. A web portal is available for the quality assurance team to review the call recordings. After 90 days, the recordings are sent to an offsite location for long-term storage. The company plans to migrate the system to the AWS cloud to reduce storage costs and automate the transcription of the recordings.
Which of the following options is the recommended solution to meet the company’s requirements?

- **A.** Store all recordings in an Amazon S3 bucket. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an AWS Lambda trigger to start a transcription job using Amazon Transcribe. Update the web portal so it can be hosted on an Amazon S3 bucket, Amazon API Gateway, and AWS Lambda.
- **B.** Create an Auto Scaling group of Amazon EC2 instances to host the web portal. Provision an Application Load Balancer in front of the Auto Scaling group. Store all recordings in an Amazon EFS share that is mounted on all instances. After 90 days, archive all call recordings using AWS Backup and use Amazon Transcribe to transcribe the recordings.
- **C.** Store all recordings in an Amazon S3 bucket. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an AWS Lambda trigger to start a transcription job using AWS IQ. Create an Auto Scaling group of Amazon EC2 instances to host the web portal. Provision an Application Load Balancer in front of the Auto Scaling group.
- **D.** Store all recordings in an Amazon S3 bucket and send the object key to an Amazon SQS queue. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an Auto Scaling group of Amazon EC2 instances to push the recordings to Amazon Translate for transcription. Set the Auto Scaling policy based on the number of objects on the SQS queue. Update the web portal so it can be hosted on an Amazon S3 bucket, Amazon API Gateway, and AWS Lambda.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** call recordings; automate transcription; reduce storage cost

🪤 **Your trap:** Amazon Translate translates text — it doesn't transcribe audio; EC2 ASG adds overhead

🧠 **Rule:** Speech→text = Transcribe; text→language = Translate; text→speech = Polly.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-prem:  NFS share ──► call recordings ──► 2% được offshore team TRANSCRIBE (tối đa 3 ngày)
          Sau 90 ngày  ──► đẩy sang lưu trữ dài hạn (offsite)
          Web portal cho QA team review recordings

Mục tiêu khi lên AWS: GIẢM chi phí lưu trữ + TỰ ĐỘNG HOÁ transcription
```

Đáp án đúng: **A (S3 + Lifecycle → Glacier + Lambda trigger Amazon Transcribe + web portal S3/API Gateway/Lambda)**. Anh chọn **D (dùng Amazon Translate để "transcribe")**.

#### Vì sao A đúng

- **Amazon S3 + Lifecycle policy chuyển sang Glacier sau 90 ngày**: khớp chính xác pattern lưu trữ gốc (90 ngày → offsite long-term) với chi phí thấp nhất, không cần quản lý hạ tầng lưu trữ riêng.
- **Lambda trigger khi có object mới → gọi Amazon Transcribe**: đây là dịch vụ **speech-to-text** đúng nghĩa — nhận file audio, trả về văn bản transcript, tự động hoá hoàn toàn việc transcribe mà trước đây offshore team phải làm thủ công.
- **Web portal host trên S3 + API Gateway + Lambda**: kiến trúc serverless, rẻ, scale tốt — thay thế Linux server quản lý thủ công.

Đây là bộ ghép dịch vụ managed, rẻ và tự động hoá đúng yêu cầu "reduce storage costs and automate transcription".

#### Vì sao D — pick của anh — sai

**D dùng Amazon Translate để "transcribe"** — đây là nhầm lẫn bản chất dịch vụ:

| Dịch vụ | Input | Output | Chức năng |
|---|---|---|---|
| **Amazon Transcribe** | Audio (giọng nói) | Text | **Speech → Text** (transcription) |
| **Amazon Translate** | Text | Text (ngôn ngữ khác) | **Text → Text** (dịch ngôn ngữ) |
| **Amazon Polly** | Text | Audio (giọng nói) | **Text → Speech** (tổng hợp giọng nói) |

**Amazon Translate chỉ dịch văn bản từ ngôn ngữ này sang ngôn ngữ khác — nó không có khả năng nhận input là audio.** Đề bài cần chuyển **ghi âm cuộc gọi (audio) thành văn bản (transcript)** để QA review — đây là bài toán của **Transcribe**, không phải Translate. Dù D có vẻ hợp lý ở phần hạ tầng (S3 lifecycle, ASG theo SQS queue), toàn bộ kiến trúc vô nghĩa vì Translate không transcribe được file âm thanh.

#### Các phương án sai khác

- **B sai:** dùng ASG EC2 host web portal + EFS lưu recordings, rồi "archive bằng AWS Backup" sau 90 ngày. EFS **đắt hơn S3** đáng kể cho lưu trữ dài hạn, và việc duy trì EC2 ASG cho web portal tạo thêm overhead vận hành không cần thiết so với kiến trúc serverless.
- **C sai:** gọi **AWS IQ** để "transcribe" — AWS IQ thực chất là **nền tảng kết nối với chuyên gia freelance AWS**, không phải dịch vụ tự động hoá transcription. Dùng AWS IQ nghĩa là vẫn cần con người làm thủ công, không tự động hoá được gì cả.

#### Lưu ý thực tế

- Amazon Transcribe hỗ trợ cả **batch transcription job** (`StartTranscriptionJob` → `GetTranscriptionJob`) lẫn streaming, phù hợp cho use case trigger theo từng file audio mới upload — khớp với kiến trúc Lambda trigger trong đáp án A.
- S3 Lifecycle policy không chỉ transition sang storage class rẻ hơn (Glacier) mà còn có thể kèm **expiration action** — tuy đề không yêu cầu xoá, chỉ cần transition.

#### Quy tắc nhớ cho thi

- **Thấy "giọng nói / audio → văn bản"** → **Amazon Transcribe**.
- **Thấy "văn bản → ngôn ngữ khác"** → **Amazon Translate**.
- **Thấy "văn bản → giọng nói"** → **Amazon Polly**.
- **Thấy "AWS IQ"** → đây là **dịch vụ freelancer/chuyên gia**, không phải công cụ tự động hoá kỹ thuật — gần như luôn là đáp án nhiễu khi đề yêu cầu "automate".
- **Thấy "giảm chi phí lưu trữ dài hạn"** → **S3 + Lifecycle → Glacier**, không phải EFS.

### TD explanation

Amazon Transcribe is an AWS service that makes it easy for customers to convert speech to text. Using Automatic Speech Recognition (ASR) technology, customers can choose to use Amazon Transcribe for a variety of business applications, including transcription of voice-based customer service calls, generation of subtitles on audio/video content, and conduct (text-based) content analysis on audio/video content.
Amazon Transcribe analyzes audio files that contain speech and uses advanced machine-learning techniques to transcribe the voice data into text. You can then use the transcription as you would any text document.
Amazon Transcribe uses a deep learning process called automatic speech recognition (ASR) to convert speech to text quickly and accurately. Amazon Transcribe can be used to transcribe customer service calls, automate subtitling, and generate metadata for media assets to create a fully searchable archive. Amazon Transcribe automatically adds speaker diarization, punctuation, and formatting so that the output closely matches the quality of manual transcription at a fraction of the time and expense. Speech-to-text processing can be applied to live audio streams or batch audio content for transcription.
To transcribe an audio file, Amazon Transcribe uses three operations:
StartTranscriptionJob – Starts a batch job to transcribe the speech in an audio file to text.
ListTranscriptionJobs – Returns a list of transcription jobs that have been started. You can specify the status of the jobs that you want the operation to return. For example, you can get a list of all pending jobs or a list of completed jobs.
GetTranscriptionJob – Returns the result of a transcription job. The response contains a link to a JSON file containing the results.
To manage your objects so that they are stored cost-effectively throughout their lifecycle, configure their Amazon S3 Lifecycle. An S3 Lifecycle configuration is a set of rules that define actions that Amazon S3 applies to a group of objects. There are two types of actions:
Transition actions—Define when objects transition to another Using Amazon S3 storage classes. For example, you might choose to transition objects to the S3 Standard-IA storage class 30 days after you created them or archive objects to the S3 Glacier storage class one year after creating them.
Expiration actions—Define when objects expire. Amazon S3 deletes expired objects on your behalf. The lifecycle expiration costs depend on when you choose to expire objects.

Therefore, the correct answer is: Store all recordings in an Amazon S3 bucket. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an AWS Lambda trigger to start a transcription job using Amazon Transcribe. Update the web portal so it can be hosted on an Amazon S3 bucket, Amazon API Gateway, and AWS Lambda. Amazon S3 and Glacier offer very cheap object storage for recordings. Amazon Transcribe offers speech-to-text services that can quickly transcribe recordings. Amazon S3, API Gateway, and Lambda are cheap and scalable ways to host the web portal.
The option that says: Store all recordings in an Amazon S3 bucket. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an AWS Lambda trigger to start a transcription job using AWS IQ. Create an Auto Scaling group of Amazon EC2 instances to host the web portal. Provision an Application Load Balancer in front of the Auto Scaling group is incorrect because this AWS IQ is just a freelancing platform that provides hands-on help from AWS experts, and it does not have a feature to automate a transcription job. The correct answer is Amazon Transcribe, where in itis faster in the transcription process, which is a requirement by the company.
The option that says: Create an Auto Scaling group of Amazon EC2 instances to host the web portal. Provision an Application Load Balancer in front of the Auto Scaling group. Store all recordings in an Amazon EFS share that is mounted on all instances. After 90 days, archive all call recordings using AWS Backup and use Amazon Transcribe to transcribe the recordings is incorrect because Amazon Transcribe is primarily used to trancribe your recordings and stored on Amazon S3, not on Amazon EFS. Storing the call recordings to Amazon S3 is cheaper compared to Amazon EFS.
The option that says: Store all recordings in an Amazon S3 bucket and send the object key to an Amazon SQS queue. Create an S3 lifecycle policy to move objects older than 90 days to Amazon S3 Glacier. Create an Auto Scaling group of Amazon EC2 instances to push the recordings to Amazon Translate for transcription. Set the Auto Scaling policy based on the number of objects on the SQS queue. Update the web portal so it can be hosted on an Amazon S3 bucket, Amazon API Gateway, and AWS Lambda is incorrect because Amazon Translate is only a text translation service that uses advanced machine learning technologies to provide high-quality translation on demand. It is not used for transcribing voice messages to text.

References:
https://aws.amazon.com/transcribe/faqs/
https://docs.aws.amazon.com/transcribe/latest/dg/API_StartTranscriptionJob.html
https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html

Check out the Amazon Transcribe and Amazon S3 Cheat Sheets:
https://tutorialsdojo.com/amazon-transcribe/
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q59"></a>

## Q59

A company has a team of data analysts that uploads generated data points to an Amazon S3 bucket. The data points are used by other departments, so the objects in this primary S3 bucket need to be replicated to other S3 buckets on several AWS Accounts owned by the company. The company enforces data governance across all its AWS accounts using AWS Audit Manager. The Solutions Architect created an AWS Lambda function that is triggered by S3 PUT events on the primary bucket.
This Lambda function will replicate the newly uploaded object to other destination buckets. Since there will be thousands of object uploads on the primary bucket every day, the company is concerned that this Lambda function may affect other critical Lambda functions because of the regional concurrency limit in Lambda. The replication of the objects does not need to happen in real-time. The team initially considered using provisioned concurrency to guarantee execution capacity, but realized that it was not necessary given the non‑urgent nature of the replication. The company needs to ensure that this Lambda function will not affect the execution of other critical Lambda functions.
Which of the following options will meet the requirements in the LEAST amount of development effort?

- **A.** Configure a reserved concurrency limit for the new function to ensure that its executions will not exceed this limit. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to ensure that the concurrency limit is not being reached.
- **B.** Implement an exponential backoff algorithm in the new Lambda function to ensure that it will not run if the concurrency limit is reached. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to check if the concurrency limit is reached.
- **C.** Set the execution timeout of the new Lambda function to 5 minutes. This will allow it to wait for other Lambda function executions to finish in case the concurrency limit is reached. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to check if the concurrency limit is reached.
- **D.** Decouple the S3 event notifications and send the events to an Amazon SQS queue in a separate AWS account. Create the new Lambda function on this account, too. Invoke the Lambda function whenever an event message is received in the SQS queue.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** D

🔑 **Key words:** Lambda must not affect other functions' concurrency; LEAST development effort

🪤 **Your trap:** Separate account + SQS works but is far more work

🧠 **Rule:** Isolate a function's concurrency → reserved concurrency on that function.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
S3 (primary bucket) ──PUT event──► Lambda (replicate)
                                       │
                                       ▼
                     replicate sang nhiều bucket ở account khác
                                       │
           chung REGIONAL CONCURRENCY POOL với các Lambda function QUAN TRỌNG khác

Yêu cầu: Lambda replicate KHÔNG được chiếm hết concurrency làm ảnh hưởng Lambda khác
         replicate KHÔNG cần real-time; LEAST development effort
```

Đáp án đúng: **A (Reserved concurrency + CloudWatch alarm theo dõi Throttles)**. Anh chọn **D (tách sang SQS + account riêng + Lambda riêng)**.

#### Vì sao A đúng

Toàn bộ Lambda function trong 1 account/region **chia sẻ chung một regional concurrency quota**. Nếu function replicate bị gọi dồn dập (hàng nghìn PUT/ngày), nó có thể **chiếm phần lớn pool chung**, khiến các Lambda quan trọng khác bị throttle. Giải pháp đúng và đơn giản nhất: **đặt reserved concurrency** cho riêng function replicate — việc này:
- **Giới hạn cứng** số lượng execution đồng thời tối đa mà function replicate được dùng.
- Đồng thời **"trích" một phần pool chung thành dành riêng cho nó, không ai khác đụng vào được** — nghĩa là các Lambda khác cũng không bị nó tranh giành capacity.
- Chỉ cần **1 thay đổi cấu hình** (set reserved concurrency), không cần viết thêm code hay dựng thêm hạ tầng → đúng tiêu chí "LEAST development effort".
- Thêm CloudWatch alarm theo dõi metric **Throttles** để biết khi nào limit đang bị chạm, phục vụ giám sát.

#### Vì sao D — pick của anh — sai

**D có đúng về mặt kỹ thuật** (tách Lambda sang account riêng với SQS queue trung gian sẽ cô lập hoàn toàn concurrency pool của nó khỏi account chính) — TD explanation xác nhận cách này **khả thi**. Nhưng đề hỏi **"LEAST amount of development effort"**, và D đòi hỏi:
- Tạo **một AWS account mới**.
- Cấu hình **cross-account S3 event → SQS** (thêm policy, permission, routing).
- Deploy lại Lambda function ở account mới, cấu hình lại mọi quyền truy cập cần thiết để vẫn ghi được vào các bucket đích.

So với việc chỉ **set một con số reserved concurrency** trên function hiện có, D là một khối lượng công việc lớn hơn nhiều lần cho cùng một mục tiêu — vi phạm đúng tiêu chí "ít công sức nhất" mà đề nhấn mạnh.

#### Các phương án sai khác

- **B sai:** exponential backoff **chỉ có tác dụng SAU KHI function đã được invoke và đang chạy** — nó không ngăn được việc function chiếm slot concurrency ngay từ đầu. Backoff giải quyết retry logic khi gặp lỗi tạm thời, không giải quyết bài toán cô lập concurrency.
- **C sai:** tăng execution timeout lên 5 phút để "chờ" slot trống là hiểu sai cơ chế — trong lúc "chờ", function **vẫn đang giữ 1 slot concurrency đang chạy** (timeout không nhả slot, nó vẫn tính là 1 execution đang active cho tới khi kết thúc hoặc timeout). Cách này **làm vấn đề tệ hơn**, không giải quyết gì cả.

#### So sánh nhanh

| Phương án | Cô lập concurrency? | Development effort | Đúng cơ chế kỹ thuật? |
|---|---|---|---|
| **A. Reserved concurrency** | Có — pool riêng, cứng | Thấp nhất (1 cấu hình) | Đúng |
| B. Exponential backoff | Không thực sự ngăn chiếm slot | Trung bình (viết code) | Sai mục đích |
| C. Timeout 5 phút | Không — vẫn giữ slot khi "chờ" | Thấp nhưng vô nghĩa | Sai, làm tệ hơn |
| D. Account riêng + SQS | Có — cô lập tuyệt đối | Cao nhất | Đúng nhưng thừa effort |

#### Lưu ý thực tế

- AWS **tự động dành 100 unit concurrency chung** cho các function chưa set reserved concurrency, để đảm bảo function mới luôn có ít nhất một phần capacity — reserved concurrency của function replicate được **trừ ra từ pool chung**, phần còn lại vẫn chia sẻ bình thường cho các Lambda khác.
- Đề có nhắc "provisioned concurrency ban đầu được cân nhắc nhưng không cần" — đúng, vì provisioned concurrency dùng để **giảm cold start / đảm bảo sẵn sàng tức thời**, không liên quan tới việc **giới hạn/cô lập** concurrency; ở đây yêu cầu ngược lại — không cần tốc độ tức thời (replicate không real-time) mà cần **giới hạn** mức sử dụng.

#### Quy tắc nhớ cho thi

- **Thấy "Lambda function A ảnh hưởng tới Lambda function khác qua concurrency chung"** → **reserved concurrency** trên function A.
- **Thấy "least development effort"** → luôn ưu tiên giải pháp **chỉ cần đổi cấu hình**, tránh giải pháp phải dựng thêm hạ tầng/account mới.
- **Thấy "tăng timeout để chờ"** → sai, vì slot concurrency vẫn bị giữ trong lúc chờ.
- **Thấy "provisioned concurrency"** → dùng để giảm cold start/đảm bảo capacity sẵn sàng, **không phải** công cụ giới hạn/cô lập concurrency.

### TD explanation

Concurrency is the number of requests that your function is serving at any given time. When your function is invoked, Lambda allocates an instance of it to process the event. When the function code finishes running, it can handle another request. If the function is invoked again while a request is still being processed, another instance is allocated, which increases the function’s concurrency. Concurrency is subject to a Regional quota that is shared by all functions in a Region.
There are two types of concurrency available:
Reserved concurrency – Reserved concurrency creates a pool of requests that can only be used by its function, and also prevents its function from using unreserved concurrency.
Provisioned concurrency – Provisioned concurrency initializes a requested number of execution environments so that they are prepared to respond to your function’s invocations.
In a single account with the default concurrency limit of 1000 concurrent executions, when other services invoke Lambda function concurrently, there is the possibility for two issues to pop up:
– One or more of these services could invoke enough functions to consume a majority of the available concurrency capacity. This could cause others to be starved for it, causing failed invocations.
– A service could consume too much concurrent capacity and cause a downstream service or database to be overwhelmed, which could cause failed executions.
For Lambda functions that are launched in a VPC, you have the potential to consume the available IP addresses in a subnet or the maximum number of elastic network interfaces to which your account has access. One way to solve both of these problems is by applying a concurrency limit to the Lambda functions in an account.
You can set a concurrency limit on individual Lambda functions in an account. The concurrency limit that you set reserves a portion of your account-level concurrency for a given function. All of your functions’ concurrent executions count against this account-level limit by default.
If you set a concurrency limit for a specific function, then that function’s concurrency limit allocation is deducted from the shared pool and assigned to that specific function. AWS also reserves 100 units of concurrency for all functions that don’t have a specified concurrency limit set. This helps to make sure that future functions have the capacity to be consumed.

Therefore, the correct answer is: Configure a reserved concurrency limit for the new function to ensure that its executions will not exceed this limit. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to ensure that the concurrency limit is not being reached.
The option that says: Set the execution timeout of the new Lambda function to 5 minutes. This will allow it to wait for other Lambda function executions to finish in case the concurrency limit is reached. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to check if the concurrency limit is reached is incorrect. This will still invoke the new Lambda function and cause more problems because, during the wait time, the slice for the Lambda function is still being consumed. Other Lambda functions won’t be able to execute if all slices are consumed.
The option that says: Decouple the S3 event notifications and send the events to an Amazon SQS queue in a separate AWS account. Create the new Lambda function on this account, too. Invoke the Lambda function whenever an event message is received in the SQS queue is incorrect. This is possible, and you will have the concurrency limit on the separate AWS account for the new Lambda function. However, this only requires more work and the creation of another AWS account. Setting a concurrency limit is recommended, as it can limit the number of executions of a particular function.
The option that says: Implement an exponential backoff algorithm in the new Lambda function to ensure that it will not run if the concurrency limit is being reached. Use Amazon CloudWatch alarms to monitor the Throttles metric for Lambda functions to check if the concurrency limit is reached is incorrect. This will simply require you to write a backoff algorithm to check the concurrency limit. The function needs to execute in order to run the backoff algorithm, which defeats the purpose of limiting concurrency.

References:
https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html
https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html
https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html
https://aws.amazon.com/blogs/compute/managing-aws-lambda-function-concurrency/

Check out the AWS Lambda Cheat Sheet:
https://tutorialsdojo.com/aws-lambda/

</details>

---

# Group F — Storage, migration & ops (3)

<a id="q43"></a>

## Q43

A company is planning to migrate its workload to the AWS cloud. The solutions architect is looking to reduce the amount of time spent managing database instances from the on-premises data center by migrating to a managed relational database service in AWS such as Amazon Relational Database Service (RDS). In addition, the solutions architect plans to move the application hosted in the on-premises data center to a fully managed platform such as AWS Elastic Beanstalk. 
Which of the following is the most cost-effective migration strategy that should be implemented to meet the above requirement?

- **A.** Replatform
- **B.** Refactor / Re-architect
- **C.** Rehost
- **D.** Repurchase

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** C

🔑 **Key words:** DB to RDS + app to Elastic Beanstalk; most cost-effective strategy

🪤 **Your trap:** Rehost = lift-and-shift to EC2 unchanged

🧠 **Rule:** Move to managed platforms (RDS, Beanstalk) without code rewrite → Replatform.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises data center                 AWS Cloud
┌─────────────────────┐                 ┌─────────────────────┐
│ Database tự quản lý  │   ─migrate──►  │ Amazon RDS (managed) │
│ Application tự host  │   ─migrate──►  │ AWS Elastic Beanstalk │
└─────────────────────┘                 └─────────────────────┘
        Mục tiêu: giảm thời gian quản lý DB instance
        Yêu cầu: chiến lược di cư CHI PHÍ THẤP NHẤT
```

Đáp án đúng: **A (Replatform)**. Anh chọn **C (Rehost)** — nghe có vẻ "đơn giản = rẻ", nhưng không khớp với việc **đổi sang dịch vụ managed** (RDS, Beanstalk).

#### Vì sao A đúng

**Replatform ("lift, tinker and shift")** là di cư có **tinh chỉnh vừa đủ** để tận dụng lợi ích cloud, nhưng **không đổi kiến trúc lõi** của ứng dụng. Đây chính xác là những gì đề mô tả:

```
Database tự quản  →  [tinker: đổi engine/kết nối cho phù hợp]  →  Amazon RDS
Application tự host →  [tinker: đóng gói lại để Beanstalk quản lý]  →  Elastic Beanstalk
```

Không viết lại logic nghiệp vụ, không đổi ngôn ngữ/kiến trúc — chỉ "tinh chỉnh" vừa đủ để chuyển sang nền tảng managed. Kết quả: giảm được công sức vận hành DB (RDS tự lo backup, patching, failover) mà **không phải trả chi phí re-architect toàn bộ hệ thống**.

#### Vì sao C (lựa chọn của Anh) sai — Rehost không đổi gì cả

**Rehost ("lift and shift")** nghĩa là chuyển nguyên trạng — ví dụ cài database lên EC2 y hệt cấu hình on-premises, **không dùng RDS**, không dùng Beanstalk. Nó nhanh và phù hợp khi mục tiêu là "di chuyển gấp, đúng deadline kinh doanh", nhưng đề bài yêu cầu rõ **"managed relational database service" và "fully managed platform"** — hai thứ Rehost không cung cấp. Nếu dùng Rehost rồi sau đó mới chuyển tiếp sang RDS/Beanstalk, thực chất bạn đang làm **thêm một bước Replatform nữa**, tốn thời gian + chi phí hơn so với đi thẳng vào Replatform ngay từ đầu.

#### Các lựa chọn sai còn lại

- **B — Refactor / Re-architect:** chỉ cần khi có **nhu cầu kinh doanh mạnh** để thêm tính năng/scale/performance mà kiến trúc hiện tại không đáp ứng được. Đây là chiến lược **tốn nhiều chi phí nhất** trong 6 chiến lược vì phải viết lại/tái kiến trúc, không phù hợp khi mục tiêu chỉ là "giảm công sức quản lý DB".
- **D — Repurchase:** nghĩa là đổi sang **sản phẩm/license khác hẳn** ("drop and shop", ví dụ chuyển từ Oracle sang SaaS khác). Đề không hề nói tới việc đổi sản phẩm hay mô hình license, nên không liên quan.

| Chiến lược | Đặc điểm | Phù hợp với đề? |
|---|---|---|
| **A. Replatform (đúng)** | Tinh chỉnh vừa đủ để lên managed service, không đổi kiến trúc | Có — đúng với RDS + Beanstalk |
| C. Rehost (Anh chọn) | Chuyển nguyên trạng, không đổi gì | Không — không dùng managed service |
| B. Refactor | Viết lại/tái kiến trúc, chi phí cao nhất | Không — không có nhu cầu đổi tính năng/scale |
| D. Repurchase | Đổi sang sản phẩm/license khác | Không — không liên quan |

#### Lưu ý thực tế

- 6 chiến lược di cư ("6 R's") của AWS: **Rehost, Replatform, Repurchase, Refactor/Re-architect, Retire, Retain**. Đề thi SAP hay cho tình huống có từ khóa gợi ý managed service (RDS, Beanstalk, Fargate...) để kiểm tra khả năng nhận diện **Replatform**.
- Phân biệt nhanh: Rehost = "y chang, chỉ đổi hạ tầng chạy"; Replatform = "y chang + vài tinh chỉnh để tận dụng managed service"; Refactor = "thiết kế lại hẳn vì nhu cầu business mới".

#### Quy tắc nhớ cho thi

- **"Chuyển sang RDS / Elastic Beanstalk / Fargate, không đổi kiến trúc core, cost-effective"** → **Replatform**.
- **"Nhanh nhất, deadline gấp, không đổi gì cả"** → **Rehost**.
- **"Cần thêm tính năng/scale/performance mà kiến trúc cũ không đáp ứng"** → **Refactor/Re-architect**.
- **"Đổi hẳn sang sản phẩm/license khác"** → **Repurchase**.

### TD explanation

Organizations usually begin to think about how they will migrate an application during Phase 2 (Portfolio Discovery and Planning) of the migration process. This is when you determine what is in your environment and the migration strategy for each application. The six approaches detailed below are common migration strategies employed and build upon “The 5 R’s” that Gartner Inc, a global research and advisory firm, outlined in 2011.
You should gain a thorough understanding of which migration strategy will be best suited for certain portions of your portfolio. It is also important to consider that while one of the six strategies may be best for migrating certain applications in a given portfolio, another strategy might work better for moving different applications in the same portfolio.

1. Rehost (“lift and shift”) – In a large legacy migration scenario where the organization is looking to quickly implement its migration and scale to meet a business case, we find that the majority of applications are rehosted.
2. Replatform (“lift, tinker and shift”) – This entails making a few cloud optimizations in order to achieve some tangible benefit without changing the core architecture of the application.
3. Repurchase (“drop and shop”) – This is a decision to move to a different product and likely means your organization is willing to change the existing licensing model you have been using. For workloads that can easily be upgraded to newer versions, this strategy might allow a feature set upgrade and smoother implementation.
4. Refactor / Re-architect – Typically, this is driven by a strong business need to add features, scale, or performance that would otherwise be difficult to achieve in the application’s existing environment.
5. Retire – Identifying IT assets that are no longer useful and can be turned off will help boost your business case and direct your attention towards maintaining the resources that are widely used.
6. Retain – You may want to retain portions of your IT portfolio because there are some applications that you are not ready to migrate and feel more comfortable keeping them on-premises, or you are not ready to prioritize an application that was recently upgraded and then make changes to it again.
Therefore, the correct answer is: Replatform. This strategy is done by making a few cloud optimizations on your existing systems before migrating them to AWS, which is what will happen if you move your existing database and web applications to AWS. This strategy is more suitable when you want to reduce the amount of time you spend managing database instances by migrating to a managed relational database service such as Amazon Relational Database Service (RDS), or migrating your application to a fully managed platform like AWS Elastic Beanstalk.
Rehost is incorrect. Rehost (“lift and shift”) strategy is more suitable for quickly migrating the systems to AWS to meet a certain business case without no additional configuration involved. Take note that if you migrate your systems to either Elastic Beanstalk or RDS, you will still need to set up, configure, and test your systems, which takes additional time and effort.
Repurchase is incorrect. This strategy entails a decision to move to a different product and likely means your organization is willing to change the existing licensing model you have been using. Hence, this is not a suitable migration strategy for this scenario.
Refactor / Re-architect is incorrect. This strategy is suitable if there is a strong business need to add features, scale, or performance that would otherwise be difficult to achieve in the application’s existing environment. This type of migration strategy also entails additional cost, compared with the Replatform strategy, since you are allocating time, effort, and budget to optimize your systems.

References:
https://aws.amazon.com/cloud-migration/
https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/
https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-migration/planning-phase.html

Tutorials Dojo’s AWS Certified Solutions Architect Professional Exam Study Guide:
https://tutorialsdojo.com/aws-certified-solutions-architect-professional/

</details>

<a id="q56"></a>

## Q56

A global enterprise web application is using a private S3 bucket, named MANILATECH-CONFIG, which has Server-Side Encryption with Amazon S3-Managed Encryption Keys (SSE-S3) to store its configuration files for different regions in North America, Latin America, Europe, and Asia. There has been a lot of database changes and feature toggle switching for the past few weeks. Your CTO assigned you the task of enabling versioning on this bucket to track any changes made to the configuration files and have the ability to use the old settings if needed. In the coming days ahead, a new region in Oceania will be supported by the web application and thus, a new configuration file will be added soon. Currently, there are already four files in the bucket, namely: MNL-NA.config, MNL-LA.config, MNL-EUR.config, and MNL-ASIA.config which are updated regularly. As instructed, you enabled the versioning in the bucket and after a few days, the new MNL-O.config configuration file for the Oceania region has been uploaded. A week after, a configuration has been done on MNL-NA.config, MNL-LA.config, and MNL-O.config files. 
In this scenario, which of the following is correct about files inside the MANILATECH-CONFIG S3 bucket? (Select TWO.)

- **A.** The first Version ID of MNL-NA.config and MNL-LA.config has a value of 1.
- **B.** The MNL-EUR.config and MNL-ASIA.config files will have a Version ID of null.
- **C.** The MNL-EUR.config and MNL-ASIA.config files will have a Version ID of 1.
- **D.** There would be two available versions for each of the MNL-NA.config, MNL-LA.config, and MNL-O.config files. The first Version ID of MNL-NA.config and MNL-LA.config has a value of null.
- **E.** The latest Version ID of MNL-NA.config and MNL-LA.config has a value of null.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** B, D · **You picked:** A, E

🔑 **Key words:** versioning enabled after 4 files existed; later updates (Select TWO)

🪤 **Your trap:** Version IDs are never '1'; pre-existing objects keep null

🧠 **Rule:** Objects existing before versioning → version ID null; new versions → random alphanumeric IDs.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Thời điểm 0: bucket MANILATECH-CONFIG đã có 4 file (chưa bật Versioning)
   MNL-NA.config  MNL-LA.config  MNL-EUR.config  MNL-ASIA.config

Thời điểm 1: BẬT VERSIONING
   → 4 file cũ đều nhận Version ID = null (vì đã tồn tại từ trước)

Thời điểm 2: upload file MỚI
   MNL-O.config  → version đầu tiên là ID alphanumeric (vì tạo SAU khi bật versioning)

Thời điểm 3: update 3 file
   MNL-NA.config, MNL-LA.config, MNL-O.config  → có thêm version mới (alphanumeric)
   MNL-EUR.config, MNL-ASIA.config  → KHÔNG đổi gì, vẫn giữ nguyên version null
```

Chọn **HAI** đáp án đúng. Đáp án đúng: **B + D**. Anh chọn **A + E** — cả hai pick đều hiểu sai cách S3 Versioning gán Version ID.

#### Vì sao B đúng — file không bị update giữ nguyên null

**B: "MNL-EUR.config và MNL-ASIA.config sẽ có Version ID = null."** Đúng, vì quy tắc là: **object tồn tại TRƯỚC khi Versioning được bật sẽ nhận Version ID = null**, và **chỉ khi có một update mới** thì mới phát sinh version alphanumeric tiếp theo. Hai file EUR và ASIA **không hề bị động tới** ở bước update sau cùng (đề chỉ nói NA, LA, O được update), nên chúng vẫn giữ nguyên trạng thái ban đầu: version ID null, không có version thứ hai.

#### Vì sao D đúng — NA/LA/O có đúng 2 version, bắt đầu từ null

**D: "Có hai version cho mỗi file NA, LA, O. Version đầu tiên của NA và LA có giá trị null."** Phân tích từng file:

- **MNL-NA.config, MNL-LA.config:** đã tồn tại trước khi bật Versioning → version đầu = **null**. Sau đó bị update 1 lần → version thứ hai = alphanumeric. Tổng: **2 version**, cái đầu null.
- **MNL-O.config:** được tạo **sau khi** Versioning đã bật → version đầu tiên của nó đã là alphanumeric (không phải null) ngay từ lúc upload. Sau đó bị update thêm 1 lần → có version alphanumeric thứ hai. Tổng: **2 version**, nhưng cả 2 đều alphanumeric (không có null).

D gộp đúng cả 3 file vào "2 version mỗi file", và chính xác hóa riêng phần "version đầu = null" chỉ áp dụng cho NA/LA (không áp dụng cho O) — đây là điểm tinh tế D diễn đạt đúng.

#### Vì sao A (lựa chọn của Anh) sai — Version ID không bao giờ là số nguyên

**A: "Version đầu tiên của NA và LA có giá trị = 1."** Sai hoàn toàn về bản chất: S3 Version ID **không phải số đếm tuần tự (1, 2, 3...)** — nó hoặc là **null** (object có trước khi versioning bật) hoặc là một **chuỗi alphanumeric ngẫu nhiên** do S3 tự sinh (ví dụ `3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`). Không có khái niệm "version số 1" kiểu đếm số nguyên trong S3.

#### Vì sao E (lựa chọn của Anh) sai — nhầm lẫn version đầu và version mới nhất

**E: "Version mới nhất của NA và LA có giá trị null."** Sai vì NA và LA **đã bị update** sau khi versioning bật → chúng có version mới hơn (alphanumeric) đè lên. **null chỉ là version ĐẦU TIÊN (cũ nhất)**, còn **version MỚI NHẤT (latest)** của NA/LA phải là bản alphanumeric vừa tạo ra ở lần update sau cùng. Đây là lỗi nhầm giữa "version đầu" và "version mới nhất".

#### Lựa chọn sai còn lại

- **C — "EUR và ASIA có Version ID = 1":** sai hai lần — vừa sai về việc hai file này không bị động tới (Version ID vẫn null, không đổi), vừa sai về việc Version ID là số nguyên "1".

| Phát biểu | Đúng/Sai | Vì sao |
|---|---|---|
| **B (đúng)** | Đúng | EUR/ASIA không update → giữ nguyên null |
| **D (đúng)** | Đúng | NA/LA/O có 2 version; version đầu của NA/LA là null |
| A (Anh chọn) | Sai | Version ID không phải số "1" |
| E (Anh chọn) | Sai | Nhầm "version đầu = null" với "version mới nhất = null" |
| C | Sai | Vừa sai file, vừa sai định dạng ID |

#### Lưu ý thực tế

- Khi bật Versioning, **chỉ những object được tạo/update SAU thời điểm bật** mới nhận Version ID alphanumeric; mọi object có sẵn trước đó giữ **null** cho tới khi chúng được ghi đè lần đầu.
- "null" cũng là giá trị hợp lệ để **GET/DELETE** chỉ định chính version đó — không phải placeholder vô nghĩa.

#### Quy tắc nhớ cho thi

- **"Object có trước khi bật Versioning"** → Version ID đầu tiên = **null**.
- **"Object tạo/update sau khi bật Versioning"** → Version ID = **chuỗi alphanumeric ngẫu nhiên**, không bao giờ là số đếm (1, 2, 3...).
- **"Version mới nhất" ≠ "Version đầu tiên"** — object bị update thì latest luôn là bản mới hơn (alphanumeric), còn version null (nếu có) chỉ nằm ở vị trí cũ nhất trong lịch sử.

### TD explanation

Versioning is a means of keeping multiple variants of an object in the same bucket. You can use versioning to preserve, retrieve, and restore every version of every object stored in your Amazon S3 bucket. With versioning, you can easily recover from both unintended user actions and application failures.
In this scenario, we have an initial 4 files in the MANILATECH-CONFIG bucket: MNL-NA.config, MNL-LA.config, MNL-EUR.config, and MNL-ASIA.config. Then, the Versioning feature was enabled which caused all of the 4 existing files to have a Version ID of null. This new configuration will enable the new files that will be added to have an alphanumeric VERSION ID, as well as any new updates for the first 4 files. Hence, when a new MNL-O.config configuration file was added, its Version ID was an alphanumeric key since this file was uploaded after the Versioning feature was enabled.
A week after, a new update has been done on the 3 configuration files only (MNL-NA.config, MNL-LA.config, and MNL-O.config files). Take note that at this point, there are NO changes made on the MNL-EUR.config and MNL-ASIA.config files, which is why their first (and latest) version ID will still remain as null since there were no new updates made yet.
However, for MNL-NA.config and MNL-LA.config, it has the first Version ID of null and then the second Version ID would be an alphanumeric key. For the MNL-O.config file, the first Version ID is already an alphanumeric key since this file was created after the Versioning was enabled.
Therefore, the correct answers are:
– There would be two available versions for each of the MNL-NA.config, MNL-LA.config, and MNL-O.config files. The first Version ID of MNL-NA.config and MNL-LA.config has a value of null.
– The MNL-EUR.config and MNL-ASIA.config files will have a Version ID of null

The option that says: The first Version ID of MNL-NA.config and MNL-LA.config has a value of 1 is incorrect. The first VERSION ID of these files would be null since they were already existing when the S3 Versioning was enabled.
The option that says: The MNL-EUR.config and MNL-ASIA.config files will have a Version ID of 1 is incorrect because the Version ID for these files is null.
The option that says: The latest Version ID of MNL-NA.config and MNL-LA.config has a value of null is incorrect because the latest VERSION ID value for these 2 files would be an alphanumeric value and not null.

References:
https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html
https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectVersioning.html
https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html

Check out this Amazon S3 Cheat Sheet:
https://tutorialsdojo.com/amazon-s3/

</details>

<a id="q67"></a>

## Q67

A company is migrating a legacy Oracle database from its on-premises data center to AWS. It will be deployed in an existing Amazon EBS backed Amazon EC2 instance with multiple EBS volumes attached. For the migration, a new volume must be created for the Oracle database and then attached to the instance. This will be used by a financial web application and will primarily store historical financial data that are infrequently accessed. The company is also considering using Amazon GuardDuty to monitor its AWS environment for security threats.
Which of the following is the MOST cost-effective and throughput-oriented solution that the Solutions Architect should implement?

- **A.** Migrate the database using the AWS Database Migration Service and use a Cold HDD (sc1) EBS volume.
- **B.** Migrate the database using the AWS Database Migration Service and use a Provisioned IOPS (io1) EBS volume.
- **C.** Migrate the database using the AWS Transform MGN and use a General Purpose (gp2) EBS Volume.
- **D.** Migrate the database using the AWS Transform MGN and use a Throughput Optimized (st1) EBS volume.

<details>
<summary><b>Answer & explanation</b></summary>

**Correct:** A · **You picked:** B

🔑 **Key words:** infrequently accessed historical data; most cost-effective, throughput-oriented

🪤 **Your trap:** io1 = most expensive SSD

🧠 **Rule:** High IOPS → io1/io2; frequent throughput → st1; infrequent + cheapest → sc1.

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
On-premises Oracle DB                 EC2 instance (EBS-backed)
┌─────────────────────┐               ┌─────────────────────────┐
│ Legacy Oracle DB      │  ─migrate──► │ + EBS volume mới cho DB  │
└─────────────────────┘               └─────────────────────────┘

Dữ liệu: tài chính, LỊCH SỬ, ÍT TRUY CẬP (infrequently accessed)
Yêu cầu: giải pháp RẺ NHẤT + hướng THROUGHPUT (không phải IOPS cao)
```

Đáp án đúng: **A (DMS + Cold HDD sc1)**. Anh chọn **B (DMS + Provisioned IOPS io1)** — chọn đúng công cụ migrate nhưng sai loại volume, vì io1 là SSD đắt nhất, không phù hợp với dữ liệu ít truy cập.

#### Vì sao A đúng

Hai phần của đáp án A đều khớp với yêu cầu:

1. **AWS DMS** đúng công cụ: DMS dùng để migrate **database** (Oracle → Oracle hoặc sang engine khác) trong khi nguồn vẫn hoạt động bình thường, giảm downtime. Đây chính xác là bài toán — "migrate legacy Oracle database".
2. **Cold HDD (sc1)** đúng loại volume: sc1 là loại **EBS rẻ nhất**, được thiết kế riêng cho **throughput** (không phải IOPS) và cho **dữ liệu lớn, tuần tự, ít truy cập** (less frequently accessed workloads) — khớp 100% với mô tả "historical financial data that are infrequently accessed" và yêu cầu "most cost-effective and throughput-oriented".

```
sc1 (Cold HDD): rẻ nhất, throughput-based, dữ liệu lạnh/ít đọc  ← khớp đề
st1 (Throughput Optimized HDD): throughput-based, nhưng cho dữ liệu NÓNG/truy cập thường xuyên
gp2 (General Purpose SSD): đa dụng, không tối ưu riêng cho throughput hay chi phí thấp nhất
io1 (Provisioned IOPS SSD): đắt nhất, cho workload cần IOPS cao, độ trễ thấp
```

#### Vì sao B (lựa chọn của Anh) sai

B cũng dùng đúng **AWS DMS**, nhưng chọn **Provisioned IOPS (io1)** — đây là loại volume **SSD cao cấp nhất, đắt nhất**, thiết kế cho workload **mission-critical, cần độ trễ thấp hoặc throughput/IOPS rất cao và ổn định** (ví dụ database giao dịch OLTP tần suất cao). Dữ liệu trong đề là **historical, infrequently accessed** — hoàn toàn ngược lại với use-case của io1. Chọn io1 ở đây vừa **tốn kém không cần thiết**, vừa đi ngược yêu cầu "most cost-effective" của đề.

#### Các lựa chọn sai còn lại

- **D — AWS Transform MGN + Throughput Optimized (st1):** sai ở cả hai vế. Công cụ migrate-service-dùng-để-chuyển-máy-ảo (MGN) chỉ dùng để migrate **máy ảo on-premises** (VMware vSphere, Hyper-V, Azure) sang EC2, **không phải** công cụ để migrate một **database** như Oracle — phải dùng AWS DMS. Về volume, st1 tuy rẻ hơn SSD nhưng được thiết kế cho workload **truy cập thường xuyên** (frequently accessed, throughput-intensive), không hợp với dữ liệu "infrequently accessed" trong đề — sc1 mới đúng.
- **C — AWS Transform MGN + gp2:** cũng sai công cụ migrate (phải là DMS, không phải MGN cho database), và gp2 là SSD đa dụng, chi phí cao hơn HDD, không phải lựa chọn rẻ nhất cho dữ liệu lạnh.

| Lựa chọn | Công cụ migrate | Volume | Vấn đề |
|---|---|---|---|
| **A (đúng)** | AWS DMS | Cold HDD (sc1) | — |
| B (Anh chọn) | AWS DMS | Provisioned IOPS (io1) | io1 đắt nhất, sai use-case |
| C | AWS Transform MGN | gp2 | Sai công cụ (migrate máy ảo, không phải DB) + gp2 không rẻ nhất |
| D | AWS Transform MGN | Throughput Optimized (st1) | Sai công cụ + st1 dành cho dữ liệu "nóng" |

#### Lưu ý thực tế

- Phân biệt nhanh 4 loại EBS phổ biến trong đề SAP: **gp2/gp3** (đa dụng, boot volume), **io1/io2** (IOPS cao, mission-critical, đắt nhất), **st1** (throughput cao, dữ liệu truy cập thường xuyên như big data/log), **sc1** (rẻ nhất, throughput thấp hơn st1, dành cho dữ liệu lạnh/ít truy cập). Bootable volume **không hỗ trợ** trên st1/sc1.
- Công cụ migrate: **AWS DMS** cho database; **AWS Application Migration Service (MGN)** cho máy chủ/máy ảo nguyên khối (lift-and-shift server-level).

#### Quy tắc nhớ cho thi

- **"Migrate database (Oracle, MySQL, SQL Server…)"** → **AWS DMS**, không phải MGN.
- **"Migrate nguyên server/VM từ on-prem"** → AWS Application Migration Service (MGN).
- **"Dữ liệu lạnh, ít truy cập, cần rẻ nhất, throughput-oriented"** → **Cold HDD (sc1)**.
- **"Dữ liệu nóng, truy cập thường xuyên, throughput-oriented"** → Throughput Optimized HDD (st1).
- **"Cần IOPS cao, độ trễ thấp, mission-critical"** → Provisioned IOPS (io1/io2) — đắt nhất, không phải lựa chọn "cost-effective".

### TD explanation

AWS Database Migration Service helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database.
The AWS Database Migration Service can migrate your data to and from the most widely used commercial and open-source databases. AWS Database Migration Service supports homogeneous migrations such as Oracle to Oracle, as well as heterogeneous migrations between different database platforms, such as Oracle or Microsoft SQL Server to Amazon Aurora. With AWS Database Migration Service, you can continuously replicate your data with high availability and consolidate databases into a petabyte-scale data warehouse by streaming data to Amazon Redshift and Amazon S3.

Cold HDD volumes provide low-cost magnetic storage that defines performance in terms of throughput rather than IOPS. With a lower throughput limit than Throughput Optimized HDD, this is a good fit ideal for large, sequential cold-data workloads. If you require infrequent access to your data and are looking to save costs, Cold HDD provides inexpensive block storage. Take note that bootable Cold HDD volumes are not supported.
Cold HDD provides the lowest cost HDD volume and is designed for less frequently accessed workloads. Therefore, the correct answer is: Migrate the database using the AWS Database Migration Service and use a Cold HDD (sc1) EBS volume.
The option that says: Migrate the database using the AWS Database Migration Service and use a Provisioned IOPS (io1) EBS volume is incorrect because it costs more than the Cold HDD and thus, not cost-effective for this scenario. It provides the highest performance SSD volume for mission-critical low-latency or high-throughput workloads, which is not needed in the scenario.
The option that says: Migrate the database using the AWS Transform MGN and use a Throughput Optimized (st1) EBS volume is incorrect. Although it is cheaper than SSD, it is primarily designed and used for frequently accessed throughput-intensive workloads. Cold HDD perfectly fits the description as it is used for their infrequently accessed data and provides the lowest cost, unlike Throughput Optimized HDD. In addition, the AWS Transform MGN is primarily used to migrate on-premises virtual machines from VMware vSphere, Windows Hyper-V, or Microsoft Azure only. You have to use the AWS Database Migration Service instead in this situation.
The option that says: Migrate the database using the AWS Transform MGN and use a General Purpose (gp2) EBS Volume is incorrect because a General purpose SSD volume costs more and it is mainly used for a wide variety of workloads. It is recommended to be used as system boot volumes, virtual desktops, low-latency interactive apps, and many more. Moreover, you have to use the AWS Database Migration Service instead in this scenario and not AWS Transform MGN.

References:
https://aws.amazon.com/ebs/details/
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html
https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.html

Check out this Amazon EBS Cheat Sheet:
https://tutorialsdojo.com/amazon-ebs/

</details>
