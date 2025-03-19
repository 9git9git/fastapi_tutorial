from fastapi import APIRouter, Depends, Query, HTTPException, status, Request
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession


from fastapi_tutorial.db.session import get_db
from fastapi_tutorial.models.todo import TodoStatus
from fastapi_tutorial.schemas.todo import Todo, TodoCreate
from fastapi_tutorial.services.todo import get_all_todos, create_new_todo

# APIRouter 인스턴스를 생성하여 여러 엔드포인트를 그룹화하고 관리합니다.
# 이는 경로 작업(라우트)을 정의하고 구성하는 데 사용됩니다.
router = APIRouter()


# 할 일 목록을 조회하는 엔드포인트입니다.
# GET 요청을 처리하며 Todo 객체의 리스트를 반환합니다.
@router.get("/", response_model=List[Todo])
async def read_todos(
    # Query 매개변수를 사용하여 선택적으로 상태 필터링을 허용합니다.
    status: Optional[TodoStatus] = Query(None, description="할 일 상태로 필터링"),
    # 의존성 주입을 통해 데이터베이스 세션을 가져옵니다.
    db: AsyncSession = Depends(get_db),
):
    """
    모든 할 일 목록을 조회합니다.
    선택적으로 상태로 필터링할 수 있습니다.
    """
    try:
        # 서비스 계층을 호출하여 데이터를 가져옵니다.
        todos = await get_all_todos(db, status)
        return todos
    except Exception as e:
        # 예상치 못한 오류 발생 시 500 에러를 반환합니다.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"서버 오류가 발생했습니다: {str(e)}",
        )


# 새로운 할 일을 생성하는 엔드포인트입니다.
# POST 요청을 처리하며 생성된 Todo 객체를 반환합니다.
@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(
    # 요청 본문에서 TodoCreate 스키마를 파싱합니다.
    todo: TodoCreate,
    # 의존성 주입을 통해 데이터베이스 세션을 가져옵니다.
    db: AsyncSession = Depends(get_db),
):
    """
    새로운 할 일을 생성합니다.
    """
    try:
        # 서비스 계층을 호출하여 새 할 일을 생성합니다.
        return await create_new_todo(db, todo)
    except Exception as e:
        # 예상치 못한 오류 발생 시 500 에러를 반환합니다.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"서버 오류가 발생했습니다: {str(e)}",
        )
