import collections 

def solution(friends, gifts):
    result = 0
    
    giveCount = collections.defaultdict(int)
    getCount = collections.defaultdict(int)
    relation = collections.defaultdict(list)
    giftScore = collections.defaultdict(int)
    answer = collections.defaultdict(int)
    
    for i in friends:
        giveCount[i] += 0
        getCount[i] += 0
    
    for data in gifts:
        sender, receiver = data.split(" ")
        giveCount[sender] += 1
        getCount[receiver] += 1
        relation[sender].append(receiver)
    
    for i in friends:
        giftScore[i] = giveCount[i] - getCount[i]
        
    for i in friends:
        answer[i] = 0
        for j in friends:
            if i == j:
                continue
            if j in relation[i] or i in relation[j]:
                give = relation[i].count(j)
                receive = relation[j].count(i)    
                if give > receive:
                    answer[i]+=1
                elif give == receive:
                    if giftScore[i] > giftScore[j]:
                        answer[i]+=1

            if j not in relation[i] and i not in relation[j]:
                if giftScore[i] > giftScore[j]:
                    answer[i]+=1

    for i in answer:
        result = max(result, answer[i])
    return result