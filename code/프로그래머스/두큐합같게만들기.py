# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    q1_sum = sum(queue1)
    half_sum = (q1_sum + sum(queue2)) / 2
    answer = 0
    
    while queue1 and queue2:
        if q1_sum == half_sum:
            return answer
        elif q1_sum > half_sum:
            q1_sum -= queue1.popleft()
        else:
            queue1.append(queue2.popleft())
            q1_sum += queue1[-1]
        answer += 1
    
    return -1