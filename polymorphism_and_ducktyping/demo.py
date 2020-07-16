class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        return self.age


strr = 'asd'
ll = [1, 2, 3, 4]
ss = {5, 4, 1}
pp = Person('Pesho', 14)
print(len(strr))
print(len(ll))
print(len(ss))
print(len(pp))


def f(my_list: list):
    print(my_list)


f([1, 2, 3])
f(Person('Penka', 17))
