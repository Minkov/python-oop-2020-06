def generate_line(index, n):
    indent = ' ' * (n - index - 1)
    stars = '* ' * (index + 1)
    return f'{indent}{stars}'


def print_rhombus(n):
    for i in range(n):
        print(generate_line(i, n))

    for i in range(n - 2, -1, -1):
        print(generate_line(i, n))


print_rhombus(int(input()))
'''
 *
* *
 *
'''
'''
n = 4
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
'''

# print_rhombus(1)
# print_rhombus(2)
# print_rhombus(3)
# print_rhombus(4)
