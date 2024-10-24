from fastapi import FastAPI, HTTPException, Query,APIRouter
from fastapi.responses import Response, JSONResponse, StreamingResponse
from API.Funcion_Ruta.loop import registrar_rutas_desde_directorio
import json
import requests
from io import BytesIO
from pydantic import BaseModel
import os
import importlib.util
app = FastAPI()


carpeta_api = os.path.join(os.path.dirname(__file__), 'API')
router_principal = APIRouter()

registrar_rutas_desde_directorio(router_principal, carpeta_api)
app.include_router(router_principal)

@app.get("/")
def on_router():
    return "index.html"

@app.get("/api/")
def on_router():
    return Response(json.dumps({"status": 200, "data": {"message": "Mc API co: /level/, /card/"}}, indent=2), media_type="application/json", status_code=200)

@app.get("/api/level/")
def on_router():
    return Response(json.dumps({"status": 200, "data": {"message": "API Level co: /level_up, /level_card, /auto_level"}}, indent=2), media_type="application/json", status_code=200)
