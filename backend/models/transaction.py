from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    contractor = Column(String(100))
    amount = Column(Float)
    status = Column(String(20))
