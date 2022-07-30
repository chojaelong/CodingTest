# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
array = [int(input()) for _ in range(n)]

array.sort()

count = 0
while k != 0:
    if k < array[-1]:
        array.pop()
    else:
        i = k // array[-1]
        k -= array.pop() * i
        count += i

print(count)