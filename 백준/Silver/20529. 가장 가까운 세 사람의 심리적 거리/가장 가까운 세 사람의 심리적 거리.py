import sys
import copy

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    answer = int(1e9)
    graph = []
    n = int(sys.stdin.readline().rstrip())
    data = list(map(str, sys.stdin.readline().split()))
    if n >= 33:
        print(0)
        continue
    for i in data:
        graph.append(i)

    check = [0 for _ in range(n + 3)]
    temp = []
    member = []


    def dfs(node):
        global temp
        global member
        if len(temp) == 3:
            temp2 = copy.deepcopy(temp)
            member.append(temp2)
            return
        for i in range(node, n):
            if check[i] == 0:
                check[i] = 1
                temp.append(i)
                dfs(i)
                check[i] = 0
                temp.pop()


    dfs(0)
    for friend in member:
        tmp = 0
        for i in range(4):
            if graph[friend[0]][i] != graph[friend[1]][i]:
                tmp += 1
            if graph[friend[1]][i] != graph[friend[2]][i]:
                tmp += 1
            if graph[friend[0]][i] != graph[friend[2]][i]:
                tmp += 1
        answer = min(answer, tmp)
    print(answer)