import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_ReverseTests(CustomListTestsBase):
    def test_customlistReverse_whenEmpty_shouldReturnEmpty(self):
        cl = self.setup_list()
        result = cl.reverse()

        self.assertEmpty(result)

    def test_customlistReverse_whenSingleElement_shouldReturnListWithSingleElement(self):
        values = [1]
        cl = self.setup_list(*values)
        result = cl.reverse()

        self.assertListEqual(values[::-1], result)

    def test_customlistReverse_whenMultipleElements_shouldReturnThemReversed(self):
        values = list(range(4))
        cl = self.setup_list(*values)

        result = cl.reverse()
        self.assertListEqual(values[::-1], result)

if __name__ == '__main__':
    unittest.main()
