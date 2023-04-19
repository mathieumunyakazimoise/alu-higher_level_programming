#!/usr/bin/python3
""" model_state.py module """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ state class """
    # declare table name
    __tablename__ = 'states'
    # define colum names and characteristics
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
