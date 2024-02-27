import sys
sys.setrecursionlimit(10**6)

K = int(sys.stdin.readline().rstrip())

for _ in range(K):
    v, e = map(int, sys.stdin.readline().split())
    check = [0 for _ in range(v + 1)]
    number = [0 for _ in range(v + 1)]
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    flag = 0


    def dfs(node):
        global flag
        check[node] = 1
        for i in graph[node]:
            if check[i] == 0:
                number[i] = (number[node] + 1) % 2
                dfs(i)
            if number[node] == number[i]:
                flag = 1
                return


    for i in range(1, v + 1):
        if flag == 0:
            dfs(i)
        else:
            break
    if flag == 0:
        print("YES")
    else:
        print("NO")