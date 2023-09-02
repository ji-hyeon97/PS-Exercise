import sys

n = int(sys.stdin.readline().rstrip())
graph = []
top = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    top = max(top, b)
    graph.append([a, b])
graph.sort(key=lambda v: v[0])

floor = graph[0][0]
height = graph[0][1]
answer = 0
left = 0
right = 0
for a, b in graph:
    if b > height:
        answer += (a - floor) * height
        floor = a
        height = b
    if b == top:
        left = a
        break

graph.sort(key=lambda v: -v[0])
floor = graph[0][0]
height = graph[0][1]
for a, b in graph:
    if b > height:
        answer += (a - floor) * height * -1
        floor = a
        height = b
    if b == top:
        right = a
        break
answer += (right - left + 1) * top
print(answer)