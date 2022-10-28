def solution(brown, yellow):
    x = 3
    y = 3
    carpet = brown + yellow
    while True:
        if x * y == carpet:
            nbrown = (x * 2) + ((y - 2) * 2)
            if nbrown == brown:
                return [x, y]
        
        if x * y > carpet:
            y += 1
            x = y
        
        else:
            x += 1

print(solution(24, 24))