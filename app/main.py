from typing import Annotated

from fastapi import Depends, FastAPI

from app.core.config import Settings, get_settings

app = FastAPI(title="TeamFlow API", version="0.1.0")


@app.get("/health")
async def health() -> dict[str, str]:
    """Liveness check used by load balancers and Docker."""
    return {"status": "ok"}


@app.get("/info")
async def info(
    settings: Annotated[Settings, Depends(get_settings)],
) -> dict[str, str | bool]:
    return {
        "app": settings.app_name,
        "environment": settings.environment,
        "debug": settings.debug,
    }
