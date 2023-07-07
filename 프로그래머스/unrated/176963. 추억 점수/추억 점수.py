def solution(name, yearning, photo):
    answer = []
    
    total = 0
    
    for element in photo:
        for i in element:
            if i not in name:
                continue
            target = name.index(i)
            total+=yearning[target]
        answer.append(total)
        total = 0
            
    return answer