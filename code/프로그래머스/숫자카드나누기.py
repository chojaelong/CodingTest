import math

def gcd(array):
    _gcd = array[0]
    for i in array[1:]:
        _gcd = math.gcd(_gcd, i)
        
        if _gcd == 1:
            return _gcd
    
    return _gcd

def solution(arrayA, arrayB):
    array = []
    array.append(arrayA)
    array.append(arrayB)
    
    gcds = []
    gcds.append((gcd(arrayA), 1))
    gcds.append((gcd(arrayB), 0))
    gcds.sort(reverse=True)
    
    answer = []
    
    for value, idx in gcds:
        if value == 1:
            continue
        
        condition = True
        for i in array[idx]:
            if i % value == 0:
                condition = False
                break
        
        if condition:
            answer.append(value)
            break
        
    return 0 if len(answer) == 0 else answer[0]