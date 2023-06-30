import math

def solution(number, limit, power):
    answer = 0
    element = 0
    for i in range(1,number+1):
        t = int(math.sqrt(i))
        for j in range(1,t+1):
            if i%j == 0:
                element+=1
        if t**2==i:
            element = (element*2)-1
        else:
            element = element*2
            
        if element>limit:
            element = power
            
        answer+=element
        element = 0
    return answer