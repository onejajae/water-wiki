from sqlalchemy.orm import Session
from sqlalchemy import or_

from db.models import Vendor, Product


def get(db: Session, vendor_id: int):
  return db.query(Vendor).get(vendor_id)

def get_list(db: Session, offset: int = 0, limit: int = 30, keyword: str = ""):
  vendors = db.query(Vendor)
  if keyword:
    filters = or_(
      Vendor.name.ilike(f'%{keyword}%'),
      Product.name.ilike(f'%{keyword}%'),
    )
    vendors = vendors.join(Product).filter(filters).distinct()  # distinct might be unnecessary?

  return vendors.offset(offset).limit(limit).all()

# def create(db: Session, vendor_in: VendorCreate):
#   vendor = Vendor(**vendor_in.dict())
#   db.add(vendor)
#   db.commit()
#   # return vendor.

def delete(db: Session, vendor_id: int):
  db.query(Vendor).filter(Vendor.id == vendor_id).delete()
  db.commit()