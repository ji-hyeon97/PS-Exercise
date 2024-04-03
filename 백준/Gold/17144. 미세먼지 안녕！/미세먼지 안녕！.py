import sys
from collections import deque
import copy

R, C, T = map(int, sys.stdin.readline().split())

graph = []

for _ in range(R):
    graph.append(list(map(int, sys.stdin.readline().split())))

cleanX = [-1, 0]
cleanY = [-1, 0]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(R):
    if graph[i][0] == -1:
        cleanX = [i, 0]
        cleanY = [i + 1, 0]
        break


def bfs():
    plus = [[0 for _ in range(C)] for _ in range(R)]
    while queue:
        x, y = queue.popleft()
        dust = graph[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if [nx, ny] == cleanX or [nx, ny] == cleanY:
                continue

            plus[nx][ny] += int(dust / 5)
            graph[x][y] -= int(dust / 5)

    for i in range(R):
        for j in range(C):
            graph[i][j] += plus[i][j]


def move():
    x, y = cleanX[0], cleanX[1]
    test = copy.deepcopy(graph)
    graph[x][y + 1] = 0
    for _ in range(C - 1):
        if test[x][y] == -1:
            y += 1
            continue
        graph[x][y + 1] = test[x][y]
        y += 1

    while x >= 1:
        graph[x - 1][y] = test[x][y]
        x -= 1

    for _ in range(C, 1, -1):
        graph[x][y - 1] = test[x][y]
        y -= 1

    for _ in range(cleanX[0]):
        if test[x + 1][y] == -1:
            graph[x + 1][y] = -1
            continue
        graph[x + 1][y] = test[x][y]
        x += 1

    x, y = cleanY[0], cleanY[1]
    graph[x][y + 1] = 0
    for _ in range(C - 1):
        if test[x][y] == -1:
            y += 1
            continue
        graph[x][y + 1] = test[x][y]
        y += 1

    while x < R - 1:
        graph[x + 1][y] = test[x][y]
        x += 1

    for _ in range(1, C):
        graph[x][y - 1] = test[x][y]
        y -= 1

    for _ in range(R - cleanY[0] - 1):
        if test[x - 1][y] == -1:
            graph[x - 1][y] = -1
            continue
        graph[x - 1][y] = test[x][y]
        x -= 1


for _ in range(T):
    queue = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] >= 1:
                queue.append((i, j))
    bfs()
    move()


answer = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1 or graph[i][j] == 0:
            continue
        answer += graph[i][j]
print(answer)