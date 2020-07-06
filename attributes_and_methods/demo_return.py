# variant 1
def f1():
    x = int(input())
    y = int(input())
    result = x + y
    print(result)


# Correct variant
def f2(x, y):
    result = x + y
    return result


def solve():
    x = int(input())
    y = int(input())
    result = f2(x, y)
    print(result)


# (input), expected_output
tests = [
    ([1, 2], 3),
    ([3, 5], 8),
    ([-3, 3], 0),
    ([-13, 5], -8),
]


def execute_test(func, params, expected_output):
    output = func(*params)
    print(f'Input: {params}, ' +
          f' Actual: {output},' +
          f' Expected: {expected_output}, ' +
          f'Correct: {output == expected_output}')


[execute_test(f2, params, expected) for (params, expected) in tests]
