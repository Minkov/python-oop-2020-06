import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_IndexTests(CustomListTestsBase):
    def test_customListIndex_whenListIsEmpty_shouldReturnMinus1(self):
        cl = self.setup_list()
        index = cl.index(-5)
        self.assertEqual(-1, index)

    def test_customListIndex_whenValueNotInList_shouldReturnMinus1(self):
        cl = self.setup_list(1, 2, 3, 4)
        index = cl.index(-5)
        self.assertEqual(-1, index)

    def test_customListIndex_whenListConstainsValueSingleTime_shouldReturnItsIndex(self):
        cl = self.setup_list(1, 2, 3, 4)
        index = cl.index(3)
        self.assertEqual(2, index)

    def test_customListIndex_whenListContainsValueMultipleTimes_shouldReturnItsSmallestIndex(self):
        cl = self.setup_list(1, 2, 3, 4, 3)
        index = cl.index(3)
        self.assertEqual(2, index)

if __name__ == '__main__':
    unittest.main()
