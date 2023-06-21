from fastapi import FastAPI
# import uvicorn

from app.api.routers import main_router
from app.core.config import settings

app = FastAPI()


app.include_router(main_router)