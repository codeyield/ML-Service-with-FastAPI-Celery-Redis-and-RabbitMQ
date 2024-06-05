from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from loguru import logger

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next: RequestResponseEndpoint) -> Response:
        logger.info(f"Request: {request.method} {request.url.path}")
        
        response = await call_next(request)
        
        logger.info(f"Responce: {response.status_code}")
        return response
