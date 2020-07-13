from random import randint


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'[{", ".join(self.data[::-1])}]'


#
# class Stack2(list):
#     def push(self, value):
#         self.append(value)
#
#     def peek(self):
#         return self[-1]
#
#     def is_empty(self):
#         return len(self) == 0

# s2 = Stack2()

s = Stack()
[s.push(str(randint(0, 100))) for _ in range(15)]

print(s)
print(s.pop())
print(s.peek())
print(s)
