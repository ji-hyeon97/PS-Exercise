import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
total = [-1001] * (n + 1)

for i in range(n):
    total[i + 1] = max(data[i], total[i] + data[i])
print(max(total))