array = []

def recursion(n, m, prev):
    global array
    repeat = 1
    if len(array) != 0:
        repeat = array[-1]
    for i in range(repeat, n + 1):
        array.append(i)
        if prev < m:
            recursion(n, m, prev + 1)
        else:
            print(' '.join(map(str, array)))
        array.pop()

n, m = map(int, input().split())
visited = [False] * (n + 1)
recursion(n, m, 1)