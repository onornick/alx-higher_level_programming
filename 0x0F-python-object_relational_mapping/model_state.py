#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(15))
    fullname = Column(String(20))
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>"\
            %(self.name, self.fullname, self.nickname)

    def __str__(self):
        print(Users.__table__)

    