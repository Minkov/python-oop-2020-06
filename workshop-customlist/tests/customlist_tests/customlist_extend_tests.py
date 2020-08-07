import unittest

from customlist import CustomListTypeException
from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_ExtendTests(CustomListTestsBase):
    def test_customlistExtend_whenEmptyAndExtendWithNonEmptry_shouldExtendIt(self):
        cl = self.setup_list()
        other_list = list(range(4))

        result = cl.extend(other_list)

        self.assertListEqual(other_list, result)
        self.assertCustomListStringsEqual(other_list, cl)

    def test_customlistExtend_whenNonEmptyAndExtendWithEmptry_shouldExtendIt(self):
        initial_values = list(range(4))
        cl = self.setup_list(*initial_values)
        other_list = []

        result = cl.extend(other_list)

        self.assertListEqual(initial_values, result)
        self.assertCustomListStringsEqual(initial_values, cl)

    def test_customlistExtend_whenNonEmptyAndExtendWithNonEmptry_shouldExtendIt(self):
        initial_values = list(range(4))
        cl = self.setup_list(*initial_values)
        other_list = list(range(5, 10))

        result = cl.extend(other_list)

        self.assertListEqual(initial_values + other_list, result)
        self.assertCustomListStringsEqual(initial_values + other_list, cl)

    def test_customlistExtend_whenEmptyAndCustomIterable_shouldExtendIt(self):
        class CustomIterable:
            def __init__(self, value):
                self.is_done = False
                self.value = value

            def __iter__(self):
                return self

            def __next__(self):
                if self.is_done:
                    raise StopIteration
                self.is_done = True
                return self.value

        initial_values = list(range(4))
        cl = self.setup_list(*initial_values)
        other_list = CustomIterable(1)

        result = cl.extend(other_list)

        self.assertListEqual(initial_values + [1], result)
        self.assertCustomListStringsEqual(initial_values + [1], cl)

    def test_customlistExtend_whenNonIterable_shouldRaise(self):
        cl = self.setup_list()

        with self.assertRaises(CustomListTypeException) as context:
            cl.extend(1)

        self.assertIsNotNone(context.exception)

if __name__ == '__main__':
    unittest.main()
