import sys

graph = [[0] * 8]
for _ in range(4):
    data = list(map(int, sys.stdin.readline().rstrip()))
    graph.append(data)
n = int(sys.stdin.readline().rstrip())
top = [0 for _ in range(5)]

for _ in range(n):
    idx, dr = map(int, sys.stdin.readline().split())
    tlist = [(idx, 0)]
    for i in range(idx + 1, 5):
        if graph[i - 1][(top[i - 1] + 2) % 8] != graph[i][(top[i] + 6) % 8]:
            tlist.append((i, (i - idx) % 2))
        else:
            break
    for i in range(idx - 1, 0, -1):
        if graph[i][(top[i] + 2) % 8] != graph[i+1][(top[i + 1] + 6) % 8]:
            tlist.append((i, (i - idx) % 2))
        else:
            break
    for i, rotate in tlist:
        if rotate == 0:
            top[i] = (top[i] - dr + 8) % 8
        else:
            top[i] = (top[i] + dr + 8) % 8
answer = 0
for i in range(1, 5):
    answer += graph[i][top[i]]*(2**(i-1))
print(answer)