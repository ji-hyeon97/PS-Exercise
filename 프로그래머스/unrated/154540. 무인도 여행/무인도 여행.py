from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(queue,check,maps):
    stay = 0
    row = len(maps)
    col = len(maps[0])
    while(queue):
        x,y = queue.popleft()
        stay += int(maps[x][y])
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=row or ny>=col:
                continue
            if check[nx][ny] == 1:
                continue
            if maps[nx][ny]!='X' and check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.append((nx,ny))
    return stay

def solution(maps):
    answer = []
    row = len(maps)
    col = len(maps[0])
    check = [[0 for _ in range(col)] for _ in range(row)]
    queue = deque()
    for i in range(row):
        for j in range(col):
            if maps[i][j] != 'X' and check[i][j] == 0:
                queue.append((i,j))
                check[i][j] = 1
                answer.append(bfs(queue,check,maps))
    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer