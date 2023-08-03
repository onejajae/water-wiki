from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session
from db.core import get_db

from .schema import VendorReadMinimal, VendorRead
from .service import get_list, get

router = APIRouter()

@router.get("/", response_model=list[VendorReadMinimal])
def get_vendors(db: Session = Depends(get_db),
                 page: int = 0, size: int = 30, keyword: str = ""):
  return get_list(db=db, offset=page*size, limit=size, keyword=keyword)

@router.get("/{vendor_id}", response_model=VendorRead)
def get_vendor(vendor_id: int, db: Session = Depends(get_db)):
  vendor = get(db=db, vendor_id=vendor_id)
  if not vendor:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

  return vendor

# @router.post("/")
# def create_vendor(_vendor_create: VendorCreate, db: Session = Depends(get_db)):
#   create(db=db, vendor_in=_vendor_create)
