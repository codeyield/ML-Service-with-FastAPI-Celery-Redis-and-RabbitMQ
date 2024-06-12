from fastapi import FastAPI

from src.schemas.prediction import TextRequest, PredictionResult
from src.schemas.healthcheck import HealthcheckResult

from src.services.lifespan import LifespanLogging
from src.celery.start import celery

from loguru import logger
from datetime import datetime, timezone
import toml
import sys

from src.constants import PREDICT_TASK_NAME, TIMEOUT


logger.add(sys.stderr, level="INFO")
cfg = toml.load('pyproject.toml')


app = FastAPI(title=cfg['tool']['poetry']['name'], 
              description=cfg['tool']['poetry']['description'], 
              version=cfg['tool']['poetry']['version'], 
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
