import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

dp = [[num] for num in data]

for i in range(n):
    for j in range(i):
        if data[i] >= data[j]:
            continue
        if len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [data[i]]

answer = 0
for i in range(n):
    answer = max(answer, len(dp[i]))
print(answer)