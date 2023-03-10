def solution(board):
    o, x = 0, 0
    board = [list(t) for t in board]
    for temp in board:
        for word in temp:
            if word == 'O':
                o += 1
            elif word == 'X':
                x += 1
    # O와 X의 갯수가 0일 때            
    if o == 0 and x == 0:
        return 1
                
    # X의 갯수가 더 많을 때
    elif x > o:
        return 0
    # O의 갯수가 2개 이상 더 많을 때
    elif o - x >= 2:
        return 0

    # 이미 O가 이겼는데 X를 표시한 경우
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == 'O' or board[0][i] == board[1][i] == board[2][i] == 'O') and x >= o:
            return 0
    if (board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O') and x >= o:
        return 0
    
    # 이미 X가 이겼는데 게임을 계속 진행 했을 경우
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == 'X' or board[0][i] == board[1][i] == board[2][i] == 'X') and o > x:
            return 0
    if (board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X') and o > x:
        return 0
    
    return 1