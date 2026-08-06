# Kế hoạch Phase 9: Nâng cấp Hàng đợi & Nhắc lại âm thanh

## 1. Mục tiêu
- Phụ huynh gọi học sinh sẽ thấy được danh sách các học sinh đang chờ.
- Âm thanh nhắc lại có thể được kích hoạt bởi Phụ huynh hoặc Giáo viên (thông qua Firebase Realtime DB).
- Giáo viên có thể thao tác vuốt ngang màn hình iPad để xác nhận học sinh đã về.

## 2. Các thay đổi kỹ thuật
- **Firebase Database**: Cập nhật trường `lastRecall` (timestamp) khi có lệnh nhắc loa.
- **receiver.html**: 
  - Lắng nghe `lastRecall` để kích hoạt `speechSynthesis`.
  - Thay đổi logic render `calledList` thành một mảng được sort theo `timestamp`.
  - Gắn Touch Event (`touchstart`, `touchmove`, `touchend`) để swipe thẻ học sinh.
- **sender.html**: Thêm UI danh sách học sinh có `status === 'called'`, cho phép tương tác nút Nhắc lại.

## 3. Cách kiểm thử
1. Gọi nhiều học sinh, kiểm tra thứ tự có đúng không.
2. Bấm nhắc loa từ điện thoại, iPad phát tiếng.
3. Vuốt sang phải trên iPad, học sinh bay khỏi danh sách.
