import sys

n = int(sys.stdin.readline().rstrip())
one, two = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
check = [0 for _ in range(n + 1)]
data = []
answer = 0
flag = 1
data = []
def dfs(start, end, idx):
    if start == end:
        data.append(idx)
        return idx
    for i in graph[start]:
        if check[i] == 0:
            check[i] = 1
            dfs(i, end,idx+1)

check[one] = 1
dfs(one, two, 0)
if len(data) == 0:
    print(-1)
else:
    print(data[0])