from pydantic import BaseModel, Field, validator
from typing import List, Optional, ForwardRef


class ProductBase(BaseModel):
  id: int
  name: str

  class Config:
    orm_mode = True


class ProductCreate(BaseModel):
  name: str
  vendor_id: Optional[int]
  suppliers_id: Optional[List[int]]


class ProductReadMinimal(ProductBase):
  vendor: 'VendorBase'
  suppliers: List['SupplierBase'] = []

  @validator("vendor", pre=True)
  def set_vendor_default(cls, v):
    if v is None:
      return VendorBase(id=-1, name="")
    else:
      return v


class ProductRead(ProductBase):
  vendor: 'VendorBase'
  suppliers: List['SupplierReadMinimal'] = []

  @validator("vendor", pre=True)
  def set_vendor_default(cls, v):
    if v is None:
      return VendorBase(id=-1, name="")
    else:
      return v


class ProductPagination(BaseModel):
  items: List['ProductReadMinimal']


from api.vendor.schema import VendorReadMinimal, VendorBase
from api.supplier.schema import SupplierReadMinimal, SupplierBase

ProductReadMinimal.update_forward_refs()
ProductRead.update_forward_refs()