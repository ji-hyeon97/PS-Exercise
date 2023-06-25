import sys

s = list(map(str,sys.stdin.readline().rstrip()))
graph = []

s.reverse()
for i in s:
    if len(graph) == 0:
        graph.append(i)
    else:
        word = graph.pop()
        graph.append(word)
        graph.append(i+word)

graph.sort()
for i in graph:
    print(i)