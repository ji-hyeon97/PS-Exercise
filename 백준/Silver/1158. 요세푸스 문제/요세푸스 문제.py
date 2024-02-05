import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
queue = deque()

for i in range(n):
  queue.append(i+1)
  
answer = ['<']
while(True):
  if len(queue) == 0:
    break

  for i in range(k-1):
    target = queue.popleft()
    queue.append(target)

  target = queue.popleft()
  answer.append(target)
  
  if len(queue) == 0:
    continue
  answer.append(', ')

answer.append('>')
for i in answer:
  print(i, end="")