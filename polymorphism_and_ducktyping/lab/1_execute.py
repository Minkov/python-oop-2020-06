def execute(func, *args):
    return func(*args)


# Test Code
def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")


def say_bye(name):
    print(f"Bye, {name}")


execute(say_hello, "Peter", "George")  # Hello, Peter, I am George
execute(say_bye, "Peter")  # Bye, Peter
