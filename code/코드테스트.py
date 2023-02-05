n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def back_tracking(x, y, value):
    global answer
    # 위, 오른쪽
    dx = [-1, 0]
    dy = [0, 1]

    # 종료 조건
    if x == 0 and y == n - 1:
        answer = max(answer, value)
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            back_tracking(nx, ny, value + array[nx][ny])

back_tracking(n - 1, 0, array[n - 1][0])
print(answer)