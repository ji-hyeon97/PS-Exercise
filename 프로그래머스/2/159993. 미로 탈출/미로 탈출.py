from collections import deque


def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    queue1 = deque()
    queue2 = deque()

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                queue1.append((i, j))
            if maps[i][j] == 'L':
                queue2.append((i, j))

    def bfs1():
        while queue1:
            x, y = queue1.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] == 'X':
                    continue
                if maps[nx][ny] == 'L':
                    return check[x][y] + 1
                if maps[nx][ny] == 'O' and check[nx][ny] == 0:
                    queue1.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1
                if maps[nx][ny] == 'E' and check[nx][ny] == 0:
                    queue1.append((nx,ny))
                    check[nx][ny] = check[x][y]+1

    def bfs2():
        while queue2:
            x, y = queue2.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] == 'X':
                    continue
                if maps[nx][ny] == 'E':
                    return check[x][y] + 1
                if maps[nx][ny] == 'O' and check[nx][ny] == 0:
                    queue2.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1
                if maps[nx][ny] == 'S' and check[nx][ny] == 0:
                    queue2.append((nx, ny))
                    check[nx][ny] = check[x][y] + 1

    check = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    oneStep = bfs1()
    check = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    twoStep = bfs2()

    if oneStep == None or twoStep == None:
        return -1
    else:
        return oneStep + twoStep