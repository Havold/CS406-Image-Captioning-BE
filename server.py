from flask import Flask, request, jsonify
from transformers import CLIPProcessor, AutoTokenizer
from my_model.clip_mt5 import CLIPMT5ImageCaptioningModel  # Import lớp tùy chỉnh đã định nghĩa
from my_model.clip_mbart import CLIPMBartImageCaptioningModel
from PIL import Image
import os
from flask_cors import CORS

# Khởi tạo Flask app
app = Flask(__name__)
CORS(app)

# Tải processor, tokenizer và mô hình
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
# tokenizer = AutoTokenizer.from_pretrained("google/mt5-base")
clip_mt5_model = CLIPMT5ImageCaptioningModel.from_pretrained("clip_mt5_base_model")
clip_mbart_model = CLIPMBartImageCaptioningModel.from_pretrained("clip_mbart_model")

@app.route("/clip-mt5", methods=["POST"])
def generate_caption():
    try:
        # Kiểm tra file trong request
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided."}), 400

        # Lấy file ảnh
        image_file = request.files['image']
        
        # Kiểm tra định dạng ảnh
        if not image_file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
            return jsonify({"error": "Unsupported file format. Please upload PNG, JPG, or JPEG."}), 400

        # Mở và xử lý ảnh
        image = Image.open(image_file).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")
        pixel_values = inputs["pixel_values"]

        # Sinh caption từ mô hình
        output_ids = clip_mt5_model.generate(pixel_values)
        caption = output_ids[0]

        return jsonify({"caption": caption})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/clip-mbart", methods=["POST"])
def generate_caption_clip_mbart():
    try:
        # Kiểm tra file trong request
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided."}), 400

        # Lấy file ảnh
        image_file = request.files['image']
        
        # Kiểm tra định dạng ảnh
        if not image_file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
            return jsonify({"error": "Unsupported file format. Please upload PNG, JPG, or JPEG."}), 400

        # Mở và xử lý ảnh
        image = Image.open(image_file).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")
        pixel_values = inputs["pixel_values"]

        # Sinh caption từ mô hình
        output_ids = clip_mbart_model.generate(pixel_values)
        caption = output_ids[0]

        return jsonify({"caption": caption})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)