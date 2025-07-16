from fastapi import APIRouter, status
from src.models.model import Variety

fruits = APIRouter()

@fruits.post("/fruit", 
            tags=["notes"],
            description="Create a new fruit variety",
            response_description="The created fruit variety",
            responses={200: {"description": "Fruit created successfully"}},
            response_model=Variety,
            operation_id="create_fruit",
            summary="Create a fruit variety",             
            status_code=status.HTTP_200_OK)
async def fruit(variety: Variety):
    return variety