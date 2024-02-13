#!/usr/bin/python3
"""Module for the Base Class."""

from datetime import datetime
import uuid

class BaseModel:
    """Base Model Class."""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """Returns the class's representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def store(self):
        """Modifies the updated_at with the current time."""
        self.updated_at = datetime.now()


    def dictionary(self):
        """Returns a dictionary of __dict__."""
        dict_object = self.__dict__.copy()

        dict_object['__class__'] = self.__class__.__name__
        dict_object['created_at'] = self.created_at.isoformat()
        dict_object['updated_at'] = self.updated_at.isoformat()
        return dict_object
