import sys

graph = [[0 for _ in range(101)]for _ in range(101)]
for _ in range(4):
    a,b,c,d = map(int,sys.stdin.readline().split())
    for i in range(a,c):
        for j in range(b,d):
            if graph[j][i] == 0:
                graph[j][i] = 1

answer = 0
for data in graph:
    for i in data:
        if i == 1:
            answer+=1

print(answer)