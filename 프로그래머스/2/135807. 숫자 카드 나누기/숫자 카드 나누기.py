import math

def solution(arrayA, arrayB):
    answer = 0
    data1 = arrayA[0]
    data2 = arrayB[0]
    for i in arrayA[1:]:
        data1 = math.gcd(data1,i)
    for i in arrayB[1:]:
        data2 = math.gcd(data2,i)
    flag = 1
    for i in arrayB:
        if i%data1 == 0:
            flag = 0
            break
    if flag == 1:
        answer = max(answer,data1)
    flag = 1
    for i in arrayA:
        if i%data2 == 0:
            flag = 0
            break
    if flag == 1:
        answer = max(answer,data2)
    return answer