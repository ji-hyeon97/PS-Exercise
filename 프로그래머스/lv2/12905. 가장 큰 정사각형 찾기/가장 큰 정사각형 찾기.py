def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    for i in range(row):
        if board[i][0] == 1:
            answer = 1
            break
    for i in range(col):
        if board[0][i] == 1:
            answer = 1
            break
    for i in range(1,row):
        for j in range(1,col):
            if board[i][j] == 0:
                continue
            board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
            answer = max(answer,board[i][j])
    return answer*answer