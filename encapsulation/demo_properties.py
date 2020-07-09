class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, full_name):
        (first_name, last_name) = full_name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError('Name must be a non-empty string')
        self.__name = value
        
    def __setattr__(self, key, value):
        super(Person, self).__setattr__(key, value)


person = Person('George', 'Petrov', 32)

print(person.first_name)
person.first_name = 'Gosheto'
print(person.first_name)
print(person.full_name)
person.full_name = 'Peter Goshov'
print(person.full_name)
