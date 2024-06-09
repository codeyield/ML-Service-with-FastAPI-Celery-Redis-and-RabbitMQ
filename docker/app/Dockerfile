# App
FROM python:3.10-slim

WORKDIR /app

# COPY pyproject.toml poetry.lock /app/
COPY pyproject.toml /app/

RUN pip install --no-cache-dir poetry

RUN poetry install --without=ml --no-interaction

# COPY ./src /app/src/
COPY tmain.py /app/

# CMD ["poetry", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["sh", "-c", "poetry run python tmain.py"]
