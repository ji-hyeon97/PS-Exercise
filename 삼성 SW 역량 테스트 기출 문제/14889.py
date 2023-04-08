import sys
n = int(sys.stdin.readline().rstrip())

graph = []
for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

visit = [0 for i in range(n+2)]

answer = int(1e9)

def dfs(depth, index):
  global answer
  if depth == int(n//2):
    start = 0
    link = 0
    for i in range(n):
      for j in range(n):
        if visit[i] ==0 and visit[j] ==0:
          start+=graph[i][j]
        if visit[i] ==1 and visit[j] ==1:
          link+=graph[i][j]
    answer = min(answer,abs(start-link))
    return
  for i in range(index,n):
    if visit[i]==0:
      visit[i]=1
      dfs(depth+1,i+1)
      visit[i]=0
dfs(0,0)
print(answer)