from sqlalchemy import Table, Column, Integer, Text
from .database import Base, engine

class Anek(Base):
    __table__ = Table('anek', Base.metadata, autoload=True, autoload_with=engine)