from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n + 1)])
array = []

for j in range(n):
    count = 0
    while count < k - 1:
        queue.append(queue.popleft())
        count += 1
    
    array.append(queue.popleft())

print('<', end='')
print(', '.join(map(str, array)), end = '')
print('>')