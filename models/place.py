#!/usr/bin/python3
"""Module meant for handling the class: place."""

from models.base_model import BaseModel

class Place(BaseModel):
    id_city: str = ""
    id_user: str = ""
    name: str = ""
    description: str = ""
    room_numer: int = 0
    bathroom_number: int = 0
    maximum_guest: int = 0
    price_per_night: int = 0
    gps_latitude: float = 0.0
    gps_longitude: float = 0.0
    id_amenity: list = []
