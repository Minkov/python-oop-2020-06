from customlist import CustomList

cl = CustomList()

[cl.append(x) for x in range(6)]

print(cl.dictionize())

cl.append(-5)
print(cl.dictionize())
