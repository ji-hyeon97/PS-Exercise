def solution(players, callings):
    answer = []
    dic = {}
    check = {}
    for i in range(len(players)):
        dic[players[i]] = i
    for i in range(len(players)):
        check[i] = players[i]
                
    for i in callings:
        target = dic[i]-1
        loser = check[dic[i] - 1]
        dic[loser] = dic[loser] + 1
        dic[i] -=1
        check[target+1] = loser
        check[target] = i
    
    for i in range(len(check)):
        answer.append(check[i])
        
    return answer