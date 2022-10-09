# https://www.acmicpc.net/problem/10026
import copy
from collections import deque

def bfs(x, y, array, visited):
    queue = deque([(x, y)])
    
    
    # 동 서 남 북
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif not visited[nx][ny] and array[nx][ny] == array[x][y]:
                visited[nx][ny] = True
                queue.append((nx, ny))
        

n = int(input())
array = [list(input()) for _ in range(n)]
color_weakness = copy.deepcopy(array)
visited_a = [[False for _ in range(n)] for _ in range(n)]
visited_b = [[False for _ in range(n)] for _ in range(n)]
answer_a = 0
answer_b = 0

for i in range(n):
    for j in range(n):
        if color_weakness[i][j] == 'R':
            color_weakness[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited_a[i][j]:
            bfs(i, j, array, visited_a)
            answer_a += 1
        
        if not visited_b[i][j]:
            bfs(i, j, color_weakness, visited_b)
            answer_b += 1
            
print(answer_a, answer_b)