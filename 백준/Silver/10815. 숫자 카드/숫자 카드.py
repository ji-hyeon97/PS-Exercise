import sys
import collections

n = int(sys.stdin.readline().rstrip())
got = list(map(int, sys.stdin.readline().split()))
dic = collections.defaultdict(int)
for i in got:
    dic[i] += 1

m = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
answer = ""

for i in data:
    if i in dic:
        print(1,end=" ")
    else:
        print(0,end=" ")