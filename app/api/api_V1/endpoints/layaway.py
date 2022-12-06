from typing import Any, List

from fastapi import APIRouter, Depends

from app import schemas
from app.services.layaway_service import LayawayService
from app.services.user_service import UserService

router = APIRouter()

user_service_instance = UserService()


def validate_token(user_id=Depends(user_service_instance)):
    return user_id


@router.post(
    "/addToLayaway",
    response_model=schemas.LayawayInDBBase,
    response_model_by_alias=False,
)
def create_layaway(
    layaway_in: schemas.LayawayCreateRequest,
    user_id: schemas.PyObjectId = Depends(validate_token),
    layaway_service: LayawayService = Depends(),
) -> Any:
    """
    Create a new Layaway.
    """
    return layaway_service.create(user_id=user_id, layaway_in=layaway_in)


@router.get(
    "/getLayawayList",
    response_model=List[schemas.LayawayInDBBase],
    response_model_by_alias=False,
)
def read_layaways(
    layaway_service: LayawayService = Depends(),
    user_id: schemas.PyObjectId = Depends(validate_token),
) -> Any:
    """
    Read Layaways from User
    """
    return layaway_service.find_by_user_id(user_id=user_id)
