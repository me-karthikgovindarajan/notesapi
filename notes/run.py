import uvicorn
from fastapi import FastAPI
from src.routes.root import routers as root_router


def make_app() -> FastAPI:
    app = FastAPI(title="Notes API",
                description="Rest api for test notes app.",
                version="0.1.0",                
                docs_url="/docs")
    app.include_router(root_router)
    return app


if __name__ == "__main__":
    uvicorn.run(
        app=make_app(),
        port=8000,
        reload=False        
    )