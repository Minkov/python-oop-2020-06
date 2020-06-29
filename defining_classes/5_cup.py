class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def can_fill(self, milliliters):
        return milliliters <= self.status()

    def fill(self, milliliters):
        if not self.can_fill(milliliters):
            return

        self.quantity += milliliters

    def status(self):
        return self.size - self.quantity


class Cup2:
    def __init__(self, size, quantity):
        self.size = size
        self.free_space = size - quantity

    def can_fill(self, milliliters):
        return milliliters <= self.status()

    def fill(self, milliliters):
        if not self.can_fill(milliliters):
            return

        self.free_space -= milliliters

    def status(self):
        return self.free_space


cup = Cup2(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())

cup = Cup2(100, 50)
cup.fill(10)
cup.fill(50)
print(cup.status())
