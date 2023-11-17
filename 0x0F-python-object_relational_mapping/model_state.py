#!/usr/bin/python3
""" defines 'State' class using SQlAlchemy to map it to
    'states' table in MySQL db """
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ class for state that inherits from Base """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
