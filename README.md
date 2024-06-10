# Hi-loaded Model Service API

This is an example of a web application that provides a highly loaded API to interact with the ML model. Here a pre-trained Transformer model is used to predict the sentiment for the input text.

**FastAPI**, **Celery**, **Redis** and **RabbitMQ** are used to create a system that processes a large stream of incoming requests in asynchronous mode.

## Operational logic

- The client sends an HTTP request with text data in json to the FastAPI endpoint.
- FastAPI receives the request, validates it and creates a new Celery task.
- Celery asynchronously queues the RabbitMQ broker running "under the bonnet".
- Celery Worker asynchronously fetches a task from the queue and sends it to the ML model, receives the response and returns the result.
- Redis is used to cache intermediate results to speed up repeated requests with the same data.
- The response is returned via RabbitMQ to FastAPI, which sends it back to the client as an HTTP response.

## Project structure

```
├── docker-compose.yml          # Docker container managing
└── src
    ├── Dockerfile              # Docker container for App & Worker
    ├── app.py                  # Main app, FastAPI initializing
    ├── constansts.py           # Global app's constants
    ├── entrypoint.sh           # Script for launching the App or Worker
    ├── pyproject.toml          # Dependencies
    ├── celery                  # Package with Celery & Worker
    │   ├── start.py            # Celery initializing
    │   └── worker.py           # Celery worker
    ├── schemas                 # Package with data models
    │   ├── healthcheck.py      # Schema for service health state responses
    │   └── prediction.py       # Schema for input requests to the API
    └── services                # Package with ML model & services
        ├── lifespan.py         # At startup & at completion logging
        └── model.py            # ML model with prediction
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
