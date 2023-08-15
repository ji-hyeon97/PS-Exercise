import math

def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        y = int(math.sqrt(d*d - i*i))//k + 1
        answer+=y
    return answer