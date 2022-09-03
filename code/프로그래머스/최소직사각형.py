# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    for array in sizes:
        if array[0] < array[1]:
            array[0], array[1] = array[1], array[0]
    
    max_x = 0
    max_y = 0
    
    for array in sizes:
        max_x = max(array[0], max_x)
        max_y = max(array[1], max_y)
        
    return max_x * max_y