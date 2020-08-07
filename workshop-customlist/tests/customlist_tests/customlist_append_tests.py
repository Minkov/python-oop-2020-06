import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_AppendTests(CustomListTestsBase):
    def test_customListAppend_whenEmptyList_shouldReturnListWithTheElement(self):
        value = 5

        cl = self.setup_list()
        result = cl.append(5)

        self.assertListEqual([value], result)

    def test_customListAppend_whenListHasTwoElement_shouldReturnListWithNewElementAtTheEnd(self):
        cl = self.setup_list(1, 2)

        result = cl.append(3)

        self.assertListEqual([1, 2, 3], result)

if __name__ == '__main__':
    unittest.main()
