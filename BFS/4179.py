import sys
from collections import deque

r,c = map(int,sys.stdin.readline().split())
graph = []
for _ in range(r):
  data = list(map(str,sys.stdin.readline().rstrip()))
  graph.append(data)

fire = [[0 for _ in range(c)] for _ in range(r)]
jihoon = [[0 for _ in range(c)] for _ in range(r)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
fireQueue = deque()
jihoonQueue = deque()

def bfs():
  while(fireQueue):
    x,y = fireQueue.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if nx<0 or ny<0 or nx>=r or ny>=c:
        continue
      if graph[nx][ny] == 'F':
        continue
      if graph[nx][ny] == '#':
        continue
      if fire[nx][ny] == 0:
        if graph[nx][ny] == '.' or graph[nx][ny] == 'J':
          fire[nx][ny] = fire[x][y] + 1
          fireQueue.append((nx,ny))
  while(jihoonQueue):
    x,y = jihoonQueue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx<0 or ny<0 or nx>=r or ny>=c:
        print(jihoon[x][y])
        return
      if graph[nx][ny] == 'F':
        continue
      if graph[nx][ny] == '#':
        continue
      if jihoon[nx][ny] == 0 and graph[nx][ny] == '.':
        jihoon[nx][ny] = jihoon[x][y] + 1
        if jihoon[nx][ny] >= fire[nx][ny] and fire[nx][ny] != 0:
          continue
        jihoonQueue.append((nx,ny))
  print('IMPOSSIBLE')
  return
for i in range(r):
  for j in range(c):
    if graph[i][j] == 'F':
      fireQueue.append((i,j))
      fire[i][j] = 1
    if graph[i][j] == 'J':
      jihoonQueue.append((i,j))
      jihoon[i][j] =1
bfs()       