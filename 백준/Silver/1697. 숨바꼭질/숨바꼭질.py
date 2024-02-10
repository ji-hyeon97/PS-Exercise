import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
queue = deque()
queue.append((n,k))
answer = [0 for i in range(200000)]

def bfs():
  while queue:
    x,y = queue.popleft()
    if x==y:
      print(0)
      return

    for i in [x+1,x-1,2*x]:
      nx = i

      if nx<0 or nx>100010:
        continue
        
      if nx == y:
        answer[nx] = answer[x]+1
        print(answer[y])
        return
        
      if answer[nx] != 0:
        continue
        
      if answer[nx] ==0:
        answer[nx] = answer[x]+1
        queue.append((nx,y))
bfs()