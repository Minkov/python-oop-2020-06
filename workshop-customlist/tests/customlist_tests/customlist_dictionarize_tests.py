import unittest

from tests.customlist_tests.base.CustomListTestsBase import CustomListTestsBase


class CustomList_DictionarizeTests(CustomListTestsBase):
    def test_customListDictionarize_whenEmptyList_shouldReturnEmptyDictionary(self):
        cl = self.setup_list()

        result = cl.dictionize()

        self.assertEmpty(result)

    def test_customListDictionarize_whenListContainsEvenCountOfValues_shouldReturnDictionaryWithoutSpaces(self):
        count = 4
        cl = self.setup_list(*range(count))
        expected = {
            0: 1,
            2: 3,
        }

        self.assertDictEqual(expected, cl.dictionize())

    def test_customListDictionarize_whenListContainsOddCountOfValues_shouldReturnDictionaryWithSpace(self):
        count = 5
        cl = self.setup_list(*range(count))
        expected = {
            0: 1,
            2: 3,
            4: ' ',
        }

        self.assertDictEqual(expected, cl.dictionize())

if __name__ == '__main__':
    unittest.main()
