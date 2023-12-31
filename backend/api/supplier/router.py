from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session
from db.core import get_db

from .schema import SupplierReadMinimal, SupplierRead
from .service import get_list, get


# Solve Circular imports in Pydantic v2
SupplierReadMinimal.model_rebuild()
SupplierRead.model_rebuild()

router = APIRouter()


@router.get("/", response_model=list[SupplierReadMinimal])
def get_suppliers(
    db: Session = Depends(get_db), page: int = 0, size: int = 30, keyword: str = ""
):
    return get_list(db=db, offset=page * size, limit=size, keyword=keyword)


@router.get("/{supplier_id}", response_model=SupplierRead)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = get(db=db, supplier_id=supplier_id)
    if not supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return supplier


# @router.post("/")
# def create_supplier(_supplier_create: SupplierCreate, db: Session = Depends(get_db)):
#   create(db=db, supplier_in=_supplier_create)
