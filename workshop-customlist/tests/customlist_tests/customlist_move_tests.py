import unittest

from customlist import CustomListIndexException
from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_MoveTests(CustomListTestsBase):
    def test_customListMove_whenEmptyList_shouldAddIt(self):
        cl = self.setup_list()
        result = cl.move(0)

        self.assertEmpty(result)

    def test_customListMove_whenSingleLement_shouldReturnIt(self):
        cl = self.setup_list(1)

        result = cl.move(3)

        self.assertListEqual([1], result)
        self.assertListEqual([1], cl.reverse())

    def test_customListMove_whenMultipleElements_shouldMoveThem(self):
        part_1 = [1, 2]
        part_2 = [3, 4, 5]
        cl = self.setup_list(*part_1, *part_2)

        result = cl.move(2)
        expected = part_2 + part_1

        self.assertListEqual(expected, result)
        self.assertCustomListStringsEqual(expected, cl)

if __name__ == '__main__':
    unittest.main()
