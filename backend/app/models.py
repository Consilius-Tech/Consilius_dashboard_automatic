from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, index=True)
    name = Column(String)
    price = Column(Float)
    sector = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())