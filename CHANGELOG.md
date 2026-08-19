# Changelog - goiHS

Tất cả các thay đổi đáng chú ý của dự án này sẽ được ghi chép lại trong file này.

Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).



## [1.17.0] - 2026-08-19

### Added (Thêm mới)
- **Tự động gọi anh/chị/em:** Nâng cấp tính năng gọi học sinh. Giờ đây, khi phụ huynh nhấn đón 1 bé trên Cổng phụ huynh (parent.html) hoặc giáo viên gọi 1 bé trên Cổng gọi tên (sender.html), hệ thống sẽ tự động tìm kiếm các anh/chị/em có cùng số điện thoại (parentEmail) và đồng thời phát loa thông báo đón tất cả các bé cùng lúc.

## [1.16.0] - 2026-08-19

### Added (Thêm mới)
- Tải hàng loạt 13 tệp danh sách học sinh tiểu học lên Firebase bằng script Python tự động (upload_to_firebase.py).
- Hỗ trợ xử lý trường hợp anh, chị, em có cùng một số điện thoại (tự động mapping parentEmail để hiển thị nhiều học sinh trên cùng một tài khoản phụ huynh).

### Fixed (Sửa lỗi)
- Sửa lỗi không đồng nhất trường dữ liệu: Cập nhật dmin.html để sử dụng parentEmail thay vì parentContact, đồng bộ với logic kiểm tra của cổng phụ huynh (parent.html).

## [1.15.0] - 2026-08-15

### Added (Thêm mới)
- **Tách biệt cổng đăng nhập**: Thiết kế lại toàn bộ hệ thống đăng nhập. Trang chủ (`index.html`) nay trở thành Landing Page giới thiệu và phân luồng người dùng (Nhà trường và Phụ huynh).
- **Giao diện Nhà trường (`login_school.html`)**: Cổng đăng nhập riêng biệt dành cho Ban Giám hiệu và Giám thị, chuyển hướng trực tiếp đến Bảng Điều Khiển (`dashboard.html`).
- **Giao diện Phụ huynh (`login_parent.html`)**: Cổng đăng nhập dành riêng cho phụ huynh để vào màn hình đón con, giao diện ấm áp với tông màu cam.
- **Bảng Điều Khiển (`dashboard.html`)**: Menu trung tâm dành cho Nhà trường sau khi đăng nhập, nơi điều hướng đến tính năng Quản trị hoặc Gọi học sinh.

### Changed (Đã tối ưu)
- **Design System cao cấp**: Cập nhật toàn bộ giao diện (UI) theo hướng giáo dục, chuyên nghiệp, bắt mắt (màu sắc tươi sáng, font chữ Inter, hiệu ứng hover, glassmorphism).

### Removed (Đã xóa)
- **Xóa bỏ `login.html` cũ**: Do đã được tách thành hai luồng đăng nhập riêng biệt để trải nghiệm tốt hơn.

## [1.14.0] - 2026-08-14

### Added (Thêm mới)
- **Tích hợp Azure Speech SDK**: Cấu hình sử dụng SDK của Microsoft với giọng đọc vi-VN-NamMinhNeural cho tính năng TTS trong 
eceiver.html nhằm sửa lỗi không phát đúng giọng trên thiết bị di động (iPad, Android).
- **Fallback Cơ chế phát âm**: Thay thế Web Speech API cũ bằng hàm callStudentWithAzure, giữ đảm bảo đóng tài nguyên (synthesizer.close()) chống tràn bộ nhớ trên iPad.

## [1.13.2] - 2026-08-12

### Changed (Đã tối ưu)
- **Định dạng thông báo gọi học sinh**: Lược bỏ chữ "lớp" và chữ "đã về" khi thực hiện gọi tên qua giọng nói (chỉ còn lại "Tên + Lớp"), giúp ngắn gọn và rõ ràng hơn. 
- **Tốc độ đọc giọng TTS**: Điều chỉnh tốc độ âm thanh chậm thêm (playbackRate từ 0.75 xuống 0.70) trên cả điện thoại và laptop để phát âm rõ chữ hơn.

