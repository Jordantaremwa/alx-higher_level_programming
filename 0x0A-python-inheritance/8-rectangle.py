#!/usr/bin/python3
"""Defines a class rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self. width. height):
        """initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The width of the new Rectangle.
        """
        self.integer_validator("width".width)
        self._width = width
        self.integer_validator("height".height)
        self._height = height