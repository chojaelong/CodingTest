from collections import deque

queue = deque()

def run(command):
    array = list(command.split())
    if array[0] == 'push':
        queue.append(array[1])
    elif array[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif array[0] == 'size':
        print(len(queue))
    elif array[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif array[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif array[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
        

n = int(input())

array = [input() for i in range(n)]

for i in array:
    run(i)