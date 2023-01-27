def solution(maps):
    answer = []
    visited = []
    new_map = []
    idx = 0
    row = len(maps)
    column = len(maps[0])
    
    # 방문해야 할 위치 처리
    for m in maps:
        array = list(m)
        visited.append([])
        new_map.append([])
        for word in array:
            if word =='X':
                visited[idx].append(True)
                new_map[idx].append(-1)
            else:
                visited[idx].append(False)
                new_map[idx].append(int(word))
        idx += 1
    
    # 동 서 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    value = []
    
    def dfs(x, y):
        visited[x][y] = True
        value.append(new_map[x][y])
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or nx >= row or ny < 0 or ny >= column:
                continue
            
            if not visited[nx][ny]:
                dfs(nx, ny)
                
    # 모든 섬을 순회하며 방문하지 않은 섬 DFS 수행
    for i in range(row):
        for j in range(column):
            if not visited[i][j]:
                value = []
                dfs(i, j)
                answer.append(sum(value))
    
    if len(answer) == 0:
        answer.append(-1)
    
    answer.sort()
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))

