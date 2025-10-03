from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    timestamp = Column(DateTime, nullable=False)
    type = Column(String, nullable=False)  # 'income' or 'expense'

    def __init__(self, amount, category, description, timestamp, transaction_type):
        self.amount = amount
        self.category = category
        self.description = description
        self.timestamp = timestamp
        self.type = transaction_type

