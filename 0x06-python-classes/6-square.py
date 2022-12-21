#!/usr/bin/python3
""" Creates square class"""


class Square:
    """ A square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialise sqaure instance
        Args:
            size: Size of square
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Return size of self"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrives position of square instance"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not
                all(isinstance(num, int) for num in value) or not
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return Area of Square instance
        Returnl:
            area of square
        """
        return (self.__size)**2

    def my_print(self):
        """Prints to stdout the square with# symbol"""
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            [print("#", end="") for j in range(self.__size)]
            print("")
