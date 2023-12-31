T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    check = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    def dfs(group):
        for i in graph[group]:
            if check[i] == 0:
                check[i] = 1
                dfs(i)


    answer = 0
    for i in range(1, n + 1):
        if check[i] == 0:
            check[i] = 1
            answer += 1
            dfs(i)
    print("#"+str(test_case)+" "+str(answer))