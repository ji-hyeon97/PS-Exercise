import sys
import copy
from collections import deque
from itertools import combinations

N, M, D = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)
dy = [-1, 0, 1]
dx = [0, -1, 0]
result = 0


def fight(archer):
    board = copy.deepcopy(graph)
    check = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for i in range(N - 1, -1, -1):
        die = []
        for m in archer:
            queue = deque()
            queue.append((i, m, 1))
            while queue:
                x, y, d = queue.popleft()
                if board[x][y] == 1:
                    die.append((x, y))
                    if check[x][y] == 0:
                        check[x][y] = 1
                        count += 1
                    break
                if d < D:
                    for j in range(3):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if 0 <= nx < N and 0 <= ny < M:
                            queue.append([nx, ny, d + 1])
        for x, y in die:
            board[x][y] = 0
    return count


for archer in combinations([i for i in range(M)], 3):
    result = max(result, fight(archer))
print(result)