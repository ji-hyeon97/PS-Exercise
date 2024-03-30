import sys
import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
count = 0
while True:
    n = int(sys.stdin.readline().rstrip())
    count+=1
    if n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    dist = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]

    data = [(graph[0][0], 0, 0)]

    while data:
        cost, x, y, = heapq.heappop(data)
        if x == n - 1 and y == n - 1:
            print("Problem "+str(count)+": "+str(cost))
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if dist[nx][ny] > cost+graph[nx][ny]:
                dist[nx][ny] = cost + graph[nx][ny]
                heapq.heappush(data, (dist[nx][ny], nx, ny))