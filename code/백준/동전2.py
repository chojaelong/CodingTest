# https://www.acmicpc.net/problem/2294

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [100001] * 100001

for i in coins:
    dp[i] = 1

for i in range(1, k + 1):
    for coin in coins:
        pre_index = i - coin
        if pre_index > 0:
            dp[i] = min(dp[pre_index] + 1, dp[i])

print(-1) if dp[k] == 100001 else print(dp[k])