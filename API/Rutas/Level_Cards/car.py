from easy_pil import Editor, Canvas, Font
from io import BytesIO
from fastapi import APIRouter, Response, HTTPException
import requests
import random

router = APIRouter()

@router.get("/api/level/level_up/")
def level(avatar: str, username: str, level:int):
    if not str(level).isdigit(): 
        level = 1
       
    canvas = Canvas((700, 130), color=(0, 0, 0, 0))
    editor = Editor(canvas.image)

   
    avatar_response = requests.get(avatar)
    if avatar_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Khong tai duoc anh dai dien.")
    profile = Editor(BytesIO(avatar_response.content)).resize((101, 101)).circle_image()

   
    texts = ["<a:Mc_Giveaway1:1277106976463126620>", "<a:Mc_Giveaway2:1277107011531837491>", "<a:Mc_Giveaway3:1277107033988010116>", "<a:Mc_Giveaway4:1277107067651625032>", "<a:Mc_Giveaway5:1277107089004695594>", "<a:Mc_Giveaway6:1277107108776644651>", "<a:Mc_Giveaway7:1277107132914860143>", "<a:Mc_Giveaway8:1277107153680990269>"]
    random = print(random.choice(texts))
    poppins = Font.poppins(size=30)
    desplazamiento_x = 17  
    editor.rectangle((110, 16), width=250, height=100, fill="#25262a", radius=15)
    editor.ellipse((30 + desplazamiento_x, 11), width=110, height=110, outline="white", stroke_width=8)
    editor.text((180, 57), f"Level Up {level}! (random)", font=poppins, color="white")
    editor.paste(profile.image, (35 + desplazamiento_x, 16))

    
    img_buffer = BytesIO()
    editor.image.save(img_buffer, format="PNG")
    img_buffer.seek(0)

       
    return Response(content=img_buffer.getvalue(), media_type="image/png")
