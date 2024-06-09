# poetry run celery -A tworker.celery_app worker --loglevel=info --logfile=.logs/celery.log

from celery import Celery
import os

# celery_app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')
# celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# print(f"$CELERY_BROKER: {os.getenv('CELERY_BROKER')}")
# print(f"$CELERY_BACKEND: {os.getenv('CELERY_BACKEND')}")


# celery_app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

celery_app = Celery('tasks', 
                    broker='amqp://guest:guest@rabbitmq3:5672/', 
                    backend='redis://redis:6379/0'
)

celery_app.conf.update({
    'broker_connection_retry': True,  
    'broker_connection_retry_on_startup': True, 
})

@celery_app.task(name='hello_world')
def hello_world():
    return 'Hello, World!'
