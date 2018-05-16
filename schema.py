from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Musician(Base):
    __tablename__ = 'musicians'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    instrument = Column(String)
    dob = Column(DateTime)
    alive = Column(Boolean)


engine = create_engine('sqlite:///musicians.db', echo=True)
Base.metadata.create_all(engine)
