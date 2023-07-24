import math
def solution(n, words):
    answer = []
    cnt = 0
    data = ''
    flag = 1
    dic = {}
    for i in words:
        cnt+=1
        if i in dic:
            flag = 0
            break
        dic[i] = 1
        if len(data) == 0:
            data = i[-1]
            continue
        if data != i[0]:
            flag = 0
            break
        if data == i[0]:
            data = i[-1]
            
    if flag == 1:
        answer = [0,0]
    else:
        if cnt%n == 0:
            data = n
        else:
            data = cnt%n
        answer = [data, math.ceil(cnt/n)]
    return answer