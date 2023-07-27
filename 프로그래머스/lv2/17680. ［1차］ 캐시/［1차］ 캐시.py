from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    for i in cities:
        i = i.lower()
        if len(queue) < cacheSize:
            if i in queue:
                new = deque()
                for j in queue:
                    if j!= i:
                        new.append(j)
                new.append(i)
                answer+=1
                queue = new
                continue
            queue.append(i)
            answer+=5
            continue
        if len(queue) == cacheSize:
            if i in queue:
                new = deque()
                for j in queue:
                    if j!= i:
                        new.append(j)
                new.append(i)
                answer+=1
                queue = new
            else:
                answer+=5
                queue.append(i)
                queue.popleft()
    return answer