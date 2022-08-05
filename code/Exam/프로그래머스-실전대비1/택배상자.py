from collections import deque

def solution(order):
    queue = deque(order)
    now = 1
    temp = []
    truck = []
    while queue:
        next = queue.popleft()
        if next > now:
            for i in range(now, next):
                temp.append(i)
                now += 1
            truck.append(next)
            now += 1
        elif next < now:
            while temp:
                value = temp.pop()
                if value != next:
                    return len(truck)
                elif value == next:
                    truck.append(value)
                    break
        elif now == next:
            truck.append(next)
            now += 1
            
    return len(truck)