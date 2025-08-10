from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.ai.chain import test_chain
from app.config import settings

app = FastAPI(
    title="AI Backend",
    description="AI Backend Server",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/health")
async def health_check():
    return {"code": 200, "status": "healthy"}


@app.get("/test")
async def health_check():
    return await test_chain.ainvoke()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
