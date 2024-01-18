import sys
from collections import deque

n,m,r = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
queue = deque()

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0 for _ in range(n+1)]
temp = 1
def bfs():
    global temp
    while queue:
        index,depth = queue.popleft()
        graph[index].sort()
        for i in graph[index]:
            if check[i] == 0:
                temp+=1
                check[i] = temp
                queue.append((i,temp))



queue.append((r,1))
check[r] = 1
bfs()

for i in range(1,len(check)):
    print(check[i])