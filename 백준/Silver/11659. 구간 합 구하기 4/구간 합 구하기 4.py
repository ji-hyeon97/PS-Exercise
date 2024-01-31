import sys

n,m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
result = [0] * (n+5)
for i in range(1, n+1):
  result[i] = result[i-1]+data[i-1]

for _ in range(m):
  i,j = map(int,sys.stdin.readline().split())
  print(result[j] - result[i-1])