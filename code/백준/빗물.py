# https://www.acmicpc.net/problem/14719

h, w = map(int, input().split())
array = list(map(int, input().split()))

answer = 0
for x in range(1, w - 1):
    for y in range(0, h):    
        if array[x] <= y:
            continue
        if array[x-1] > y and array[x+1] > y:
            answer += 1