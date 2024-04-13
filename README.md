# Hướng dẫn Bài tập 1

Kho lưu trữ này chứa mã nguồn và báo cáo cho Bài tập 1. Dưới đây là chi tiết về nhiệm vụ của bài tập và cách sử dụng mã nguồn được cung cấp.

## Chi tiết Bài tập

### Thư viện Sử dụng
- OpenCV
- NumPy
- Matplotlib
- LaTeX

### Biểu diễn Hình ảnh
Một bức ảnh có thể được biểu diễn dưới dạng một mảng NumPy của "pixel", với các chiều H × W × C, trong đó H là chiều cao, W là chiều rộng, và C là số kênh màu. Hình ảnh dưới đây minh họa hệ tọa độ. Gốc tọa độ nằm ở góc trên bên trái và chiều thứ nhất chỉ ra hướng Y (dòng), trong khi chiều thứ hai chỉ ra chiều X (cột). Thông thường, chúng ta sẽ sử dụng một hình ảnh với các kênh màu cho đỏ, xanh lá cây và xanh lam "cấp độ" của mỗi pixel, được gọi tắt là RGB. Giá trị cho mỗi kênh nằm trong khoảng từ 0 (tối nhất) đến 255 (sáng nhất). Tuy nhiên, khi tải một hình ảnh thông qua Matplotlib, khoảng này sẽ được tỷ lệ từ 0 (tối nhất) đến 1 (sáng nhất) thay vì là một số nguyên.

### Nhiệm vụ Bài tập
- Viết mã Python để tải một bức ảnh và thực hiện một số thao tác trên ảnh và hiển thị các hiệu ứng của chúng.
- File `uet.png` là bắt buộc cho nhiệm vụ này. Hãy chắc chắn rằng bạn đã có nó từ cùng nơi mà bạn tải xuống bài tập này.
- Thực hiện tất cả các hàm trong file `ex1.py`.
- Báo cáo kết quả của các hàm `flip_image`, `rotate_image`, `grayscale_image` bằng cách sử dụng mẫu LaTeX được cung cấp.

## Nội dung Kho lưu trữ

### File
1. `ex1.py`: Chứa mã Python thực hiện các hàm biến đổi hình ảnh.
2. `report.tex`: Mẫu LaTeX để báo cáo kết quả.
3. `uet.png`: File hình ảnh cần thiết cho việc biến đổi.
4. `images`: Thư mục chứa các ảnh sau khi biến đổi
5. `22028202_LuongThiLinh.ipynb`: Bài tập trên Google Colab
6. `README.md`: File này cung cấp một cái nhìn tổng quan về kho lưu trữ.

### Hướng dẫn
1. Sao chép kho lưu trữ này vào máy tính cục bộ của bạn.
2. Đảm bảo bạn đã cài đặt các thư viện cần thiết (`opencv`, `numpy`, `matplotlib`).
3. Chạy các hàm trong `ex1.py` để thực hiện các biến đổi hình ảnh.
4. Sử dụng mẫu LaTeX trong `report.tex` để báo cáo kết quả của các hàm `flip_image`, `rotate_image`, và `grayscale_image`.
