class  Rectangle:
    def __init__(self,width=0,height=0): 
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    
    @property   
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
    
    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        
        return (self.__width + self.__height) * 2
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        
        return (("#" * self.__width + "\n") * self.__height)[:-1]
    
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    
    def __del__(self):
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        
        return rect_2

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-rectangle.txt")

Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))