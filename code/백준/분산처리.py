# https://www.acmicpc.net/problem/1009
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    data = a % 10
    b = b % 4 + 4
    for _ in range(b - 1):
        data = (data * (a % 10)) % 10
    
    if(data == 0):
        print(10)
    else:
        print(data)