def solution(n, horizontal):
    result = [[1 for _ in range(n)] for _ in range(n)]

    count = 1
    repeat = 1
    x = 0
    y = 0
    while(repeat < n):
        if horizontal:
            y += 1
            count += 1
            result[x][y] = count
            for _ in range(repeat):
                x += 1
                count += 1
                result[x][y] = count
            for _ in range(repeat):
                y -= 1
                count += 1
                result[x][y] = count
            horizontal = not horizontal
        elif not horizontal:
            x += 1
            count += 1
            result[x][y] = count
            for _ in range(repeat):
                y += 1
                count += 1
                result[x][y] = count
            for _ in range(repeat):
                x -= 1
                count += 1
                result[x][y] = count
            horizontal = not horizontal
        repeat += 1
    
    return result

solution(4, True)