# from celery import Celery
from src.celery.celinit import celery

# from src.services.model import EmotionClassifier
# from fastapi import BackgroundTasks
# from src.schemas.prediction import TextRequest
# from src.services.model import EmotionClassifier

from loguru import logger


@celery.task(name='analyze_sentiment', bind=True)
def analyze_sentiment(self, text):
    sentiment = {'label': 'TEST', 'score': 1.}
    return sentiment


# @celery.task(name='analyze_sentiment', bind=True)
# def analyze_sentiment(self, text):
#     try:
#         logger.info(f"Starting prediction task {self.request.id}")
        
#         # Prediction task (main inference)
#         # sentiment = EmotionClassifier.predict_emotion(text)
        
#         ### DEBUG START
#         sentiment = {'label': 'TEST', 'score': 1.}
#         ### DEBUG END
        
#         logger.info(f"Input text: {text}")
#         logger.info(f"Predicted: {sentiment}")
#         logger.info(f"Completing prediction task {self.request.id}")
    
#     except Exception as e:
#         logger.exception(f"Prediction task error {self.request.id}: {e}")

#     return sentiment

if __name__ == '__main__':
    args = ['worker', '--loglevel=INFO']
    celery.worker_main(argv=args)
