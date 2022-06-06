t = int(input())
answer = []
for i in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for _ in range(n):
        dp.append(array[index:index + m])
        index += m

    for y in range(1, m):
        for x in range(n):
            value = dp[x][y]
            if x == 0:
                dp[x][y] = max(dp[x][y-1] + value, dp[x+1][y-1] + value)
            elif x == n - 1:
                dp[x][y] = max(dp[x][y-1] + value, dp[x-1][y-1] + value)
            else:
                dp[x][y] = max(dp[x][y-1] + value, dp[x-1][y-1] + value, dp[x+1][y-1] + value)

    answer.append(max(map(max, dp)))

print(answer)