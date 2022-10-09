# https://www.acmicpc.net/problem/7576
from collections import deque

def bfs(queue, array):   
    # 동 서 남 북
    x_array = [0, 0, -1, 1]
    y_array = [1, -1, 0, 0]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            dx = x + x_array[i]
            dy = y + y_array[i]
            
            if dx < 0 or dx >= n or dy < 0 or dy >= m:
                continue

            elif array[dx][dy] == 0:
                array[dx][dy] = array[x][y] + 1
                queue.append((dx, dy))
                
                
            

m, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            queue.append((i, j))
            
bfs(queue, array)
answer = 0

for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            print(-1)
            exit()
    answer = max(answer, max(array[i]))
    
print(answer - 1)