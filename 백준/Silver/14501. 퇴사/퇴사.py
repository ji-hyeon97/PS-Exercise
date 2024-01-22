import sys
n = int(sys.stdin.readline().rstrip())
graph = []

for _ in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    graph.append(data)

dp = [0] * (n+1)
for i in range(n):
    for j in range(i+graph[i][0],n+1):
        dp[j] = max(dp[j], dp[i]+graph[i][1])
print(dp[-1])