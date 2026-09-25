# Vietnamese Explanation Style (🇻🇳 Phân tích chi tiết)

Style guide for per-question Vietnamese deep-dive explanations appended to test review files
(`test-review-flow.md`, `--vi` flag). Also usable on demand for any single question the user asks about.

## Format rules

- Fragment file per question: `Q{n}.md`, first line exactly `### 🇻🇳 Phân tích chi tiết`
- Subsections use `####` only — never `#`/`##`, no other `###` (merge script rejects them)
- Balanced code fences; ASCII diagrams go inside ``` blocks
- Length ~50–130 lines; no filler

## Sections (adapt to the question)

1. `#### Tình huống` — ASCII diagram of the scenario + the deciding requirement (e.g. "downtime ÍT NHẤT"),
   then one line: correct answer vs what the learner picked ("Anh chọn …")
2. Correct option(s) — why they fit the requirement words; for multi-select, show how picks form ONE solution
3. Learner's pick — why it looked right and exactly why it fails
4. Every other wrong option — one short reason each
5. Comparison table when options differ on one axis (speed, cost, ops overhead, RTO…)
6. `#### Lưu ý thực tế` — only real exam-adjacent traps (KMS keys cross-account, service limits…)
7. `#### Quy tắc nhớ cho thi` — bullets "**Thấy X** → **Y**"; mnemonic for repeat mistakes

## Tone

- Vietnamese prose, address learner as "Anh"
- Keep AWS service names, API names, console settings and exam keywords in English
- Callouts: `⚠️ Lỗi lặp lại` for concepts already missed before (check weak areas in progress/drill files);
  `📝 Ghi chú kỹ thuật` when the exam option wording differs from real-world behavior

## Accuracy rules (critical)

- Ground every claim in the TD explanation (verbatim in the review file) + well-established AWS facts
- Never contradict the `**Correct:**` answer
- No invented limits, prices, feature names; if unsure, omit
- When exam wording diverges from reality, keep the exam answer and add a `📝 Ghi chú kỹ thuật` note

## Example (TD Set 5 Q36)

### 🇻🇳 Phân tích chi tiết

#### Tình huống

```
Source Account                       Target Account
┌───────────────────────┐            ┌───────────────────────┐
│ Lambda (ZIP trên S3)  │   ──────►  │ Lambda ?              │
│ Aurora MySQL cluster  │   ──────►  │ Aurora MySQL ?        │
└───────────────────────┘            └───────────────────────┘
        Cùng Organization, cùng Region
        Yêu cầu: downtime ÍT NHẤT
```

Phải chọn **một cách cho Lambda** và **một cách cho Aurora**. Đáp án đúng: **A (Aurora clone qua RAM)** + **D (tạo lại Lambda từ ZIP)**. Anh chọn đúng D, sai ở phần database (chọn E – snapshot).

#### Phần Lambda — D đúng, C sai

**C sai vì Lambda không chia sẻ được qua RAM.** RAM chỉ hỗ trợ một danh sách resource nhất định (subnet, Transit Gateway, Route 53 Resolver rules, License Manager, Aurora DB cluster…). Lambda function không nằm trong danh sách. Hơn nữa, "share" không phải "migrate" — function vẫn thuộc account nguồn.

**D đúng** vì Lambda thực chất chỉ là code + cấu hình. Code đã có sẵn trong file ZIP:

```
Tải ZIP từ S3 account nguồn
    → upload vào S3 bucket account đích
    → create-function trong account đích, trỏ đến ZIP đó
    → tạo lại execution role, env vars, trigger, VPC config
```

#### Phần Aurora — Vì sao Clone (A) nhanh hơn Snapshot (E)

Mấu chốt là hiểu **Aurora tách compute và storage** (storage phân tán 6 bản copy trên 3 AZ).

**Aurora Clone — copy-on-write:**

```
Cluster nguồn                      Clone (account đích)
     │                                  │
     └──────────► Storage volume ◄──────┘
                  (DÙNG CHUNG các trang dữ liệu)

Lúc tạo clone:
    → Không copy data
    → Tạo xong nhanh, KHÔNG phụ thuộc kích thước DB
Sau đó:
    → Bên nào ghi thay đổi thì mới tạo trang mới riêng cho bên đó
```

Cross-account clone: account nguồn **share cluster qua RAM** cho account đích → account đích tạo clone từ cluster được share. (RAM cũng share được cho account ngoài Organization, nhưng khi đó account đích phải chấp nhận lời mời; trong cùng Organization thì đơn giản hơn.)

**Snapshot share + restore (E):** tạo snapshot → share → restore thành cluster mới với volume mới → chậm hơn clone. Snapshot phù hợp hơn khi cần **cross-region** hoặc backup lâu dài; clone chỉ trong cùng region.

**mysqldump (B) chậm nhất:** export/import logic từng câu lệnh; `--single-transaction` cho bản dump nhất quán nhưng dữ liệu ghi sau đó vẫn bị thiếu → vẫn phải dừng ghi khi cutover.

| Cách | Cơ chế | Tốc độ | Phụ thuộc kích thước DB |
|---|---|---|---|
| **A. Clone qua RAM** | Copy-on-write, dùng chung storage | Nhanh nhất | Không |
| E. Snapshot + restore | Chụp → share → dựng cluster mới | Trung bình | Có |
| B. mysqldump | Export/import logic | Chậm nhất | Rất nhiều |

#### Lưu ý thực tế (đề không hỏi nhưng dễ vấp)

- **Mã hóa KMS:** cluster/snapshot mã hóa bằng **AWS managed key (aws/rds)** không share cross-account được → phải dùng **customer managed key** và cấp quyền key cho account đích.
- **Clone là bản chụp tại một thời điểm:** cutover thực tế: dừng ghi ngắn → clone → trỏ Lambda mới vào clone. Cần gần zero downtime → thêm **binlog replication** từ nguồn sang clone rồi mới cắt chuyển.

#### Quy tắc nhớ cho thi

- **"copy Aurora sang account khác, cùng region, nhanh nhất"** → **share cluster qua RAM + Aurora clone**
- **"cross-region" / "long-term backup"** → **snapshot**
- **"mysqldump / pg_dump"** → gần như luôn là đáp án chậm nhất
- **"share Lambda via RAM"** → sai, RAM không hỗ trợ Lambda
- **"encrypted cross-account"** → cần **customer managed KMS key**
