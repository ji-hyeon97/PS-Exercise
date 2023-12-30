T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = []
    for _ in range(n):
        temp = list(map(str, input().split()))
        graph.append(temp)
    answer = -int(1e9)
    target = [[] for _ in range(n)]
    for i in range(n):
        temp = ""
        for j in range(n):
            temp += graph[n - 1 - j][i]
        target[i].append(temp)

        temp2 = ""
        for j in range(n):
            temp2 += graph[n-1-i][n - 1 - j]
        target[i].append(temp2)

        temp3 = ""
        for j in range(n):
            temp3 += graph[j][n - 1 - i]
        target[i].append(temp3)
    print("#"+str(test_case))
    for data in target:
        for i in data:
            print(i, end=" ")
        print("")