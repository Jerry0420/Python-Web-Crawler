from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class Fragrantica(Base):
    __tablename__ = 'fragrantica'
    id = Column(Integer, primary_key=True)
    title = Column(String)