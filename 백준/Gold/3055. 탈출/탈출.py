import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = []

for _ in range(r):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))

check = [[int(1e9) for _ in range(c)] for _ in range(r)]
check2 = [[0 for _ in range(c)] for _ in range(r)]

animal = deque()
water = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            animal.append((i, j, 0))
            check[i][j] = 1
        if graph[i][j] == '*':
            water.append((i, j, 0))
            check[i][j] = 1


def flood():
    while water:
        x, y, time = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == 'D':
                check[nx][ny] = time + 1
                continue
            if graph[nx][ny] == '.' and check[nx][ny] == int(1e9):
                check[nx][ny] = time + 1
                water.append((nx, ny, time + 1))


flood()
answer = int(1e9)


def move():
    global answer
    while animal:
        x, y, times = animal.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if graph[nx][ny] == 'D':
                answer = min(answer, times+1)

            if graph[nx][ny] == '.' and check2[nx][ny] == 0:
                check2[nx][ny] = times + 1
                if check[nx][ny] > check2[nx][ny]:
                    animal.append((nx, ny, times + 1))
                else:
                    check2[nx][ny] = 0


move()
if answer == int(1e9):
    print('KAKTUS')
else:
    print(answer)