from collections import Counter
from collections import deque

def solution(k, tangerine):
    c = Counter(tangerine)
    q = deque(c.most_common())
    answer = 0
    
    while k > 0:
        digit, number = q.popleft()
        k -= number
        answer += 1
    
    return answer
        