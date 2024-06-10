from fastapi import FastAPI
from loguru import logger


class LifespanLogging:
    async def lifespan(app: FastAPI):
        # Logic at startup
        logger.info("Service initialized")
       
        yield
        # Logic at completion
        logger.info("Service shutdown")
