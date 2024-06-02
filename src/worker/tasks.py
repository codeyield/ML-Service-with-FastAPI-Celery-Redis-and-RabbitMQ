from celery import Celery

from src.constants import RABBITMQ_BROKER, REDIS_BACKEND
from src.services.model import EmotionClassifier


celery_app = Celery('tasks', broker=RABBITMQ_BROKER, backend=REDIS_BACKEND)


@celery_app.task(name='analyze_sentiment')
def analyze_sentiment(text):
    sentiment = EmotionClassifier.predict_emotion(text)
    return sentiment
