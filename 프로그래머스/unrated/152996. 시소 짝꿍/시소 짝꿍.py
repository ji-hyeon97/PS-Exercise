import collections

def solution(weights):
    answer = 0
    dic = collections.defaultdict(int)
    far = [2,3,4]
    for i in range(len(weights)):
        dic[weights[i]] +=1
    data = []
    for i in weights:
        for j in far:
            for k in far:
                if (i*j)/k in dic:
                    if i == (i*j)/k:
                        if dic[i]>1:
                            data.append((i,(i*j)/k))
                        else:
                            continue
                    else:
                        data.append((i,(i*j)/k))
    data = list(set(data))
    temp = 0
    for a,b in data:
        if a==b:
            answer+=dic[a]*(dic[a]-1)//2
        else:
            temp+=dic[a]*dic[b]
    temp = temp//2
    answer+=temp
                        
                        
                        
                            
                    
                    
    
    return answer