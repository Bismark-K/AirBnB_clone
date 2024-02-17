#!/usr/bin/python3
""" Module for handling the class: city."""
from models.base_model import BaseModel


class City(BaseModel):
    """Attributes

    id_state: str = ""
    name: str = ""
    """

    state_id: str = ""
    name: str = ""
