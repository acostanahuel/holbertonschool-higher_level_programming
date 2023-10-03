#!/usr/bin/python3

class Rectangle:
    
    def __init__(self, width=0, lenght=0):
    
        self.width = width
        self.lenght = lenght
        
    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value
        
    