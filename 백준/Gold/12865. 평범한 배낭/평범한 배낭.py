import sys

n, k = map(int, sys.stdin.readline().split())

item = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    item.append(data)

dp = [[-1 for _ in range(100_003)] for _ in range(n)]


def recur(idx, weight):
    if weight > k:
        return -9999999
    if idx == n:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx][weight] = max(recur(idx + 1, weight + item[idx][0]) + item[idx][1], recur(idx + 1, weight))
    return dp[idx][weight]


recur(0, 0)
print(dp[0][0])