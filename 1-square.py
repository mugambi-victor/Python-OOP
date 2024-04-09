#!/usr/bin/python3

#Write a class Square that defines a square by: (based on 0-square.py)

# Private instance attribute: size
# Instantiation with size (no type/value verification)
# You are not allowed to import any module
class Square:
    # The __init__ method is run as soon as an object of a class is instantiated.
    # this method is useful to do Initialization with your object. i.e assigning initial attributes that
    # an object should have
    def __init__(self,size):
        # in pyhton, to create a private attribute, we prifix it with two underscore(__)
        self.__size = size
