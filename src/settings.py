import pytz
from pydantic import (
    BaseSettings,
    AnyHttpUrl,
    SecretStr,
    HttpUrl,
)

class Settings(BaseSettings):
    LOCAL_TZ = pytz.timezone("Europe/Copenhagen")

class OpenAiSettings(BaseSettings):
    OPENAI_BASE_URL: str="https://api.openai.com"
    OPENAI_API_KEY: SecretStr="OPENAI_API_KEY"
    OPENAI_ORG_ID: SecretStr="OPENAI_ORG_ID"

settings = Settings()
openaisettings = OpenAiSettings()