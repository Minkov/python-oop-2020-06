import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_ClearTests(CustomListTestsBase):
    def test_customListPop_whenEmptyList_shouldClear(self):
        cl = self.setup_list()
        cl.clear()

        self.assertEmpty(cl.reverse())

    def test_customListPop_whenNonEmpty_shouldClear(self):
        value_to_pop = -22
        cl = self.setup_list(1, 2, value_to_pop)

        cl.clear()

        self.assertEmpty(cl.reverse())

if __name__ == '__main__':
    unittest.main()
