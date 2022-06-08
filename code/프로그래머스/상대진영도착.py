from collections import deque

def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                if nx == 0 and ny == 0:
                    continue
                graph[nx][ny] = graph[x][y] + 1

    print(graph[n-1][m-1])
    for i in graph:
        print(i)

    return graph[n-1][m-1] if graph[n-1][m-1] != 1 else -1

def solution(graph):
    return bfs(0, 0, graph)

graph = [[1,1,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,1,0,1]]
n = len(graph)
m = len(graph[0])
solution(graph)