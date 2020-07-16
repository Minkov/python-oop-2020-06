from abc import ABC, abstractmethod
from math import pi


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f'Hello! I am {self.name}')


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius * self.__radius

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


def print_info(obj):
    if isinstance(obj, Person):
        obj.introduce()
    # elif isinstance(obj, Circle) or isinstance(obj, Rectangle):
    elif isinstance(obj, Shape):
        print(f'Perimeter: {obj.calculate_perimeter()}')
        print(f'Area: {obj.calculate_area()}')
    else:
        print('I don\'t know!')


print_info(Circle(3))
print_info(Rectangle(2, 3))
print_info(Person('Pesho'))
