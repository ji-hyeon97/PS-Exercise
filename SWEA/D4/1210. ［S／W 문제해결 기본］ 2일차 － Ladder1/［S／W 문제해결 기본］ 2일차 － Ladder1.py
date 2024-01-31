for test_case in range(1, 11):
    graph = []
    n = int(input())
    for _ in range(100):
        data = list(map(int, input().split()))
        graph.append(data)
    c = 101
    for i in range(100):
        if graph[99][i] == 2:
            c = i
    for r in range(99, 0, -1):
        if c > 0 and graph[r][c - 1]:
            while c > 0 and graph[r][c - 1]:
                c -= 1
        elif c < 99 and graph[r][c + 1]:
            while c < 99 and graph[r][c + 1]:
                c += 1
    print("#" + str(test_case) + " " + str(c))