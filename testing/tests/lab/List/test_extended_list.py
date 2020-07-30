import unittest

from lab.List.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def _test_integerListInit_whenNotOnlyIntegers_raiseException(self):
        with self.assertRaises(Exception) as context:
            IntegerList(1, 2, 3, True, 5)

        self.assertIsNotNone(context.exception)

    def test_integerListInit_whenOnlyIntegers_shouldStoreThem(self):
        values = [1, 2, 3, 4, 5]
        il = IntegerList(*values)

        self.assertListEqual(values, il.get_data())

    def test_integerListAdd_whenValueIsInteger_shouldBeAdded(self):
        il = IntegerList()
        il.add(1)

        self.assertListEqual([1], il.get_data())

    def test_integerListAdd_whenValueNotInteger_shouldRaise(self):
        il = IntegerList()

        with self.assertRaises(Exception) as context:
            il.add({})

        self.assertIsNotNone(context.exception)

    def test_integerListRemoveIndex_whenIndexIsValid_shouldRemoveElementAndReturnIt(self):
        il = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = il.remove_index(3)

        self.assertListEqual([1, 2, 3, 5, 6, 7], il.get_data())
        self.assertEqual(4, returned)

    def test_integerListRemoveIndex_whenIndexIsInvalid_shouldRaise(self):
        il = IntegerList(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(Exception) as context:
            il.remove_index(len(il.get_data()))

        self.assertIsNotNone(context.exception)

    def test_integerListGet_whenIndexIsValid_shouldReturnIt(self):
        il = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = il.get(3)

        self.assertEqual(4, returned)

    def test_integerListGet_whenIndexIsInvalid_shouldRaise(self):
        il = IntegerList(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(Exception) as context:
            il.get(len(il.get_data()))

        self.assertIsNotNone(context.exception)

    def test_integerListGetBiggest_shouldReturnTheMaxElement(self):
        il = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = il.get_biggest()

        self.assertEqual(7, returned)

    def test_integerListGetIndex_shouldReturnTheIndex(self):
        il = IntegerList(1, 2, 3, 4, 5, 6, 7)
        returned = il.get_index(4)

        self.assertEqual(3, returned)

    def test_integerListInsert_whenIndexIsValid_shouldInsertIt(self):
        il = IntegerList(1, 2, 3, 4, 5, 6, 7)
        il.insert(2, -1)

        self.assertListEqual([1, 2, -1, 3, 4, 5, 6, 7], il.get_data())

    def test_integerListInsert_whenIndexIsInvalid_shouldRaise(self):
        il = IntegerList(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(Exception) as context:
            il.insert(len(il.get_data()), -1)

        self.assertIsNotNone(context.exception)

    def test_integerListInsert_whenValueIsNotInteger_shouldRaise(self):
        il = IntegerList(1, 2, 3, 4, 5, 6, 7)

        with self.assertRaises(Exception) as context:
            il.insert(0, True)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
