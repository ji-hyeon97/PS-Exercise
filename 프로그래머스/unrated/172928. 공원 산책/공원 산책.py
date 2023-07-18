def solution(park, routes):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    d = {'N': 0, 'E' : 1, 'S' : 2, 'W' : 3}
    r = len(park)
    c = len(park[0])
    for i in range(r):
        for j in range(c):
            if park[i][j] == 'S':
                a,b = i,j
    for i in routes:
        command = i.split(" ")
        direction = command[0]
        dis = int(command[1])
        flag = 1
        n,m = a,b
        for _ in range(dis):
            nx = n + dx[d[direction]] 
            ny = m + dy[d[direction]]
            if nx<0 or ny<0 or nx>=r or ny>=c or park[nx][ny]=='X':
                flag = 0
                break
            n,m = nx,ny
        if flag:
            a,b = nx,ny
            
    answer = [a,b]
    return answer