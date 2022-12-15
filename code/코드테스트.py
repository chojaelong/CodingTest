from collections import deque

array = [1, 2, 3]
queue = deque(array)
queue.popleft()
queue.popleft()
queue.popleft()

while queue:
    print(1)
    break