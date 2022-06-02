n, k = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

for _ in range(k):
    max_value = max(arrayB)
    min_value = min(arrayA)
    max_index = arrayB.index(max_value)
    min_index = arrayA.index(min_value)
    if min_value >= max_value:
        break
    arrayA[min_index], arrayB[max_index] = arrayB[max_index], arrayA[min_index]

print(arrayA)
print(arrayB)
print(sum(arrayA))