from unittest import TestCase


class TestCaseBase(TestCase):
    def assertEmpty(self, iterable):
        if type(iterable) == dict:
            return self.assertDictEqual({}, iterable)
        if type(iterable) == set:
            return self.assertSetEqual(set(), iterable)

        return self.assertListEqual([], list(iterable))
