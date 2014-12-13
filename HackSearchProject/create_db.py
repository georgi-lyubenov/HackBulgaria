from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class Website(Base):
    __tablename__ = "Website"
    id = Column(Integer, primary_key=True)
    URL = Column(String)
    title = Column(String)
    description = Column(String)
