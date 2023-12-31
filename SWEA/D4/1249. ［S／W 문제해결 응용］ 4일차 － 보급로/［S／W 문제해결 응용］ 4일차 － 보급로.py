from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test_case in range(1, T + 1):
    queue = deque()
    n = int(input())
    graph = []
    for _ in range(n):
        data = list(map(int, input()))
        graph.append(data)

    temp = [[int(1e9) for _ in range(n)] for _ in range(n)]
    temp[0][0] = graph[0][0]
    queue.append((0, 0))

    def bfs():
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if temp[nx][ny] > temp[x][y] + graph[nx][ny]:
                    temp[nx][ny] = temp[x][y] + graph[nx][ny]
                    queue.append((nx, ny))

    bfs()
    print("#"+str(test_case)+" "+str(temp[n - 1][n - 1]))