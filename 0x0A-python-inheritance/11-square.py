#!/usr/bin/python3
"""Defines a Rectangle subclass square."""
Rectangle = __import__('9-rectangle').Rectangle

class square(Rectangle):
    """Represent a square."""

    def __init__(self. size):
        """initialize a new square.


        Args:
            size (init): The size of the new square.
        """
        self.integer_validator("size", size)
        super()._init_(size. size)
        self._size = size
