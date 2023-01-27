from collections import deque

def solution(x, y, n):    
    q = deque([x])
    s = set([x])
    cnt = 0
    
    def add(value):
        if (value not in s) and (value <= y):
            q.append(value)
            s.add(value)
    
    while q:
        cnt += 1
        size = len(q)
        for i in range(size):
            value = q.popleft()
            
            plus = value + n
            add(plus)
            
            multi2 = value * 2
            add(multi2)
            
            multi3 = value * 3
            add(multi3)
            
            if plus == y or multi2 == y or multi3 == y:
                return cnt
    
    return -1

print(solution(1, 100000, 3))