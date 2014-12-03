from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
#from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
#from sqlalchemy.orm import relationship

Base = declarative_base()


class Operation(Base):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sign = Column(String)
    value1 = Column(Integer)
    value2 = Column(Integer)
    result = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


class Highscore(Base):
    __tablename__ = "highscore"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

    def calc_score(self, number):
        return number ** 2
