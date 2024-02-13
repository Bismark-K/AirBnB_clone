#!/usr/bin/python3
"""Module for the Base Class."""

from datetime import datetime
import uuid

class BaseModel:
    """Base Model Class."""
    id = str(uuid.uuid4())
    time_created = datetime.now()
    time_modified = datetime.now()

    def __str__(self):
        """Returns the class's representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def store(self):
        """Modifies the time_modified with the current time."""
        self.time_modified = datetime.now()


    def dictionary(self):
        """Returns a dictionary of __dict__."""
        dict_object = self.__dict__.copy()

        dict_object['__class__'] = self.__class__.__name__
        dict_object['time_created'] = self.time_created.isoformat()
        dict_object['time_modified'] = self.time_modified.isoformat()
        return dict_object
