import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_SizeTests(CustomListTestsBase):
    def test_customListSize_whenEmptyList_shouldReturnEmptyCustomList(self):
        cl = self.setup_list()

        self.assertEqual(0, cl.size())

    def test_customListSize_whenNonEmptyList_shouldReturnEmptyCustomList(self):
        values = [1, 2, 3, 4, 5, 6]
        cl = self.setup_list(*values)

        self.assertEqual(len(values), cl.size())

if __name__ == '__main__':
    unittest.main()
