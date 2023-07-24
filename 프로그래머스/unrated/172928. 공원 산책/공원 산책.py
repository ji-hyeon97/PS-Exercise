def solution(park, routes):
    answer = []
    row = len(park)
    col = len(park[0])
    x,y = 0,0
    
    graph = [[] for _ in range(row)]
    
    idx = 0
    for i in park:
        for j in i:
            graph[idx].append(j)
        idx+=1     
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 'S':
                x,y = i,j
    for data in routes:
        where, go = data.split(" ")
        nx = x
        ny = y
        for _ in range(int(go)):
            if where == 'E':
                dx = nx
                dy = ny+1
                if dx<0 or dy<0 or dx>=row or dy>=col or graph[dx][dy] =='X':
                    nx = x
                    ny = y
                    break
                nx = dx
                ny = dy
            if where == 'N':
                dx = nx-1
                dy = ny
                if dx<0 or dy<0 or dx>=row or dy>=col or graph[dx][dy] =='X':
                    nx = x
                    ny = y
                    break
                nx = dx
                ny = dy
            if where == 'S':
                dx = nx+1
                dy = ny
                if dx<0 or dy<0 or dx>=row or dy>=col or graph[dx][dy] =='X':
                    nx = x
                    ny = y
                    break
                nx = dx
                ny = dy
            if where == 'W':
                dx = nx
                dy = ny-1
                if dx<0 or dy<0 or dx>=row or dy>=col or graph[dx][dy] =='X':
                    nx = x
                    ny = y
                    break
                nx = dx
                ny = dy
        x = nx
        y = ny
        
    answer = [x,y]
    return answer