def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        
    for data in photo:
        score = 0
        for i in data:
            if i not in dic:
                continue
            score+=dic[i]
        answer.append(score)
            
    return answer