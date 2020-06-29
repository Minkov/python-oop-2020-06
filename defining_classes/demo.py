def print_text(text):
    print('*' * len(text))
    print(text)
    print('*' * len(text))


print_text('Hello')

for i in range(1, 10):
    print_text(f'This is {i}')

print_text('End')
