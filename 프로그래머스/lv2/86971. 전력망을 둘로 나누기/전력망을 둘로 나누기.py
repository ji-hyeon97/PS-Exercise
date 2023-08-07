answer = 1
def dfs(a,check,graph):
    global answer
    check[a] = 1
    for i in graph[a]:
        if check[i] == 0:
            answer +=1
            dfs(i,check,graph)
    
def solution(n, wires):
    global answer
    graph = [[]for _ in range(n+3)]
    data = []
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a,b in wires:
        check = [0] * (n+3)
        answer = 1
        check[b] = 1
        dfs(a,check,graph)
        data.append(abs(2*answer - n))
    data.sort()
    return data[0]