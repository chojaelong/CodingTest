# https://www.acmicpc.net/problem/1260
from collections import deque

def dfs(graph, visited, x):
    print(x, end=' ')
    visited[x] = True
    for value in graph[x]:
        if not visited[value]:
            dfs(graph, visited, value)
            
def bfs(graph, visited, x):
    visited[x] = True
    queue = deque([x])
    
    while queue:
        next = queue.popleft()
        print(next, end=' ')
        
        for value in graph[next]:
            if not visited[value]:
                queue.append(value)
                visited[value] = True
                
        


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
array = [list(map(int, input().split())) for _ in range(m)]

for arr in array:
    x, y = arr[0], arr[1]
    graph[x].append(y)
    graph[y].append(x)
    
for arr in graph:
    arr.sort()

dfs(graph, visited, v)
print()
visited = [False] * (n + 1)
bfs(graph, visited, v)