class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.current_water = 0
        self.is_happy = False

    def water(self, quantity):
        self.current_water += quantity
        self.is_happy = self.get_happy_status()

    def get_happy_status(self):
        return self.water_requirements <= self.current_water

    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        else:
            return f'{self.name} is not happy'


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
