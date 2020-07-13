from mixins.debug_attributes_setter_mixin import DebugAttributesSetterMixin

class Person(DebugAttributesSetterMixin):
    def __init__(self, name, age):
        self.name = name

        # validate age
        self.age = age

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}'

    def eat(self):
        print(f'{self.name} is eating')

    def get_greeting(self):
        return f'Hello, I am {self.name}'


class Student(Person):
    def __init__(self, name, age, grade):
        # super(Student, self).__init__(name, age)
        # super().__init__(name, age)
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.grade = grade

    def get_greeting2(self):
        print(self.get_greeting())

    def __repr__(self):
        parent_repr = super().__repr__()
        return f'{parent_repr}, Grade: {self.grade}'


class HighSchoolPerson(Student):
    pass


class Employee(Person):
    def __init__(self, name, age, company, salary, role):
        super().__init__(name, age)
        self.role = role
        self.company = company
        self.salary = salary

    def __repr__(self):
        parent_repr = super().__repr__()
        return f'{parent_repr}, Company {self.company}'


class Manager(Employee):
    pass


class Director(Manager):
    pass


class PersonExample(Person):
    @property
    def is_adult(self):
        return self.age >= 18


#
Person('John the Person', 18).eat()
Student('John the Student', 18, 3).eat()
Employee('John the Employee', 18, 'SoftUni', 100000).eat()

# student = Student('Pesho', 8, 2)
# print(student)
# student.get_greeting2()
