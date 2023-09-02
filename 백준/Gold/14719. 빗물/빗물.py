import sys

h, w = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
top = max(data)
original = sum(data)

graph = []
for i in range(w):
    graph.append([i, data[i]])

temp = 0
row = graph[0][0]
col = graph[0][1]
left = 0
right = 0
for a, b in graph:
    if b > col:
        temp += (a - row) * col
        row = a
        col = b
    if b == top:
        left = a
        break
graph.sort(key=lambda v: -v[0])
row = graph[0][0]
col = graph[0][1]
for a, b in graph:
    if b > col:
        temp += (row-a) * col
        row = a
        col = b
    if b == top:
        right = a
        break
temp += (right - left + 1) * top
print(temp-original)