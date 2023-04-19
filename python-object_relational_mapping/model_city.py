#!/usr/bin/python3
"""model_city module"""
from model_state import Base, State
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class inherits
    """
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False
