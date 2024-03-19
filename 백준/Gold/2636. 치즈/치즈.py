import sys
from collections import deque
import collections

n, m = map(int, sys.stdin.readline().split())
graph = []
queue = deque()

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dic = collections.defaultdict(int)
queue.append((0, 0, 0))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

check = [[0 for _ in range(m)] for _ in range(n)]


def bfs():
    while queue:
        x, y, count = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0 and check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.appendleft((nx, ny, count))

            if check[nx][ny] == 0 and graph[nx][ny] == 1:
                check[nx][ny] = 1
                graph[nx][ny] = 0
                queue.append((nx, ny, count + 1))
                dic[count] += 1


bfs()
time = sorted(dic)[-1] + 1
print(time)
print(dic[time - 1])