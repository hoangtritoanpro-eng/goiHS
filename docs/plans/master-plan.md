# Master Plan - goiHS

## Kế hoạch phát triển tổng thể

Tài liệu này theo dõi tiến độ các Phase của dự án. AI Agent chỉ được phép làm việc trên Phase hiện tại (Phase đang có biểu tượng `[/]`) hoặc tiếp tục đánh dấu `[x]` sau khi hoàn thành. Không được tự ý làm Phase khác.

---

### [x] Phase 1: Xây dựng Minimum Viable Product (MVP)
Mục tiêu: Đảm bảo luồng Realtime cơ bản giữa việc nhận diện giọng nói và phát âm thanh hoạt động trơn tru.
- `[x]` Thiết lập cấu trúc dự án và kết nối Firebase Realtime Database.
- `[x]` Xây dựng giao diện Cổng trường (`sender.html`): Tích hợp Web Speech API (Speech-to-Text).
- `[x]` Xây dựng thuật toán Fuzzy Match so khớp tên học sinh và cập nhật trạng thái `called` lên Firebase.
- `[x]` Xây dựng giao diện Lớp học (`receiver.html`): Lắng nghe Realtime trạng thái `called`.
- `[x]` Tích hợp Web Speech API (Text-to-Speech) phát tiếng Việt và hiệu ứng Flash trên màn hình.
- `[x]` Xây dựng luồng hoàn tất: Bấm "Đã về" để cập nhật trạng thái `completed`.
- `[x]` Áp dụng Solo Builder Starter Kit và đồng bộ tài liệu.

### [x] Phase 2: Quản lý danh sách học sinh & Xác thực (Dự kiến)
Mục tiêu: Không dùng dữ liệu cứng (mock data) mà cho phép quản trị viên thêm/xóa/sửa học sinh và bảo mật hệ thống.
- `[x]` Thêm xác thực Firebase Auth (Đăng nhập cho Giám thị / Giáo viên).
- `[x]` Xây dựng giao diện Admin (`admin.html`) để quản lý học sinh (CRUD).
- `[x]` Nâng cấp rules bảo mật trên Firebase.

### [x] Phase 3: Tính năng mở rộng & Báo cáo (Dự kiến)
- `[x]` Lịch sử đón học sinh trong ngày (Tích hợp bộ lọc vào Admin).
- `[x]` Cảnh báo nếu học sinh chờ quá lâu (ví dụ 5 phút) mà giáo viên chưa xác nhận "Đã về" (Đổi màu UI trên receiver).

### [x] Phase 4: Thống kê & Báo Cáo (Export)
- `[x]` Hiển thị Dashboard thống kê số lượng học sinh thời gian thực trên màn hình Admin (Tổng số, Đang trong lớp, Đang gọi, Đã về).
- `[x]` Tính năng Xuất dữ liệu Lịch sử ra file CSV (Tương thích Excel, UTF-8).

### [x] Phase 5: Tối ưu Trải Nghiệm & Đóng Gói (PWA)
- `[x]` Nút "Reset Ngày Mới" trên trang Quản trị giúp dọn dẹp data chỉ với 1 click.
- `[x]` Biến website thành PWA (Progressive Web App) với `manifest.json` để cài trực tiếp lên Homescreen của iPhone/iPad như một App thực thụ.

### [x] Phase 6: Nhập dữ liệu (Import Excel)
- `[x]` Thư viện SheetJS cho phép đọc dữ liệu từ file Excel.
- `[x]` Cấu hình nút Nhập Excel trên trang Admin để lấy Cột A (Họ và Tên) đẩy thẳng lên Firebase Realtime Database.

### [x] Phase 7: Tìm kiếm Thông minh & Triển khai (Deploy)
- `[x]` Thêm thanh tìm kiếm (Realtime Search) trên giao diện Admin và Gọi Học Sinh (Sender).
- `[x]` Khởi tạo cấu hình `firebase.json` và `.firebaserc` để chuẩn bị đưa ứng dụng lên Firebase Hosting.

### [x] Phase 8: Quản lý & Phân loại theo Lớp học
- `[x]` Trang Admin: Bổ sung ô nhập Lớp, hiển thị cột Lớp, cho phép Import/Export dữ liệu có Lớp (Cột B trong Excel).
- `[x]` Trang Receiver: Đọc và hiển thị rõ Lớp học để tránh trùng tên.
- `[x]` Trang Sender: Hiển thị tên Lớp trong kết quả tìm kiếm.

### [x] Phase 9: Nâng cấp Hàng đợi & Nhắc lại âm thanh
- `[x]` Quản lý danh sách học sinh gọi theo đúng thứ tự (Queue).
- `[x]` Tính năng "Nhắc Loa" (Phát lại âm thanh) cho Phụ huynh và Giáo viên.
- `[x]` Hỗ trợ Vuốt để xóa (Swipe to Dismiss) thay cho nút bấm cứng nhắc trên iPad.

### [x] Phase 10: Trải nghiệm WOW (UX & Hiệu ứng)
- `[x]` Thêm chuông báo (Chime) trước khi AI đọc tên học sinh.
- `[x]` Nổ pháo giấy (Confetti) chúc mừng khi danh sách trống (tất cả đã về).
- `[x]` Tính năng giao diện ban đêm (Dark Mode) cho Phụ huynh và Giáo viên.

### [x] Phase 11: Hợp nhất Giao diện (Unified Mode)
- `[x]` Bỏ giao diện "Lớp học" (`receiver.html`) ra khỏi hệ thống.
- `[x]` Đưa bảng danh sách thẻ lớn, tính năng đọc âm thanh, vuốt xóa, pháo hoa vào trang Cổng trường (`sender.html`).
- `[x]` Tối ưu hóa lại cấu trúc của trang Cổng trường (1 thiết bị dùng chung cho cả việc Gọi và Hiển thị/Đọc).

### [x] Phase 12: Hàng Đợi Thông Minh & Cổng Phụ Huynh
- `[x]` Xây dựng logic phân loại cấp học (Tiểu học: 1-5, THCS: 6-9) dựa vào `className`.
- `[x]` Tích hợp bộ đếm thời gian thực trên Cổng trường để kiểm tra khung giờ (Tiểu học: 16h20, THCS: 16h40).
- `[x]` Các học sinh được gọi sớm hơn khung giờ sẽ chỉ hiển thị chờ trên UI, không phát loa.
- `[x]` Tự động phát loa danh sách chờ khi đến đúng giờ quy định.
- `[x]` Thiết kế giao diện Cổng Phụ Huynh (`parent.html`) rút gọn và tính năng tự động gọi/thông báo thời gian chờ.
- `[x]` Nâng cấp hệ thống đăng nhập (`login.html`) phân quyền Giám thị và Phụ huynh.
