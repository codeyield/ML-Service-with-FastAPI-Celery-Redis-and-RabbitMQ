FROM python:3.8-slim

WORKDIR /app

# COPY pyproject.toml poetry.lock /app/
COPY pyproject.toml /app/

RUN pip install --no-cache-dir poetry

RUN poetry install --no-dev

# COPY ./src /app/src/
COPY tmain.py tworker.py /app/

# COPY entrypoint.sh /app/
# RUN chmod +x entrypoint.sh

# CMD ["poetry", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["poetry", "run", "python", "tmain.py"]
