import sys

a, b = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(a):
    id, pw = map(str, sys.stdin.readline().split())
    dic[id] = pw

for _ in range(b):
    check = sys.stdin.readline().rstrip()
    print(dic[check])