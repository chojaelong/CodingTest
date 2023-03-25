def find_start(park):
    for x, p in enumerate(park):
        for y, word in enumerate(list(p)):
            if word == "S":
                return x, y
    
    return "ERROR"

def solution(park, routes):
    # 동 서 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    directions = {"E": 0, "W": 1, "S": 2, "N": 3}
    
    # 가로 : m, 세로 : n
    m = len(park[0])
    n = len(park)
    
    x, y = find_start(park)
    for route in routes:
        px, py = x, y
        direction, cnt = route.split()
        direction = directions[direction]
        cnt = int(cnt)
        
        condition = True
        for i in range(cnt):
            x = x + dx[direction]
            y = y + dy[direction]
            
            if x < 0 or x >= n or y < 0 or y >= m or park[x][y] == "X":
                condition = False
                break
            
        if not condition:
            x, y = px, py
    
    return [x, y]