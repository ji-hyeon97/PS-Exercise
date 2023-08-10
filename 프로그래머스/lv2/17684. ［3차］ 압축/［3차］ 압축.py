def solution(msg):
    answer = []
    dic = {}
    for i in range(65,91):
        dic[chr(i)] = i-64
    check = [0] * (len(msg)+3)
    for i in range(len(msg)):
        if check[i] == 1:
            continue
        temp = ''
        for j in range(i,len(msg)):
            temp+=msg[j]
            check[j] = 1
            if temp not in dic:
                answer.append(dic[temp[:-1]])
                dic[temp] = len(dic)+1
                check[j] = 0
                break
            if j == len(msg)-1:
                answer.append(dic[temp])
    return answer