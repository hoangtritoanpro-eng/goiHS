# Kế hoạch Phase 10: Trải nghiệm WOW (UX & Hiệu ứng)

## 1. Mục tiêu
Nâng cấp trải nghiệm người dùng thông qua các chi tiết nhỏ nhưng tinh tế: Âm thanh, Hiệu ứng hình ảnh và Sự thoải mái cho mắt (Dark Mode).

## 2. Thay đổi Kỹ thuật
- **Chuông báo sân bay**: Dùng file mp3 hoặc ogg online nhỏ gọn. Tại `receiver.html`, thay vì gọi thẳng `speak()`, ta sẽ play thẻ `<audio>`, bắt sự kiện `onended` của audio rồi mới gọi `speak()`.
- **Pháo giấy (Confetti)**: Import thư viện CDN `canvas-confetti`. Thêm biến `previousStudentCount`. Trong hàm render, nếu `previousStudentCount > 0` và `currentCount === 0`, thì gọi hàm `confetti()`.
- **Dark Mode**: Ở `sender.html` và `admin.html`, gắn một nút switch nhỏ ở góc. Thêm CSS `.dark-mode` cho thẻ `:root` hoặc `body` ghi đè CSS Variables. Lưu cấu hình vào `localStorage.getItem('theme')`.

## 3. Kiểm thử
- Phải đảm bảo âm "Ting Ting" kêu xong mới bắt đầu đọc giọng nói (chứ không bị đè lên nhau).
- Phải đảm bảo pháo giấy không tự nhiên nổ lúc vừa reload trang (phải có sự chuyển đổi từ có học sinh -> trống).
- Đổi Dark Mode xong reload trang vẫn giữ nguyên (persistent state).
