def solution(dirs):
    move = ['U', 'D', 'R', 'L']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = 0, 0
    move_set = set()
    
    for dir in dirs:
        i = move.index(dir)
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        move_set.add((x, y, nx, ny))
        move_set.add((nx, ny, x, y))
        x = nx
        y = ny
    
    return len(move_set) // 2

solution('LULLLLLLU')