### Fixed (Đã sửa)
- **Lỗi không phát âm thanh học sinh đã về**: Sửa lỗi laptop không phát thông báo "đã về" nếu người dùng đọc tên học sinh ngay sau khi vừa tải trang. Cập nhật cơ chế nhận diện thời gian (timestamp) để đảm bảo mọi thông báo mới trong vòng 15 giây luôn được loa laptop phát đầy đủ.

## [1.13.1] - 2026-08-10

### Changed (Đã tối ưu)
- **Cải thiện độ trễ TTS (Timeout)**: Tăng thời gian chờ kết nối máy chủ Colab TTS (AI Voice) từ 5 giây lên 30 giây trong `sender.html` và `receiver.html` để hỗ trợ phản hồi tốt hơn khi máy chủ tải nặng.
- **Tốc độ đọc giọng Clone**: Điều chỉnh tốc độ giọng Clone chậm lại 15% (playbackRate = 0.85, preservesPitch = true) để giọng đọc tự nhiên, truyền cảm và dễ nghe hơn.

### Fixed (Đã sửa)
- **Gỡ bỏ hoàn toàn giọng mặc định Safari**: Xóa bỏ tính năng dự phòng bằng giọng đọc của thiết bị (SpeechSynthesisUtterance) trên cả 2 màn hình. Hiện tại ứng dụng sẽ bắt buộc ưu tiên 100% sử dụng giọng Clone từ Colab AI nhằm tránh tình trạng chuyển đổi giọng đột ngột gây khó chịu.

---

## [1.13.0] - 2026-08-08

### Changed (Đã tối ưu)
- **Dò tìm thông minh (Smart Search)**: Cải tiến thuật toán trên trang Cổng trường (`sender.html`), tự động chuyển đổi các từ chỉ số (một, hai, ba, tư...) thành chữ số khi người dùng đọc tên lớp, giúp việc nhận diện chính xác tuyệt đối kể cả khi trình duyệt nhận diện sai định dạng.
- **AutoCall Tức thì (Zero Latency)**: Hệ thống nay không còn chờ đợi 1.2s hay 800ms khi người dùng ngừng đọc. Nếu thuật toán khoanh vùng được 1 học sinh khớp 100% ngay giữa câu (interim), nó sẽ tự động chốt kết quả và gửi lệnh gọi lập tức.
- **Loại bỏ độ trễ phát loa (Event-Driven)**: Viết lại luồng xử lý trên trang Lớp học (`receiver.html`). Loa sẽ phát ra tín hiệu ngay ở mili-giây đầu tiên khi có dữ liệu từ Firebase thay vì phải chờ bộ đếm `setInterval` quét như trước đây, tiết kiệm tối đa thời gian chờ đợi.

### Fixed (Đã sửa)
- **Sửa lỗi lặp giọng đọc (Double Audio Spam)**: Thêm cơ chế Debounce ở tầng âm thanh. Nếu phát hiện hệ thống nhận tín hiệu hoặc bắt gặp danh sách gửi lệnh gọi một người quá 2 lần trong vòng 4 giây, hệ thống sẽ tự động hủy bỏ lệnh phía sau, giúp không bao giờ bị tình trạng đọc đè hoặc nhắc lại thừa thãi.
- **Sửa lỗi AutoCall khi gõ chữ**: Khi dùng tính năng Tìm kiếm thủ công (Gõ phím), hệ thống sẽ không tự động gọi nữa mà yêu cầu người dùng phải tự nhấp chọn, tránh tình trạng gõ nhầm chữ nhưng máy tự chốt kết quả sai.

---

## [1.12.0] - 2026-08-08

### Added (Đã thêm)
- **Tự động gọi Anh/Chị/Em (Siblings Auto-call)**: Hệ thống sử dụng chung một mã "SĐT Phụ huynh / Mã Gia Đình" để liên kết các học sinh là anh em. Khi gọi một học sinh ở cổng trường, hệ thống sẽ tự động quét và gọi luôn người anh/em đang học lớp khác xuống cùng một lúc, tiết kiệm rất nhiều thời gian cho giám thị. 
- **Phát thanh học sinh Đã Về**: Bổ sung tính năng thông minh, nếu phụ huynh đến muộn không biết con đã về và tiếp tục đọc tên con, hệ thống sẽ nhận diện trạng thái "Đã về" và lập tức phát thanh thông báo "[Tên học sinh] [Lớp] đã về" thay vì đẩy học sinh vào danh sách chờ gọi như cũ.

