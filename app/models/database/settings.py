from pydantic_settings import SettingsConfigDict

from settings import AppSettings


class Settings(AppSettings):
    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_"
    )

    host: str
    port: str
    user: str
    password: str
    database: str


config = Settings()
