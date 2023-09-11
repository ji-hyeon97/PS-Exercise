import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().split()))
data.sort()
target = int(sys.stdin.readline().rstrip())

check = [0] * (target+1)
count = 0
for i in data:
  if i > target:
    continue
  if check[target-i] == 1:
    count+=1
  check[i] = 1
print(count)