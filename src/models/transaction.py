import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
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

