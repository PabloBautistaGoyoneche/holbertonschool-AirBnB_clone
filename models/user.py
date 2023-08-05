#!/usr/bin/python3
from models.base_model import BaseModel
""" User class inheriting from basemodel """
class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""