from sqlalchemy.orm import Session
from sqlalchemy import or_

from pydantic.error_wrappers import ValidationError

from db.models import Product, Vendor, Supplier

from .schema import ProductCreate


# Bussiness logics for product domain

def get(db: Session, product_id: int):
  return db.query(Product).get(product_id)

def get_list(db: Session, offset: int = 0, limit: int = 30, keyword: str = ""):
  products = db.query(Product)
  if keyword:
    filters = or_(
      Product.name.ilike(f'%{keyword}%'),
      Supplier.name.ilike(f'%{keyword}%'),
      Supplier.address.ilike(f'%{keyword}%'),
      Vendor.name.ilike(f'%{keyword}%'),
    )
    products = products.join(Supplier, Product.suppliers).join(Vendor).filter(filters).distinct()  # distinct might be unnecessary?

  return products.offset(offset).limit(limit).all()

def get_all(db:Session):
  return db.query(Product).all()

def create(db:Session, product_in: ProductCreate):
  product = Product(name=product_in.name)
  
  vendor = db.query(Vendor).get(product_in.vendor_id)
  vendor.products.append(product)

  suppliers = []
  for supplier_id in product_in.suppliers_id:
    supplier = db.query(Supplier).get(supplier_id)
    supplier.products.append(product)
    suppliers.append(supplier)
  db.commit()




def delete(db: Session, product_id: int):
  db.query(Product).filter(Product.id == product_id).delete()
  db.commit()
  