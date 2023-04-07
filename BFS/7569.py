import sys
from collections import deque

n,m,h = map(int,sys.stdin.readline().split())
queue = deque()
graph = [[list(map(int,sys.stdin.readline().split())) for _ in range(m)] for _ in range(h)]
answer = 0
for i in range(h):
  for j in range(m):
    for k in range(n):
      if graph[i][j][k] == 0:
        answer+=1
      if graph[i][j][k] == 1:
        queue.append((i,j,k))
if answer == 0:
  print(0)
  exit()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
  while(queue):
    z,x,y = queue.popleft()
    for i in range(6):
      nz = z+dz[i]
      nx = x+dx[i]
      ny = y+dy[i]
      if nz<0 or nx<0 or ny<0 or nz>=h or nx>=m or ny>=n:
        continue
      if graph[nz][nx][ny] == 0:
        graph[nz][nx][ny] = graph[z][x][y] + 1
        queue.append((nz,nx,ny))
bfs()

target = []
for i in range(h):
  for j in range(m):
    for k in range(n):
      target.append(graph[i][j][k])

if 0 in target:
  print(-1)
else:
  print(max(target)-1)