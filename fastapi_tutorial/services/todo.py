from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_tutorial.models.todo import TodoStatus
from fastapi_tutorial.models.todo import Todo
from fastapi_tutorial.schemas.todo import TodoCreate
from fastapi_tutorial.crud.todo import get_todos, create_todo

# 서비스 레이어는 비즈니스 로직을 캡슐화하고, CRUD 작업을 사용하여 데이터를 조작합니다.
# 컨트롤러(엔드포인트)와 데이터 액세스 레이어(CRUD) 사이의 중간 계층입니다.


# 모든 할 일 항목을 조회하는 서비스 함수입니다.
async def get_all_todos(
    db: AsyncSession, status: Optional[TodoStatus] = None
) -> List[Todo]:
    # 데이터베이스에서 할 일 목록을 가져옵니다.
    # 상태가 지정된 경우 해당 상태로 필터링합니다.
    return await get_todos(db, status)


# 새로운 할 일을 생성하는 서비스 함수입니다.
async def create_new_todo(db: AsyncSession, todo_data: TodoCreate) -> Todo:
    # 데이터베이스에 새 할 일을 생성합니다.
    return await create_todo(db, todo_data)
