#!/usr/bin/python3
"""ReviewModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review inherits from the BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
