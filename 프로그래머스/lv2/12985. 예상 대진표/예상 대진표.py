import math
def solution(n,a,b):
    small = min(a,b)
    big = max(a,b)
    answer = 1
    while True:
        if big-small == 1 and small%2==1:
            break
        answer+=1
        small = math.ceil(small/2)
        big = math.ceil(big/2)
    return answer