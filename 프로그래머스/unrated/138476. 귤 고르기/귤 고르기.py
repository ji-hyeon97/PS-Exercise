import collections

def solution(k, tangerine):
    answer = 0
    dic = collections.defaultdict(int)
    for i in tangerine:
        dic[i] +=1
    data = sorted(dic.items(), key=lambda v:-v[1])
    
    while True:
        for i in range(len(data)):
            if k<=0:
                return answer
            k = k-data[i][1]
            answer+=1