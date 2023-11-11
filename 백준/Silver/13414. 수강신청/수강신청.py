import sys

a, b = map(int, sys.stdin.readline().split())
dic = {}

for i in range(b):
    human = sys.stdin.readline().rstrip()
    if human in dic:
        del dic[human]
        dic[human] = 1
    dic[human] = 1

cnt = 0
for i in dic:
    if cnt == a:
        break
    print(i)
    cnt += 1