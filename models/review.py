#!/usr/bin/python3
""" Module: Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Meant to store review information."""
    place_id = ""
    user_id = ""
    text = ""
