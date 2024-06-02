from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from celery import Celery
from loguru import logger
from datetime import datetime, timezone

from src.constants import TITLE, DESCRIPTION, VERSION, TIMEOUT
from src.constants import RABBITMQ_BROKER, REDIS_BACKEND
from src.schemas.requests import TextRequest
from src.schemas.healthcheck import HealthcheckResult
from src.services.utils import return_current_time


app = FastAPI(title=TITLE, version=VERSION, debug=False, description=DESCRIPTION)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST"],
#     allow_headers=["*"],
# )

celery_app = Celery('tasks', broker=RABBITMQ_BROKER, backend=REDIS_BACKEND)


@app.post("/predict/")
async def predict_emotion(text_request: TextRequest, background_tasks: BackgroundTasks):
    task = celery_app.send_task("analyze_sentiment", args=[text_request.text])
    result = task.get(timeout=TIMEOUT)
    return result


@app.get("/healthcheck/", response_model=HealthcheckResult, name="healthcheck")
def get_health_check() -> HealthcheckResult:
    current_time = lambda: datetime.now(timezone.utc).isoformat()
    health_check = HealthcheckResult(is_alive=True, date=current_time)
    return health_check
