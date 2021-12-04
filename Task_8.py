"""
Create a Rectangle class whose attributes will be the height and width
of the figure. Implement methods to measure the perimeter and area of
a rectangle.

Then create a Square class, remembering that every square is a
rectangle, but not every rectangle is a square.
"""


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height)*2

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)


if __name__ == '__main__':

    r1 = Rectangle(5, 4)
    print(r1.perimeter())
    print(r1.area())

    s1 = Square(6)
    print(s1.perimeter())
    print(s1.area())
