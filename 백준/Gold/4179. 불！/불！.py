import sys
from collections import deque

r,c = map(int, sys.stdin.readline().split())
graph = []
for i in range(r):
  data = list(map(str,sys.stdin.readline().rstrip()))
  graph.append(data)

fire = [[0] * c for j in range(r)]
jihoon = [[0] * c for j in range(r)]

fireQueue = deque()
jihoonQueue = deque()
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs():
  while fireQueue:
    x,y = fireQueue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if nx<0 or ny<0 or nx>=r or ny>=c:
        continue
      if graph[nx][ny] == '#':
        continue
      if graph[nx][ny] == 'F':
        continue
      if fire[nx][ny] == 0:
        if (graph[nx][ny] == '.' or graph[nx][ny] == 'J'):
          fire[nx][ny] = fire[x][y] + 1 
          fireQueue.append((nx,ny))
        
  while jihoonQueue:
    x,y = jihoonQueue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx<0 or ny<0 or nx>=r or ny>=c:
        print(jihoon[x][y])
        return 
      if graph[nx][ny] == '#':
        continue
      if graph[nx][ny] == 'F':
        continue
      if graph[nx][ny] == '.' and jihoon[nx][ny]==0:
        jihoon[nx][ny] = jihoon[x][y] + 1 
        if jihoon[nx][ny] >= fire[nx][ny] and fire[nx][ny] !=0:
          continue
        jihoonQueue.append((nx,ny))
  print("IMPOSSIBLE")
  return

for i in range(r):
  for j in range(c):
    if graph[i][j] == 'F':
      fire[i][j] = 1
      fireQueue.append((i,j))
    
    if graph[i][j] == 'J':
      jihoon[i][j] = 1
      jihoonQueue.append((i,j))

bfs()
