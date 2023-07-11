#!/usr/bin/python3
"""Module with a function that adds a new attribute to
   an object if it's possible
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible
    Args:
        obj (object): object to add attribute to
        name (str): attribute's name
        value (any): attribute's value
    Raises:
        TypeError: 'if object can't have new attribute'
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
