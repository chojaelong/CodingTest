# https://www.acmicpc.net/problem/2636
from collections import deque
from collections import Counter
import copy

def bfs(array, visited):
    cnt = 0
    queue = deque([(0, 0)])
    visited[0][0] = True
    # 동 서 남 북
    x_array = [0, 0, -1, 1]
    y_array = [1, -1, 0, 0]
    
    while(queue):
        dx, dy = queue.popleft()
        
        for i in range(4):
            mx = dx + x_array[i]
            my = dy + y_array[i]
            
            if mx >= n or mx < 0 or my >= m or my < 0:
                continue
            
            if not visited[mx][my] and array[mx][my] == 0:
                queue.append((mx, my))
                visited[mx][my] = True
            
            elif array[mx][my] == 1:
                array[mx][my] = 0
                visited[mx][my] = True
                cnt += 1
        
    return cnt

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
count = 0
condition = True

while condition:
    count += 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = bfs(array, visited)
    
    for arr in array:
        if any(arr):
            condition = True
            break
        else:
            condition = False
        
print(count)
print(cnt)