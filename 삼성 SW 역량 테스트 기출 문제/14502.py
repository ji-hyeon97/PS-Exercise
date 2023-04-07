import sys
import copy
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0

def bfs():
  virus = deque()
  test = copy.deepcopy(graph)
  for i in range(n):
    for j in range(m):
      if test[i][j] == 2:
        virus.append((i,j))
        
  while(virus):
    x,y = virus.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if test[nx][ny] == 0:
        test[nx][ny] = 2
        virus.append((nx,ny))
        
  count = 0
  global result
  for i in range(n):
    for j in range(m):
      if test[i][j] == 0:
        count+=1
  result = max(result, count)

def makeWall(count):
  if count == 3:
    bfs()
    return
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        makeWall(count+1)
        graph[i][j] = 0
        
makeWall(0)
print(result)