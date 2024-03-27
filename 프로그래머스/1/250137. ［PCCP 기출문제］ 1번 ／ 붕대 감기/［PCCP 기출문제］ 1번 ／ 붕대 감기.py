import collections

def solution(bandage, health, attacks):
    answer = -1
    times = []
    damages = []
    dic = {}
    
    for a,b in attacks:
        times.append(a)
        damages.append(b)
        dic[a] = b
    end = times[-1]
    
    success = 0
    care = health
    flag = 0
    
    for i in range(end+1):
        if i not in times:
            success+=1
            if care == health:
                continue
            else:
                care+=bandage[1]
                if care >= health:
                    care = health
                    continue
            if success == bandage[0]:
                care+=bandage[2]
                success = 0
                if care >= health:
                    care = health
                    continue
        if i in times:
            success = 0
            care = care-dic[i]
            if care<=0:
                flag = 1
                break
    if flag == 0:
        answer = care
    
    return answer