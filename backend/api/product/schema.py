from pydantic import field_validator, ConfigDict, BaseModel


class ProductBase(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    name: str
    vendor_id: int | None
    suppliers_id: list[int] = []


class ProductReadMinimal(ProductBase):
    vendor: "VendorBase"
    suppliers: list["SupplierBase"] = []

    @field_validator("vendor", mode="before")
    @classmethod
    def set_vendor_default(cls, v):
        if v is None:
            return VendorBase(id=-1, name="")
        else:
            return v


class ProductRead(ProductBase):
    vendor: "VendorBase"
    suppliers: list["SupplierReadMinimal"] = []

    @field_validator("vendor", mode="before")
    @classmethod
    def set_vendor_default(cls, v):
        if v is None:
            return VendorBase(id=-1, name="")
        else:
            return v


class ProductPagination(BaseModel):
    items: list["ProductReadMinimal"]


from api.vendor.schema import VendorReadMinimal, VendorBase
from api.supplier.schema import SupplierReadMinimal, SupplierBase
