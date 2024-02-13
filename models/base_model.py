#!/usr/bin/python3
"""Module for the Base Class."""

from datetime import datetime
import uuid


class BaseModel:
    """Base Model Class."""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Initializes every new instance of the class: BaseModel."""
        if kwargs:
            if 'created_at':
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__':
                del kwargs['__class__']
            if 'updated_at':
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.item():
                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the class's representation."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Modifies the updated_at with the current time."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of __dict__."""
        dict_object = self.__dict__.copy()

        dict_object['__class__'] = self.__class__.__name__
        dict_object['created_at'] = self.created_at.isoformat()
        dict_object['updated_at'] = self.updated_at.isoformat()

        return dict_object
