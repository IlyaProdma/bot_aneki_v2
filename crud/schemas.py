from typing import Union
from pydantic import BaseModel

class AnekBase(BaseModel):
    cat: str
    text: str

class Anek(AnekBase):
    id: int
    
    class Config:
        orm_mode = True