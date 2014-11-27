from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship


Base = declarative_base()


class Movie(Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)


class Projection(Base):
    __tablename__ = "Projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("Movies.id"))
    type = Column(String)
    date = Column(String)
    time = Column(String)


class Reservation(Base):
    __tablename__ = "Reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey("Projections.id"))
    row = Column(Integer)
    col = Column(Integer)




