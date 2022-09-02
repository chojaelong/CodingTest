# https://school.programmers.co.kr/learn/courses/30/lessons/12906

from collections import deque

def solution(arr):
    queue = deque(arr)
    array = []
    array.append(queue.popleft())
    
    while queue:
        value = queue.popleft()
        if array[-1] != value:
            array.append(value)
    
    return array
    