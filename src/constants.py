# Celery parameters
CELERY_BROKER = 'amqp://guest:guest@rabbitmq3:5672/'
CELERY_BACKEND = 'redis://redis:6379/0'

# Task job name
PREDICT_TASK_NAME = "analyze_sentiment"

# Set a workload-aware timeout so that the inference
# of the prediction model has time to return a response
TIMEOUT = 30
