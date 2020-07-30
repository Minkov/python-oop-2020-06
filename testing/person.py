class PersonValidator:
    def is_valid(self, name, age):
        return name and 0 <= age <= 150


class Person:
    def __init__(self, name, age):
        self.__validator = PersonValidator()
        if not self.__validator.is_valid(name, age):
            raise Exception('Invalid person name or age')

        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # if value is None:
        #     raise ValueError('Name must be non-empty string')
        self.__name = value

    def get_greeting(self):
        return f'Hello! My name is {self.name} and I\'m {self.age}-years-old!'


# name = input()
# age = int(input())
#
# p = Person(name, age)
#
# print(p.get_greeting())

def test_valid_name_and_valid_age_should_return_correct_greeting():
    # Arrange
    name = 'Test user'
    age = 1
    expected = f'Hello! My name is {name} and I\'m {age}-years-old!'
    p = Person(name, age)

    # Act
    actual = p.get_greeting()

    # Assert
    if actual != expected:
        raise ValueError('Invalid test')


def test_invalid_name_should_raise_exception():
    # Arrange
    name = None
    age = 1

    is_failed = False

    # Act
    try:
        Person(name, age)
        is_failed = True
    except:
        pass

    # Assert
    if is_failed:
        raise ValueError('Invalid test')

#
# test_valid_name_and_valid_age_should_return_correct_greeting()
# test_invalid_name_should_raise_exception()
