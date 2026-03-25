from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    file_server_url: str
    database_url: str
    model_config = SettingsConfigDict(env_file="/home/user/react-fastapi-mysql-template/server/src/base-settings.py")

settings = Settings()