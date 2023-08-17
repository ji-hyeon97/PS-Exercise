import collections
import heapq
def solution(n, k, enemy):
    answer = 0
    data = []
    dic = collections.defaultdict(int)
    while True:
        for i in enemy:
            if n<i and k==0:
                return answer
            n = n-i
            heapq.heappush(data,-i)
            dic[i]+=1
            if n<0 and k>0:
                k = k-1
                m = -heapq.heappop(data)
                n = n + m
            answer+=1
        break 
    return answer