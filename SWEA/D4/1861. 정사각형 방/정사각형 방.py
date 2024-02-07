from collections import deque
import collections

test_case = int(input())

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

for t in range(1, test_case + 1):
    n = int(input())
    graph = []
    for _ in range(n):
        data = list(map(int, input().split()))
        graph.append(data)
    left = int(1e9)
    right = -int(1e9)
    queue = deque()
    dic = collections.defaultdict(list)


    def bfs():
        global right
        global flag
        while queue:
            x, y, times = queue.popleft()
            if right <= times:
                right = times
                flag = 1
                dic[right].append(int(1e9))

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny] == graph[x][y] + 1:
                    queue.append((nx, ny, times + 1))


    for i in range(n):
        for j in range(n):
            flag = 0
            queue.append((i, j, 1))
            bfs()
            if flag == 1:
                dic[right].append(graph[i][j])

    a = sorted(dic[max(dic)])
    left = a[0]
    print("#"+str(t)+" "+str(left)+" "+str(right))