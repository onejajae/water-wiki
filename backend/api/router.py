from fastapi import APIRouter

from .health import router as health_check_router
from .product import router as product_router
from .supplier import router as supplier_router
from .vendor import router as vendor_router
from .user import router as user_router

# all endpoints of the services
router = APIRouter()

router.include_router(health_check_router.router, tags=["Health Check"])
router.include_router(product_router.router, prefix="/product", tags=["Product"])
router.include_router(supplier_router.router, prefix="/supplier", tags=["Supplier"])
router.include_router(vendor_router.router, prefix="/vendor", tags=["Vendor"])
router.include_router(user_router.router, prefix="/user", tags=["User"])
