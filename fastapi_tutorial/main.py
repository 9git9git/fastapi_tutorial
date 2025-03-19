from fastapi import FastAPI
from fastapi import status
from fastapi_tutorial.api.v1.router import router

app = FastAPI(
    title="FastAPI Tutorial",
    description="This is a simple tutorial for FastAPI",
    version="0.1.0",
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
