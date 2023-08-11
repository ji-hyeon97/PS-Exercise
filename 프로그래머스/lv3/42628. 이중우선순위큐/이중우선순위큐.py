import heapq

def solution(operations):
    data = []
    for i in operations:
        a,b = i.split(" ")
        b = int(b)
        if a == 'I':
            heapq.heappush(data,b)
        if a == 'D' and b == -1:
            if len(data) == 0:
                continue
            heapq.heappop(data)
        if a == 'D' and b == 1:
            if len(data) == 0:
                continue
            temp = []
            for i in data:
                heapq.heappush(temp,-i)
            heapq.heappop(temp)
            data = []
            for i in temp:
                heapq.heappush(data,-i)
    if len(data) == 0:
        return [0,0]
    return[max(data),data[0]]