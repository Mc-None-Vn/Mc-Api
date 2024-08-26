from easy_pil import Editor, Canvas, Font
from io import BytesIO
from fastapi import APIRouter, Response, HTTPException, Query
import requests


router = APIRouter()

@router.get("/api/card/rp_card/")
def param(avatar: str, name: str=None, description: str=None, age: str=None, sex: str=None, nation: str=None, birthday: str=XX / XX / XXXX):
    
    canvas = Canvas((350, 200), color="black")


    avatar_response = requests.get(avatar)
    if avatar_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Khong the tai anh dai dien.")
    perfil = Editor(BytesIO(avatar_response.content)).resize((100,100))


    fondo = Editor(canvas)


    poppins = Font.poppins(size=15, variant="bold")
    fondo.rectangle((-2, 50), width=450, height=200, color=(153,153,153,255), radius=1)
    fondo.paste(perfil, (30,70), radius=5)


    poppins = Font.poppins(size=15, variant="bold")
    fondo.text((26, 20), text="Thẻ Thông Tin Cá Nhân",font=poppins ,color="white")

    NOM = Font.poppins(size=12, variant="bold")
    fondo.text((157, 75), text=f"Họ và Tên: {name}",font=NOM ,color="black")


    fondo.text((157, 95), text=f"Mô tả: {description}",font=NOM ,color="black")


    fondo.text((157, 116), text=f"Tuổi: {age}",font=NOM ,color="black")


    fondo.text((157, 135), text=f"Giới tính:{sex} ",font=NOM ,color="black")

    fondo.text((157, 155), text=f"Quốc tịch: {nation}",font=NOM ,color="black")

    fondo.text((157, 175), text=f"Sinh nhật: {birthday}",font=NOM ,color="black")


    NOM2 = Font.poppins(size=8, variant="bold")
    fondo.text((28, 180), text="Đây không phải thông tin thật!",font=NOM2 ,color="black")

    img_buffer = BytesIO()
    fondo.image.save(img_buffer, format="PNG")
    img_buffer.seek(0)
    return Response(content=img_buffer.getvalue(), media_type="image/png")

