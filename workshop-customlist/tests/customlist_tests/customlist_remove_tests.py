import unittest

from customlist import CustomListIndexException, CustomListTypeException
from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_RemoveTests(CustomListTestsBase):

    def test_customlistRemove_whenIndexInTheMiddle_shouldRemoveIt(self):
        """
        1. [1, 2, 3, 4], remove at index 2 => [1, 2, 4]
        """
        value_to_remove = 3
        cl = self.setup_list(1, 2, value_to_remove, 4)
        result = cl.remove(2)

        self.assertEqual(value_to_remove, result)
        self.assertCustomListStringsEqual([1, 2, 4], cl)

    def test_customlistRemove_whenIndexIs0_shouldRemoveIt(self):
        """
        3. [1, 2, 3, 4], remove at index 0 => [2, 3, 4]
        """
        value_to_remove = 3
        cl = self.setup_list(value_to_remove, 1, 2, 4)
        result = cl.remove(0)

        self.assertEqual(value_to_remove, result)
        self.assertCustomListStringsEqual([1, 2, 4], cl)

    def test_customlistRemove_whenIndexIsLenMinus1_shouldRemoveIt(self):
        """
        3. [1, 2, 3, 4], remove at index len - 1 => [1, 2, 3]
        """
        value_to_remove = 3
        cl = self.setup_list(1, 2, 4, value_to_remove)
        result = cl.remove(3)

        self.assertEqual(value_to_remove, result)
        self.assertCustomListStringsEqual([1, 2, 4], cl)

    def test_customlistRemove_whenListHasSingleElement_shouldRemoveIt(self):
        """
        3. [1], remove at index 0 => []
        """
        value_to_remove = 3
        cl = self.setup_list(value_to_remove)
        result = cl.remove(0)

        self.assertEqual(value_to_remove, result)
        self.assertCustomListStringsEqual([], cl)

    # Unhappy cases

    def test_customlistRemove_whenIndexIsEqualToLen_shouldRaise(self):
        """
        1. index >= len
        """
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.remove(list_len)

        self.assertIsNotNone(context.exception)

    def test_customlistRemove_whenIndexIsLessThanNegativeLen_shouldRaise(self):
        """
        2. index < -len
        """
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.remove(-list_len - 1)

        self.assertIsNotNone(context.exception)

    def test_customlistRemove_whenIndexIsNotInt_shouldRaise(self):
        """
        3. index is not an int
        """
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListTypeException) as context:
            cl.remove("index")

        self.assertIsNotNone(context.exception)

    def test_customlistRemove_whenListIsEmpty_shouldRaise(self):
        """
        4. list is empty
        """
        cl = self.setup_list()
        with self.assertRaises(CustomListIndexException) as context:
            cl.remove(0)

        self.assertIsNotNone(context.exception)
if __name__ == '__main__':
    unittest.main()