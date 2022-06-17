import sys
from collections import deque

n, m = map(int, input().split())
room_names = [input() for _ in range(n)]
uses = [list(map(str, input().split())) for _ in range(m)]
times = [deque([9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) for _ in range(n)]

for i in uses:
    index = room_names.index(i[0])
    for k in range(int(i[1]), int(i[2])):
        times[index].remove(k)

for i in range(n):
    print(f"Room {room_names[i]}:")
    array = []
    count = 0
    
    while times[i]:
        start = times[i][0]
        while True:
            if len(times[i]) == 1:
                end = times[i].popleft()
                array.append((start, end))
                count += 1
                break
            if times[i][0] + 1 == times[i][1]:
                times[i].popleft()
                continue
            else:
                end = times[i].popleft()
                array.append((start, end))
                count += 1
                break
    
    print("Not available") if count == 0 else print(f"{count} available:")
    for j in array:
        print(f"{j[0]}-{j[1]}")
    print("-----")
        