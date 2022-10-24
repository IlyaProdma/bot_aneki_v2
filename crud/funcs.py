from sqlalchemy.orm import Session
from sqlalchemy import func
import random
from datetime import datetime

from . import anek_model, schemas, database

random.seed(datetime.now())

def get_anek_number(db: Session) -> int:
    return db.query(anek_model.Anek).count()

def get_random_anek(db: Session) -> anek_model.Anek:
    gen_id = random.randint(1, get_anek_number(db))
    return db.query(anek_model.Anek).filter(anek_model.Anek.id == gen_id).first()

def get_category_anek(db: Session, category: str) -> anek_model.Anek:
    return db.query(anek_model.Anek).filter(anek_model.Anek.cat == category).order_by(func.random()).first()

def get_categories(db: Session) -> list:
    return list(map(lambda x: x[0], db.query(anek_model.Anek.cat).distinct().all()))

def get_categories_by_range(db: Session, start: int, limit: int) -> list:
    return list(map(lambda x: x[0], db.query(anek_model.Anek.cat).distinct().offset(start).limit(limit)))

def get_categories_count(db: Session) -> int:
    return db.query(anek_model.Anek.cat).distinct().count()