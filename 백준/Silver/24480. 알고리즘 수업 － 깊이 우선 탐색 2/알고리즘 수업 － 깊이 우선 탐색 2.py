import sys
sys.setrecursionlimit(10**6)

n,m,r = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0 for _ in range(n+1)]
temp = 1
def dfs(index):
    global temp
    check[index] = temp
    graph[index].sort(reverse=True)
    for i in graph[index]:
        if check[i] == 0:
            temp+=1
            dfs(i)
dfs(r)
for i in range(1, len(check)):
    print(check[i])