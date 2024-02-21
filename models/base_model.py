#!/usr/bin/python3
"""Defines a BaseModel"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base class for other models. Includes methods common to all models."""

    def __init__(self, *args, **kwargs):
        """Initializes a new base model instance"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if len(kwargs) !=0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the model instance.
           Converts datetime objects to ISO format strings
        """
        model_dict = self.__dict__.copy()
        model_dict["created_at"] = model_dict["created_at"].isoformat()
        model_dict["updated_at"] = model_dict["updated_at"].isoformat()
        model_dict["__class__"] = self.__class__.__name__
        return model_dict

    def __str__(self):
        """:return: A string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
