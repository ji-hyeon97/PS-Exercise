import collections 
from collections import deque

def solution(land):
    answer = 0
    
    n = len(land)
    m = len(land[0])
    check = [[0 for _ in range(m)] for _ in range(n)]
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    oil = collections.defaultdict(int)
    
    def bfs(cnt):
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if check[nx][ny] != 0:
                    continue
                if land[nx][ny] == 1 and check[nx][ny] == 0:
                    check[nx][ny] = cnt
                    queue.append((nx,ny))

    queue = deque()
    cnt = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and check[i][j] == 0:
                queue.append((i,j))
                check[i][j] = cnt
                bfs(cnt)
                cnt+=1
    for i in range(n):
        for j in range(m):
            if check[i][j] != 0:
                oil[check[i][j]]+=1
    
    for i in range(m):
        temp = set()
        value = 0
        for j in range(n):
            temp.add(check[j][i])
        for i in temp:
            value+=oil[i]
        answer = max(answer,value)

    return answer