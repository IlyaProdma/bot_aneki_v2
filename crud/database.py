from sqlalchemy import create_engine, inspect, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker, Session
from config import DBNAME, DBUSER, DBPASSWORD, HOST, PORT

DATABASE_URL = f"postgresql://{DBUSER}:{DBPASSWORD}@{HOST}:{PORT}/{DBNAME}"

engine = create_engine(DATABASE_URL)
Base = declarative_base(engine)

def load_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session