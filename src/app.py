from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.constants import TITLE, DESCRIPTION, VERSION, TIMEOUT
from src.constants import PREDICT_TASK_NAME

from src.schemas.prediction import TextRequest, PredictionResult
from src.schemas.healthcheck import HealthcheckResult

from src.middleware.logging import LoggingMiddleware
from src.middleware.cors import CustomCORSMiddleware

from src.services.model import EmotionClassifier
from src.services.lifespan import LifespanLogging

from celery.result import AsyncResult
from src.celery.celinit import celery

from loguru import logger
from datetime import datetime, timezone
import sys


logger.add(sys.stderr, level="INFO")


app = FastAPI(title=TITLE, description=DESCRIPTION, version=VERSION, 
              lifespan=LifespanLogging.lifespan,
              debug=False
              )



@app.post("/predict/", response_model=PredictionResult, name="requests")
async def predict_emotion(text_request: TextRequest) -> PredictionResult:
    task = celery.send_task(PREDICT_TASK_NAME, args=[text_request.text])
    result = task.get(timeout=TIMEOUT)
    
    # task_id = JSONResponse({"task_id": task.id})
    # task_result = AsyncResult(task_id)
    # return task_result

    result = EmotionClassifier.predict_emotion(text_request.text)
    return result


@app.get("/healthcheck/", response_model=HealthcheckResult, name="healthcheck")
def get_health_check() -> HealthcheckResult:
    health_check = HealthcheckResult(is_alive=True, 
                                     date=datetime.now(timezone.utc).isoformat())
    return health_check


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
