"""
Handles User Operation
"""
from bson import ObjectId
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.services.api_client import APIRequest

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class UserService:
    def __init__(self) -> None:

        self.user_service_client = APIRequest(
            base_url="http://localhost:8000/api/v1/",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )

    def __call__(self, token: str = Depends(oauth2_scheme)):
        """
        Validates token
        """
        header_auth = {"Authorization": f"Bearer {token}"}
        response = self.user_service_client.send_request(
            method="GET", route="users/me", **{"headers": header_auth}
        )

        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(
                detail=response.text, status_code=response.status_code
            )

        return ObjectId(response.json()["_id"])
