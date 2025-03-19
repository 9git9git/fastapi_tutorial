from fastapi import APIRouter

# APIRouter 인스턴스를 생성하여 여러 엔드포인트를 그룹화하고 관리합니다.
router = APIRouter()


@router.get("/")
async def get_todos():
    return {"message": "Hello World"}
