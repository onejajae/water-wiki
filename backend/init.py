from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.core import Base
from db.models import *

from utils.get_data import vendors, suppliers, products

SQLALCHEMY_DATABASE_URL = 'sqlite:///test.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

# create tables
Base.metadata.create_all(engine)

db_session = sessionmaker(bind=engine)()


# append suppliers
for supplier in suppliers:
  print(supplier)
  supplier_in = Supplier(**supplier)
  db_session.add(supplier_in)
  db_session.commit()

# appeend vendors
for vendor in vendors:
  print(vendor)
  vendor_in = Vendor(
    name=vendor["name"],
    address=vendor["address"],
    ceo_name=vendor["ceo_name"],
    declare_datetime=vendor["declare_datetime"],
    is_running=vendor["is_running"]
  )
  db_session.add(vendor_in)
  db_session.commit()

# append products
for product_name, product in products.items():
  print(product)
  current_vendor = db_session.query(Vendor).filter(Vendor.name == product["vendor"]).first()

  if not current_vendor:
    current_vendor_id = None
  else:
    current_vendor_id = current_vendor.id

  product_in = Product(
      name=product_name,
      vendor_id = current_vendor_id
  )
  db_session.add(product_in)

  if current_vendor: current_vendor.products.append(product_in)
  
  for supplier_name in product["suppliers"]:
    current_supplier = db_session.query(Supplier).filter(Supplier.name == supplier_name).first()
    current_supplier.products.append(product_in)

  db_session.commit()
    

