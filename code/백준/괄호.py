n = int(input())

for i in range(n):
    condition = True
    array = list(input())
    stack = []
    
    for val in array:
        if val == '(':
            stack.append('1')
        elif val == ')':
            if len(stack) == 0:
                condition = False
                break
            stack.pop()
    
    if len(stack) != 0:
        condition = False
    
    print('YES' if condition else 'NO')