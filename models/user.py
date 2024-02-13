#!/usr/bin/python3

"""User class model, inherits from BaseModel."""
from models.base_model import BaseModel

class User(BaseModel):
    """User with parent class being BaseModel

    Attributes:
    email: string
    password: string
    first name: string
    last name: string.
    """
    email = ""
    password = ""
    last_name = ""
    first_name = ""
