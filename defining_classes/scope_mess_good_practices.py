x = "global"


def outer():
    def inner(x):
        new_x = f"nonlocal {x}"
        print("inner:", new_x)
        return new_x

    def change_global():
        return "global: changed!"

    x = "local"
    print("outer:", x)
    x = inner()
    print("outer:", x)

    return change_global()


print(x)
x = outer()
print(x)

'''
global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!
'''
