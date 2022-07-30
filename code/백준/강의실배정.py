# https://www.acmicpc.net/problem/11000

from queue import PriorityQueue

n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]
array.sort(key=lambda x: x[0])

pque = PriorityQueue()
pque.put((-array[0][1], array[0][1]))
for i in range(1, n):
    if pque.queue[-1][1] <= array[i][0]:
        pque.get()
        pque.put((-array[i][1], array[i][1]))
    else:
        pque.put((-array[i][1], array[i][1]))

print(pque.qsize())