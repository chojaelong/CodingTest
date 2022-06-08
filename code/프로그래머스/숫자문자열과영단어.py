change = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for i in range(10):
    code = code.replace(change[i], str(i))

print(code)