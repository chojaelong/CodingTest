array = []
visited = []
result = set()

def recursion(n, m):
    global array
    for i in range(n):
        if not visited[i]:
            array.append(nums[i])
            visited[i] = True
        else:
            continue
        if len(array) < m:
            recursion(n, m)
        else:
            result.add(tuple(array))
        array.pop()
        visited[i] = False

n, m = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False] * n
recursion(n, m)
result = list(result)
result.sort()
for arr in result:
    print(' '.join(map(str, arr)))