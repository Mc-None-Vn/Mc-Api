from fastapi import APIRouter, Response, HTTPException
from easy_pil import Editor, Font
from io import BytesIO
import requests
import logging

router = APIRouter()

@router.get("/api/card/welcome/")
def get_custom_image(avatar: str, background: str, title: str="Welcome", description: str="Now has 10 members"):
    try:
        
        avatar_response = requests.get(avatar)
        if avatar_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Khong tai đuoc anh dai dien.")
        avatar_image = Editor(BytesIO(avatar_response.content)).resize((180, 180)).circle_image()

        
        background_response = requests.get(background)
        if background_response.status_code != 200:
            raise HTTPException(status_code=400, detail=f"Khong tai duoc hinh nen. Ma trang thai: {background_response.status_code}, Ly do: {background_response.reason}")
        background_image = Editor(BytesIO(background_response.content)).resize((800, 400)).image

        
        poppins = Font.poppins(size=50, variant="bold")
        poppins_small = Font.poppins(size=37.5, variant="regular")

       
        horizontal_shift = 67.5

       
        editor = Editor(background_image)

        
        editor.paste(avatar_image.image, (230 + horizontal_shift, 65))
        editor.ellipse((230 + horizontal_shift, 65), 180, 180, outline="white", stroke_width=5)

       
        editor.text((320 + horizontal_shift, 275), title, color="white", font=poppins, align="center")
        editor.text((320 + horizontal_shift, 332.5), description, color="white", font=poppins_small, align="center")

        
        img_buffer = BytesIO()
        editor.image.save(img_buffer, format="PNG")
        img_buffer.seek(0)

       
        return Response(content=img_buffer.getvalue(), media_type="image/png")
    
    except Exception as e:
        logging.error(f"Loi khi tao hinh anh: {e}")
        raise HTTPException(status_code=500, detail=str(e))
