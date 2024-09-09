from flask import Flask, jsonify, request
import os
import uuid

app = Flask(__name__)

# Dữ liệu ảnh
images = [
    {"id": 1, "url": "https://example.com/image1.jpg"},
    {"id": 2, "url": "https://example.com/image2.jpg"},
    {"id": 3, "url": "https://example.com/image3.jpg"},
    #...
]

# Nhận ngẫu nhiên một ảnh
@app.route('/api/random_image', methods=['GET'])
def get_random_image():
    import random
    random_image = random.choice(images)
    return jsonify({"image": random_image})
  
