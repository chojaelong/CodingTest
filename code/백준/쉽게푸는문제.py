# https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())

array = []
condition = True
num = 1
while True:
    for i in range(num):
        if len(array) == 1000:
            condition = False
            break
        array.append(num)
    if not condition:
        break
    num += 1

print(sum(array[a-1:b]))