from sqlalchemy.orm import Session
from sqlalchemy import or_

from db.model import Supplier, Product


def get(db: Session, supplier_id: int):
  return db.query(Supplier).get(supplier_id)

def get_list(db: Session, offset: int = 0, limit: int = 30, keyword: str = ""):
  suppliers = db.query(Supplier)
  if keyword:
    filters = or_(
      Supplier.name.ilike(f'%{keyword}%'),
      Supplier.address.ilike(f'%{keyword}%'),
      Product.name.ilike(f'%{keyword}%'),
    )
    suppliers = suppliers.join(Product, Supplier.products).filter(filters).distinct()

  return suppliers.order_by(Supplier.name.asc()).offset(offset).limit(limit).all()

# def create(db: Session, supplier_in: SupplierCreate):
#   new_supplier = Supplier(**supplier_in.dict())
#   db.add(new_supplier)
#   db.commit()

def delete(db: Session, supplier_id: int):
  db.query(Supplier).filter(Supplier.id == supplier_id)
  db.commit()