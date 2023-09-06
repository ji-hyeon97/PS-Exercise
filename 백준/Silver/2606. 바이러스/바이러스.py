import sys

n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n + 3):
    graph.append([])

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (n + 2)
count = 0
visit[1] = 1


def dfs(idx):
    global count
    for i in graph[idx]:
        if visit[i] == 0:
            visit[i] = 1
            count += 1
            dfs(i)


dfs(1)
print(count)