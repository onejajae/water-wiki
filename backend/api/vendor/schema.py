from datetime import datetime

from pydantic import BaseModel, Field
from typing import List, Optional, ForwardRef


class VendorBase(BaseModel):
  id: int
  name: str

  class Config:
    orm_mode = True


class VendorCreate(BaseModel):
  name: str
  address: str
  phone_number: str
  ceo_name: str
  declare_datetime: datetime
  is_running: bool


class VendorReadMinimal(VendorBase):
  address: str
  phone_number: Optional[str]
  ceo_name: str
  products: List['ProductBase']


class VendorRead(VendorBase):
  id: int
  name: str
  address: str
  phone_number: Optional[str]
  ceo_name: str
  declare_datetime: datetime
  is_running: bool
  products: List['ProductReadMinimal'] = []


from api.product.schema import ProductReadMinimal, ProductBase
VendorReadMinimal.update_forward_refs()
VendorRead.update_forward_refs()