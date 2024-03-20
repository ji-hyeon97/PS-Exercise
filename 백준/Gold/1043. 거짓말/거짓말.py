import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

party = []
for _ in range(M):
    member = list(map(int, sys.stdin.readline().split()))
    party.append(member[1:])

visit = [0 for _ in range(N + 3)]

if len(data) != 1:
    queue = deque(data[1:])
    while queue:
        x = queue.popleft()
        visit[x] = 1
        for info in party:
            if info == -1:
                continue
            if x in info:
                party = party + [-1]
                for y in info:
                    if visit[y] == 0:
                        queue.append(y)
                party.remove(info)
answer = 0
for i in party:
    if i == -1:
        continue
    else:
        answer += 1
print(answer)