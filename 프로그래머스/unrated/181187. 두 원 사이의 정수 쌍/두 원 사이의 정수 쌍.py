import math 

def solution(r1, r2):
    answer = 0
    for i in range(r2+1):
        if i == 0:
            answer+=2*(r2-r1+1)
        if 0<i and i<r1:
            target1 = int(math.sqrt(r2*r2-i*i))
            target2 = int(math.sqrt(r1*r1-i*i))
            if target2 != math.sqrt(r1*r1-i*i):
                target2+=1
            answer+=(2*(target1-target2+1))*2
        if i>=r1:
            target1 = int(math.sqrt(r2*r2-i*i))
            answer+=(2*target1+1)*2
    return answer