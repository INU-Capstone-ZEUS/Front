from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return "root Router입니다."