from functools import wraps


def vowel_filter(func):
    @wraps(func)
    def wrapper():
        result = func()
        vowels = {'a', 'e', 'u', 'o', 'i', 'y'}
        return [x for x in result if x in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

@vowel_filter
def get_name():
    return 'Pesho'

print(get_letters())  # ["a", "e"]
print(get_name())