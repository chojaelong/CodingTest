n = int(input())
array = list(map(int, input().split()))

count = 0

for i in range(n - 1):
    if array[i] < array[i + 1]:
        array.pop(i + 1)
        count += 1

print(count)
