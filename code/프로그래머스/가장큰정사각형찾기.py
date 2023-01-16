import copy

def solution(board):
    row = len(board[0])
    column = len(board)
    dp = copy.deepcopy(board)
    answer = 0
    
    if len(board) == 1 and len(board[0]) == 1:
        if board[0][0] == 0:
            return 0
        elif board[0][0] == 1:
            return 1
    
    for i in range(1, column):
        for j in range(1, row):
            if dp[i][j] != 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                answer = max(dp[i][j], answer)
    
    return answer ** 2
    
    