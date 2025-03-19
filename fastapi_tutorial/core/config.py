from pydantic_settings import BaseSettings
from pydantic import ConfigDict


# 애플리케이션 설정을 관리하는 클래스입니다.
# Pydantic의 BaseSettings를 상속받아 환경 변수로부터 설정을 로드합니다.
class Settings(BaseSettings):
    # 데이터베이스 로그 출력을 제어하는 설정
    DB_ECHO_LOG: bool = False
    # 비동기 데이터베이스 URL 설정
    ASYNC_DATABASE_URL: str
    # 동기 데이터베이스 URL 설정
    SYNC_DATABASE_URL: str

    # 환경 변수 파일(.env)로부터 설정을 로드하고, 추가 필드를 허용하도록 설정합니다.
    model_config = ConfigDict(env_file=".env", extra="allow")


# Settings 클래스의 인스턴스를 생성하여 설정을 전역적으로 사용할 수 있도록 합니다.
settings = Settings()
