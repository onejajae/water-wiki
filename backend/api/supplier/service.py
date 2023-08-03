
from sqlalchemy.orm import Session

from db.models import Supplier



def get(db: Session, supplier_id: int):
  return db.query(Supplier).get(supplier_id)

def get_list(db: Session, keyword: str = ""):
  suppliers = db.query(Supplier)
  if keyword:
    suppliers = suppliers.filter(Supplier.name.ilike(f'%{keyword}%'))
    
  return suppliers.all()

# def create(db: Session, supplier_in: SupplierCreate):
#   new_supplier = Supplier(**supplier_in.dict())
#   db.add(new_supplier)
#   db.commit()

def delete(db: Session, supplier_id: int):
  db.query(Supplier).filter(Supplier.id == supplier_id)
  db.commit()