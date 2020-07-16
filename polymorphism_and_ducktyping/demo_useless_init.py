from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print('Bark...')


dog = Dog('Sharo')
dog.sound()
