FROM python:3.10-slim

WORKDIR /app

# COPY pyproject.toml poetry.lock /app/
COPY pyproject.toml /app/

RUN pip install --no-cache-dir poetry

RUN poetry install --without=ml --no-interaction

# COPY ./src /app/src/
COPY tworker.py /app/

# CMD ["sh", "-c", "poetry run celery -A src.worker.tasks.celery --loglevel=info --logfile=/logs/celery.log"]
CMD ["sh", "-c", "poetry run celery -A tworker.celery_app worker --loglevel=info --logfile=/logs/celery.log"]
