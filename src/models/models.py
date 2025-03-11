from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = 'sqlite:///MONEYger.db'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Transacao(Base):
    __tablename__ = 'Transacao'
    id = Column(Integer, primary_key=True)
    data = Column(String(20))
    valor = Column(Float())
    descricao = Column(String(50))

Base.metadata.create_all(engine)