def get_summator():
    result = 0

    def add(x):
        nonlocal result
        result += x
        return result

    return add


summator = get_summator()
summator2 = get_summator()

print(summator(1))
print(summator(1))
print(summator(1))
print(summator(1))
print(summator2(1))
print(summator(1))


def add(x):
    def internal_add(y):
        return x + y

    return internal_add


f = add(1)
print(f)
print(f(2))
print(f(3))
