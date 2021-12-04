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

    def area(self):
        return self.width * self.height


if __name__ == '__main__':

    rectan = Rectangle(5, 4)
    print(rectan.area())
