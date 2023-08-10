def solution(n):
    answer = ''
    dic = {'1':'1','2':'2','3':'4'}
    data = ''
    while True:
        if n==0:
            break
        if n%3==0:
            data+=str(3)
            n = (n//3)-1
        else:
            data+=str(n%3)
            n = n//3
    for i in range(len(data)-1,-1,-1):
        answer+=dic[data[i]]
    return answer