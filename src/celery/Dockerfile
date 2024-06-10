# Celery worker
FROM python:3.10-slim

WORKDIR /app

# COPY pyproject.toml poetry.lock /app/
COPY pyproject.toml /app/

RUN pip install --no-cache-dir poetry
RUN poetry install --without=ml --no-interaction

# COPY tworker.py /app/
COPY . /app/src/

# CMD ["sh", "-c", "poetry run celery -A tworker.celery_app worker --loglevel=info --logfile=/logs/celery.log"]
CMD ["sh", "-c", "poetry run celery -A src.celery.worker.celery worker --loglevel=info --logfile=/logs/celery.log"]
