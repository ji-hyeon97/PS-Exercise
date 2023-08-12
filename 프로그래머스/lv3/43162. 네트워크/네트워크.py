def dfs(graph,check,n):
    for i in graph[n]:
        if check[i] ==0:
            check[i] = 1
            dfs(graph,check,i)

def solution(n, computers):
    answer = 0
    check = [0 for _ in range(n)]
    graph = []
    for i in range(n):
        temp = []
        for j in range(n):
            if computers[i][j] ==1:
                temp.append(j)
        graph.append(temp)
    for i in range(n):
        if check[i] == 0:
            dfs(graph,check,i)
            answer+=1
    return answer