# SAP-C02 — Mẹo đọc đề, chọn đáp án và quản lý thời gian (210 phút ESL)

> Cập nhật 2026-10-28. Dựa trên lỗi thật của bạn:
> - Neal A/B **đều hết giờ**, 1/3 cuối đề chỉ đúng **16/25**.
> - Neal B: câu 1 đáp án chỉ đúng **67%**, **6/7 câu cắm cờ dồn ở Q69–74**.
> - Nhóm D (đọc sót đề, làm vội) chiếm 4/20 câu sai.
>
> Xem thêm: [rule-sheet.md §0](rule-sheet.md) (7 quy tắc đọc đề).

---

## 1. Quản lý thời gian — rủi ro số 1

### Các mốc cần đạt (75 câu / 210 phút)

| Mốc | Phút | Còn lại |
|---|---|---|
| Xong **câu 25** | ≤ **60'** | 150' |
| Xong **câu 50** | ≤ **125'** | 85' |
| Xong **câu 75** | ≤ **185'** | **25' để xem lại câu cắm cờ** |

- Trung bình **2,5 phút/câu**. Câu ngắn làm trong 1–1,5 phút để dành thời gian cho câu dài.
- Mỗi lần qua một mốc, liếc đồng hồ. **Chậm hơn 5 phút** thì 5 câu tiếp theo đi nhanh hơn: bắt từ khóa, loại phương án, chọn rồi đi tiếp.

### Quy tắc 2 phút
- Sau **2 phút** mà vẫn phân vân giữa 2 phương án: **chọn phương án đang nghiêng về, cắm cờ, sang câu tiếp**. Không có câu nào đáng giá hơn 4 phút.
- **Không bao giờ để trống.** Sai không bị trừ điểm, và câu đã cắm cờ cũng phải có đáp án tạm.
- Khi xem lại câu cắm cờ, **chỉ đổi đáp án khi tìm ra lý do mới**, ví dụ phát hiện một từ khóa đã đọc sót. Đừng đổi chỉ vì cảm giác.

### Không để dồn ở cuối đề
- Ở phút ~100, **nhắm mắt 30 giây và thở sâu**. Không cần nghỉ dài, chỉ để đầu óc tỉnh lại.
- **Cắm cờ ít thôi:** chỉ những câu thật sự phân vân, khoảng 8–10 câu. Cắm 20 câu thì 25 phút xem lại không đủ.

---

## 2. Cách đọc đề — 4 bước, khoảng 40–60 giây

**Bước 1. Đọc câu hỏi cuối trước.** Ví dụ "Which solution… **MOST cost-effective** / **LEAST operational overhead**?" Câu này cho biết bạn đang tìm gì trước khi đọc đoạn mô tả dài.

**Bước 2. Tìm từ khóa ràng buộc.** Đây là thứ quyết định chọn giữa 2 phương án cùng chạy được:

| Từ khóa | Nghĩa là chọn |
|---|---|
| least operational overhead | Dịch vụ managed / serverless, không tự dựng |
| most cost-effective | Rẻ nhất mà **vẫn đáp ứng mọi yêu cầu**. Spot chỉ dùng cho việc chịu được gián đoạn |
| minimal changes / no code changes | Rehost / replatform, không viết lại |
| quickest / urgent | Giải pháp đơn giản nhất, đừng làm quá tay |
| prevent / enforce | SCP / IAM deny (chặn trước) |
| detect / don't block | Config rule + remediation (phát hiện sau) |
| fastest transfer | Tính dung lượng ÷ băng thông trước (1 Gbps ≈ 10 TB/ngày) |

**Bước 3. Gạch các yêu cầu cứng** trên giấy hoặc whiteboard, viết tắt 2–4 ý. Ví dụ: `3 AZ · read-heavy · EU+US · 99.9`. Đề SAP hay giấu một yêu cầu ở giữa đoạn, chẳng hạn "existing on-prem AD", "must not traverse internet", "no SSH keys".

**Bước 4. Để ý từ phủ định và giới hạn phạm vi:** NOT, EXCEPT, *only*, *existing*, *within the Region*, *across accounts*. Các câu Q41 và Q68–74 của Neal B thuộc dạng này.

---

## 3. Cách chọn đáp án

### Loại phương án trước, chọn sau
Gặp các dấu hiệu sau thì **loại ngay**:
- **Tính năng không tồn tại:** "global Lambda functions", "DocumentDB table in front of Aurora", Global Accelerator đứng trước S3.
- **Thao tác thủ công** khi đề đòi tự động hóa: "manually create accounts", "SSH in and run…".
- **Tự dựng** (EC2 + cron + script) trong khi có dịch vụ managed làm được: Macie, Patch Manager, Transfer Family, Batch.
- **Làm quá tay:** dùng multi-Region / Global Database khi đề chỉ cần nhiều AZ (Neal B Q63); dùng Step Functions cho từng job đơn lẻ (thẻ E8).
- **Một mệnh đề sai là loại cả phương án.** Một phương án đúng 3 ý nhưng sai 1 ý vẫn là phương án sai.

### Hai phương án gần giống nhau
Khi 2 phương án giống nhau gần hết, **chỉ so cụm từ khác nhau** (IA hay Deep Archive, public hay VPC endpoint, ALB hay NLB, account nào). Không đọc lại toàn bộ.

### Câu chọn 2–3 đáp án
- "Which **combination of steps**…": các lựa chọn là **các bước của cùng một giải pháp**, phải ghép lại chạy được với nhau.
- "Which **solutions** meet…": **mỗi lựa chọn phải tự đáp ứng được đề**.
- Chọn được phương án chắc chắn rồi thì **thử từng phương án còn lại với từng yêu cầu**. Ở Neal A, 8/9 câu nhiều đáp án sai là do chỉ đúng một nửa.

### Câu một đáp án (Neal B 67%)
Trước khi bấm, tự hỏi: **"Phương án này đáp ứng TỪ KHÓA RÀNG BUỘC chưa?"** Nếu 2 phương án đều chạy được, phương án đúng là phương án thắng ở từ khóa đó.

---

## 4. Mẹo cho bài thi tiếng Anh dài (ESL +30 phút)

- Đoạn mô tả câu chuyện công ty ("A company is a global leader in…") chỉ cần **lướt**. Thông tin quan trọng thường nằm ở **2 câu cuối và các gạch đầu dòng yêu cầu**.
- Gặp từ lạ, không cần dịch cả câu. Chỉ cần biết nó là **ràng buộc** hay **mô tả hiện trạng**.
- Câu quá dài thì đọc **phương án trước** để biết đề đang so sánh dịch vụ nào, sau đó đọc stem tìm dữ kiện quyết định.

---

## 5. Áp dụng khi làm đề luyện

- Làm đúng **các mốc 60' / 125' / 185'**. Khi qua mỗi mốc, ghi lại đang ở câu số mấy.
- Đếm số câu cắm cờ, mục tiêu **≤ 10**.
- Câu nào mất hơn 3 phút thì ghi số câu lại, để sau đó xem do **đọc đề chậm** hay do **không biết kiến thức**.
- Lịch luyện: `exam-udemy2.html` (10-28) → `exam-udemy3.html` (10-29) → Official Practice Exam (10-30) → `exam-mix-nealc-td6-udemy1.html` (10-31, cổng quyết định).

---

## Tóm tắt

> **Đọc câu hỏi trước → tìm từ khóa ràng buộc → loại phương án sai → kẹt quá 2 phút thì cắm cờ rồi đi tiếp → giữ đúng mốc 60 / 125 / 185.**
