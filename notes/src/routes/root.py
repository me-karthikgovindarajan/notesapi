from fastapi import APIRouter

from src.routes.fruits import fruits as fruits_router
from src.routes.meats import meats as meats_router
from src.routes.vegetables import vegetables as vegetables_router

routers = APIRouter(
    prefix="/api/v1",    
    tags=["notes"],
)
sub_routers: tuple[APIRouter, ...] = (    
    fruits_router,
    vegetables_router,
    meats_router,
)

for router in sub_routers:
    routers.include_router(router)