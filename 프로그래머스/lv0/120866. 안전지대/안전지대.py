def solution(board):
    answer = 0
    
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    
    test = [[0 for _ in range(len(board))]  for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                test[i][j]=1
                for k in range(8):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if nx<0 or ny<0 or ny>=len(board) or nx>=len(board):
                        continue
                    test[nx][ny]=1
    for i in range(len(test)):
        for j in range(len(test)):
            if test[i][j] == 0:
                answer+=1                                          
    return answer