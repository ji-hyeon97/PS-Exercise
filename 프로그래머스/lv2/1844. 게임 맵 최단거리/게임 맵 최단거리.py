from collections import deque

def solution(maps):
    answer = 0
    queue = deque()
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    row = len(maps)
    col = len(maps[0])
    check = [[1 for _ in range(col)] for _ in range(row)]
    queue.append((0,0))
    
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=row or ny>= col:
                continue
            if check[nx][ny] != 1:
                continue
            if maps[nx][ny] == 0:
                continue
            if nx ==row and ny == col:
                return check[nx][ny]
            if maps[nx][ny] == 1 and check[nx][ny]==1:
                check[nx][ny] = check[x][y] + 1
                queue.append((nx,ny))
    if check[row-1][col-1] == 1:
        answer = -1
    else:
        answer = check[row-1][col-1]
    return answer