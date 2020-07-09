class SmartPhone:
    def __init__(self, vendor, model):
        self.__vendor = vendor
        self.__model = model

    def get_vendor(self):
        return self.__vendor

    def set_vendor(self, new_vendor):
        self.__vendor = new_vendor


p = SmartPhone('Doncho\'s Phone', 'SoftUni')

print(p.__dict__)
print(p._SmartPhone__vendor)
print(p.get_vendor())
