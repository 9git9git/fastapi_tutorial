from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import NullPool
from fastapi_tutorial.core.config import settings

# 비동기 SQLAlchemy 엔진을 생성합니다.
# 데이터베이스 URL과 로그 설정은 환경 변수에서 로드됩니다.
# 데이터베이스 엔진은 데이터베이스와의 연결을 관리하고 SQL 쿼리를 실행하는 역할을 합니다.
engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,  # 비동기 데이터베이스 URL을 사용하여 연결 설정
    echo=settings.DB_ECHO_LOG,  # SQLAlchemy가 실행하는 모든 SQL을 로그에 출력하여 디버깅에 도움
    future=True,  # SQLAlchemy의 최신 기능을 사용하도록 설정
    pool_pre_ping=True,  # 연결이 유효한지 확인하여 끊어진 연결을 자동으로 재연결
    poolclass=NullPool,  # 연결 풀을 사용하지 않도록 설정하여 각 연결이 독립적임
)

# 비동기 세션 메이커를 생성합니다.
# 세션 메이커는 데이터베이스와의 세션을 생성하고 관리하는 팩토리 역할을 합니다.
# 세션은 데이터베이스 트랜잭션을 캡슐화하며, ORM 객체와 데이터베이스 간의 상호작용을 관리합니다.
async_session_maker = async_sessionmaker(
    bind=engine,  # 생성된 엔진을 세션에 바인딩
    class_=AsyncSession,  # 비동기 세션 클래스를 사용하여 비동기 작업 지원
    expire_on_commit=False,  # 커밋 후 객체가 만료되지 않도록 설정하여 세션 외부에서도 객체 사용 가능
    autocommit=False,  # 자동 커밋을 비활성화하여 명시적인 트랜잭션 관리
    autoflush=False,  # 자동 플러시를 비활성화하여 명시적인 플러시 관리
)


# 데이터베이스 초기화를 위한 함수입니다.
# 데이터베이스 스키마를 생성합니다.
async def init_db():
    from fastapi_tutorial.models.base import Base

    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)  # 모든 테이블을 생성
    except Exception as e:

        raise e
