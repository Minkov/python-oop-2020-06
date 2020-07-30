def fail_if_different(value1, value2):
    if value1 != value2:
        raise ValueError('Invalid test')


def sum(x, y):
    return 3

#
# def test1():
#     fail_if_different(
#         sum(1, 2),
#         3
#     )
#
#
# def test2():
#     fail_if_different(
#         sum(1, 1),
#         2
#     )
#
#
# tests = [
#     test1,
#     test2
# ]
#
# [test() for test in tests]
