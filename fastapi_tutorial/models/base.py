from sqlalchemy.orm import DeclarativeBase


# Base 클래스는 SQLAlchemy의 모든 ORM 모델 클래스가 상속받는 기본 클래스입니다.
# 이 클래스는 데이터베이스 테이블과 매핑되는 ORM 모델을 정의하는 데 사용됩니다.
class Base(DeclarativeBase):
    pass  # 이 클래스 자체는 비어 있지만, 상속받는 클래스들이 테이블을 정의하게 됩니다.


# DeclarativeBase는 SQLAlchemy의 선언적 매핑(declarative mapping)을 지원하는 기본 클래스입니다.
# 선언적 매핑은 Python 클래스를 데이터베이스 테이블에 매핑하는 방식으로, 클래스의 속성을 테이블의 컬럼으로 정의합니다.
# 이를 통해 ORM 모델을 더 직관적이고 간결하게 정의할 수 있습니다.
