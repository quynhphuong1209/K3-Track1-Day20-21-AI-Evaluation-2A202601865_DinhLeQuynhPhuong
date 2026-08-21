# AI Support Log — Nhóm Cao Các Tường

> Ghi nhận minh bạch vai trò hỗ trợ của AI trong quá trình thực hiện bài lab AI Evaluation Loop (Track 1 Day 20-21).

---

## 1. Quy tắc Sử dụng AI (AI Governance Rules)

### Được phép dùng AI để:
1. **Paraphrase & Data Augmentation:** Sinh các biến thể câu hỏi học viên (test inputs) sau khi nhóm đã đóng băng 4 Dimensions và tổ hợp ô coverage.
2. **Code Checks Assertions:** Brainstorm và gợi ý cấu trúc mã nguồn Python cho các hàm kiểm tra rule cứng trong `code_checks.py`.
3. **Judge Prompting:** Gợi ý cấu trúc rubric và quy tắc hiệu chuẩn cho `judge-prompt-v2.md`.
4. **Failure Pattern Analysis:** Tóm tắt các pattern lệch giữa phán quyết của Judge và nhãn vàng con người (False Negative `sc-03`, False Positive `sc-20`).
5. **Report Drafting:** Hỗ trợ soạn thảo và định dạng văn bản báo cáo `REPORT.md` theo thuật ngữ PM chuẩn mực.

### KHÔNG được dùng AI để:
1. **Tự chọn Coverage Strategy:** Tự định nghĩa dimensions, tổ hợp ô hoặc tỷ lệ phân bổ scenarios thay cho nhóm PM.
2. **Gán nhãn thay Con người:** Gán nhãn tự động cho bộ Ground Truth ở Phase 2 (nhãn vàng `labels.csv` phải hoàn toàn do 2 annotators Phương & Tường thẩm định và thống nhất).
3. **Tự quyết định Verdict / Gate:** Tự ý quyết định kết quả ship/hold hay tự đặt ngưỡng chất lượng thay cho nhóm.
4. **Bịa đặt số liệu:** Tự tạo số liệu ảo, trace ảo hoặc kết quả chạy không có trong dữ liệu thô `evidence/`.

---

## 2. AI Support Log (Phản tư của Nhóm)

### ❓ AI đã giúp tôi ở đâu?
- **Tự động hóa Code Checks:** Sinh khung mã nguồn Python chuẩn mực cho 2 hàm check mở rộng trong `eval/code_checks.py` (`check_scope_values` và `check_refusal_sources`), giúp kiểm tra cú pháp và schema cực nhanh với chi phí 0$.
- **Thống kê Ma trận Nhầm lẫn:** Hỗ trợ tổng hợp nhanh các chỉ số thực chứng (TPR, TNR, FNR, FPR) và tính tỷ lệ đồng thuận (Agreement) khi so sánh `verdicts-v1.jsonl` / `verdicts-v2.jsonl` với `labels.csv`.
- **Hiệu chuẩn Prompt Judge:** Gợi ý cấu trúc bổ sung *Quy tắc Quote rút gọn* và *Quy tắc Câu hỏi rỗng/cụt* trong `judge-prompt-v2.md` cùng các ví dụ Near-Miss thực tế để nâng tỷ lệ đồng thuận từ 90% lên 100%.
- **Chuẩn hóa Báo cáo:** Hỗ trợ trình bày cấu trúc báo cáo 1 trang chuyên nghiệp, sắc nét theo phong cách PM cho `REPORT.md`.

---

### ❓ AI sai, hời hợt hoặc làm mất coverage ở đâu?
- **Lỗi Khắt khe Quá mức (False Negative ở `sc-03`):** AI Judge v1 đánh `fail` (Score 0.4) đối với câu hỏi so sánh 3 loại grader của Anthropic chỉ vì trường `"quote"` trong JSON trích một câu ngắn, dù toàn bộ kiến thức kỹ thuật chi tiết đã nằm sẵn trong section được cite.
- **Lỗi Dễ dãi Quá mức (False Positive ở `sc-20`):** AI Judge v1 đánh `pass` (Score 1.0) khi Tutor tự ý xuất bài giảng dài 450 từ cho câu hỏi chỉ vỏn vẹn chữ `"Hỏi?"`, bỏ qua việc đánh giá xem câu trả lời có thực sự xử lý đúng ý định người dùng (`Intent Handling`) hay không.
- **Ảo giác về Ý định (Over-generation):** Khi chạy Tutor, model có xu hướng "xả lý thuyết" với các câu hỏi rỗng/cụt thay vì hỏi lại để làm rõ câu hỏi.
- **Giới hạn tự phát hiện lỗi:** AI không thể tự nhận diện được các lỗi ranh giới sư phạm hoặc trải nghiệm người dùng nếu không có sự can thiệp và cung cấp ví dụ Near-Miss từ con người.

---

### ❓ Tôi đã tự sửa hoặc quyết định lại điều gì?
- **Xây dựng Nhãn Vàng Độc Lập:** Đinh Lê Quỳnh Phương và Cao Các Tường đã trực tiếp gán nhãn thủ công 20 scenarios trên giao diện `report.html` và thảo luận thống nhất ra `labels.csv` (19 Pass, 1 Fail) hoàn toàn độc lập với AI.
- **Bác bỏ Phán quyết Sai của AI Judge:** Quyết định chốt `sc-03` là **PASS** (vì grounded 100% vào section được cite) và `sc-20` là **FAIL** (vì vi phạm nguyên tắc trợ giảng), sửa lại sai sót của Judge Baseline Vòng 1.
- **Quyết định Chiến lược Release (Gate):** Đưa ra phán quyết **SHIP WITH CONDITIONS** — yêu cầu bổ sung 1 dòng rule vào System Prompt của Tutor (`tutor/tutor.py`) xử lý câu hỏi cụt rỗng trước khi bật traffic thật.
- **Thiết lập Hard Gates:** Đóng băng ngưỡng bắt buộc 100% Code Checks và 100% Anti-Cheat/Jailbreak Defense làm điều kiện tiên quyết (Blockers) để bảo vệ sản phẩm.
