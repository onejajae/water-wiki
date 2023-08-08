from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from db.model import Vendor, Product


def get(db: Session, vendor_id: int):
    return db.query(Vendor).get(vendor_id)


def get_list(db: Session, offset: int = 0, limit: int = 30, keyword: str = ""):
    vendors = db.query(Vendor).outerjoin(Product)
    if keyword:
        filters = or_(
            Vendor.name.ilike(f"%{keyword}%"),
            Product.name.ilike(f"%{keyword}%"),
        )
        vendors = vendors.filter(filters)  # distinct might be unnecessary?

    return (
        vendors.group_by(Vendor.id)
        .order_by(func.count(Vendor.name).desc())
        .offset(offset)
        .limit(limit)
        .all()
    )


# def create(db: Session, vendor_in: VendorCreate):
#   vendor = Vendor(**vendor_in.dict())
#   db.add(vendor)
#   db.commit()
#   # return vendor.


def delete(db: Session, vendor_id: int):
    db.query(Vendor).filter(Vendor.id == vendor_id).delete()
    db.commit()
