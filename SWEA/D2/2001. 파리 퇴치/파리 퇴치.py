t = int(input().rstrip())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        data = list(map(int, input().split()))
        graph.append(data)
    answer = 0
    for k in range(0, n - (m-1)):
        for t in range(0, n - (m-1)):
            temp = 0
            for i in range(k, k + m):
                for j in range(t, t + m):
                    temp += graph[i][j]
            answer = max(temp, answer)
    print("#" + str(test_case) + " " + str(answer))