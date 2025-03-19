from pydantic import BaseModel, ConfigDict
from fastapi_tutorial.utils.to_camel import to_camel


# CamelBaseModel은 모든 Pydantic 스키마의 기본 클래스로 사용됩니다.
# 이 클래스는 JSON 직렬화 시 camelCase 변환을 적용하여 클라이언트와의 데이터 교환을 일관되게 유지합니다.
class CamelBaseModel(BaseModel):
    """모든 스키마의 기본 클래스로, camelCase 변환을 적용합니다."""

    # model_config는 Pydantic의 설정을 정의하는 데 사용됩니다.
    # from_attributes: 모델 인스턴스를 생성할 때 속성에서 값을 가져올 수 있도록 허용합니다.
    # populate_by_name: 필드 이름을 사용하여 값을 설정할 수 있도록 허용합니다.
    # alias_generator: 필드 이름을 camelCase로 변환하는 함수(to_camel)를 지정합니다.
    model_config = ConfigDict(
        from_attributes=True,  # 모델 인스턴스를 생성할 때 속성에서 값을 가져올 수 있도록 허용
        populate_by_name=True,  # 필드 이름을 사용하여 값을 설정할 수 있도록 허용
        alias_generator=to_camel,  # 필드 이름을 camelCase로 변환하는 함수 지정
    )


# BaseModel은 Pydantic의 기본 모델 클래스로, 데이터 검증 및 직렬화를 지원합니다.
# CamelBaseModel은 BaseModel을 상속받아 camelCase 변환을 추가로 적용합니다.
# 이는 클라이언트와 서버 간의 데이터 교환 시 일관된 네이밍 컨벤션을 유지하는 데 유용합니다.
