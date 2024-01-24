import sys

r, c = map(int, sys.stdin.readline().split())
graph = []
for _ in range(r):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visit = [0 for _ in range(30)]
visit[ord(graph[0][0])-65] = 1
answer = 0


def dfs(x, y, depth):
    global answer
    answer = max(answer, depth)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if visit[ord(graph[nx][ny])-65] == 0:
            visit[ord(graph[nx][ny])-65] = 1
            dfs(nx, ny, depth + 1)
            visit[ord(graph[nx][ny])-65] = 0


dfs(0, 0, 1)
print(answer)