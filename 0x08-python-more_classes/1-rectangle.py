#!/usr/bin/python3
"""A pyhton module that defines Rectangle class"""


class Rectangle:
    """A rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle class.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Returns height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets width property of the rectangle.

        Args:
            value (int): width value.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets size property of the square.

        Args:
            value (int): height value.

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
