import heapq
import collections

def solution(N, road, K):
    answer = 0
    dic = collections.defaultdict(int)
    graph = [[] for _ in range(N+1)]
    dist = [K+1 for _ in range(N+1)]
    newRoad = []
    for a,b,c in road:
        if (a,b) not in dic:
            dic[(a,b)] = c
            dic[(b,a)] = c
        else:
            if c<dic[(a,b)]:
                dic[(a,b)] = c
                dic[(b,a)] = c
    for a,b in dic:
        graph[a].append([b,dic[(a,b)]])
        graph[b].append([a,dic[(b,a)]])
    dist[1] = 0
    temp = []
    heapq.heappush(temp,[0,1])
    while temp:
        w,node = heapq.heappop(temp)
        for a,b in graph[node]:
            if dist[a] > dist[node]+b:
                dist[a] = dist[node]+b
                heapq.heappush(temp,[dist[a],a])
    for i in range(1,len(dist)):
        if dist[i] <= K:
            answer+=1
    return answer
