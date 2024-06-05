from fastapi import FastAPI
from loguru import logger
import os

class LifespanLogging:
    async def lifespan(app: FastAPI):
        # Logic at startup
        logger.info("Service initialized")
        
        logger.info(f"$CELERY_BROKER: {os.getenv('CELERY_BROKER')}")
        logger.info(f"$CELERY_BACKEND: {os.getenv('CELERY_BACKEND')}")
        
        yield
        # Logic at completion
        logger.info("Service shutdown")
