import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(m):
  data = list(map(int, sys.stdin.readline().split()))
  graph.append(data)
  
queue = deque()

def bfs():
  while queue:
    x,y = queue.popleft()
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if nx<0 or ny<0 or nx>=m or ny>=n:
        continue

      if graph[nx][ny] != 0:
        continue

      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y]+1
        queue.append((nx,ny))
         
for i in range(m):
  for j in range(n):
    if graph[i][j] == 1:
      queue.append((i,j))     
bfs()

result = []
for i in graph:
  for j in i:
    result.append(j)
result.sort()
if 0 in result:
  print(-1)
else:
  print(result[-1]-1)