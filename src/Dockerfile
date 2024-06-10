# Service API app
FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry
RUN poetry install --no-interaction

COPY . /app/src/

COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Depending on the value (defined in docker-compose.yml) 
#  the App or the Worker will be launched via entrypoint.sh
CMD ["./entrypoint.sh"]