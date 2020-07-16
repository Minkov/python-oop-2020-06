from math import pi


class Shape:
    def __init__(self):
        if type(self) == Shape:
            raise TypeError('This an abstract class')

    def perimeter(self):
        raise TypeError('This is an abstract method')

    def area(self):
        raise TypeError('This is an abstract method')

    def print_info(self):
        print(self.area(), self.perimeter())


sh = Shape()


# print(sh.perimeter())
# sh.print_info()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, wight, height):
        self.wight = wight
        self.height = height

    def perimeter(self):
        return 2 * (self.wight + self.height)

    def area(self):
        return self.wight * self.height


class Circle2:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2


def print_shape_info(shape: Shape):
    print(f'Perimeter: {shape.perimeter()}')
    print(f'Area: {shape.area()}')


circle = Circle(3)
print(circle.perimeter())
print_shape_info(circle)
print_shape_info(Rectangle(3, 2))

print(isinstance(circle, Circle))
print(isinstance(circle, Shape))
print(isinstance(circle, Circle2))
