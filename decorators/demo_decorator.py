from functools import wraps
from time import sleep

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

    print_func = print_to_cmd
    if type == LOGGER_TYPES['file']:
        print_func = print_to_file

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args_str = ", ".join(map(str, args))
            print_func(f' --- Executing {func.__name__}({args_str}) ---')
            func(*args, **kwargs)

        return wrapper

    return decorator


def delay(seconds=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


class delay_decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        sleep(5)
        result = self.func(*args, **kwargs)
        return result


@delay_decorator
@log(LOGGER_TYPES['file'])
def say_hello(name):
    print(f'Hello, {name}')


class PrintPropertiesMixin:
    def __str__(self):
        pairs = [f'{key}={value}' for (key, value) in self.__dict__.items()]
        return '; '.join(pairs)


class Person(PrintPropertiesMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hi! I am {self.name}')

    @delay()
    def __str__(self):
        return super().__str__()

    def __call__(self, *args, **kwargs):
        return f'From __call__: {self}'


# print(Person)
# say_hello('Pesho')
# gosho = Person('Gosho', 18)
# print(gosho)
# gosho.say_hello()
#
# print(gosho())

print = log(type=LOGGER_TYPES['file'])(print)


@log()
def my_print(*args, **kwargs):
    return print(*args, **kwargs)


print('Hello')
# my_print('Hello')
