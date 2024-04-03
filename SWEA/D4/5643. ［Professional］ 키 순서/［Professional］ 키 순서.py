T = int(input().rstrip())


def dfs1(node):
    for i in graph1[node]:
        if check[i] == 0:
            check[i] = 1
            dfs1(i)


def dfs2(node):
    for i in graph2[node]:
        if check[i] == 0:
            check[i] = 1
            dfs2(i)


for t in range(1, T + 1):
    N = int(input().rstrip())
    M = int(input().rstrip())
    answer = 0
    graph1 = [[] for _ in range(N + 1)]
    graph2 = [[] for _ in range(N + 1)]

    for i in range(M):
        a, b = map(int, input().split())
        graph1[a].append(b)
        graph2[b].append(a)

    for i in range(1, N + 1):
        check = [0 for _ in range(N + 1)]
        check[i] = 1
        dfs1(i)
        dfs2(i)
        if sum(check) == N:
            answer += 1
    print("#" + str(t) + " " + str(answer))