#https://www.acmicpc.net/problem/1405

def back_tracking(cnt, visited, x, y, probability):
    global sum_probability

    if cnt == n:
        sum_probability += probability
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            back_tracking(cnt + 1, visited, nx, ny, probability * (probabilities[i] / 100))
            visited.pop()

n, E, W, S, N = map(int, input().split())
probabilities = [E, W, S, N]
array = ['E', 'W', 'S', 'N']
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
sum_probability = 0
back_tracking(0, [(0,0)], 0, 0, 1)
print(sum_probability)

# d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 4방향 탐색

# def dfs(r, c, visited, total):
#     global answer
#     if len(visited) == N+1:
#         answer += total
#         return
#     for idx in range(4):
#         nr = r + d[idx][0]
#         nc = c + d[idx][1]
#         if (nr, nc) not in visited:
#             visited.append((nr, nc))
#             dfs(nr, nc, visited, total*probability[idx])
#             visited.pop()

# N, ep, wp, sp, np = map(int, input().split())
# probability = [ep, wp, sp, np]
# answer = 0

# dfs(0, 0, [(0, 0)], 1)
# print(answer * (0.01 ** N))