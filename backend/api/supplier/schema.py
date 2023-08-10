from datetime import datetime

from pydantic import ConfigDict, BaseModel, Field
from typing import List, Optional, ForwardRef


class SupplierBase(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class ViolationBase(BaseModel):
    id: int
    level: str
    title: str
    model_config = ConfigDict(from_attributes=True)


class ViolationRead(ViolationBase):
    issued_datetime: datetime
    start_datetime: datetime | None
    end_datetime: datetime | None
    detail: str


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
    phone_number: str | None
    ceo_name: str
    is_running: bool
    products: list["ProductBase"]


class SupplierRead(SupplierBase):
    address: str
    phone_number: str | None
    ceo_name: str
    first_permit_datetime: datetime
    last_permit_datetime: datetime
    pipes: int
    intakes: int
    is_running: bool
    products: list["ProductReadMinimal"] = []
    violations: list[ViolationRead] = []


from api.product.schema import ProductReadMinimal, ProductBase
