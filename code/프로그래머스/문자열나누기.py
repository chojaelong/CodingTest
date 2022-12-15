from collections import deque
import sys
sys.setrecursionlimit(10001)

def split(queue, answer):
    if len(queue) == 0:
        return answer - 1
    
    first = queue.popleft()
    x, y = 1, 0
    
    while queue:
        word = queue.popleft()
        if first == word:
            x += 1
        else:
            y += 1
            
        if x == y:
            return split(queue, answer + 1)
    
    return answer

def solution(s):
    array = list(s)
    return split(deque(array), 1)
    
    
    
    