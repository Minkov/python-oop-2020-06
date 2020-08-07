import unittest

from customlist import CustomListIndexException
from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_PopTests(CustomListTestsBase):
    def test_customListPop_whenEmptyList_shouldRaise(self):
        cl = self.setup_list()
        with self.assertRaises(CustomListIndexException) as context:
            cl.pop()

        self.assertIsNotNone(context.exception)

    def test_customListPop_whenNonEmpty_shouldReturnLastElement(self):
        value_to_pop = -22
        cl = self.setup_list(1, 2, value_to_pop)

        result = cl.pop()

        self.assertEqual(value_to_pop, result)
        self.assertCustomListStringsEqual([1, 2], cl)

if __name__ == '__main__':
    unittest.main()
