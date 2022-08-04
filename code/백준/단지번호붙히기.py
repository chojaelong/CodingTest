# https://www.acmicpc.net/problem/2667
from collections import deque

def bfs(i, j):
    global n
    # 동 서 남 북
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    array[i][j] = 0
    queue = deque([(i, j)])
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue

            if array[nx][ny] == 1:
                queue.append((nx, ny))
                array[nx][ny] = 0
                count += 1
    
    return count
        

n = int(input())
array = [list(map(int, input())) for _ in range(n)]

answer = []
for x in range(n):
    for y in range(n):
        if array[x][y] == 1:
            value = bfs(x, y)
            answer.append(value)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
