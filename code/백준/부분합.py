# https://www.acmicpc.net/problem/1806

n, s = map(int, input().split())
array = list(map(int, input().split()))

answer = 1000001
for i in range(n - 1):
    for j in range(i+1, n):
        if sum(array[i:j+1]) == s:
            answer = min(len(array[i:j]), answer)

if answer == 100001: 
    print(0) 
else: 
    print(answer)