### Changed (Đã thay đổi)
- **Cải tiến tính năng Nhập Excel (Admin)**: Đổi trường "Email Phụ huynh" thành "SĐT Phụ huynh / Mã Gia Đình". Hàm nhập Excel sẽ tự động nhận diện các cột chứa chữ "SĐT", "Điện thoại" để lấy làm mã liên kết anh em. Gỡ bỏ tính năng tạo user Firebase Auth không cần thiết để tối ưu hóa tốc độ nhập liệu.

---

## [1.11.1] - 2026-08-08

### Fixed (Đã sửa)
- **Sửa lỗi nhận diện lớp khi đọc giọng nói**: Cập nhật biểu thức chính quy (regex) xử lý số lớp để hỗ trợ bắt được các cụm từ lớp có khoảng trắng (ví dụ: "9 5" thay vì chỉ "9/5" hay "95"). Bổ sung các từ khóa "lớp", "lop" vào danh sách stopWords để loại bỏ khi đối chiếu tên, giúp tăng độ chính xác lên tối đa và không còn bị gọi nhầm các học sinh khác lớp (ví dụ lớp 7/5 khi gọi lớp 9/5).

---

## [1.11.0] - 2026-08-06

### Fixed (Đã sửa)
- **Sửa lỗi không phát âm thanh khi deploy lên Vercel**: Thêm tính năng dự phòng (fallback). Khi ứng dụng không kết nối được đến máy chủ TTS cục bộ (127.0.0.1:5000), hệ thống sẽ tự động chuyển sang sử dụng giọng đọc mặc định của trình duyệt (`window.speechSynthesis`), giúp hệ thống vẫn phát âm thanh bình thường trên môi trường production.

---

## [1.10.0] - 2026-08-03

### Added (Đã thêm)
- **Âm thanh Ting Ting (Airport Chime)**: Bổ sung âm báo hiệu Ting Ting (bằng Web Audio API) phát lên trước khi AI đọc tên học sinh, giúp tạo sự chú ý tốt hơn.
- **Hiệu ứng Pháo giấy (Confetti)**: Thêm hiệu ứng tung pháo giấy trên màn hình iPad khi tất cả học sinh đã về hết (Empty State), khích lệ tinh thần người dùng.
- **Chế độ Ban đêm (Dark Mode)**: Thêm công tắc chuyển đổi Giao diện Sáng / Tối trên trang Cổng trường và trang Quản trị, giúp phụ huynh và giáo viên đỡ chói mắt khi dùng buổi tối. Hệ thống tự động ghi nhớ tùy chọn.

---

## [2.0.0] - 2026-08-03
### Changed (Thay đổi lớn)
- **Hợp nhất Hệ thống (Unified Mode)**: Gộp trang Lớp học và Cổng trường làm một. Thiết bị điều phối ở cổng giờ đây đảm nhận cả việc Gọi học sinh, Hiển thị danh sách lớn, và Tự động đọc loa AI.
- Đổi cách đọc tên Lớp (vd 7/5 thành "bảy năm") để AI đọc không bị ngọng.

## [1.9.0] - 2026-08-03

### Added (Đã thêm)
- **Hàng đợi ưu tiên (Queue)**: Danh sách học sinh trên trang Receiver giờ đây được sắp xếp theo đúng thứ tự (bé nào được gọi trước sẽ hiển thị phía trên).
- **Nhắc lại âm thanh**: Phụ huynh (trên màn hình Sender) và Giáo viên (trên màn hình Receiver) có thể bấm nút "🔊 Nhắc lại" để kích hoạt iPad phát lại âm thanh thông báo.
- **Vuốt để xóa (Swipe to Dismiss)**: Cải thiện trải nghiệm (UX) trên iPad, cho phép Giáo viên vuốt thẻ học sinh sang trái hoặc phải để xác nhận học sinh đã về.
- **Theo dõi học sinh đang chờ**: Trang Sender (Cổng trường) giờ đây có thêm tính năng hiển thị danh sách các bé đang chờ ở cổng, giúp phụ huynh dễ dàng quan sát và thao tác nhắc loa.

