import sys

n = int(sys.stdin.readline().rstrip())
day = []
money = []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    day.append(a)
    money.append(b)

for i in range(n - 1, -1, -1):
    if i + day[i] <= n:
        dp[i] = max(dp[i + 1], money[i] + dp[i + day[i]])
    else:
        dp[i] = dp[i + 1]
print(dp[0])