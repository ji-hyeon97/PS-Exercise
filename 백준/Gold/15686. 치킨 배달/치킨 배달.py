import sys
from collections import deque
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))
home = deque()
chicken = deque()

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      home.append((i,j))
    if graph[i][j] == 2:
      chicken.append((i,j))

answer = 999999
for chi in combinations(chicken,m):
  path = 0
  for h in home:
    target = 99999
    for i in range(m):
      target = min(target,abs(h[0]-chi[i][0])+abs(h[1]-chi[i][1]))
    path+=target
  answer=min(answer,path)
print(answer)