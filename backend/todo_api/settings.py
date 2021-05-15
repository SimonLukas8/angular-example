from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_folder = Field("../database", env="DB_FOLDER")
    production = Field(False, env="PRODUCTION")
    spoof_user = Field(True, env="SPOOF_USER")


SETTINGS = Settings()