---

## [1.8.0] - 2026-08-03

### Added (Đã thêm)
- **Quản lý theo Lớp học (Class Categorization)**: Hệ thống chính thức hỗ trợ phân loại học sinh theo lớp học (ví dụ: 1A, 2B) để giải quyết triệt để vấn đề gọi nhầm học sinh trùng tên.
- **Nâng cấp Import Excel**: File mẫu Excel giờ đây sẽ tự động nhận diện Cột B làm tên Lớp Học (Cột A vẫn là Tên học sinh).
- **Giọng đọc AI thông minh hơn**: Tại trang Lớp học (Receiver), AI sẽ tự động đọc cả tên lớp: "Mời bạn Nguyễn Văn A lớp 1A xuống cổng".

---

## [1.7.0] - 2026-08-03

### Added (Đã thêm)
- Tính năng **Tìm kiếm thông minh**: Thêm thanh tìm kiếm theo tên học sinh (gõ tới đâu lọc kết quả tới đó) trên cả 2 giao diện: Quản trị (Admin) và Cổng trường (Sender).
- Tính năng **Gọi thủ công (Backup cho Voice API)**: Tại trang Cổng trường, giám thị có thể gõ tên vào ô tìm kiếm và bấm gọi trực tiếp mà không cần dùng Micro. Đây là phương án dự phòng hoàn hảo khi cổng trường quá ồn ào.
- **Firebase Deploy Config**: Khởi tạo file `.firebaserc` và `firebase.json`, sẵn sàng đưa dự án lên máy chủ Firebase Hosting bằng lệnh `firebase deploy`.

---

## [1.6.0] - 2026-08-03

### Added (Đã thêm)
- Tính năng **Nhập từ Excel (Import)**: Thêm nút "Nhập Excel" trên trang Admin. Người dùng có thể upload file Excel (`.xlsx`, `.csv`) để đẩy hàng trăm học sinh lên hệ thống trong 1 cú click. Yêu cầu định dạng file đơn giản (chỉ lấy cột A là Họ và tên).
- Tích hợp thư viện **SheetJS (xlsx)** thông qua CDN để đọc dữ liệu từ file Excel nguyên bản ngay trên trình duyệt mà không cần xử lý qua Server Backend.

---

## [1.5.0] - 2026-08-03

### Changed (Đã thay đổi)
- **Gỡ bỏ hệ thống Đăng nhập (Auth)**: Nhằm đơn giản hoá quá trình triển khai cho trường học nội bộ, yêu cầu đăng nhập bằng Firebase Auth trên trang Admin (`admin.html`) đã được gỡ bỏ hoàn toàn.
- **Thêm Landing Page (`index.html`)**: Tạo 1 trang chủ duy nhất (1 đường link) làm Menu chính để người dùng chọn giao diện tương ứng (Quản Trị, Cổng Trường, Lớp Học) dễ dàng thay vì phải nhớ đường dẫn từng trang.

---

## [1.4.0] - 2026-08-03

### Added (Đã thêm)
- Tính năng **Reset Ngày Mới**: Thêm nút Reset Tất Cả (màu cam) trên trang Admin, cho phép đưa tất cả dữ liệu học sinh (cả những em đang chờ hay đã về) quay lại trạng thái "Đang trong lớp" chỉ bằng 1 cú click.
- Tính năng **Progressive Web App (PWA)**: Bổ sung file `manifest.json` và cấu hình meta tags cho toàn bộ các trang (`sender`, `receiver`, `admin`, `login`). Giao diện giờ đây tương thích tối đa với thiết bị di động, cho phép cài đặt (Add to Home Screen) thành một ứng dụng độc lập trên điện thoại/iPad.

---
*Ghi chú: Phase 5 hoàn thành, đánh dấu sự kết thúc của dự án GoiHS. Ứng dụng đã sẵn sàng 100% về mặt tính năng và trải nghiệm người dùng (UX).*

