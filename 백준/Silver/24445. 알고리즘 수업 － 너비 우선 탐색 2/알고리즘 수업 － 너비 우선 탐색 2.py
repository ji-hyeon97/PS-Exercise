import sys
from collections import deque

n,m,r = map(int,sys.stdin.readline().split())

check = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
queue = deque()

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

index = 1
def bfs():
    global index
    while queue:
        node = queue.popleft()
        graph[node].sort(reverse=True)
        for i in graph[node]:
            if check[i] == 0:
                index+=1
                check[i] = index
                queue.append(i)

queue.append(r)
check[r] = index
bfs()

for i in range(1, len(check)):
    print(check[i])