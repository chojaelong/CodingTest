import math

def solution(levels):
    length = len(levels)
    levels.sort(reverse=True)
    # x / 문제 갯수 < 0.25
    # x < 0.25 * 문제 갯수
    num = math.trunc(0.25 * length)
    
    if num == 0:
        return -1
    
    return levels[num - 1]

solution([1, 2, 3, 4, 5, 6, 7, 8, 9])