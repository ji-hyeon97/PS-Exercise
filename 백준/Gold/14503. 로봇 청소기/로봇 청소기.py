import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def recur(row, col, dr):
    cnt = 0
    while True:
        graph[row][col] = 2
        cnt += 1

        flag = 1
        while flag == 1:
            for i in [(dr + 3) % 4, (dr + 2) % 4, (dr + 1) % 4, dr]:
                nx = row + dx[i]
                ny = col + dy[i]
                if graph[nx][ny] == 0:
                    row = nx
                    col = ny
                    dr = i
                    flag = 0
                    break

            else:
                nx = row - dx[dr]
                ny = col - dy[dr]
                if graph[nx][ny] == 1:
                    return cnt
                else:
                    row = nx
                    col = ny


print(recur(r, c, d))