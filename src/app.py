from fastapi import FastAPI, BackgroundTasks

from src.schemas.prediction import TextRequest, PredictionResult
from src.schemas.healthcheck import HealthcheckResult

from src.services.lifespan import LifespanLogging
from src.celery.start import celery

from loguru import logger
from datetime import datetime, timezone
import sys

from src.constants import TITLE, DESCRIPTION, VERSION, TIMEOUT
from src.constants import PREDICT_TASK_NAME


logger.add(sys.stderr, level="INFO")


app = FastAPI(title=TITLE, description=DESCRIPTION, version=VERSION, 
              lifespan=LifespanLogging.lifespan,
              debug=False
              )


@app.post("/predict/", response_model=PredictionResult, name="requests")
async def predict_emotion(text_request: TextRequest) -> PredictionResult:
    task = celery.send_task(PREDICT_TASK_NAME, args=[text_request.text])
    result = task.get(timeout=TIMEOUT)
    return result


@app.get("/healthcheck/", response_model=HealthcheckResult, name="healthcheck")
def get_health_check() -> HealthcheckResult:
    health_check = HealthcheckResult(is_alive=True, 
                                     date=datetime.now(timezone.utc).isoformat())
    return health_check
