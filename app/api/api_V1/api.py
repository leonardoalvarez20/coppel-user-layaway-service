"""
Application API routes
"""

from fastapi import APIRouter, status

from app.api.api_V1.endpoints import layaway

api_router = APIRouter()

api_router.include_router(
    layaway.router,
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)
