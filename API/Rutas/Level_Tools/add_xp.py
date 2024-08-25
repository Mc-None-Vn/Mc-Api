from fastapi import APIRouter

router = APIRouter()

@router.get("/api/level/auto_level/")
def xp(xp: int, req: int, level: int, add: int):
    xp += add

    while xp >= req:
        xp -= req
        req *= 2
        level += 1
    
    return {"xp": xp, "req": req, "level": level}
