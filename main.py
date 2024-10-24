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

@app.get("/api/public/emojis")
def on_router():
    return Response(json.dumps({"status": 200, "data": {"Empty": "<:Mc_TangHinh:1267097733223940118>",
  "True": "<a:Mc_TrueIcon:1286674619633242166>",
  "False": "<a:Mc_FalseIcon:1285828621034065982>",
  "T-Arrow": "<a:Mc_TrueArrow:1280449874101534792>",
  "F-Arrow": "<a:Mc_FalseArrow:1280449893600591934>",
  "Moderator": "<:Mc_ModeratorIcon:1279604755664080916>",
  "Verify": "<:Mc_VerifyIcon:1279604736793772052>",
  "Tick": "<:Mc_TickIcon:1275003606327627828>",
  "Admin": "<:Mc_AdministratorIcon:1279604715876909056>",
  "A-Left": "<:Mc_LeftArrow:1275409626627571722>",
  "A-Right": "<:Mc_RightArrow:1275409505055670294>",
  "Msc": "$getVar[Msc;$authorID]",
  "List": ":clipboard:",
  "Normal": "<:Mc_IconNormal:1285914894239268865>",
  "Fun": ":smile:",
  "Info": "<a:Mc_IconInfo:1271406725760680059>",
  "Name": "<:Mc_NameCard:1273564965592109158>",
  "Owner": "<:Mc_OwnerIcon:1279596390959550535>",
  "Member": "<:Mc_MemberIcon:1279734703582220319>",
  "M-On": "<:Mc_IconOnline:1286678935425253387>",
  "M-Id": "<:Mc_IconIdle:1286679020100128868>",
  "M-Dnd": "<:Mc_IconDoNotDisturb:1287271977010200657>",
  "M-Off": "<:Mc_IconOffline:1286679446652325889>",
  "Boost": "<:Mc_ServerBoostIcon:1279590017802436793>",
  "Protect": "<:Mc_ProtectIcon:1271418300517191761>",
  "Emoji": "<:Mc_IconEmoji:1261971623360200787>",
  "Developer": "<:Mc_DeveloperIcon:1279722734401753088>",
  "VerifyBot": "<:Mc_MemberVerify:1279734787296202845>",
  "Ping": "<:Mc_PingIcon:1272873337479102476>",
  "Version": ":wrench:",
  "Cpr": "<:Mc_Copyright:1265473145960272024>",
  "Bank": "<:Mc_BankCard:1271406155155111970>",
  "Rod": "<:Mc_CanCau:1172527572198887516>",
  "Bait": "<:Mc_Bait:1271349787698004000>",
  "Cart": "<:Mc_ShoppingCart:1263502758070194206>",
  "Pre": {
    "1": "<:Mc_Premium1:1264076342371291278>",
    "2": "<:Mc_Premium2:1264076461963214959>",
    "3": "<:Mc_Premium3:1264076540174532709>",
    "4": "<:Mc_Premium4:1264076594839031850>"
  },
  "Ca": {
    "Thuong": "<:Mc_CaThuong:1170359432773902466>",
    "Hoi": "<:Mc_CaHoi:1170359586327384194>",
    "Tuyet": "<:Mc_CaTuyet:1170359518685827123>",
    "NhietDoi": "<:Mc_CaNhietDoi:1170359652987445288>"
  },
  "HopQua": "<:Mc_GiftBoxIcon:1286681296642244619>",
  "A-Slot": "<a:Mc_SlotDangQuay:1277913646680248320>",
  "A-Tx": "<a:Mc_TungXx:1248850629774938154>",
  "Reload": "<:Mc_IconReload:1280376810751787068>",
  "Rule": "<:Mc_RuleIcon:1259492975654735953>",
  "Slot": {
    "1": "<:Mc_Slots:1277803187797098528>",
    "2": "<:Mc_Slots:1277803218721706054>",
    "3": "<:Mc_Slots:1277803243300454472>",
    "4": "<:Mc_Slots:1277803264544604211>",
    "5": "<:Mc_Slots:1277803285209940031>",
    "6": "<:Mc_Slots:1277803314880446539>",
    "7": "<:Mc_Slots:1277803337114452020>",
    "8": "<:Mc_Slots:1277803361164333138>",
    "9": "<:Mc_Slots:1277803378591928330>",
    "10": "<:Mc_Slots:1277803400339263618>",
    "11": "<:Mc_Slots:1277803426809647174>",
    "12": "<:Mc_Slots:1277803449240522913>",
    "13": "<:Mc_Slots:1277803474184175617>",
    "14": "<:Mc_Slots:1277803504219586601>"
  },
  "Xx": {
    "1": "<:Mc_XucXac:1272883838896308325>",
    "2": "<:Mc_XucXac:1272883958094499850>",
    "3": "<:Mc_XucXac:1272884039145226332>",
    "4": "<:Mc_XucXac:1272884094446993472>",
    "5": "<:Mc_XucXac:1272884164542070797>",
    "6": "<:Mc_XucXac:1272884214051770369>"
  }
}}, indent=2), media_type="application/json", status_code=200)
