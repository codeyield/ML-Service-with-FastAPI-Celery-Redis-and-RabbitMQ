from celery import Celery
import os
# from src.constants import CELERY_BROKER, CELERY_BACKEND

celery = Celery(
    'tasks', 
    broker='redis://localhost:6379/0',  # os.getenv('CELERY_BROKER'),
    backend='redis://localhost:6379/0'  # os.getenv('CELERY_BACKEND')
)

celery.conf.update({
    'broker_connection_retry': True,  
    'broker_connection_retry_on_startup': True, 
})
