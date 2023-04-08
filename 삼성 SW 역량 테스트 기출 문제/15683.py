import sys
from collections import deque
import copy

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

cctv = deque()
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
  for j in range(m):
    if 1<=graph[i][j]<=5:
      cctv.append((graph[i][j],i,j))

minValue = int(1e9)

def fill(board,mm,x,y):
  for i in mm:
    nx=x
    ny=y
    while(True):
      nx += dx[i]
      ny += dy[i]
      if nx<0 or ny<0 or nx>=n or ny>=m:
        break
      if board[nx][ny] ==6:
        break
      if board[nx][ny] == 0:
        board[nx][ny] = 7
        
def dfs(depth,array):
  global minValue
  if depth == len(cctv):
    count = 0
    for i in range(n):
      count+=array[i].count(0)
    minValue = min(minValue,count)
    return
  temp = copy.deepcopy(array)
  cctvNumber,x,y = cctv[depth]
  for i in mode[cctvNumber]:
    fill(temp,i,x,y)
    dfs(depth+1, temp)
    temp = copy.deepcopy(array)

dfs(0,graph)
print(minValue)