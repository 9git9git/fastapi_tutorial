from fastapi_tutorial.schemas.base import CamelBaseModel
from uuid import UUID
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import model_validator


# TodoStatus Enum 정의 - 할 일의 상태를 나타내는 열거형 클래스입니다.
# 각 상태는 문자열로 정의되며, 데이터베이스 및 API에서 사용됩니다.
class TodoStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


# 기본 Todo 스키마 - 공통 필드를 정의하는 기본 클래스입니다.
# CamelBaseModel을 상속받아 camelCase 변환을 적용합니다.
class TodoBase(CamelBaseModel):
    title: str  # 할 일의 제목을 나타내는 필드
    content: str  # 할 일의 내용을 나타내는 필드


# Todo 생성 시 사용할 스키마 - 새로운 할 일을 생성할 때 사용됩니다.
# 기본 스키마에 추가 필드를 포함합니다.
class TodoCreate(TodoBase):
    status: TodoStatus = TodoStatus.NOT_STARTED  # 할 일의 초기 상태
    start_date: Optional[datetime] = None  # 시작 날짜 (선택적)
    end_date: Optional[datetime] = None  # 종료 날짜 (선택적)

    # 모델 검증기 - 날짜의 유효성을 검사합니다.
    @model_validator(mode="after")
    def validate_dates(self) -> "TodoCreate":
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValueError("종료 날짜는 시작 날짜 이후여야 합니다")
        return self


# 데이터베이스에서 가져온 Todo 정보를 반환할 스키마
# 데이터베이스의 Todo 객체를 API 응답으로 변환할 때 사용됩니다.
class Todo(CamelBaseModel):
    id: UUID  # 고유 식별자
    title: str  # 제목
    content: str  # 내용
    status: TodoStatus  # 상태
    start_date: Optional[datetime] = None  # 시작 날짜 (선택적)
    end_date: Optional[datetime] = None  # 종료 날짜 (선택적)
    created_at: datetime  # 생성된 날짜와 시간
    updated_at: datetime  # 마지막으로 수정된 날짜와 시간
