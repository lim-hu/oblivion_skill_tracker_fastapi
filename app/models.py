from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from .database import Base

class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    collected = Column(Integer, nullable=False, server_default='0')
    attribute = Column(String, nullable=False)