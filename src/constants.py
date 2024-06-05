TITLE = "Emotion classification service"
DESCRIPTION = "ML service for classifying emotions in text"
VERSION = "0.1.0"

PREDICT_TASK_NAME = "analyze_sentiment"

TIMEOUT = 10

CELERY_BROKER = 'amqp://guest:guest@localhost:5672/%2F'   # Equivalent to // at the end
CELERY_BACKEND = 'rpc://'
# CELERY_BACKEND = 'redis://localhost:6379/1'
# CELERY_BROKER = 'redis://localhost:6379/0'       # 'redis://my_container_redis'
