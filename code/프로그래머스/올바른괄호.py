from collections import deque

def solution(s):
    queue = deque([])
    
    for word in s:
        if word == '(':
            queue.append('(')
        elif word == ')':
            if len(queue) == 0:
                return False
            queue.popleft()
    
    if len(queue) != 0:
        return False
    
    return True