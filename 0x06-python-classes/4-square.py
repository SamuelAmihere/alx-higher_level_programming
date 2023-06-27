#!/usr/bin/python3
"""Square class."""


class Square:
    """Square class.

    Attributes:
        size: size of square - a side.
    """
    def __init__(self, size=0):
        """Initialize Square class.

        Args:
            size(int): size of square - a side.
        """
        self.__size = size
    
    def size(self):
        """Gets size of the square."""
        return self.__size

    def size(self, value):
        """Sets size property of the square.
        
        Args:
            value (int): size of square - a side.

        Raises:
            ValueError: size must be >= 0
            TypeError: size must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns area of the square."""
        return self.__size ** 2
