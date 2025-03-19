from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_tutorial.db.base import async_session_maker


# 데이터베이스 세션을 제공하는 비동기 제너레이터 함수입니다.
# FastAPI의 의존성 주입 시스템과 함께 사용되어 각 요청에 대해 데이터베이스 세션을 제공합니다.
# 예를 들어, API 엔드포인트에서 다음과 같이 사용할 수 있습니다:
# @app.get("/items/")
# async def read_items(db: AsyncSession = Depends(get_db)):
#     # db 세션을 사용하여 데이터베이스 작업을 수행합니다.
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    # 비동기 세션을 생성하고 관리합니다.
    async with async_session_maker() as session:
        try:
            yield session  # 세션을 호출자에게 반환하여 데이터베이스 작업을 수행할 수 있게 합니다.
            await session.commit()  # 작업이 성공적으로 완료되면 트랜잭션을 커밋합니다.
        except Exception:
            await session.rollback()  # 예외가 발생하면 트랜잭션을 롤백하여 변경 사항을 취소합니다.
            raise  # 예외를 다시 발생시켜 호출자에게 알립니다.
        finally:
            await session.close()  # 세션을 닫아 연결을 정리합니다.
