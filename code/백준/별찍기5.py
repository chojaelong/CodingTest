n = int(input())

dot = '*'
for i in range(1, n + 1):
    for j in range(n-i, 0, -1):
        print('', end=' ')
    print(dot * ((i * 2) - 1))