from itertools import combinations

def solution(number):
    array = list(combinations(number, 3))
    answer = 0
    
    for arr in array:
        if sum(arr) == 0:
            answer += 1
    
    return answer