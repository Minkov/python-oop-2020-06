import unittest

from unittest import TestCase

from person import Person


class TestPerson(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Executing setUpClass')

    def setUp(self) -> None:
        print('Executing setUp()')

    def test_valid_name_and_valid_age_should_return_correct_greeting(self):
        # Arrange
        name = 'Test user'
        age = 1
        expected = f'Hello! My name is {name} and I\'m {age}-years-old!'
        p = Person(name, age)

        # Act
        actual = p.get_greeting()

        # Assert
        self.assertEqual(expected, actual)

    def test_invalid_name_should_raise_exception(self):
        # Arrange
        name = None
        age = 1

        self.assertRaises(ValueError, lambda: Person(name, age))


if __name__ == '__main__':
    unittest.main()
