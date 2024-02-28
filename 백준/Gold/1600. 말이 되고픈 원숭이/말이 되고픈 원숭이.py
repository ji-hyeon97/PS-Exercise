import sys
from collections import deque

K = int(sys.stdin.readline().rstrip())
W, H = map(int, sys.stdin.readline().split())

graph = []
for _ in range(H):
    graph.append(list(map(int, sys.stdin.readline().split())))

visit = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
able = 0
def bfs(x, y, cnt):
    global able

    q = deque()
    dx = [-1, 1, 0, 0,  -2, -1, 1, 2, -2, -1, 1, 2]
    dy = [0, 0, -1, 1,  -1, -2, -2, -1, 1, 2, 2, 1]
    visit[y][x][cnt] = 0
    q.append([x, y, cnt])
    while q:
        x, y, count = q.popleft()
        if x == W - 1 and y == H - 1:
            print(visit[y][x][count])
            able = 1
            break
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] != 1:
                if i < 4:
                    if visit[ny][nx][count] == 0:
                        visit[ny][nx][count] = visit[y][x][count] + 1
                        q.append([nx, ny, count])
                else:
                    if count < K and visit[ny][nx][count + 1] == 0:
                        visit[ny][nx][count + 1] = visit[y][x][count] + 1
                        q.append([nx, ny, count + 1])
    if able == 0:
        print(-1)


bfs(0, 0, 0)