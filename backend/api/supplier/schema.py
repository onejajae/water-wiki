from datetime import datetime

from pydantic import BaseModel, Field
from typing import List, Optional, ForwardRef


class SupplierBase(BaseModel):
  id: int
  name: str

  class Config:
    orm_mode = True


class SupplierCreate(BaseModel):
  name: str
  address: str
  phone_number: str
  ceo_name: str
  first_permit_datetime: datetime
  last_permit_datetime: datetime
  is_running: bool


class SupplierReadMinimal(SupplierBase):
  address: str
  phone_number: Optional[str]
  ceo_name: str
  is_running: bool
  products: List['ProductBase']


class SupplierRead(SupplierBase):
  address: str
  phone_number: Optional[str]
  ceo_name: str
  first_permit_datetime: datetime
  last_permit_datetime: datetime
  pipes: int
  intakes: int
  is_running: bool
  products: List['ProductReadMinimal'] = []


from api.product.schema import ProductReadMinimal, ProductBase
SupplierReadMinimal.update_forward_refs()
SupplierRead.update_forward_refs()