#!/usr/bin/python3
class Square:
    """ class square that defines a square.
    """
    def __init__(self, size=0):
        """ Method to initialize
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.___size = size

    def area(self):
        """ Method to returnthe square area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Method to return size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
