from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session
from db.core import get_db

from .schema import SupplierReadMinimal, SupplierRead
from .service import get_list, get

router = APIRouter()

@router.get("/", response_model=list[SupplierReadMinimal])
def get_suppliers(db: Session = Depends(get_db)):
  suppliers = get_list(db=db)
  return suppliers

@router.get("/{supplier_id}", response_model=SupplierRead)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
  supplier = get(db=db, supplier_id=supplier_id)
  if not supplier:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  return supplier

# @router.post("/")
# def create_supplier(_supplier_create: SupplierCreate, db: Session = Depends(get_db)):
#   create(db=db, supplier_in=_supplier_create)

