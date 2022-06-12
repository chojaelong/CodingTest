n = int(input())

dot = '*'
for i in range(n):
    for j in range(n-i, 1, -1):
        print('', end=' ')
    print(dot * (i+1))