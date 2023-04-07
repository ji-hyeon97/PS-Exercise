import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
queue = deque()
queue.append((n,m))
times = [0 for _ in range(200000)]

def bfs():
  while(queue):
    x,y = queue.popleft()
    dx = [x-1,x+1,2*x]

    if x==y:
      print(0)
      continue
    
    for i in range(3):
      nx = dx[i]
      if nx<0 or nx>100010:
        continue
        
      if nx == y:
        times[nx] = times[x]+1
        print(times[nx])
        return
        
      if times[nx] != 0:
        continue
        
      if times[nx] == 0:
        times[nx] = times[x] +1
        queue.append((nx,y))
bfs()