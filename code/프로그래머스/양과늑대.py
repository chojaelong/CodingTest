def dfs(idx, sheep, wolf, possible):
    global g_info, answer, graph
    if g_info[idx] == 0:
        sheep += 1
        answer = max(answer, sheep)
    else:
        wolf += 1

    if wolf >= sheep:
        return 

    possible.extend(graph[idx])
    for p in possible:
        dfs(p, sheep, wolf, [i for i in possible if i != p])
        
def solution(info, edges):
    global answer, g_info, visited, graph
    answer = 0
    g_info = info
    n = len(info)
    graph = [[] for _ in range(n)]

    for a, b in edges:
        graph[a].append(b)


    dfs(0, 0, 0, [])
    return answer

solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])