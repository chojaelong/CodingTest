# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(list)

    for array in clothes:
        clothes_dict[array[1]].append(array[0])

    arrays = list(clothes_dict.values())
    
    answer = 1
    for array in arrays:
        value = len(array) + 1
        answer *= value
    
    return answer - 1