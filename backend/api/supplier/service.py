from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from db.model import Supplier, Product


def get(db: Session, supplier_id: int):
    return db.query(Supplier).get(supplier_id)


def get_list(db: Session, offset: int = 0, limit: int = 30, keyword: str = ""):
    suppliers = db.query(Supplier).outerjoin(Product, Supplier.products).distinct()
    if keyword:
        filters = or_(
            Supplier.name.ilike(f"%{keyword}%"),
            Supplier.address.ilike(f"%{keyword}%"),
            Product.name.ilike(f"%{keyword}%"),
        )
        suppliers = suppliers.filter(filters)

    return (
        suppliers.group_by(Supplier.id)
        .order_by(func.count(Supplier.name).desc())
        .offset(offset)
        .limit(limit)
        .all()
    )


# def create(db: Session, supplier_in: SupplierCreate):
#   new_supplier = Supplier(**supplier_in.dict())
#   db.add(new_supplier)
#   db.commit()


def delete(db: Session, supplier_id: int):
    db.query(Supplier).filter(Supplier.id == supplier_id)
    db.commit()
