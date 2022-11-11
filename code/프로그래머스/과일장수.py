from collections import deque

def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    q = deque(score)
    
    while len(q) >= m:
        value = 0
        for _ in range(m):
            value = q.popleft()
        
        answer += value * m
    
    return answer