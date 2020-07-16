class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    ## __lt__
    ## __le__
    ## __ne__

ia_smaller = ImageArea(2, 3)
ia_bigger = ImageArea(3, 3)

print(' --- > ---')
print(ia_smaller > ia_bigger, False)
print(ia_smaller >= ia_bigger, False)
print(ia_smaller >= ia_smaller, True)

print(' --- < ---')
print(ia_smaller < ia_bigger, True)
print(ia_smaller <= ia_bigger, True)
print(ia_smaller <= ia_smaller, True)

print(' --- == ---')
print(ia_smaller == ia_bigger, False)
print(ia_smaller == ImageArea(ia_smaller.width, ia_smaller.height), True)

print(' --- != ---')
print(ia_smaller != ia_bigger, True)
print(ia_smaller != ImageArea(ia_smaller.width, ia_smaller.height), False)
