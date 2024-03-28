def solution(board, h, w):
    answer = 0
    target = board[h][w]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = dx[i] + h
        ny = dy[i] + w
        
        if nx<0 or ny<0 or nx>=len(board) or ny>=len(board[0]):
            continue
        
        if board[nx][ny] == target:
            answer+=1
    return answer