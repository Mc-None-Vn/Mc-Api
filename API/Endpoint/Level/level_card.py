from easy_pil import Editor, Canvas, Font
from io import BytesIO
from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import FileResponse
from API.Funciones_API.convert_k_m import abreviar_numero
import os
import shutil
import uuid
import requests

router = APIRouter()

# Thư mục lưu trữ ảnh
UPLOAD_DIR = 'uploads/'
STATIC_URL = '/static/uploads/'

# Tạo thư mục nếu chưa tồn tại
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/api/level/card/")
def rank(avatar: str, username: str, level: str, req: str, xp: str, color_bg: str, color_xp: str, color_font: str, color_xp_bg: str):
    background = Editor(Canvas((800, 200), color="#23272a"))

    avatar_response = requests.get(avatar)
    if avatar_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Không tải được ảnh đại diện.")
    profile = Editor(BytesIO(avatar_response.content)).resize((120, 120)).circle_image()

    background.paste(profile, (15, 14))

    card_right_shape = [(520, 0), (750, 300), (900, 300), (900, 0)]
    background.polygon(card_right_shape, color_bg)

    # Đường trắng
    background.rectangle((15, 148), width=608, height=35, fill=f"{color_xp_bg}", radius=17)

    req = float(req)
    xp = float(xp)
    porcentaje = (xp / req) * 100
    porcentaje = int(min(porcentaje, 100))

    # Áp dụng tỷ lệ phần trăm cho thanh
    background.bar((15, 148), max_width=608, height=35, percentage=porcentaje, fill=f"{color_xp}", radius=17)

    # Dòng bên dưới văn bản op
    background.rectangle((150, 80 + 4), width=145, height=2, fill=color_bg)

    poppins = Font.poppins(size=35)
    background.text((150, 37 + 4), username, font=poppins, color=f"{color_font}")

    poppins = Font.poppins(size=25)
    background.text((145, 107), f"Level: {int(level)}          XP: {abreviar_numero(int(xp))} / {abreviar_numero(int(req))}", font=poppins, color=f"{color_font}")

    img_buffer = BytesIO()
    background.image.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    # Tạo tên file ngẫu nhiên
    file_name = f"{uuid.uuid4().hex}.png"
    file_path = os.path.join(UPLOAD_DIR, file_name)

    # Lưu ảnh vào thư mục
    with open(file_path, 'wb') as f:
        shutil.copyfileobj(img_buffer, f)

    # Tạo URL của ảnh
    image_url = f"{STATIC_URL}{file_name}"

    return {"image_url": image_url}

# Định nghĩa endpoint để phục vụ các tệp tĩnh
@router.get("/static/uploads/{file_name}")
async def serve_file(file_name: str):
    file_path = os.path.join(UPLOAD_DIR, file_name)
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)
