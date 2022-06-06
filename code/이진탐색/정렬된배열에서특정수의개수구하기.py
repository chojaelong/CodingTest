from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

leftIndex = bisect_left(array, x)
rightIndex = bisect_right(array, x)

print(leftIndex)

if(leftIndex == n):
    print(-1)
else:
    print(rightIndex - leftIndex)