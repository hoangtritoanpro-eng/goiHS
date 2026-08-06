# Project Brief: goiHS

**Mô tả ngắn gọn (Elevator Pitch):**
Ứng dụng Web "Gọi Học Sinh" (goiHS) là giải pháp số hóa quy trình đón học sinh giờ tan trường, kết nối trực tiếp giữa Giám thị (ở cổng trường) và Giáo viên (ở trong lớp) thông qua công nghệ Realtime.

**Mục tiêu chính:**
- Loại bỏ việc dùng loa phóng thanh thủ công, giảm tiếng ồn.
- Đảm bảo thông tin đón học sinh được truyền tải ngay lập tức (realtime) và chính xác vào tận lớp học.
- Ứng dụng công nghệ Text-to-Speech và Speech-to-Text để tăng tốc độ thao tác cho giám thị.

**Phạm vi dự án (Scope):**
- **In-scope:** 
  - Giao diện giám thị (Web trên mobile): Nhận diện giọng nói, tìm kiếm học sinh, gửi tín hiệu.
  - Giao diện giáo viên (Web trên iPad): Lắng nghe tín hiệu, nhấp nháy màn hình, đọc tên học sinh qua loa, xác nhận học sinh đã về.
- **Out-of-scope (Hiện tại):**
  - Đăng nhập/Xác thực người dùng (Auth).
  - Quản lý danh sách học sinh phức tạp (CRUD qua giao diện quản trị).
  - Báo cáo thống kê.

**Công nghệ sử dụng (Tech Stack):**
- HTML5, CSS3, Vanilla JavaScript.
- Firebase Realtime Database.
- Web Speech API (SpeechRecognition & SpeechSynthesis).
