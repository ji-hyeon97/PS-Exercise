from collections import deque
cnt= 0
def solution(maps):
    answer = []
    queue =deque()
    row = len(maps)
    col = len(maps[0])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    check = [[0 for _ in range(col)] for _ in range(row)]
    global cnt
    
    def bfs():
        while queue:
            global cnt
            x,y = queue.popleft()
            cnt+=int(maps[x][y])
            check[x][y] = 1
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx<0 or ny<0 or nx>=row or ny>= col:
                    continue
                if check[nx][ny] ==1:
                    continue
                if maps[nx][ny] != 'X':
                    check[nx][ny] = 1
                    queue.append((nx,ny))
        return cnt
                    
    for i in range(row):
        for j in range(col):
            if maps[i][j] != 'X' and check[i][j] ==0:
                queue.append((i,j))
                answer.append(bfs())
                cnt = 0
    answer.sort()
    if len(answer) == 0:
        return [-1]    
    return answer