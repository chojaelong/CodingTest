# https://www.acmicpc.net/problem/2583
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    array[x][y] = 1
    # 동 서 남 북
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            if array[nx][ny] == 0:
                array[nx][ny] = 1
                queue.append((nx, ny))
                count += 1
    answer.append(count)


m, n, k = map(int, input().split())
array = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    i, j, x, y= map(int, input().split())
    for nx in range(i, x):
        for ny in range(j, y):
            array[nx][ny] = 1

count = 0
answer = []
for x in range(n):
    for y in range(m):
        if array[x][y] == 0:
            bfs(x, y)
            count += 1

print(count)
answer.sort()
print(*answer, sep=' ')
