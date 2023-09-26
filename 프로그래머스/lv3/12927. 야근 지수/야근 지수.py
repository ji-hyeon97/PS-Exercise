import heapq

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    data = []
    for i in works:
        heapq.heappush(data,-1*i)
    while True:
        if n == 0:
            break
        target = heapq.heappop(data) * -1
        target -= 1
        n -= 1 
        heapq.heappush(data, -1*target)
    for i in data:
        answer += i*i
    return answer