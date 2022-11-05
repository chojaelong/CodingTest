'''
import sys
read = sys.stdin.readline

N, K = map(int, read().split())
cache = [0] * (K+1)

for _ in range(N):
    w, v = map(int, read().split())
    for j in range(K, w-1, -1):
        cache[j] = max(cache[j], cache[j-w] + v)
print(cache[-1])
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = [[0, 0]]
for _ in range(n):
    array.append(list(map(int, input().split())))
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    weight = array[i][0]
    value = array[i][1]
    for j in range(1, k + 1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])