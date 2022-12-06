"""
Handles User Operation
"""
from bson import ObjectId
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.services.api_client import APIRequest

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class SearchService:
    def __init__(self) -> None:

        self.user_service_client = APIRequest(
            base_url="http://coppel-search-service-app:8001/api/v1/",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )

    def search(self, comic: str):
        """
        Search if layaway Comic exists
        """
        response = self.user_service_client.send_request(
            method="GET", route="searchComics", params={"comic": comic}
        )

        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(
                detail=response.text, status_code=response.status_code
            )

        response_data = response.json()

        if not response_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"There is no comics available with search criteria: {comic}",
            )
