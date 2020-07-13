class Parent:
    def get_parent(self):
        return 'Parent'


class Child(Parent):
    def get_child(self):
        return 'Child'


class GrandChild(Child):
    def get_grand_child(self):
        return 'Grand child'


print(Parent().get_parent())
print(Child().get_parent())
print(Child().get_child())

print(GrandChild().get_parent())
print(GrandChild().get_child())
print(GrandChild().get_grand_child())

print(GrandChild.__dict__)