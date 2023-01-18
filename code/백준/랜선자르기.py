k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]
array.sort()

start = 1
end = array[-1]

while start <= end:
    mid = (start + end) // 2
    value = 0
    for idx, s in enumerate(array):
        value += s // mid
    
    if value >= n:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)