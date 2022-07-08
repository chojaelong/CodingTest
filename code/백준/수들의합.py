n = int(input())

dp = [0, 1]

i = 2
while True:
    value = dp[i-1] + i
    dp.append(value)

    if value > n:
        break

    i += 1

print(i - 1)