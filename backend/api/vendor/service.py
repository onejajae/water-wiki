from sqlalchemy.orm import Session

from db.models import Vendor


def get(db: Session, vendor_id: int):
  return db.query(Vendor).get(vendor_id)

def get_list(db: Session):
  return db.query(Vendor).all()

# def create(db: Session, vendor_in: VendorCreate):
#   vendor = Vendor(**vendor_in.dict())
#   db.add(vendor)
#   db.commit()
#   # return vendor.

def delete(db: Session, vendor_id: int):
  db.query(Vendor).filter(Vendor.id == vendor_id).delete()
  db.commit()