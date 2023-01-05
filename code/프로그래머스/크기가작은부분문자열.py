from collections import deque

def solution(t, p):
    length = len(p)
    array = list(t)
    answer = 0
    q1 = deque(array)
    q2 = deque([])
    
    for _ in range(length - 1):
        q2.append(q1.popleft())
    
    while q1:
        q2.append(q1.popleft())
        value = int(''.join(q2))
        if int(p) >= value:
            answer += 1       
        q2.popleft()
    
    return answer
        