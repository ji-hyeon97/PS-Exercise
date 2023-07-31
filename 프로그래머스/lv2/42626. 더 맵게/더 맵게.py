import heapq

def solution(scoville, K):
    answer = 0
    data = []
    for i in scoville:
        heapq.heappush(data,i)
    flag = 0
    while True:
        first = heapq.heappop(data)
        if first >= K:
            flag = 1
            break
        if len(data) < 1:
            break
        second = heapq.heappop(data)
        mix = first + 2*second
        heapq.heappush(data,mix)
        answer+=1
    if flag == 0:
        return -1
    return answer