def even_numbers(func):
    def is_even(number):
        return number % 2 == 0

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # return [x for x in result if is_even(x)]
        return list(filter(is_even, result))

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))  # [2, 4]
