from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque(people)
    
    while True:
        if len(queue) == 0:
            break
        if len(queue) > 1 and queue[0] + queue[-1] <= limit:
            answer+=1
            queue.pop()
            queue.popleft()
        else:
            answer+=1
            queue.pop()
    return answer