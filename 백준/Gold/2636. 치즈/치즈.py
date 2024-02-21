import sys
from collections import deque
import collections

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)

queue = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

check = [[0 for _ in range(m)] for _ in range(n)]

totalTime = 0

queue.append((0, 0, 0))
check[0][0] = 1
dic = collections.defaultdict(list)


def bfs():
    global totalTime
    while queue:
        x, y, cnt = queue.popleft()
        totalTime = max(totalTime, cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if check[nx][ny] == 0 and graph[nx][ny] == 0:
                check[nx][ny] = 1
                queue.appendleft((nx, ny, cnt))
                continue
            if check[nx][ny] == 0 and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                check[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))
                dic[cnt].append((nx, ny))


bfs()
print(totalTime)
print(len(dic[totalTime-1]))