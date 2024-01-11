#!/usr/bin/python3
"""CityModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City inherits from the BaseModel"""
    state_id = ""
    name = ""
