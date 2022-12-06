"""
Layaway Schemas
"""
from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from app.schemas.types.pyobjectid import PyObjectId


class LayawayCreateRequest(BaseModel):
    """
    Layaway creatation attributes
    """

    comic_id: int
    title: str
    qty_layaway_pieces: int


class LayawayCreateDB(BaseModel):
    """
    Layaway creatation attributes for DB
    """

    user_id: PyObjectId = Field(default_factory=PyObjectId)
    comic_id: int
    title: str
    qty_layaway_pieces: int
    created_at: datetime = datetime.now()


class LayawayInDBBase(BaseModel):
    """
    Layaway In DB
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId = Field(default_factory=PyObjectId)
    comic_id: int
    title: str
    qty_layaway_pieces: int
    created_at: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
