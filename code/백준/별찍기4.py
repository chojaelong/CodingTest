n = int(input())

dot = '*'
for i in range(n, 0, -1):
    for j in range(n-i):
        print('', end=' ')
    print(dot * i)