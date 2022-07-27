# https://www.acmicpc.net/problem/1182

from itertools import combinations

n, s = map(int, input().split())
array = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
    combination = list(combinations(array, i))
    for value in combination:
        if sum(value) == s:
            count += 1

print(count)