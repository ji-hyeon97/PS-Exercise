import math

def solution(fees, records):
    answer = []
    inTime = [0] * 10010
    isIn = [0] * 10010
    sumT = [0] * 10010
    
    for data in records:
        a,b,c = data.split(" ")
        h,m = a.split(":")
        if c == "IN":
            isIn[int(b)] = 1
            inTime[int(b)] = int(h)*60 + int(m)
        if c == "OUT":
            isIn[int(b)] = 0
            stay = int(h)*60 + int(m) - inTime[int(b)]
            sumT[int(b)] += stay
            
    for i in range(10002):
        if isIn[i] != 0:
            stay = 23*60 + 59 - inTime[i]
            sumT[i]+=stay
    
    for i in sumT:
        if i!=0:
            answer.append(fees[1]+max(math.ceil((i-fees[0])/fees[2]),0)*fees[3])
    return answer