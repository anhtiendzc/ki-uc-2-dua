from flask import Flask, render_template, request, redirect
import cloudinary
import cloudinary.uploader
import os

app = Flask(__name__)

# 🔐 Cấu hình Cloudinary (thay bằng thông tin thật của bạn)
cloudinary.config(
    cloud_name='dh8zykd67',
    api_key='836368494927138',
    api_secret='VqIqa9NebMYbubcjCCEJN5Ey2zY'
)

# Tạo file tạm lưu danh sách ảnh (lưu vào file local đơn giản)
IMAGE_URL_FILE = "image_urls.txt"

def read_image_urls():
    if not os.path.exists(IMAGE_URL_FILE):
        return []
    with open(IMAGE_URL_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_image_url(url):
    with open(IMAGE_URL_FILE, "a") as f:
        f.write(url + "\n")

@app.route('/')
def index():
    image_urls = read_image_urls()
    return render_template('index.html', image_urls=image_urls)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect('/')
    file = request.files['image']
    if file.filename == '':
        return redirect('/')
    result = cloudinary.uploader.upload(file)
    image_url = result['secure_url']
    save_image_url(image_url)
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
