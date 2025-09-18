import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
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

def add_transaction(amount, category, description, timestamp, transaction_type):
    session = SessionLocal()
    try:
        transaction = Transaction(
            amount=amount,
            category=category,
            description=description,
            timestamp=timestamp,
            transaction_type=transaction_type
        )
        session.add(transaction)
        session.commit()
        session.refresh(transaction) 
        return transaction
    except Exception as e:
        session.rollback()
        print(f"Erro ao adicionar transação: {e}")
    finally:
        session.close()

