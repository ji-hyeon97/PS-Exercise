import sys

n,c = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(n)]

for i in data:
    temp = min(dp)
    for j in range(len(dp)):
        if dp[j] == temp:
            print(j+1, end=" ")
            dp[j] += i
            break