## [1.3.0] - 2026-08-03

### Added (Đã thêm)
- Tính năng **Dashboard Thống kê**: Trang Admin giờ đây hiển thị 4 chỉ số (Tổng số, Đang trong lớp, Đang gọi, Đã về) tự động cập nhật Realtime, giúp quản lý có cái nhìn tổng quan.
- Tính năng **Xuất Dữ Liệu (Export CSV)**: Thêm nút "Xuất CSV" trên trang Admin. Toàn bộ danh sách học sinh và thời gian gọi sẽ được đóng gói thành file Excel-compatible (hỗ trợ tiếng Việt UTF-8) để báo cáo.

---
*Ghi chú: Phase 4 hoàn thành. Dự án cơ bản đã đầy đủ các chức năng vận hành, giám sát và báo cáo chuyên nghiệp.*

## [1.2.0] - 2026-08-03

### Added (Đã thêm)
- Tính năng **Lịch sử**: Thêm thanh lọc (Filter Toolbar) vào trang Admin (`admin.html`) để xem nhanh các học sinh "Đang trong lớp", "Đang chờ ở cổng" và "Đã về" (Lịch sử).
- Hiển thị **Thời gian gọi** có định dạng giờ/phút/ngày trên bảng danh sách của trang Admin.
- Tính năng **Cảnh báo quá giờ**: Thêm logic `setInterval` chạy ngầm trên `receiver.html`. Nếu học sinh chờ ở cổng quá 5 phút, thẻ tên sẽ nhấp nháy đỏ kèm nhãn "QUÁ GIỜ!".

---
*Ghi chú: Phase 3 hoàn thành. Ứng dụng đã giải quyết được trọn vẹn bài toán vận hành và quản lý trễ hẹn.*

## [1.1.0] - 2026-08-03

### Added (Đã thêm)
- Xây dựng trang Quản trị (`admin.html`) cho phép Thêm, Xóa, Reset trạng thái học sinh (CRUD).
- Tích hợp **Firebase Authentication** để bảo mật ứng dụng.
- Xây dựng trang Đăng nhập (`login.html`) yêu cầu tài khoản Email/Password để truy cập Admin.

### Changed (Đã thay đổi)
- Cập nhật `firebase-config.js` để tự động kiểm tra và khởi tạo database động, tránh lỗi undefined trên các trang không import database.

---
*Ghi chú: Phase 2 hoàn thành. Ứng dụng đã có thể hoạt động hoàn chỉnh với dữ liệu thật thay vì mock data.*

## [1.0.0] - 2026-08-03

### Added (Đã thêm)
- Thiết lập thành công hệ thống **Solo Builder Starter Kit** cho dự án.
- Tạo file cấu hình `firebase-config.js` kết nối với Realtime Database.
- Xây dựng giao diện Giám thị (`sender.html`) với tính năng Nhận diện giọng nói (Speech-to-Text) và thuật toán tìm kiếm tên học sinh.
- Xây dựng giao diện Giáo viên (`receiver.html`) với tính năng đọc tên học sinh (Text-to-Speech) và hiệu ứng Flash màn hình.
- Thêm script `seed.js` để đẩy dữ liệu mẫu lên Firebase an toàn, không bị lỗi font Tiếng Việt.
- Khởi tạo tài liệu dự án (`brief.md`, `BRD.md`, `master-plan.md`).

### Changed (Đã thay đổi)
- Đổi cấu hình Firebase sang Database thật của người dùng.

### Fixed (Đã sửa)
- Sửa lỗi font chữ Tiếng Việt khi đẩy mock data từ PowerShell bằng cách chuyển sang dùng Node script.

---
*Ghi chú: Phase 1 (MVP) đã hoàn thành và sẵn sàng nghiệm thu.*

### Thm m?i
- Tch h?p API gi?ng d?c mi?n ph c?a trnh duy?t Microsoft Edge (Edge TTS) thay th? cho Vieneu TTS. H? tr? gi?ng Hoi My v Nam Minh, cho t?c d? ph?n h?i nhanh hon v khng c?n t?i model n?ng.

