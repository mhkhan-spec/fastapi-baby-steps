from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All configuration comes from environment variables (12-factor app)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "TeamFlow"
    environment: str = "local"
    debug: bool = False


@lru_cache
def get_settings() -> Settings:
    # Cached so we parse the environment once, not on every request.
    return Settings()
