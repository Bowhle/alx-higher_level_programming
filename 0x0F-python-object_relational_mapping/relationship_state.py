#!/usr/bin/python3
"""State class with cities relationship"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City
from model_state import Base


class State(Base):
    """State class definition with cities relationship"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship with City class
    cities = relationship('City', backref='state', cascade='all, delete-orphan')
