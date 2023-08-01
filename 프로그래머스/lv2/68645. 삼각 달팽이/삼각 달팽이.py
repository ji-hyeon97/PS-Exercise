def solution(n):
    answer = []
    dic = {0:[1,0],1:[0,1],2:[-1,-1]}
    graph = [[0 for _ in range(n)] for _ in range(n)]
    
    idx = 0
    value = 1
    total = 0
    for i in range(1,n+1):
        total+=i
    x,y = 0,0    
    
    while True:
        graph[x][y] = value
        value+=1
        nx = x + dic[idx%3][0]
        ny = y + dic[idx%3][1]
        
        if nx<0 or ny<0 or nx>=n or ny>=n or graph[nx][ny] != 0:
            idx+=1
            
        nx = x + dic[idx%3][0]
        ny = y + dic[idx%3][1]
        x = nx
        y = ny
        
        if value == total+1:
            break
            
    for i in graph:
        for j in i:
            if j == 0:
                continue
            answer.append(j)
        
    return answer