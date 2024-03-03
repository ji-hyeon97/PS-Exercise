import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
person = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(1, data[0] + 1):
        graph[i].append(data[j])


def bfs(array):
    queue = deque()
    check = [0 for _ in range(n + 1)]
    queue.append(array[0])
    check[array[0]] = 1
    temp = 0
    cnt = 1
    while queue:
        x = queue.popleft()
        temp += person[x - 1]
        for nx in graph[x]:
            if check[nx] == 0 and nx in array:
                cnt += 1
                check[nx] = 1
                queue.append(nx)
    if cnt == len(array):
        return temp


def choose(N, count):
    global answer
    if count == N:
        data1 = []
        data2 = []
        for i in range(1, n + 1):
            if visit[i] == 0:
                data1.append(i)
            else:
                data2.append(i)
        x = bfs(data1)
        y = bfs(data2)
        if x and y:
            answer = min(answer, abs(x - y))
        return
    for i in range(1, n + 1):
        if visit[i] == 0:
            visit[i] = 1
            choose(N, count + 1)
            visit[i] = 0

answer = int(1e9)
for i in range(1, n//2 + 1):
    visit = [0 for _ in range(n + 1)]
    choose(i, 0)

if answer == int(1e9):
    print(-1)
else:
    print(answer)