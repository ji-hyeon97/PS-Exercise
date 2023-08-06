from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    left = sum(queue1)
    queue2 = deque(queue2)
    right = sum(queue2)
    answer = 0
    if (left+right)%2 == 1:
        return -1
    while True:
        if left == right:
            return answer
        if len(queue1) == 0 or len(queue2) == 0:
            return -1
        if answer > 600000:
            return -1
        if left < right:
            data = queue2.popleft()
            right -= data
            queue1.append(data)
            left += data
            answer+=1
            continue
        if right < left:
            data = queue1.popleft()
            left -= data
            queue2.append(data)
            right += data
            answer+=1