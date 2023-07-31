import math 

def solution(progresses, speeds):
    answer = []
    time = []
    for i in range(len(progresses)):
        time.append(math.ceil((100-progresses[i])/speeds[i]))
    
    check = [0 for i in range(len(time)+5)]
    cnt = 1
    for i in range(len(time)):
        if check[i] == 1:
            continue
        aim = time[i] 
        for j in range(i+1,len(time)):
            if aim < time[j]:
                answer.append(cnt)
                cnt = 1
                break
            cnt+=1
            check[j] = 1
    answer.append(cnt)
    return answer