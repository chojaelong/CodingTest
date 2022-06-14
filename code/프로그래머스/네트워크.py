# https://programmers.co.kr/learn/courses/30/lessons/43162

def dfs(graph, v, visited):
	visited[v] = True

	for i in range(len(graph)):
		if graph[v][i] and not visited[i]:
			dfs(graph, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
    
    return answer

n = 3
graph = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]


print(solution(3, graph))

