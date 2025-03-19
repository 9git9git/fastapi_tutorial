from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.future import select
from typing import Optional, List

from fastapi_tutorial.models.todo import Todo, TodoStatus
from fastapi_tutorial.schemas.todo import TodoCreate


# 비동기적으로 할 일 목록을 가져오는 함수입니다.
# 선택적으로 특정 상태의 할 일만 필터링할 수 있습니다.
async def get_todos(
    db: AsyncSession, status: Optional[TodoStatus] = None
) -> List[Todo]:
    query = select(Todo)  # Todo 테이블에서 모든 레코드를 선택하는 쿼리를 생성합니다.

    if status:
        query = query.where(
            Todo.status == status
        )  # 상태가 지정된 경우 해당 상태로 필터링합니다.

    result = await db.execute(query)  # 데이터베이스에서 쿼리를 실행합니다.
    return result.scalars().all()  # 결과를 스칼라 값으로 변환하여 리스트로 반환합니다.


# 비동기적으로 새로운 할 일을 생성하는 함수입니다.
async def create_todo(db: AsyncSession, todo: TodoCreate) -> Todo:
    # TodoCreate 스키마를 기반으로 새로운 Todo 객체를 생성합니다.
    db_todo = Todo(
        title=todo.title,
        content=todo.content,
        status=todo.status,
        start_date=todo.start_date,
        end_date=todo.end_date,
    )
    db.add(db_todo)  # 세션에 새로운 Todo 객체를 추가합니다.
    await db.commit()  # 데이터베이스에 변경 사항을 커밋합니다.
    await db.refresh(
        db_todo
    )  # 데이터베이스에서 새로 생성된 Todo 객체를 새로고침하여 최신 상태로 업데이트합니다.
    return db_todo  # 생성된 Todo 객체를 반환합니다.
