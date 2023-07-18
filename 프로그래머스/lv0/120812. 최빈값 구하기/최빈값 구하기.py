from collections import Counter
def solution(array):
    answer = []
    submit = 0
    data = Counter(array)
    frequent = 0
    
    for i in array:
        if data[i] >= frequent:
            frequent = data[i]
            
    for i in array:
        if data[i] == frequent:
            answer.append(i)
    
    answer = list(set(answer))
    if len(answer) >1:
        submit = -1
    else:
        submit = answer[0]
    return submit 