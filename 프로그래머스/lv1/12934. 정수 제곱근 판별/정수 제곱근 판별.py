import math

def solution(n):
    answer = -1
    target = int(math.sqrt(n))
    if target*target ==n:
        answer = (target+1)**2
    return answer