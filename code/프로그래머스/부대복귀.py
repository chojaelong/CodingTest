from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    
    for start, end in roads:
        graph[start].append(end)
        graph[end].append(start)
        
    def bfs(start):
        distances = [100001 for _ in range(n + 1)]
        queue = deque([(start, 0)])
        condition = False
        
        while queue:
            now, distance = queue.popleft()
            
            for v in graph[now]:
                if distances[v] == 100001:
                    distances[v] = distance + 1
                    queue.append((v, distance + 1))
                    
        return distances
    
    answer = []
    distances = bfs(destination)
    for source in sources:
        if source == destination:
            answer.append(0)
        elif distances[source] == 100001:
            answer.append(-1)
        else:
            answer.append(distances[source])
    
    return answer

solution(3, [[1, 2], [2, 3]], [2, 3], 1)