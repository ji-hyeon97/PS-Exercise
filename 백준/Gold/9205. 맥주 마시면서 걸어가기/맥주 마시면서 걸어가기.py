import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())


def bfs(homeX, homeY, festivalX, festivalY):
    queue = deque()
    queue.append((homeX, homeY))
    check = [0 for _ in range(n + 1)]
    while queue:
        x, y = queue.popleft()

        if abs(festivalX - x) + abs(festivalY - y) <= 1000:
            return "happy"

        for i in range(n):
            if check[i] == 0 and (abs(graph[i][0] - x) + abs(graph[i][1] - y)) <= 1000:
                check[i] = 1
                queue.append((graph[i][0], graph[i][1]))
    return "sad"


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    homeX, homeY = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(n):
        data = list(map(int, sys.stdin.readline().split()))
        graph.append(data)
    festivalX, festivalY = map(int, sys.stdin.readline().split())

    print(bfs(homeX, homeY, festivalX, festivalY))