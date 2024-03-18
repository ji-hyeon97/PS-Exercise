import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

tet = [
    [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1)],
    [(0, 1), (-1, 1), (-2, 1)], [(0, 1), (-1, 0), (-2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 1), (1, 0), (2, 0)],
    [(0, 1), (0, 2), (-1, 2)], [(-1, 0), (0, 1), (0, 2)], [(0, 1), (0, 2), (1, 2)], [(1, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (2, 1)], [(1, 0), (1, -1), (2, -1)], [(0, 1), (-1, 1), (-1, 2)], [(0, 1), (1, 1), (1, 2)],
    [(0, 1), (-1, 1), (0, 2)], [(-1, 1), (0, 1), (1, 1)], [(1, 1,), (0, 1), (0, 2)], [(-1, 0), (1, 0), (0, 1)]
]


def size(x, y, position):
    temp = graph[x][y]
    for dx, dy in position:
        nx = dx + x
        ny = dy + y
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            return 0
        temp += graph[nx][ny]
    return temp


answer = 0
for i in range(n):
    for j in range(m):
        for position in tet:
            answer = max(answer, size(i, j, position))

print(answer)