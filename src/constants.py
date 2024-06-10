TITLE = "Emotion classification service"
DESCRIPTION = "ML service for classifying emotions in text"
VERSION = "0.1.0"

PREDICT_TASK_NAME = "analyze_sentiment"

TIMEOUT = 20

CELERY_BROKER = 'amqp://guest:guest@rabbitmq3:5672/'
CELERY_BACKEND = 'redis://redis:6379/0'
