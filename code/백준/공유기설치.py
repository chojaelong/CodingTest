import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort()

start = 1
end = array[-1] - array[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    active = 1
    ts = array[0]
    for i in range(1, n):
        if array[i] - ts >= mid:
            active += 1
            ts = array[i]
    
    if active >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)