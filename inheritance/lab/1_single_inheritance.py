class Animal:
    def eat(self):
        return 'eating...'


class Dog(Animal):
    def bark(self):
        return 'barking...'

class RapidDog(Dog):

    def bark(self):
        return 'Rapid barking...'

d = RapidDog()

print(d.eat())
print(d.bark())
