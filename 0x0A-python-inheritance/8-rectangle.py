#!/usr/bin/python3
"""Defines a class Rectangle based on 7-base_geometry.py.

Attributes:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
