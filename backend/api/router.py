from fastapi import APIRouter

from .echo import router as echo_router 
from .product import router as product_router
from .supplier import router as supplier_router
from .vendor import router as vendor_router
from .auth import router as auth_router
from .user import router as user_router

# all endpoints of the services
router = APIRouter()

router.include_router(echo_router.router, prefix="/echo", tags=["test"])
router.include_router(product_router.router, prefix="/product", tags=["product"])
router.include_router(supplier_router.router, prefix="/supplier", tags=["supplier"])
router.include_router(vendor_router.router, prefix="/vendor", tags=["vendor"])
router.include_router(auth_router.router, prefix="/auth", tags=["auth"])
router.include_router(user_router.router, prefix="/user", tags=["user"])
