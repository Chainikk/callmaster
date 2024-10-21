from fastapi import APIRouter

from controllers.settings import config
from controllers.routes.client import router as client_router

router = APIRouter(prefix=f"/api/{config.api_prefix}", tags=['API v.1'])
router.include_router(client_router)
