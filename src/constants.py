TITLE = "Emotion classification service"
DESCRIPTION = "ML service for classifying emotions in text"
VERSION = "0.1.0"

TIMEOUT = 60

RABBITMQ_BROKER = 'amqp://guest:guest@localhost:5672/%2F'   # Equivalent to // at the end
REDIS_BACKEND = 'redis://localhost:6379/1'                  # 'pyamqp://guest:guest@my_container_rabbitmq//'

# REDIS_BROKER = 'redis://localhost:6379/0'       # 'redis://my_container_redis'
# CELERY_BACKEND = 'rpc://'
