from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽이므로 진행 불가
            if array[nx][ny] == 0:
                continue

            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))

n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]
bfs()

print(array[n-1][m-1])
