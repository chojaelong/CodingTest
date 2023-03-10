from collections import deque

def solution(maps):
    array = [list(i) for i in maps]
    visited = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
    s = find(array, 'S')
    l = find(array, 'L')
    e = find(array, 'E')
    
    m = bfs(s, l, 0, array, visited)
    if m == -1:
        return m
    visited = [[False for _ in range(len(array[0]))] for _ in range(len(array))]
    answer = bfs(l, e, m, array, visited)
    
    return answer
    
def find(array, word):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == word:
                return (i, j)

def bfs(now, target, move, array, visited):
    q = deque([now])
    array[now[0]][now[1]] = move
    visited[now[0]][now[1]] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while(q):
        x, y = q.popleft()
    
        if (x, y) == target:
            return array[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < len(array)) and (0 <= ny < len(array[0])) and (array[nx][ny] != 'X') and (not visited[nx][ny]):
                array[nx][ny] = array[x][y] + 1
                visited[nx][ny] = True
                q.append((nx, ny))
                
    return -1
            
solution(["SOOOO","XXXXX","LOOOO","XXXXX","EOOOO"])