from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    ForeignKey,
    Table,
    Float,
)
from sqlalchemy.orm import relationship

from .core import Base

# DB models for the services

supplied_product = Table(
    "supplied_product",
    Base.metadata,
    Column("supplier_id", ForeignKey("supplier.id"), primary_key=True),
    Column("product_id", ForeignKey("product.id"), primary_key=True),
)


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    vendor_id = Column(Integer, ForeignKey("vendor.id"))
    vendor = relationship("Vendor", back_populates="products")
    suppliers = relationship(
        "Supplier", secondary=supplied_product, back_populates="products"
    )


class Supplier(Base):
    __tablename__ = "supplier"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    address = Column(String(200), nullable=False)
    phone_number = Column(String(15), nullable=True)
    ceo_name = Column(String(10), nullable=False)
    first_permit_datetime = Column(DateTime, nullable=False)
    last_permit_datetime = Column(DateTime, nullable=False)
    pipes = Column(Integer, nullable=False)
    intakes = Column(Integer, nullable=False)
    is_running = Column(Boolean, nullable=False)
    loc_x = Column(Float, nullable=True)
    loc_y = Column(Float, nullable=True)
    products = relationship(
        "Product", secondary=supplied_product, back_populates="suppliers"
    )
    violations = relationship("Violation", back_populates="supplier")


class Vendor(Base):
    __tablename__ = "vendor"

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    address = Column(String(200), nullable=False)
    phone_number = Column(String(15), nullable=True)
    ceo_name = Column(String(10), nullable=False)
    declare_datetime = Column(DateTime, nullable=False)
    is_running = Column(Boolean, nullable=False)
    loc_x = Column(Float, nullable=True)
    loc_y = Column(Float, nullable=True)
    products = relationship("Product", back_populates="vendor")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False)


class Violation(Base):
    __tablename__ = "violation"

    id = Column(Integer, primary_key=True)
    issued_datetime = Column(DateTime, nullable=False)
    level = Column(String(10), nullable=False)
    title = Column(String, nullable=False)
    start_datetime = Column(DateTime, nullable=True)
    end_datetime = Column(DateTime, nullable=True)
    detail = Column(String, nullable=False)
    supplier_id = Column(Integer, ForeignKey("supplier.id"))
    supplier = relationship("Supplier", back_populates="violations")
