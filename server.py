from flask import Flask, request, jsonify
from transformers import CLIPProcessor, AutoTokenizer
from my_model.clip_mt5 import CLIPMT5ImageCaptioningModel  # Thay bằng lớp mô hình của bạn
from my_model.clip_mbart import CLIPMBartImageCaptioningModel
from PIL import Image
import io
import torch

app = Flask(__name__)

# Tải processor (cho CLIP) và tokenizer (cho mT5)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
# mt5_tokenizer = AutoTokenizer.from_pretrained("google/mt5-base")

# Tải mô hình đã fine-tuned
clip_mt5_model = CLIPMT5ImageCaptioningModel.from_pretrained("clip_mt5_base_model")
clip_mbart_model = CLIPMBartImageCaptioningModel.from_pretrained("clip_mbart_model")

def generate_caption(model):
    # Kiểm tra xem có file ảnh không
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    
    # Đọc file ảnh
    try:
        image = Image.open(io.BytesIO(file.read())).convert("RGB")
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    # Chuẩn hóa ảnh để phù hợp với mô hình
    inputs = processor(images=image, return_tensors="pt")

    # Chạy inference để lấy đầu ra của mô hình
    pixel_values = inputs["pixel_values"]
    output_ids = model.generate(pixel_values)

    # Đảm bảo output_ids là danh sách
    if isinstance(output_ids, torch.Tensor):
        output_ids = output_ids.tolist()  # Chuyển tensor sang list

    # Giải mã output_ids để lấy caption
    captions = output_ids[0]

    # Trả về caption dưới dạng JSON
    return jsonify({'captions': captions}), 200


@app.route('/clip-mt5', methods=['POST'])
def generate_caption_clip_mt5():
    return generate_caption(clip_mt5_model)


@app.route('/clip-mbart', methods=['POST'])
def generate_caption_clip_mbart():
    return generate_caption(clip_mbart_model)

if __name__ == '__main__':
    app.run(debug=True)
