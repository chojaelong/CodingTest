import sys

# R L U D
dx = dict()
dx["R"] = 0
dx["L"] = 0
dx["U"] = -1
dx["D"] = 1

dy = dict()
dy["R"] = 1
dy["L"] = -1
dy["U"] = 0
dy["D"] = 0

x, y = 1, 1

size = int(input())
print(size)
array = input().split()
print(array)

cancel = {0, size + 1}

for i in array:
    if x + dx[i] in cancel or y + dy[i] in cancel:
        continue
    x += dx[i]
    y += dy[i]

print(x, y)