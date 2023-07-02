def solution(k, score):
    answer = []
    queue = []
    
    value = 0
    while(True):
        if value == len(score):
            break
        queue.append(score[value])
        queue.sort()
        if len(queue) > k:
            del queue[0]
        value+=1
        answer.append(queue[0])
    return answer