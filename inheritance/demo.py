class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}'

    def eat(self):
        print(f'{self.name} is eating')


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Grade: {self.grade}'

    def eat(self):
        print(f'{self.name} is eating')


class Employee:
    def __init__(self, name, age, company, salary):
        self.name = name
        self.age = age
        self.company = company
        self.salary = salary

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Company {self.company}'

    def eat(self):
        print(f'{self.name} is eating')


print(Person('John', 18))
print(Student('John', 18, 3))
