import sys

n = int(sys.stdin.readline().rstrip())
dic = {}
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if b == 'enter':
        dic[a] = 1
    if b == 'leave':
        del dic[a]

data = sorted(dic.keys())
data.sort(reverse=True)
for i in data:
    print(i)