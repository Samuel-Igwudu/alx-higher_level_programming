#!/usr/bin/python3
class Square:
    """ defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ return the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ return the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ set position value
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 position integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return the square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """ print #
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
