from functools import wraps
from time import time, process_time, perf_counter


def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def lowercase(func):
    def wrapper():
        result = func()
        return result.lower()

    return wrapper


def measure3(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print(f'Executed in {execution_time} seconds')
        return result

    return wrapper


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        print(f' --- Executing {func.__name__}({args_str}) ---')
        func(*args, **kwargs)

    return wrapper


LOGGER_TYPES = {
    'file': 'file',
    'cmd': 'cmd'
}


def log(type=LOGGER_TYPES['cmd']):
    def print_to_cmd(text):
        print(text)

    def print_to_file(text):
        with open('log.txt', 'a') as file:
            file.write(text)
            file.write('\n')

    def decorator(func):
        print_func = print_to_cmd
        if type == LOGGER_TYPES['file']:
            print_func = print_to_file

        @wraps(func)
        def wrapper(*args, **kwargs):
            args_str = ", ".join(map(str, args))
            print_func(f' --- Executing {func.__name__}({args_str}) ---')
            func(*args, **kwargs)

        return wrapper

    return decorator


def execute_func(func, *args, **kwargs):
    print(f' --- Before {func.__name__}() ---')
    result = func(*args, **kwargs)
    print(f' --- After {func.__name__}() ---')
    return result


def operation(operation):
    @measure3
    @logger
    def sum_numbers(*args):
        return sum(args)

    @measure3
    @logger
    def multiply_numbers(*args):
        result = 1
        for x in args:
            result *= x
        return result

    if operation == '+':
        return sum_numbers
    else:
        return multiply_numbers


# execute_func(print, 'Hello')
#
# operation_func1 = operation('+')
# operation_func2 = operation('*')
#
# print(operation_func1)

print(operation('+')(1, 2, 4))
print(operation('*')(1, 2, 4))


# numbers = [x for x in range(1, 20000000)]

# print(execute_func(operation('+'), *numbers))


def measure(func, *args):
    start_time = perf_counter()
    result = func(*args)
    end_time = perf_counter()
    execution_time = end_time - start_time
    print(f'Executed in {execution_time} seconds')
    return result


def measure2(func):
    start_time = perf_counter()
    result = func()
    end_time = perf_counter()
    execution_time = end_time - start_time
    print(f'Executed in {execution_time} seconds')
    return result


# my_operation = operation('+')
# print(my_operation)
# my_operation = measure3(my_operation)
# print(my_operation)
# print(my_operation(1, 2, 3, 4, 5))

def get_greeting_1():
    return f'Hello, I am Pesho'


@uppercase
def get_greeting_2():
    return f'Hello, I am Pesho'


@lowercase
def get_greeting_3():
    return f'Hello, I am Pesho'


@uppercase
@lowercase
def get_greeting_4():
    return f'Hello, I am Pesho'


print(get_greeting_1())
print(get_greeting_2())
print(get_greeting_3())
print(get_greeting_4())
print(uppercase(lowercase(get_greeting_1))())
