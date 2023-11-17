#!/usr/bin/python3
""" class City """
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ Class for cities MySQL table """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
