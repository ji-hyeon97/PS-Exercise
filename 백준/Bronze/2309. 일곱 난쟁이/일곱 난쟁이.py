import sys
from itertools import combinations

data = []

for _ in range(9):
    n = int(sys.stdin.readline().rstrip())
    data.append(n)

total = sum(data)
minus = total - 100

check = []
for i in combinations(data, 2):
    if sum(i) == minus:
        check = i
        break

for i in check:
    data.remove(i)
data.sort()

for i in data:
    print(i)