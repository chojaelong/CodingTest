n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

array1.sort()

for i in array2:
    condition = False
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if array1[mid] == i:
            condition = True
            break
        elif array1[mid] > i:
            right = mid - 1
        elif array1[mid] < i:
            left = mid + 1
    
    if condition:
        print(1)
    else:
        print(0)