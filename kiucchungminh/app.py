from flask import Flask, render_template, request, redirect
import cloudinary
import cloudinary.uploader
import os

app = Flask(__name__)

# ✨ Cấu hình Cloudinary (thay thông tin bên dưới bằng của bạn)
cloudinary.config(
    cloud_name='dh8zykd67',
    api_key='836368494927138',
    api_secret='VqIqa9NebMYbubcjCCEJN5Ey2zY'
)

# Danh sách chứa link ảnh đã upload
image_urls = []

# Trang chủ hiển thị ảnh
@app.route('/')
def index():
    return render_template('index.html', image_urls=image_urls)

# Xử lý upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect('/')
    
    file = request.files['image']
    if file.filename == '':
        return redirect('/')
    
    # Upload lên Cloudinary
    upload_result = cloudinary.uploader.upload(file)
    image_url = upload_result['secure_url']
    image_urls.append(image_url)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
