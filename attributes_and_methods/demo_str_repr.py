print(str(1))
print(repr(1))
my_str = 'x = \'asd\''
print(str(my_str))
print(repr(my_str))
# eval(my_str)
# eval(str(my_str))
eval(repr(my_str))