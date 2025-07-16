from fastapi import APIRouter, status
from src.models.model import Variety

meats = APIRouter()

@meats.post("/meats", 
            tags=["notes"],
            description="Create a new meat variety",
            response_description="The created meat variety",
            responses={200: {"description": "Meat created successfully"}},
            response_model=Variety,
            operation_id="create_meat",
            summary="Create a meat variety",              
            status_code=status.HTTP_200_OK)
async def meat(variety: Variety):
    return variety