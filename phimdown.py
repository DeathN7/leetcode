import requests
import os
import codecs

reader = codecs.getreader('utf-8')
# Nhập liên kết trang web
url = input("Nhập liên kết trang web: https://motchill3.com/xem-phim/phim-moving-2023-tap-2-2").encode('utf-8').decode('utf-8')

# Tạo thư mục để lưu phim
if not os.path.exists("Phim"):
    os.makedirs("Phim")

# Lấy tên tệp từ liên kết
filename = url.split("/")[-1]

# Gửi yêu cầu GET đến trang web
response = requests.get(url, stream=True)

# Kiểm tra trạng thái phản hồi
if response.status_code == 200:
    # Tải xuống tệp
    with open(os.path.join("Phim", filename), "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    print("Tải xuống phim thành công!")
else:
    print("Lỗi tải xuống phim:", response.status_code)
