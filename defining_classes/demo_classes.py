def person_init(name):
    state = {'name': name}
    return state


def person_say_hello(state):
    print(f'{state["name"]} says \'Hello\'')


class Person:
    max_age = 150

    def __init__(self, name):
        print(f'Init method for person {name}')
        self.name = name
        print(self)

    def say_hello(self):
        print(f'{self.name} says \'Hello\'')

class NoInitPerson():
    pass
x = NoInitPerson()

p = Person('Pesho')
p.say_hello()
print(f'Output: {Person.say_hello(p)}')
print(Person.max_age)
# p2 = person_init('Pesho')
# person_say_hello(p2)
#
# Person('Gosho') \
#     .say_hello()
# Person('Pesho') \
#     .say_hello()
#
# Person.x = 5
# print(Person.x)
# print(str(Person))
#
#
# def f():
#     pass
#
#
# print(str(f))
# f.x = 'var'
# print(f.x)
