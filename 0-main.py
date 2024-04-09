#!/usr/bin/python3
# tests if square class was created correctly
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
