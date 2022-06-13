stack = []

def run(command):
    array = list(command.split())
    if array[0] == 'push':
        stack.append(array[1])
    elif array[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif array[0] == 'size':
        print(len(stack))
    elif array[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif array[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
        

n = int(input())

array = [input() for i in range(n)]

for i in array:
    run(i)