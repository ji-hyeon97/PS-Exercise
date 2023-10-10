def solution(m, n, board):
    answer = 0
    data = set()
    graph = []
    for i in board:
        temp = []
        for j in i:
            temp.append(j)
        graph.append(temp)
    while True:
        for i in range(m-1):
            for j in range(n-1):
                target = graph[i][j]
                if target == []:
                    continue
                if graph[i+1][j] == target and graph[i+1][j+1] == target and graph[i][j+1] ==target:
                    data.add((i,j))
                    data.add((i+1,j))
                    data.add((i+1,j+1))
                    data.add((i,j+1))
        if len(data) == 0:
            break
        else:
            answer+=len(data)
            for a,b in data:
                graph[a][b] = []
            data = set()
        while True:
            flag = 1
            for j in range(n):
                for i in range(m-1):
                    if graph[i][j] != [] and graph[i+1][j] == []:
                        graph[i][j],graph[i+1][j] = graph[i+1][j],graph[i][j]
                        flag = 0
            if flag == 1:
                break
    return answer