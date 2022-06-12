# https://www.acmicpc.net/problem/3460

T = int(input())
for i in range(T):
    n = int(input())
    b = bin(n)
    array = list(str(b))
    array.reverse()

    for i in range(len(array) - 2):
        if array[i] == '1':
            print(i, end=' ')
    

