import sys
from collections import Counter

def solution(array1, array2):
    global n, m, k
    min_value = min(n, m)
    max_value = max(n, m)

    for i in range(min_value, 0, -1):
        way1 = []
        way2 = []
        for j in range(0, max_value + 1 - i):
            if len(array1) - i >= j:
                way1.append(array1[j : i + j])
            if len(array2) - i >= j:
                way2.append(array2[j : i + j])
        
        # for k in range(0, len(array2) + 1 - i):
        #     way2.append(array2[k : i + k])
        
        for x in way1:
            if x in way2:
                return i
    return 0
        


n, m, k = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

print(solution(array1, array2))
