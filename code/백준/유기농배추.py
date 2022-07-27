def dfs(x, y):
    array[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if array[nx][ny] == 1:
            dfs(nx, ny)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    array = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        x, y = map(int,input().split())
        array[x][y] = 1
    
    dx = (1, -1, 0, 0)
    dy = (0, 0, 1, -1)
    count = 0
    for i in range(M):
        for j in range(N):
            if array[i][j] == 1:
                count += 1
                dfs(i, j)
    
    print(count)
