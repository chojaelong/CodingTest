def solution(triangle):
    dp = []
    for i in range(0, len(triangle)):
        dp.append(triangle[i])
    
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):

            if j == 0:
                left_value = 0
            else:
                left_value = dp[i-1][j-1]
            if j == len(dp[i]) - 1:
                right_value = 0
            else:
                right_value = dp[i-1][j]
            
            dp[i][j] += max(left_value, right_value)

    answer = max(map(max, dp))
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)