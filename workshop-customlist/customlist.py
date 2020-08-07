from collections.abc import Iterable


class CustomListIndexException(Exception):
    pass


class CustomListTypeException(Exception):
    pass


class CustomListSumException(Exception):
    pass


# TODO make this decorator and remove the ifs in the methods
# Decorator IS accepting an argument which is the index, so do not forget the wrapper function
def is_index_integer(index):
    # TODO refactor to be decorator
    if not isinstance(index, int):
        raise CustomListTypeException(f"Index must be of type integer it was {type(index)}")
    return True


class CustomList:
    def __init__(self, *args):
        self.sequence = [el for el in args]

    def __verify_index(self, index, shouldIncludePlusOne=False):
        try:
            if shouldIncludePlusOne:
                if not self.sequence:
                    return
                elif index > 0:
                    self.sequence[index - 1]
                else:
                    self.sequence[index]
            else:
                self.sequence[index]
        except IndexError as ex:
            raise CustomListIndexException(f"MyCustomList does not found element on this"
                                           f" index - {index}\nOriginal exception was - {str(ex)}")
        except TypeError:
            raise CustomListTypeException(
                f"Index argument does not mach the supported type. Should be integer it was {type(index)}")

    def append(self, value):
        # TODO int onj is not iterable list(value)
        self.sequence = self.sequence + [value]
        return self.sequence

    def remove(self, index):
        self.__verify_index(index)
        value = self.sequence[index]
        del self.sequence[index]
        return value

    def get(self, index):
        self.__verify_index(index)
        return self.sequence[index]

    def extend(self, iterable):
        if not isinstance(iterable, Iterable):
            raise CustomListTypeException("The argument should iterable")
        self.sequence = self.sequence + list(iterable)
        return self.sequence

    def insert(self, index, value):
        self.__verify_index(index, shouldIncludePlusOne=True)
        self.sequence = self.sequence[0:index] + [value] + self.sequence[index:]
        return self.sequence

    def pop(self):
        try:
            value = self.sequence[-1]
            del self.sequence[-1]
            return value
        except IndexError:
            raise CustomListIndexException(f"MyCustomList does not contain elements")

    def clear(self):
        self.sequence = []

    def index(self, value):
        for index in range(len(self.sequence)):
            if self.sequence[index] == value:
                return index
        return -1

    def count(self, value):
        counter = 0
        for el in self.sequence:
            if el == value:
                counter += 1
        return counter

    def reverse(self):
        return self.sequence[::-1]

    def copy(self):
        return CustomList(*self.sequence)

    def __str__(self):
        return f"{';'.join([repr(el) for el in self.sequence])}"

    def __repr__(self):
        return str(self)

    def size(self):
        return len(self.sequence)

    def add_first(self, value):
        self.sequence = [value] + self.sequence

    def dictionize(self):
        custom_dict = {}
        for index in range(0, len(self.sequence), 2):
            try:
                custom_dict[self.sequence[index]] = self.sequence[index + 1]
            except IndexError:
                custom_dict[self.sequence[index]] = " "
        return custom_dict

    def move(self, amount):
        if len(self.sequence) == 0:
            return []
        self.sequence = self.sequence[amount:] + self.sequence[0:amount]
        return self.sequence

    def sum(self):
        result = 0
        for el in self.sequence:
            if isinstance(el, int) or isinstance(el, float):
                result += el
            elif hasattr(el, '__len__'):
                result += len(el)
            else:
                raise CustomListSumException(
                    f"Please provide a len method to custom objects if you want to sum elements.\n")
        return result

    def overbound(self):
        max_number = float('-inf')
        element = None
        for el in self.sequence:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el
            if max_number < num:
                max_number = num
                element = el
        return self.index(element)

    def underbound(self):
        min_number = float('inf')
        element = None
        for el in self.sequence:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el
            if min_number > num:
                min_number = num
                element = el
        return self.index(element)
