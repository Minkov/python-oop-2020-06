from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase

import unittest


class CustomList_AddFirstTests(CustomListTestsBase):
    def test_customListAddFirst_whenEmptyList_shouldAddIt(self):
        cl = self.setup_list()
        cl.add_first(1)

        self.assertCustomListStringsEqual([1], cl)

    def test_customListAddFirst_whenNonEmpty_shouldAddItFirst(self):
        value_to_add = -22
        cl = self.setup_list(1, 2)

        cl.add_first(value_to_add)

        self.assertCustomListStringsEqual([value_to_add, 1, 2], cl)


if __name__ == '__main__':
    unittest.main()
