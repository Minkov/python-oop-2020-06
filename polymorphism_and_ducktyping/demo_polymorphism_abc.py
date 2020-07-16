from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, shape_id):
        self.id = shape_id

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def print_info(self):
        print(f'ID: {self.id}, Area: {self.area()}, Perimeter: {self.perimeter()}')


class Circle(Shape):
    def __init__(self, shape_id, radius):
        super().__init__(shape_id)
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2


def print_shape_info(shape: Shape):
    print(f'Perimeter: {shape.perimeter()}')
    print(f'Area: {shape.area()}')


print(Circle.mro())

shape = Circle(1, 3)
print(shape.perimeter())
print_shape_info(shape)

print(isinstance(shape, Circle))
print(isinstance(shape, Shape))
shape.print_info()
