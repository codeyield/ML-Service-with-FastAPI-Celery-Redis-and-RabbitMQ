# Model Service API

Example The ML Service is a web application that provides an API for interacting with a machine learning model. It allows users to send queries with prediction data and get results back.

**FastAPI**, **Celery**, **RabbitMQ** and **Redis** are used to create a system capable of asynchronously analysing the emotional colouring of texts.

## Startup logic

Operating Logic:

- The client sends an HTTP request with text data to FastAPI.
- FastAPI receives the request, checks it and sends the task to Celery for processing via RabbitMQ.
- Celery gets the task from the queue and sends it to the ML model to analyse the text, processes the response and returns the result.
- While processing the query, Celery can use Redis to cache intermediate results to speed up repeated queries with the same data.
- The result is returned back via RabbitMQ to FastAPI, which sends it back to the client as an HTTP response.

When launched, the application initializes FastAPI, which handles HTTP requests. The app also connects to the machine learning model and loads it into memory for use in making predictions.

```
.
├── .docker
│   └── Dockerfile              # Docker image with app
├── docker-compose.yml          # Docker container managing
├── pyproject.toml              # Dependencies
└── src
    ├── app.py                  # Main app, FastAPI initializing
    ├── constansts.py           # Global app constants
    ├── schemas                 # Package with data models
    │   ├── healthcheck.py      # Model for service state responses
    │   └── requests.py         # Model for input requests to the API
    ├── services                # Package with ML model
    │   ├── model.py            # ML model with prediction
    │   └── utils.py            # Supporting utilities
    └── worker                  # Package with worker(s)
        └── tasks.py            # Celery worker
```

## Launching with Docker Compose

`docker-compose up --build`

### Web-server on

`http://localhost:8000`

### UI and API Docs

`http://localhost:8000/docs`

### Testing

```
curl -X 'POST' \
  'http://localhost:8000/api/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hey, what's up? What's new?"
}'
```

## Launching locally

`pip install --no-cache-dir poetry`

`poetry install --no-dev`

`poetry run uvicorn src.app:app --host localhost --port 8000`
