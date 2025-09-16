from sqlalchemy.orm import sessionmaker
from src.models.transaction import engine

def get_session():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
    finally:
        session.close()