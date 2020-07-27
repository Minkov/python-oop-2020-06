class Fibonacci:
    def __init__(self):
        self.cache = {
            0: 0,
            1: 1,
        }

    def __call__(self, n):
        if n in self.cache:
            return self.cache[n]

        result = self(n - 1) + self(n - 2)

        self.cache[n] = result
        return result


fib = Fibonacci()
# 0 1 2 3 4 5 6  7  8  9
# 0 1 1 2 3 5 8 13 21 34
print(fib(7))
print(fib.cache)
