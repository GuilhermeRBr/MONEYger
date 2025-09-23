import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from dotenv import load_dotenv
from src.models.transaction import Transaction

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)


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

def income_total():
    session = SessionLocal()
    try:
        total = session.query(func.sum(Transaction.amount)).filter(Transaction.type == "income").scalar() or 0
        return total
    except Exception as e:
        print(f"Erro ao calcular receita total: {e}")
        return 0
    finally:
        session.close()

def expense_total():
    session = SessionLocal()
    try:
        total = session.query(func.sum(Transaction.amount)).filter(Transaction.type == "expense").scalar() or 0
        return total
    except Exception as e:
        print(f"Erro ao calcular despesa total: {e}")
        return 0
    finally:
        session.close()