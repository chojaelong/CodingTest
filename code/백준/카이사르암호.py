# https://www.acmicpc.net/problem/5598
array = list(input())

for i in range(len(array)):
    array[i] = chr((ord(array[i])-68) % 26 + 65)

print(''.join(array))