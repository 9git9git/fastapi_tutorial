from fastapi import FastAPI
from fastapi import status
from fastapi_tutorial.api.v1.router import router
from fastapi_tutorial.db.base import init_db
import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):

    try:
        await init_db()
        yield
    except asyncio.CancelledError:
        pass
    finally:
        pass


app = FastAPI(
    title="FastAPI Tutorial",
    description="This is a simple tutorial for FastAPI",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get(
    "/ping",
    tags=["Health"],
    name="Heath check API",
    description="This is a health check API",
    status_code=status.HTTP_200_OK,
    response_model=str,
)
async def health_check():
    return "PONG"


app.include_router(router, prefix="/api/v1")
