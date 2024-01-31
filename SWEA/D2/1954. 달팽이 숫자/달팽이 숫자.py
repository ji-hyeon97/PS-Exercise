t = int(input().rstrip())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test_case in range(t):
    graph = []
    n = int(input().rstrip())
    if n == 1:
        print("#" + str(test_case + 1))
        print(1)
        continue
    temp = []
    for i in range(n * n):
        temp.append(0)
        if (i + 1) % n == 0:
            graph.append(temp)
            temp = []
    idx = 1
    dir = 0
    x = 0
    y = 0
    graph[x][y] = 1
    while idx <= (n * n) + 1:
        x = x + dx[dir % 4]
        y = y + dy[dir % 4]
        if x < 0 or y < 0 or x >= n or y >= n or graph[x][y]:
            x = x - dx[dir % 4]
            y = y - dy[dir % 4]
            dir += 1
            x = x + dx[dir % 4]
            y = y + dy[dir % 4]
        idx += 1

        if graph[x][y] == 0:
            graph[x][y] = idx
    print("#" + str(test_case + 1))
    for data in graph:
        for i in data:
            print(i, end=" ")
        print()