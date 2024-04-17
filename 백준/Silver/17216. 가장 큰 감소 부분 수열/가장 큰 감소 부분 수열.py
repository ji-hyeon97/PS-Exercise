import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

dp = []
for i in data:
    dp.append([i])

for i in range(n):
    for j in range(i):
        if data[j] <= data[i]:
            continue
        if sum(dp[j]) + data[i] > sum(dp[i]):
            dp[i] = dp[j] + [data[i]]
answer = 0
for temp in dp:
    answer = max(sum(temp), answer)
print(answer)