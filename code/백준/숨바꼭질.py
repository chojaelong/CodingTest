from collections import deque
MAX_VALUE = 1000000

def bfs(n, k, depth, visited):
    queue = deque([n])
    visited[n] = True
    count = 0

    while queue:
        count += 1
        for v in list(queue):
            queue.popleft()
            if v+1 < MAX_VALUE and not visited[v+1]:
                queue.append(v+1)
                depth[v+1] = count
                visited[v+1] = True
            if v*2 < MAX_VALUE and not visited[v*2]:
                queue.append(v*2)
                depth[v*2] = count
                visited[v*2] = True
            if v-1 >= 0 and not visited[v-1]:
                queue.append(v-1)
                depth[v-1] = count
                visited[v-1] = True
            
            if visited[k]:
                return depth[k]

n, k = map(int, input().split())
visited = [False] * MAX_VALUE
depth = [0] * MAX_VALUE
print(bfs(n, k, depth, visited))


