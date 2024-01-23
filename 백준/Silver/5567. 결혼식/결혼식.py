import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph =  [[]for _ in range(n+1)]
for _ in range(m):
    a,b= map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
check = [0 for _ in range(n+1)]
queue = deque()
queue.append((1,0))
check[1] = 1
answer = []

def bfs():
    global answer
    while queue:
        node,depth = queue.popleft()
        for i in graph[node]:
            if check[i] == 0:
                check[i] = 1
                if depth<2:
                    answer.append(i)
                    queue.append((i,depth+1))

bfs()
print(len(answer))