def solution(wallpaper):
    answer = [51, 51, -1, -1]
    points = [list(w) for w in wallpaper]
    
    for x, point in enumerate(points):
        for y, word in enumerate(point):
            if word == '#':
                answer[0] = min(answer[0], x)
                answer[1] = min(answer[1], y)
                answer[2] = max(answer[2], x + 1)
                answer[3] = max(answer[3], y + 1)
                
    return answer