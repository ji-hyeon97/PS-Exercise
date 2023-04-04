import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
  data = list(map(int,sys.stdin.readline().split()))
  graph.append(data)

check = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(i,j):
  queue = deque()
  queue.append((i,j))
  size = 1
  while(queue):
    x,y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if graph[nx][ny] ==0:
        continue
      if check[nx][ny] == 1:
        continue
      if graph[nx][ny] == 1 and check[nx][ny] == 0:
        size+=1
        check[nx][ny]=1
        queue.append((nx,ny))
  return size

value = 0
number = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and check[i][j]==0:
      number +=1
      check[i][j] =1
      size = bfs(i,j)
      if size>value:
        value = size
print(number)
print(value)