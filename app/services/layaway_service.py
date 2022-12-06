"""
Handles Layaway operations
"""
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.db.database import Layaway
from app.schemas import (
    LayawayCreateDB,
    LayawayCreateRequest,
    LayawayInDBBase,
    PyObjectId,
)
from app.services.search_service import SearchService


class LayawayService:
    def create(self, user_id: PyObjectId, layaway_in: LayawayCreateRequest):
        """
        Creates a Layaway for User
        """

        search_service = SearchService()
        search_service.search(layaway_in.title)

        layaway_create = LayawayCreateDB(user_id=user_id, **layaway_in.dict())

        layaway_iserted = Layaway.insert_one(layaway_create.dict())

        return jsonable_encoder(
            LayawayInDBBase(
                **{"_id": layaway_iserted.inserted_id, **layaway_create.dict()}
            )
        )

    def find_by_user_id(self, user_id: PyObjectId):
        """
        Find Layaways by user_id
        """

        results = []
        founded_layaways = Layaway.find({"user_id": user_id})
        for layaway in founded_layaways:
            results.append(LayawayInDBBase(**layaway))

        return jsonable_encoder(results)
