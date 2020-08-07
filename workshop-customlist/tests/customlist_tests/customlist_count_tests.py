import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_CountTests(CustomListTestsBase):
    def test_customListCount_whenListIsEmpty_shouldReturn0(self):
        cl = self.setup_list()
        index = cl.count(-5)
        self.assertEqual(0, index)

    def test_customListCount_whenListConstainsValueSingleTime_shouldReturn1(self):
        cl = self.setup_list(1, 2, 3, 4)
        index = cl.count(3)
        self.assertEqual(1, index)

    def test_customListCount_whenListContainsValueTwoTimes_shouldReturnTwo(self):
        cl = self.setup_list(1, 2, 3, 4, 3)
        index = cl.count(3)
        self.assertEqual(2, index)

if __name__ == '__main__':
    unittest.main()
