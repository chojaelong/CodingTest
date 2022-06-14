import heapq
import sys

n = int(sys.stdin.readline())

array = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(array) == 0:
            print(0)
            continue
        print(-heapq.heappop(array))
    else:
        heapq.heappush(array, -x)