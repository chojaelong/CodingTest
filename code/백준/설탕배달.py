# https://www.acmicpc.net/problem/2839

n = int(input())

array = [10e9] * 5001
array[3] = 1
array[5] = 1

for i in range(6, 5001):
    array[i] = min(array[i - 3] + 1, array[i - 5] + 1)

print(-1) if array[n] >= 10e9 else print(array[n])