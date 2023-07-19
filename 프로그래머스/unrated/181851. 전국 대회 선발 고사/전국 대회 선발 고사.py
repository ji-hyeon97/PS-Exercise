def solution(rank, attendance):
    answer = 0
    new = []
    dic = {}
    
    for i in range(len(rank)):
        dic[rank[i]] = i
        
    for i in range(len(rank)):
        new.append([rank[i],attendance[i]])
    new.sort(key=lambda v:v[0])
    
    data = []
    for i in range(len(rank)):
        if new[i][1] == True:
            data.append(dic[new[i][0]])
    
    answer = data[0] * 10000 + data[1] * 100 + data[2] 
            
    return answer