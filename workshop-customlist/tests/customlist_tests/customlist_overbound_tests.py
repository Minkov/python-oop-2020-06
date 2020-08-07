import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_OverboundTests(CustomListTestsBase):
    def test_customListOverbound_whenListHasMultipleNumbersAndFloatIsBigger_shouldReturnTheIndexOfTheBiggest(self):
        values = [1, 3.14]
        cl = self.setup_list(*values)
        expected = values.index(max(values))
        actual = cl.overbound()
        self.assertEqual(expected, actual)

    def test_customListOverbound_whenListHasMultipleNumbersAndIntIsBigger_shouldReturnTheIndexOfTheBiggest(self):
        values = [1, 3.14, 5]
        cl = self.setup_list(*values)
        expected = values.index(max(values))
        actual = cl.overbound()
        self.assertEqual(expected, actual)

    def test_customListOverbound_whenListHasNumbersAndLenObjectsAndNumberIsBigger_shouldReturnTheIndexOfTheNumber(
            self):
        numbers = [1, 5.14]
        len_objects = ['123', [1, 2], (3, 4), {1, 2, 3}, {1, 2}]
        cl = self.setup_list(*numbers, *len_objects)
        expected = 1

        actual = cl.overbound()
        self.assertEqual(expected, actual)

    def test_customListOverbound_whenListHasNumbersAndLenObjectsAndLenObjectIsBigger_shouldReturnTheIndexOfTheNumber(
            self):
        numbers = [1, 3.14]
        len_objects = ['123', [1, 2], (3, 4), {1, 2, 3, 6}, {1, 2}]
        cl = self.setup_list(*numbers, *len_objects)
        expected = 5

        actual = cl.overbound()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
