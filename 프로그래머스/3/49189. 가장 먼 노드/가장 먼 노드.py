import collections
from collections import deque

def solution(n, edge):
    answer = 0
    check = [0]*(n+5)
    data = collections.defaultdict(list)
    graph = [[] for _ in range(n+1)]
    queue = deque()
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    idx = 1
    queue.append((idx,1))
    check[1] = 1
    while queue:
        index,node = queue.popleft()
        data[index].append(node)
        for i in graph[node]:
            if check[i] == 0:
                check[i] = 1
                queue.append((index+1,i))
    index = 0
    for i in data:
        index = max(index,i)
    answer = len(data[index])
    return answer