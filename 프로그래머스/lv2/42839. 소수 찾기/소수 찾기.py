import math
data = []

def dfs(cnt,check,numbers,num):
    global data
    if len(num) == cnt:
        data.append(int(num))
    else:
        for i in range(len(numbers)):
            if check[i] == 0:
                num+=numbers[i]
                check[i] = 1
                dfs(cnt,check,numbers,num)
                num = num[:-1]
                check[i] = 0
            
def solution(numbers):
    global data
    answer = 0
    check = [0] * (len(numbers)+3)
    for i in range(1, len(numbers)+1):
        dfs(i,check,numbers,"")
    data = list(set(data))
    for number in data:
        if number == 1 or number == 0:
            continue
        flag = 1
        for i in range(2,number):
            if number%i==0:
                flag = 0
                break
        if flag == 1:
            answer+=1
    return answer