# https://school.programmers.co.kr/learn/courses/30/lessons/131704

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
            truck.append(now)
            now += 1
        elif next == now:
            truck.append(now)
            now += 1
        elif next < now:
            t = temp.pop()
            if t == next:
                truck.append(t)
            else:
                break
    
    return len(truck)

solution([4, 3, 1, 2, 5])