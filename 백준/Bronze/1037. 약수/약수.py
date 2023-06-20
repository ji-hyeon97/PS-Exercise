import sys

n = int(sys.stdin.readline().rstrip())

data = list(map(int, sys.stdin.readline().split()))
big = max(data)
small = min(data)


print(big * small)