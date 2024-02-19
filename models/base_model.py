#!/usr/bin/python3
"""Defines a BaseModel"""
from datetime import datetime, timedelta
from uuid import uuid4


class BaseModel:
    """Base class for other models. Includes methods common to all models."""

    def __init__(self):
        """Initializes a new base model instance"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """:return: A string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the model instance.
           Converts datetime objects to ISO format strings
        """
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = model_dict["created_at"].isoformat()
        model_dict["updated_at"] = model_dict["updated_at"].isoformat()
        return model_dict
