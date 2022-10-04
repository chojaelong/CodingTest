array = []
#visited = []
result = []

def recursion(n, m, repeat):
    global array
    for i in range(repeat, n):
        array.append(nums[i])
        if len(array) < m:
            recursion(n, m, i)
        else:
            result.append(tuple(array))
        array.pop()
        #visited[i] = False

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
#visited = [False] * n
recursion(n, m, 0)
for arr in result:
    print(' '.join(map(str, arr)))