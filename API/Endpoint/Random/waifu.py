from flask import Flask, jsonify, request
from fastapi import APIRouter, Response, HTTPException
import os
import uuid

router = APIRouter()

# Dữ liệu ảnh
images = [
    {"id": 1, "url": "https://example.com/image1.jpg"},
    {"id": 2, "url": "https://example.com/image2.jpg"},
    {"id": 3, "url": "https://example.com/image3.jpg"},
    #...
]

# Nhận ngẫu nhiên một ảnh
@router.get("/api/random/waifu")
def get_random_image():
    import random
    random_image = random.choice(images)
    return jsonify({"image": random_image})
  
