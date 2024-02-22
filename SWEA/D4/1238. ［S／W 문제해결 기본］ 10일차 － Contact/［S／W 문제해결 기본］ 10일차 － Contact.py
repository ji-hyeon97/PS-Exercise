import collections
from collections import deque

for test_case in range(1, 11):
    a, b = map(int, input().split())
    data = list(map(int, input().split()))
    dic = collections.defaultdict(list)
    check = [0 for _ in range(101)]
    graph = [[] for _ in range(101)]
    for i in range(len(data) // 2):
        graph[data[2*i]].append(data[2*i + 1])
    temp = 0


    def bfs():
        global temp
        while queue:
            node, cnt = queue.popleft()
            temp = max(temp, cnt)
            dic[cnt].append(node)
            for i in graph[node]:
                if check[i] == 0:
                    check[i] = 1
                    queue.append((i, cnt + 1))


    queue = deque()
    queue.append((b, 0))
    check[b] = 1
    bfs()
    answer = sorted(dic[temp])
    print("#"+str(test_case)+" "+str(answer[-1]))