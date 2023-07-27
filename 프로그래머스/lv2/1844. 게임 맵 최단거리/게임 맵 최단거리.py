from collections import deque

def solution(maps):
    answer = 0
    queue = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    row = len(maps)
    col = len(maps[0])
    queue.append((0,0))
    check = [[0 for _ in range(col)] for _ in range(row)]
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx<0 or ny<0 or nx>=row or ny>=col:
                continue
            
            if maps[nx][ny] ==0 or check[nx][ny] ==1:
                continue
            
            if maps[nx][ny] == 1 and check[nx][ny] == 0:
                maps[nx][ny] = 1+maps[x][y]
                check[nx][ny] = 1
                queue.append((nx,ny)) 
                
    if maps[row-1][col-1] == 1:
        return -1
    return maps[row-1][col-1]