# https://school.programmers.co.kr/learn/courses/30/lessons/87390#

def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        quotient = i // n # 1
        remainder = (i % n) + 1 # 4
        
        if quotient + 1 >= remainder:
            answer.append(quotient + 1)
        else:
            answer.append(remainder)
    
    return answer
            
            
solution(4, 7, 14)