from datetime import datetime

from pydantic import ConfigDict, BaseModel


class VendorBase(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class VendorCreate(BaseModel):
    name: str
    address: str
    phone_number: str
    ceo_name: str
    declare_datetime: datetime
    is_running: bool


class VendorReadMinimal(VendorBase):
    address: str
    phone_number: str | None
    ceo_name: str
    products: list["ProductBase"]


class VendorRead(VendorBase):
    id: int
    name: str
    address: str
    phone_number: str | None
    ceo_name: str
    declare_datetime: datetime
    is_running: bool
    products: list["ProductReadMinimal"] = []


from api.product.schema import ProductReadMinimal, ProductBase
