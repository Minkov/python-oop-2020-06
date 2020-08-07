from customlist import CustomList
from tests.TestCaseBase import TestCaseBase


class CustomListTestsBase(TestCaseBase):
    def setup_list(self, *args):
        cl = CustomList()
        [cl.append(x) for x in args]
        return cl

    def assertCustomListStringsEqual(self, ll, cl1):
        expected = f"{';'.join([repr(el) for el in ll])}"
        self.assertEqual(expected, str(cl1))
