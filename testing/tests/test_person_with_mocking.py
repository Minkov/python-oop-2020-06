import unittest
from unittest import TestCase, mock

from person import Person


class TestPerson(TestCase):
    def test_personGetGreeting_shouldReturnCorrectGreeting(self):
        with mock.patch('person.PersonValidator') as MockPersonValidator:
            MockPersonValidator.return_value.is_valid.return_value = True

            Person(None, -1)


if __name__ == '__main__':
    unittest.main()
