import sys
import collections
n = int(sys.stdin.readline().rstrip())
a, b, c, d = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)
price = int(1e9)
element = []
answer = collections.defaultdict(list)
temp = []


def recur(idx, protein, fat, carbon, vita, cost):
    global price
    global answer
    global element
    global temp
    if protein >= a and fat >= b and carbon >= c and vita >= d:
        if price > cost:
            answer = collections.defaultdict(list)
            price = min(price, cost)
            for i in element:
                temp.append(i)
            answer[price].append(temp)
            temp = []
        return
    if idx == n:
        return
    element.append(idx + 1)
    recur(idx + 1, protein + graph[idx][0], fat + graph[idx][1], carbon + graph[idx][2], vita + graph[idx][3],
          cost + graph[idx][4])
    element.pop()
    recur(idx + 1, protein, fat, carbon, vita, cost)


recur(0, 0, 0, 0, 0, 0)

if len(answer) == 0:
    print(-1)
else:
    print(price)
    answer[price].sort()
    for i in answer[price]:
        for j in i:
            print(j,end=" ")