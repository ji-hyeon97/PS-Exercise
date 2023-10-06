import sys

n = int(sys.stdin.readline().rstrip())
data = []
for _ in range(n):
  data.append(list(map(int,sys.stdin.readline().split())))

dp = [0 for i in range(n+1)]

for i in range(n):
  for j in range(i+data[i][0],n+1):
    if dp[j] < dp[i]+data[i][1]:
      dp[j] = dp[i]+data[i][1]

print(dp[-1])