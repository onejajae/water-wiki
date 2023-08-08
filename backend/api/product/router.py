from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from db.core import get_db

from .schema import ProductPagination, ProductReadMinimal, ProductRead
from .service import get_list, get


# Solve Circular imports in Pydantic v2
ProductReadMinimal.model_rebuild()
ProductRead.model_rebuild()

router = APIRouter()


@router.get("/", response_model=list[ProductReadMinimal])
def get_products(
    db: Session = Depends(get_db), page: int = 0, size: int = 30, keyword: str = ""
):
    return get_list(db=db, offset=page * size, limit=size, keyword=keyword)


@router.get("/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = get(db=db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return product


# @router.post("/")
# def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):

#   create(db=db, product_in=product_in)


# @router.put("/{product_id}")
# def update_product(product_id: int, product_in: ProductUpdate, db: Session = Depends(get_db)):
#   current_product = get(db=db, product_id=product_id)
#   if not current_product:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
