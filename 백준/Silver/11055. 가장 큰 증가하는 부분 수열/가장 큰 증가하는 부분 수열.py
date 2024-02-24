import sys

n = int(sys.stdin.readline().rstrip())
seq = list(map(int,sys.stdin.readline().split()))

dp = [[num] for num in seq]

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j]:
            if sum(dp[j]) + seq[i] > sum(dp[i]):
                dp[i] = dp[j] + [seq[i]]

answer = 0
for i in range(n):
    answer = max(answer, sum(dp[i]))

print(answer)