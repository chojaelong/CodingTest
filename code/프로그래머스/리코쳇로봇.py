from collections import deque

def find_position(board, word):
    for x, arr in enumerate(board):
        for y, w in enumerate(arr):
            if w == word:
                return (x, y, 0)
    return 'ERROR'

def solution(board):
    # n: 가로, m: 세로
    n = len(board[0])
    m = len(board)
    
    start = find_position(board, 'R')
    end = find_position(board, 'G')
    
    q = deque([start])
    visited = [[False for _ in range(n)] for _ in range(m)]
    
    while q:
        x, y, c = q.popleft()
        
        # 동 서 남 북
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        positions = []
        
        for i in range(4):
            nx, ny = x, y
            while 0 <= nx + dx[i] < m and 0 <= ny + dy[i] < n and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx = nx + dx[i]
                ny = ny + dy[i]
            if (nx, ny, 0) == end:
                return c + 1
            if (x != nx or y != ny) and not visited[nx][ny]:
                q.append((nx, ny, c + 1))
                visited[nx][ny] = True
    
    return -1
                

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))