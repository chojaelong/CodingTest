import copy
from collections import deque

def bfs(n, wires):
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)
        
    start = wires[0][0]
    q = deque([start])
    visited[start] = True
    
    while q:
        node = q.popleft()
        for n in graph[node]:
            if not visited[n]:
                q.append(n)
                visited[n] = True

    y, n = 0, -1
    for result in visited:
        if result:
            y += 1
        else:
            n += 1
            
    return abs(y - n)
    
    
def solution(n, wires):
    array = []
    length = len(wires)
    min_value = n
    
    for i in range(length):
        temp = copy.deepcopy(wires)
        temp.pop(i)
        array.append(temp)
        
    for arr in array:
        value = bfs(n, arr)
        min_value = min(min_value, value)
    
    return min_value

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])