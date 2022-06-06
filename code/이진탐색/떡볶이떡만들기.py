from bisect import bisect_left, bisect_right

n, h = map(int, input().split())
array = list(map(int, input().split()))
hList = []
count = 0

while True:
    sum = 0
    for i in range(n):
        if array[i] > count:
            sum = sum + array[i] - count
    if sum < h:
        break
    count += 1

print(count)