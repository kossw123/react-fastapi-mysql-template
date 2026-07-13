from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    file_server_url: str
    database_url: str

    model_config = SettingsConfigDict(
        env_file="./infra/.env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
