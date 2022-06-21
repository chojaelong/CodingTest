array = list(input())

stack = []

for value in array:
    if value == '(':
        stack.append(2)
    elif value == ')':
        stack.pop()