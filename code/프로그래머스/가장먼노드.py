from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
        
    def bfs():
        q = deque([(1, 0)])
        visited = [False] * (n + 1)
        visited[1] = True
        m_distance = 0
        count = 0
        
        while q:
            now, distance = q.popleft()
            if distance > m_distance:
                m_distance = distance
                count = 1
            else:
                count += 1
            
            for next in graph[now]:
                if not visited[next]:
                    visited[next] = True
                    q.append((next, distance + 1))
        
        return count
            
    
    return bfs()