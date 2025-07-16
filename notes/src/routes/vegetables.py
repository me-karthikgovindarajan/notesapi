from fastapi import APIRouter, status
from src.models.model import Variety

vegetables = APIRouter()

@vegetables.post("/vegetable", 
                tags=["notes"],
                description="Create a new vegetable variety",
                response_description="The created vegetable variety",
                responses={200: {"description": "Vegetable created successfully"}},
                response_model=Variety,
                operation_id="create_vegetable",
                summary="Create a vegetable variety",
                status_code=status.HTTP_200_OK)
async def vegetable(variety: Variety):
    return variety