from fastapi import FastAPI
from infrastructure.user_controller import router as user_router

def create_app() -> FastAPI:
    app = FastAPI(title="User API")
    app.include_router(user_router, prefix="/users")
    return app
