import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    dic[name] = 1

cnt = 0
nlist = []
for _ in range(m):
    find = sys.stdin.readline().rstrip()
    if find in dic:
        cnt += 1
        nlist.append(find)

print(cnt)
nlist.sort()
for i in nlist:
    print(i)