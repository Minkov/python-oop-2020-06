import unittest

from customlist import CustomListIndexException, CustomListTypeException
from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_GetTests(CustomListTestsBase):

    def test_customlistGet_whenIndexInTheMiddle_shouldReturnIt(self):
        value_to_get = 3
        cl = self.setup_list(1, 2, value_to_get, 4)
        result = cl.get(2)

        self.assertEqual(value_to_get, result)

    def test_customlistGet_whenIndexIs0_shouldReturnIt(self):
        value_to_get = 3
        cl = self.setup_list(value_to_get, 1, 2, 4)
        result = cl.get(0)

        self.assertEqual(value_to_get, result)

    def test_customlistGet_whenIndexIsLenMinus1_shouldReturnIt(self):
        value_to_get = 3
        cl = self.setup_list(1, 2, 4, value_to_get)
        result = cl.get(3)

        self.assertEqual(value_to_get, result)

    def test_customlistGet_whenListHasSingleElement_shouldReturnIt(self):
        value_to_get = 3
        cl = self.setup_list(value_to_get)
        result = cl.get(0)

        self.assertEqual(value_to_get, result)

    def test_customlistGet_whenIndexIsEqualToLen_shouldRaise(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.get(list_len)

        self.assertIsNotNone(context.exception)

    def test_customlistGet_whenIndexIsLessThanNegativeLen_shouldRaise(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.get(-list_len - 1)

        self.assertIsNotNone(context.exception)

    def test_customlistGet_whenIndexIsNotInt_shouldRaise(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListTypeException) as context:
            cl.get("index")

        self.assertIsNotNone(context.exception)

    def test_customlistGet_whenListIsEmpty_shouldRaise(self):
        cl = self.setup_list()
        with self.assertRaises(CustomListIndexException) as context:
            cl.get(0)

        self.assertIsNotNone(context.exception)

if __name__ == '__main__':
    unittest.main()
