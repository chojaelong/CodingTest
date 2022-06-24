# https://www.acmicpc.net/problem/2501

n, k = map(int, input().split())

array = []

for i in range(1, n + 1):
    if n % i == 0:
        array.append(i)

print(array[k - 1]) if k <= len(array) else print(0)