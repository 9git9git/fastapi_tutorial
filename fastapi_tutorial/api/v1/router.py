from fastapi import APIRouter
from fastapi_tutorial.api.v1.endpoints import todo

# APIRouter 인스턴스를 생성하여 여러 엔드포인트를 그룹화하고 관리합니다.
router = APIRouter()

# todos 모듈에서 정의한 라우터를 포함시킵니다.
# 'tags'는 API 문서화 시 사용될 태그를 지정하며, 'prefix'는 모든 엔드포인트 경로에 추가될 경로 접두사를 설정합니다.
router.include_router(todo.router, tags=["todo"], prefix="/todos")
