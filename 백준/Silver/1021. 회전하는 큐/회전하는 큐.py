import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
queue = deque()
for i in range(1,n+1):
  queue.append(i)

count = 0
for i in data:
  while(True):
    target = queue.index(i)
    
    if queue[0] == i:
      queue.popleft()
      break
      
    if target<=len(queue)/2:
      a = queue.popleft()
      queue.append(a)
      count+=1
    else:
      a = queue.pop()
      queue.appendleft(a)
      count+=1
      
print(count)