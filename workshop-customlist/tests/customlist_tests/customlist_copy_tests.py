import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_CopyTests(CustomListTestsBase):
    def test_customListCopy_whenEmptyList_shouldReturnEmptyCustomList(self):
        cl = self.setup_list()

        result = cl.copy()

        self.assertNotEqual(cl, result)
        self.assertCustomListStringsEqual([], cl)

    def test_customListCopy_whenNonEmptyList_shouldReturnEmptyCustomList(self):
        values = [1, 2, 3, 4, 5, 6]
        cl = self.setup_list(*values)

        result = cl.copy()

        self.assertNotEqual(cl, result)
        self.assertCustomListStringsEqual(values, result)

if __name__ == '__main__':
    unittest.main()
