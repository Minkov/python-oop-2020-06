ll = [1, 2, 3, 4]

even = [x for x in ll if x % 2 == 0]

even2 = []
for x in ll:
    if x % 2 == 0:
        even2.append(x)

print(even)
print(even2)