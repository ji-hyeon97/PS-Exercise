import sys

n, l = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

for i in data:
    if i<=l:
        l+=1
print(l)