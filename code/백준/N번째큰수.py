# https://www.acmicpc.net/problem/2693

n = int(input())
for _ in range(n):
    array = list(map(int, input().split()))
    array.sort()
    print(array[-3])