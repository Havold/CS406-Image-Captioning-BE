# 📷 Image Captioning API 

This is a Flask-based API for generating captions for images using advanced models like **CLIP-MT5** and **CLIP-MBART**. The application takes an image as input, processes it, and generates a descriptive caption.

## 🌟 Features
- **CLIP-MT5 Captioning:** Generates captions using the CLIP-MT5 model.
- **CLIP-MBART Captioning:** Generates captions using the CLIP-MBART model.
- **Multi-model Support:** Provides endpoints to select between two state-of-the-art models for caption generation.

## 🛠️ Requirements

Before running the project, make sure you have the following installed:
- Python 3.x (3.10.13 recommended)
- Flask 3.1.0
- Transformers 4.47.1
- Flask-CORS 5.0.0
- Pillow 11.0.0
- PyTorch (compatible with the model)

You can install all dependencies by running:

```
pip install -r requirements.txt
```

## 🚀 Getting Started
1. Clone the repository
```
git clone https://github.com/Havold/CS406-Image-Captioning-BE.git
cd CS406-Image-Captioning-BE.git
```
2. Prepare Models

Ensure the following models are downloaded and stored in the project directory:
- `clip_mt5_base_model`: Contains files like `config.json`, `model.safetensors`, etc.
- `clip_mbart_model`: Pre-trained model files.

3. Install dependencies
Install the required Python packages using:
```
pip install -r requirements.txt
```
4. Run the Flask server:
```
python app.py
```
5. The server will start at http://localhost:5000.

## ❗ API Endpoints
**1. Generate Caption with CLIP-MT5**
   - **URL**: `/clip-mt5`
   - **Method**: `POST`
   - **Parameters**:
      - `image`: Image file (PNG, JPG, JPEG).
   - **File**: Image file (JPEG/PNG).
   - **Response**: Returns a JSON object with the generated caption.
   - Example Request (Postman)
   ```
    POST http://localhost:5000/clip-mt5
   ```
   - Form-data:
     - `image`: (Attach your image file)
   - Response:
   ```
    {
    "caption": "A scenic view of mountains during sunset."
    }
   ```

**2. Generate Caption with CLIP-MBART**
   - **URL**: `/clip-mbart`
   - **Method**: `POST`
   - **Parameters**:
      - `image`: Image file (PNG, JPG, JPEG).
   - **File**: Image file (JPEG/PNG).
   - **Response**: Returns a JSON object with the generated caption.
   - Example Request (Postman)
   ```
    POST http://localhost:5000/clip-mbart
   ```
   - Form-data:
     - `image`: (Attach your image file)
   - Response:
   ```
    {
    "caption": "A scenic view of mountains during sunset."
    }
   ```

## 🔥 Usage
Once the server is running, you can test the application by sending requests via a tool like `Postman` or via a frontend application to interact with the API.

---------------------------------------------------------
# 📷 API Mô Tả Ảnh (Image Captioning API)

Đây là một API dựa trên Flask, được sử dụng để sinh mô tả cho hình ảnh bằng các mô hình tiên tiến như **CLIP-MT5** và **CLIP-MBART**. Ứng dụng nhận hình ảnh làm đầu vào, xử lý và trả về một câu mô tả chi tiết.

## 🌟 Tính năng
- **Sinh mô tả bằng CLIP-MT5:** Tạo mô tả hình ảnh sử dụng mô hình CLIP-MT5.
- **Sinh mô tả bằng CLIP-MBART:** Tạo mô tả hình ảnh sử dụng mô hình CLIP-MBART.
- **Hỗ trợ đa mô hình:** Cung cấp các endpoint để lựa chọn giữa hai mô hình sinh mô tả tiên tiến.

## 🛠️ Yêu cầu hệ thống

Trước khi chạy dự án, hãy đảm bảo bạn đã cài đặt các dependencies sau:
- Python 3.x __(khuyến nghị 3.10.13)__
- Flask 3.1.0
- Transformers 4.47.1
- Flask-CORS 5.0.0
- Pillow 11.0.0
- PyTorch (tương thích với mô hình)

Bạn có thể cài đặt tất cả các thư viện trên bằng cách chạy:

```
pip install -r requirements.txt
```

## 🚀 Bắt đầu thôi!
1. Clone dự án về
```
git clone https://github.com/Havold/CS406-Image-Captioning-BE.git
cd CS406-Image-Captioning-BE.git
```
2. Chuẩn bị mô hình

Đảm bảo các mô hình sau được tải xuống và lưu trong thư mục dự án:
- `clip_mt5_base_model`: Chứa các file như `config.json`, `model.safetensors`, v.v.
- `clip_mbart_model`: Các file của mô hình đã được huấn luyện trước.
2. Cài đặt các dependencies:
```
pip install -r requirements.txt
```
4. Chạy Flask server:
```
python app.py
```
5. Server sẽ chạy ở: http://localhost:5000.

## ❗ API Endpoints
**1. Sinh mô tả ảnh bằng CLIP-MT5**
   - **URL**: `/clip-mt5`
   - **Method**: `POST`
   - **Parameters**:
      - `image`: File ảnh (PNG, JPG, JPEG).
   - **File**: Tệp ảnh (JPEG/PNG).
   - **Response**: Một object JSON chứa mô tả được sinh ra.
   - Ví dụ sử dụng (Postman):
      - URL:
        ```
         POST http://localhost:5000/clip-mt5
         ``` 
      - Form-data:
         - `image`: (Chọn file ảnh từ máy của bạn)
      - Kết quả:
        ```
         {
           "caption": "Khung cảnh núi non vào lúc hoàng hôn."
         }
        ```
**2. Sinh mô tả ảnh bằng CLIP-MBART**
   - **URL**: `/clip-mbart`
   - **Method**: `POST`
   - **Parameters**:
      - `image`: File ảnh (PNG, JPG, JPEG).
   - **File**: Tệp ảnh (JPEG/PNG).
   - **Response**: Một object JSON chứa mô tả được sinh ra.
   - Ví dụ sử dụng (Postman):
      - URL:
        ```
         POST http://localhost:5000/clip-mbart
         ``` 
      - Form-data:
         - `image`: (Chọn file ảnh từ máy của bạn)
      - Kết quả:
        ```
         {
           "caption": "Khung cảnh núi non vào lúc hoàng hôn."
         }
        ```
## 🔥 Sử dụng
Khi server đã chạy, bạn có thể kiểm tra ứng dụng bằng cách gửi các yêu cầu qua các công cụ như `Postman` hoặc thông qua một ứng dụng frontend để tương tác với API.
