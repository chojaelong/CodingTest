import statistics
n = int(input())
array = list(map(int, input().split()))

max_value = max(array)

for i in range(len(array)):
    array[i] = array[i] / max_value * 100

print(statistics.mean(array))