import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(n):
  command = list(map(str,sys.stdin.readline().split()))
  if command[0] == 'push_front':
    queue.appendleft(command[1])
  if command[0] == 'push_back':
    queue.append(command[1])
  if command[0] == 'pop_front':
    if len(queue) == 0:
      print(-1)
    else:
      target = queue.popleft()
      print(target)
  if command[0] == 'pop_back':
    if len(queue) == 0:
      print(-1)
    else:
      target = queue.pop()
      print(target)
  if command[0] == 'size':
    print(len(queue))
  if command[0] == 'empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  if command[0] == 'front':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[0])
  if command[0] == 'back':
    if len(queue) == 0:
      print(-1)
    else:
      print(queue[-1])