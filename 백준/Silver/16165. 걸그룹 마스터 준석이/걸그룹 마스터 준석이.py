import sys
import collections

a, b = map(int, sys.stdin.readline().split())
data = collections.defaultdict(list)
dic = {}
for _ in range(a):
    team = sys.stdin.readline().rstrip()
    nums = int(sys.stdin.readline().rstrip())
    for _ in range(nums):
        member = sys.stdin.readline().rstrip()
        data[team].append(member)
        dic[member] = team

for _ in range(b):
    question = sys.stdin.readline().rstrip()
    num = int(sys.stdin.readline().rstrip())
    if num == 1:
        print(dic[question])
    if num == 0:
        result = data[question]
        result.sort()
        for i in result:
            print(i)