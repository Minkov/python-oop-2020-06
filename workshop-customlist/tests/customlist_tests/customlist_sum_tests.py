import unittest

from customlist import CustomListSumException
from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_SumTests(CustomListTestsBase):
    def test_customListSum_whenEmptyList_shouldReturn0(self):
        cl = self.setup_list()

        self.assertEqual(0, cl.sum())

    def test_customListSum_whenListHasMultipleNumbers_shouldReturnTheirSum(self):
        values = [1, 3.14]
        cl = self.setup_list(*values)
        expected = sum(values)
        actual = cl.sum()
        self.assertEqual(expected, actual)

    def test_customListSum_whenListHasNumbersAndLenObjects_shouldReturnTheSumOfNumbersPlusSumsOfLengthsOfLenObjects(
            self):
        numbers = [1, 3.14]
        len_objects = ['123', [1, 2], (3, 4), {1, 2, 3}, {1, 2}]
        cl = self.setup_list(*numbers, *len_objects)
        expected = sum(numbers) + sum(len(x) for x in len_objects)
        actual = cl.sum()
        self.assertEqual(expected, actual)

    def test_customListSum_whenListHasInvalidObjects_shouldRaise(
            self):
        # numbers = [1, 3.14]
        numbers = []
        len_objects = ['123', [1, 2], (3, 4), {1, 2, 3}, {1, 2}]
        invalid_objects = [object()]
        cl = self.setup_list(*numbers, *len_objects, *invalid_objects)
        with self.assertRaises(CustomListSumException) as context:
            cl.sum()
        self.assertIsNotNone(context.exception)

if __name__ == '__main__':
    unittest.main()
