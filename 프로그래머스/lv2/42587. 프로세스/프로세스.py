from collections import deque

def solution(priorities, location):
    process = [chr(i+97) for i in range(len(priorities))]
    target = process[location]
    dic = {}
    for i in range(len(priorities)):
        dic[process[i]] = priorities[i]
    queue = deque(process)
    cnt = 0
    while True:
        data = queue.popleft()
        if dic[data] == max(dic.values()):
            cnt+=1
            del dic[data]
            if data == target:
                return cnt
        else:
            queue.append(data)