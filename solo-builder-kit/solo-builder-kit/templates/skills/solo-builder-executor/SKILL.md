---
name: solo-builder-executor
description: Hướng dẫn chi tiết cách thực thi một Phase trong dự án theo chuẩn vòng lặp Solo Builder (Plan -> Review -> Execute -> Test -> Commit).
---

# Solo Builder Executor Skill

Sử dụng skill này (quy trình này) BẮT BUỘC mỗi khi user yêu cầu bắt đầu thực thi một Phase hoặc một Task lớn trong dự án.

## Quy Trình Thực Thi Một Phase (The Infinite Loop)

Khi bắt đầu một Phase (ví dụ: Phase 1), bạn phải tuần tự thực hiện các bước sau một cách có kỷ luật:

### 1. Lên Plan Chi Tiết (Plan Creation)
- Xem lại `docs/plans/master-plan.md` để biết phạm vi.
- Tạo một file plan chi tiết, ví dụ: `docs/plans/phase-1.md` (dựa trên `docs/plans/phase-template.md`).
- File này phải định nghĩa rõ: 
  - Checklist công việc chi tiết (Tasks).
  - Kết quả kỳ vọng (Expected Outcomes).
  - Phương pháp kiểm thử (Testing Strategy).

### 2. Review Plan
- Trình bày tóm tắt plan cho user và đợi user xác nhận.
- Nếu có điểm nào bất hợp lý so với BRD hoặc Brief, hãy chủ động thảo luận và hoàn thiện plan.

### 3. Thực Thi (Implementation)
- Cập nhật, viết code dựa theo checklist đã đề ra.
- Đảm bảo tuân thủ đúng Tech Stack quy định trong `AGENTS.md`.
- Chỉ sử dụng các tool chỉnh sửa file chính xác, tránh ghi đè toàn bộ file lớn nếu chỉ cần sửa đổi nhỏ.

### 4. Báo Cáo Thực Thi & Review (Walkthrough)
- Sau khi hoàn tất code, lập báo cáo tóm tắt các file đã tạo/sửa.
- Review tổng thể xem các logic đã liên kết chặt chẽ và hoạt động đồng bộ chưa.

### 5. Test (Kiểm thử)
- Đề xuất script test (nếu có thể tự động).
- Đưa ra các bước hướng dẫn cụ thể để User thực hiện manual test trên Browser/Device.
- Chờ User test và cung cấp feedback.

### 6. Fix / Improve (Nếu có)
- Xử lý các bug hoặc cải tiến theo feedback của user. Lặp lại bước 5.

### 7. Đóng gói (Review & Cập nhật Docs)
- **BẮT BUỘC** cập nhật file `CHANGELOG.md` ghi lại các tính năng vừa thêm.
- **BẮT BUỘC** check tick `[x]` cho phase tương ứng trong `docs/plans/master-plan.md`.
- Đề xuất commit message rõ ràng để lưu lịch sử Git.
