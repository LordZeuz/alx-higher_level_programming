#!/usr/bin/python3
"""A class My_list that inherits """


class MyList(list):
    """An inherited class """

    def print_sorted(self):
        """print the list in assorted form"""
        print(sorted(self))
