from celery import Celery
from src.constants import CELERY_BROKER, CELERY_BACKEND


celery = Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)

celery.conf.update({
    'broker_connection_retry': True,  
    'broker_connection_retry_on_startup': True, 
})
