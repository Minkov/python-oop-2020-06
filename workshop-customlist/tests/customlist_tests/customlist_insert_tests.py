import unittest

from customlist import CustomListIndexException, CustomListTypeException
from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_InsertTests(CustomListTestsBase):
    def test_customlistInsert_whenIndexInTheMiddle_shouldInsertInAndReturnTheList(self):
        index_to_insert = 2
        value_to_insert = -3
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.insert(index_to_insert, value_to_insert)

        self.assertEqual([1, 2, value_to_insert, 3, 4], result)
        self.assertCustomListStringsEqual([1, 2, value_to_insert, 3, 4], cl)

    def test_customlistInsert_whenIndexIs0_shouldInsertInAndReturnTheList(self):
        index_to_insert = 0
        value_to_insert = -3
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.insert(index_to_insert, value_to_insert)

        self.assertEqual([value_to_insert, 1, 2, 3, 4], result)
        self.assertCustomListStringsEqual([value_to_insert, 1, 2, 3, 4], cl)

    def test_customlistInsert_whenIndexIsLenMinus1_shouldInsertInAndReturnTheList(self):
        index_to_insert = 3
        value_to_insert = -3
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.insert(index_to_insert, value_to_insert)

        self.assertEqual([1, 2, 3, value_to_insert, 4], result)
        self.assertCustomListStringsEqual([1, 2, 3, value_to_insert, 4], cl)

    def test_customlistInsert_whenIndexIsEqualToLen_shouldInsertInAndReturnTheList(self):
        index_to_insert = 4
        value_to_insert = -3
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.insert(index_to_insert, value_to_insert)

        self.assertEqual([1, 2, 3, 4, value_to_insert], result)
        self.assertCustomListStringsEqual([1, 2, 3, 4, value_to_insert], cl)

    def test_customlistInsert_whenListIsEmptyAndInsertAtIndex0_shouldInsertInAndReturnTheList(self):
        index_to_insert = 0
        value_to_insert = -3
        cl = self.setup_list()
        result = cl.insert(index_to_insert, value_to_insert)

        self.assertEqual([value_to_insert], result)
        self.assertCustomListStringsEqual([value_to_insert], cl)

    def test_customlistInsert_whenIndexIsLessThanNegativeLen_shouldRaise(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.insert(-list_len - 1, 3)

        self.assertIsNotNone(context.exception)

    def test_customlistInsert_whenIndexIsNotInt_shouldRaise(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListTypeException) as context:
            cl.insert("index", 3)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
