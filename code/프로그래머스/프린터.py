from collections import deque

def check(queue, location):
    count = 0

    while queue:
        condition = True
        value = queue.popleft()
        
        for i in queue:
            if value < i:
                condition = False
                queue.append(value)
                break

        if condition:
            count += 1
            if location == 0:
                return count

        location = len(queue) - 1 if location == 0 else location - 1
            
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    print(check(queue, m))

            
        