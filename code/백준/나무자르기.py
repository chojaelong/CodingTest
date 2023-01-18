import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    value = 0
    
    for i in array:
        if i > mid:
            value += i - mid
    
    if value >= m:
        start = mid + 1
    elif value < m:
        end = mid - 1
    
print(end)