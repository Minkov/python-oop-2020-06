import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_UnderboundTests(CustomListTestsBase):
    def test_customListUnderbound_whenListHasMultipleNumbersAndFloatIsSmaller_shouldReturnTheIndexOfTheBiggest(self):
        values = [1, 3.14]
        cl = self.setup_list(*values)
        expected = values.index(min(values))
        actual = cl.underbound()
        self.assertEqual(expected, actual)

    def test_customListUnderbound_whenListHasMultipleNumbersAndIntIsSmaller_shouldReturnTheIndexOfTheBiggest(self):
        values = [1, 3.14, 5]
        cl = self.setup_list(*values)
        expected = values.index(min(values))
        actual = cl.underbound()
        self.assertEqual(expected, actual)

    def test_customListUnderbound_whenListHasNumbersAndLenObjectsAndNumberIsSmaller_shouldReturnTheIndexOfTheNumber(
            self):
        numbers = [1, 5.14]
        len_objects = ['123', [1, 2], (3, 4), {1, 2, 3}, {1, 2}]
        cl = self.setup_list(*numbers, *len_objects)
        expected = 0

        actual = cl.underbound()
        self.assertEqual(expected, actual)

    def test_customListUnderbound_whenListHasNumbersAndLenObjectsAndLenObjectIsSmaller_shouldReturnTheIndexOfTheNumber(
            self):
        numbers = [1, 3.14]
        len_objects = ['123', [1, 2], (3, 4), {}, {1, 2}]
        cl = self.setup_list(*numbers, *len_objects)
        expected = 5

        actual = cl.underbound()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
