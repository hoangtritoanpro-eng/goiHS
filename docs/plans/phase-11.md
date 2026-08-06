# Kế hoạch Phase 11: Hợp nhất (Unified Mode)

## 1. Mục tiêu
Gộp chức năng của màn hình Lớp học (Receiver) vào màn hình Cổng trường (Sender) để tạo ra một giao diện All-in-one duy nhất.

## 2. Thay đổi Kỹ thuật
- Ẩn/Xoá menu truy cập `receiver.html` trên `index.html`.
- Chỉnh sửa `sender.html`:
  - Khung HTML: Cần có lớp phủ `#startScreen` chặn ban đầu để lấy quyền truy cập Audio.
  - Mang CSS của `student-card`, `done-btn`, `@keyframes slideIn`, `@keyframes flash` từ `receiver` sang `sender`.
  - Copy thư viện `canvas-confetti` sang `sender`.
  - Merge luồng logic JS: Khi khởi tạo, lấy `speechSynthesis.getVoices()`. Khi lắng nghe Firebase `studentsRef.on('value')`, nó sẽ filter status là `called`, sắp xếp theo time. Khởi tạo thẻ UI to (hàm `addStudentToUI`).
  - Hủy nút "🔊 Nhắc lại" bé bé cũ, thay bằng toàn bộ mặt thẻ bấm được + Swipe ngang + Nút ĐÃ VỀ.
  - Khi người dùng bấm Micro trên cùng (ở `sender`) và gọi, bản thân máy `sender` sẽ push Firebase, Firebase update `value`, và chính sự kiện listener trên `sender` sẽ bắt lại và chạy `speak()`. (Cơ chế Reactive: Cứ database đổi là UI đổi).

## 3. Kiểm thử
- Refresh web, phải click "Bắt đầu chế độ đón" trước khi thấy thanh nhập tên.
- Gọi 1 bạn: Thẻ hiện ra to đùng ở dưới, âm thanh Ting ting + Đọc loa kêu lên trên chính thiết bị đó.
- Gạt tay hoặc chuột xóa bé đó: Bắn pháo giấy (Confetti).
