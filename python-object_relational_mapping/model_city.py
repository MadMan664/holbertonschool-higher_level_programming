#!/usr/bin/python3
"""Defines the City class, linked to the table cities and to states."""
from sqlalchemy import Column, ForeignKey, Integer, String

from model_state import Base


class City(Base):
    """Maps a Python City object to a row of the MySQL table cities."""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
