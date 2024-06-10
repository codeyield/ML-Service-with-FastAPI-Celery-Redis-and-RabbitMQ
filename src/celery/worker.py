from loguru import logger

from src.celery.start import celery
from src.services.model import EmotionClassifier

from src.constants import PREDICT_TASK_NAME


@celery.task(name=PREDICT_TASK_NAME, bind=True)
def analyze_sentiment(self, text):
    try:
        logger.info(f"Starting prediction task {self.request.id}")
        
        # Launch main inference for prediction
        sentiment = EmotionClassifier.predict_emotion(text)
        
        logger.info(f"Input text: {text}")
        logger.info(f"Predicted: {str(sentiment)}")
        logger.info(f"Completing prediction task {self.request.id}")
    
    except Exception as e:
        logger.exception(f"Prediction task error {self.request.id}: {e}")

    return sentiment
