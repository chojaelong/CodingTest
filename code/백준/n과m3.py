result = []
array = []
visited = []

def recursion(n, m):
    global array
    for i in range(1, n + 1):
        if not visited[i]:
            array.append(i)
            visited[i] = True
        else:
            continue
        if len(array) < m:
            recursion(n, m)
        else:
            if set(array) not in result:
                result.append(set(array[:]))
                print(' '.join(map(str, array)))
        array.pop()
        visited[i] = False

n, m = map(int, input().split())
visited = [False] * (n + 1)
recursion(n, m)