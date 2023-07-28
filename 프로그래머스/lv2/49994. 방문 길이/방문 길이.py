import collections
def solution(dirs):
    answer = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    x,y= 0,0
    dic = {'U':0,'D':1,'R':2,'L':3}
    check = collections.defaultdict(int)
    for i in dirs:
        num = dic[i]
        nx = x+dx[num]
        ny = y+dy[num]
        if nx<-5 or ny<-5 or nx>5 or ny>5:
            continue
        data1 = ((x,y), (nx,ny))
        data2 = ((nx,ny), (x,y))
        if check[data1] == 0:
            answer+=1
            check[data1] +=1
            check[data2] +=1
        x = nx
        y = ny
    print(check)
    return answer