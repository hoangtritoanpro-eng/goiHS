# Business Requirements Document (BRD) - goiHS

## 1. Yêu cầu Người dùng (User Requirements)

### 1.1. Role: Giám thị (Sender)
- Tôi muốn có một nút bấm to để thu âm tên học sinh thay vì gõ tay.
- Tôi muốn hệ thống tự động nhận diện và tìm kiếm gần đúng (fuzzy match) tên học sinh từ giọng nói của tôi.
- Tôi muốn thấy một danh sách các kết quả khả thi và bấm vào nút để xác nhận gọi học sinh đó.
- Tôi muốn nhận được thông báo "Đã gọi thành công".

### 1.2. Role: Giáo viên (Receiver)
- Tôi muốn sử dụng iPad đặt trong lớp để nhận thông báo.
- Khi có học sinh được gọi, tôi muốn tên học sinh đó hiện thật to, rõ ở giữa màn hình và nhấp nháy để gây chú ý.
- Tôi muốn iPad tự động phát âm thanh rõ ràng: "Mời bạn [Tên học sinh] xuống cổng, có phụ huynh đón."
- Tôi muốn có nút "Đã về" để xóa tên học sinh khỏi màn hình khi học sinh đó đã rời lớp.
- (Phase 3) Cần có cơ chế cảnh báo nếu một học sinh đã được gọi ra cổng quá 5 phút mà chưa có phụ huynh đón. Lịch sử các học sinh đã về cũng cần được lưu vết và dễ dàng tra cứu.
- (Phase 4) Hệ thống cần có Dashboard thống kê số lượng học sinh theo từng trạng thái theo thời gian thực (Realtime), giúp quản lý có cái nhìn tổng quan.
- (Phase 4) Ban quản lý phải có khả năng tải xuống (Export) danh sách dữ liệu dưới dạng file CSV/Excel phục vụ mục đích báo cáo, đối soát cuối ngày.
- (Phase 5) Hệ thống phải có nút "Reset Ngày Mới" để dễ dàng khởi tạo lại trạng thái của toàn bộ dữ liệu chỉ bằng 1 thao tác (chuẩn bị cho ngày làm việc mới).
- (Phase 5) Các trang web cần hỗ trợ tính năng Progressive Web App (PWA) để cài đặt thành ứng dụng độc lập (app icon) trên màn hình chính của iPhone/iPad/Android.
- (Phase 6) Hệ thống cho phép người dùng nạp (Import) danh sách học sinh hàng loạt thông qua việc upload file Excel (`.xlsx` hoặc `.csv`). Chỉ yêu cầu cột A là tên học sinh để đơn giản hóa thao tác.
- (Phase 7) Giao diện Quản trị và Cổng trường phải cung cấp công cụ Tìm kiếm (Search) học sinh theo tên theo thời gian thực (gõ tới đâu lọc tới đó) để dễ dàng tra cứu trong danh sách lớn.
- (Phase 7) Cổng trường có khả năng bấm nút gọi thủ công từ kết quả tìm kiếm làm phương án dự phòng cho tính năng Nhận diện giọng nói.
- (Phase 8) Hệ thống hỗ trợ quản lý và phân loại theo "Lớp học" để tránh nhầm lẫn khi trùng tên. Lớp học có thể được Import từ cột B của file Excel.
- (Phase 8) Trí tuệ nhân tạo (AI) phải đọc chính xác tên Lớp học bên cạnh tên Học sinh để tăng độ tin cậy.

## 2. Yêu cầu Chức năng (Functional Requirements)

1. **Kết nối Realtime (Firebase):**
   - Dữ liệu học sinh được lưu tại node `students`.
   - Schema: `hs_id`: `{ name: string, status: 'waiting' | 'called' | 'completed', timestamp: number }`.
2. **Module Speech-to-Text (Cổng trường):**
   - Sử dụng `webkitSpeechRecognition` (ngôn ngữ `vi-VN`).
   - Xử lý loại bỏ dấu tiếng Việt (normalization) để so khớp kết quả.
3. **Module Text-to-Speech (Lớp học):**
   - Sử dụng `window.speechSynthesis` (giọng đọc tiếng Việt).
   - Yêu cầu người dùng bấm nút khởi tạo ban đầu để vượt qua chính sách autoplay của trình duyệt.
4. **Cập nhật trạng thái:**
   - App giám thị cập nhật trạng thái từ `waiting` sang `called`.
   - App lớp học lắng nghe sự kiện `child_changed` và cập nhật UI.
   - App lớp học cập nhật trạng thái từ `called` sang `completed`.

## 3. Yêu cầu Phi chức năng (Non-Functional Requirements)
- **Giao diện (UI/UX):** Hiện đại, chữ to, dễ đọc từ xa (iPad) và dễ bấm ngoài trời nắng (Mobile).
- **Hiệu năng:** Độ trễ nhận thông báo phải dưới 1 giây.
- **Tương thích:** Hoạt động tốt trên Chrome, Safari, Edge (iOS/Android/iPadOS).
