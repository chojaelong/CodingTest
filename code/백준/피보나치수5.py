
dp = [0] * 21
dp[1] = 1
def fibo(n):
    if n in {0, 1}:
        return dp[n]
    
    if dp[n] != 0:
        return dp[n]

    dp[n] = fibo(n-1) + fibo(n-2)

    return dp[n]

n = int(input())
print(fibo(n))

