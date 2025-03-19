from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID as PgUUID
from datetime import datetime
from uuid import uuid4
from fastapi_tutorial.models.base import Base
from typing import Optional
from enum import Enum as PyEnum
from sqlalchemy.sql import func


# TodoStatus는 할 일의 상태를 나타내는 열거형 클래스입니다.
# 각 상태는 문자열로 정의되며, 데이터베이스에 저장될 때 사용됩니다.
class TodoStatus(str, PyEnum):
    NOT_STARTED = "NOT_STARTED"
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


# Todo 클래스는 'todo' 테이블과 매핑되는 SQLAlchemy ORM 모델입니다.
# 이 클래스는 할 일(Todo) 항목의 구조를 정의합니다.
class Todo(Base):
    __tablename__ = "todo"  # 데이터베이스에서 사용할 테이블 이름을 지정합니다.

    # 각 필드는 데이터베이스 테이블의 컬럼에 매핑됩니다.
    id: Mapped[PgUUID] = mapped_column(PgUUID, primary_key=True, default=uuid4)
    # 'id'는 기본 키로 사용되며, UUID 형식으로 자동 생성됩니다.

    title: Mapped[str] = mapped_column(String(255))
    # 'title'은 할 일의 제목을 저장하는 문자열 필드입니다.

    content: Mapped[str] = mapped_column(String(255))
    # 'content'는 할 일의 내용을 저장하는 문자열 필드입니다.

    status: Mapped[TodoStatus] = mapped_column(
        Enum(TodoStatus), default=TodoStatus.NOT_STARTED
    )
    # 'status'는 할 일의 현재 상태를 저장하며, TodoStatus 열거형을 사용합니다.

    start_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    # 'start_date'는 할 일이 시작된 날짜를 저장하며, 선택적 필드입니다.

    end_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    # 'end_date'는 할 일이 완료된 날짜를 저장하며, 선택적 필드입니다.

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),  # 데이터베이스 서버의 현재 시간을 기본값으로 사용
    )
    # 'created_at'은 할 일이 생성된 날짜와 시간을 저장하며, 기본값은 데이터베이스 서버의 현재 시간입니다.

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),  # 데이터베이스 서버의 현재 시간을 기본값으로 사용
        onupdate=func.now(),  # 업데이트 시 데이터베이스 서버의 현재 시간으로 갱신
    )
    # 'updated_at'은 할 일이 마지막으로 수정된 날짜와 시간을 저장하며,
    # 기본값은 데이터베이스 서버의 현재 시간이고, 업데이트 시 자동으로 갱신됩니다.
